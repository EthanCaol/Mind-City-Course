"""判题 worker：从 SQLite 队列里取提交，一份一份串行判完。

队列就是 `submissions` 表，不是内存队列 —— 这样服务重启后没判完的提交还在，
退回 PENDING 重判即可（判题是幂等的）。内存队列一重启就丢。

串行是硬要求：这台机器只有 2 核，并发跑 gcc 会打爆内存（isolate.md 第 8.6 条）。
"""

from __future__ import annotations

import logging
import threading
import time
from pathlib import Path

from . import config, db, verdict as V
from .gitstore import GitStore
from .isolate_runner import BoxPool, judge_ready
from .judger import judge_submission
from .problem import Problem, ProblemError, load_problem
from .roster import Roster

log = logging.getLogger("judge.worker")

IDLE_POLL_S = 2.0  # 队列空时的兜底轮询间隔；有提交时靠 wake() 立即唤醒
NOT_READY_POLL_S = 5.0
MEMINFO = Path("/proc/meminfo")


def mem_available_kb() -> int:
    try:
        for line in MEMINFO.read_text().splitlines():
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
    except (OSError, ValueError, IndexError):
        pass
    return 1 << 30  # 读不到就不拦，别因为读不到 /proc 就不判题


class JudgeWorker(threading.Thread):
    def __init__(self, db_path: Path, roster: Roster, gitstore: GitStore | None = None) -> None:
        super().__init__(name="judge-worker", daemon=True)
        self.db_path = Path(db_path)
        self.roster = roster
        self.git = gitstore or GitStore()
        self._wake = threading.Event()
        self._stop = threading.Event()
        self._pool = BoxPool()
        self._problems: dict[str, Problem] = {}

    # ------------------------------------------------------------ 生命周期

    def wake(self) -> None:
        """有新提交时叫醒 worker，正常情况零延迟开判。"""
        self._wake.set()

    def stop(self) -> None:
        self._stop.set()
        self._wake.set()

    def run(self) -> None:
        conn = db.connect(self.db_path)
        stuck = db.reset_stuck(conn)
        if stuck:
            log.warning("把 %d 份卡在 JUDGING 的提交退回队列", stuck)
        self._pool.reclaim_all()

        log.info("判题 worker 启动")
        try:
            while not self._stop.is_set():
                if not self._can_judge():
                    self._sleep(NOT_READY_POLL_S)
                    continue

                row = db.claim_next(conn)
                if row is None:
                    self._sleep(IDLE_POLL_S)
                    continue

                try:
                    self._judge_one(conn, row)
                except Exception:
                    # 单份提交把 worker 搞挂会让整个队列停摆，所以兜住
                    log.exception("判提交 #%s 时异常", row["id"])
                    db.mark_system_error(conn, row["id"], "判题服务内部异常，请联系助教")
        finally:
            self._pool.reclaim_all()
            conn.close()
            log.info("判题 worker 退出")

    def _sleep(self, seconds: float) -> None:
        self._wake.wait(seconds)
        self._wake.clear()

    def _can_judge(self) -> bool:
        """开判前的两道闸。"""
        ready, reason = judge_ready()
        if not ready:
            log.warning("判题机未就绪，暂停消费队列：%s", reason.splitlines()[0])
            return False

        available = mem_available_kb()
        if available < config.MEM_AVAILABLE_FLOOR_KB:
            log.warning("可用内存只剩 %d MB，暂缓判题", available // 1024)
            return False
        return True

    # ------------------------------------------------------------ 判一份

    def _problem(self, slug: str) -> Problem:
        """题目按需加载并缓存。改了题目文件要重启服务才会生效。"""
        if slug not in self._problems:
            self._problems[slug] = load_problem(slug)
        return self._problems[slug]

    def _judge_one(self, conn, row) -> None:
        sub_id = row["id"]
        log.info("开始判 #%s（%s %s）", sub_id, row["student_id"], row["homework"])

        try:
            problem = self._problem(row["homework"])
        except ProblemError as exc:
            db.mark_system_error(conn, sub_id, f"题目加载失败：{exc}")
            return

        with self._pool.acquire() as box:
            box.init()
            outcome = judge_submission(box, row["source"], problem)

        if outcome.verdict == V.SYSTEM:
            # 判题机自己的问题，不能给学生记错。重排一次，还是不行就记系统错误。
            if row["attempts"] < 2:
                log.warning("#%s 撞上判题机故障，重排（第 %d 次）", sub_id, row["attempts"])
                db.requeue(conn, sub_id)
                return
            db.mark_system_error(conn, sub_id, outcome.compile_error or "判题机反复故障")
            return

        db.clear_case_results(conn, sub_id)
        for case in outcome.cases:
            db.add_case_result(
                conn,
                sub_id,
                case_index=case.index,
                verdict=case.verdict,
                reason=case.reason,
                time_s=case.time_s,
                memory_kb=case.memory_kb,
                actual_output=case.actual,
            )

        db.finish(
            conn,
            sub_id,
            verdict=outcome.verdict,
            passed=outcome.passed,
            total=outcome.total,
            worst_time_s=outcome.worst_time_s,
            worst_mem_kb=outcome.worst_mem_kb,
            compile_error=outcome.compile_error or None,
        )
        log.info(
            "#%s 判完：%s（%d/%d）",
            sub_id,
            outcome.verdict,
            outcome.passed,
            outcome.total,
        )

        # 判完立刻抹掉源码 —— 判题是异步的，源码得在队列里待一会儿，
        # 但没有理由把学生一学期的代码全存下来。
        db.clear_source(conn, sub_id)
        self._write_grades(conn, row["homework"])

    def _write_grades(self, conn, homework: str) -> None:
        """重写成绩单。

        只做本地写文件（微秒级），联网推送交给 sync 线程，所以这里失败
        也不能让判题结果受影响。
        """
        try:
            rows = db.export_grades(conn, homework, self.roster.all())
            self.git.write_grades(homework, rows)
        except Exception:
            log.exception("写成绩单失败（判题结果已入库，不受影响）")
