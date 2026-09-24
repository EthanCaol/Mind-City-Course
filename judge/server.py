"""HTTP 接口。

用标准库 `http.server`，不引第三方框架：现有 webhook 服务（同样的
ThreadingHTTPServer 写法）常驻内存只有 8 MB，证明这条路够用；而同一个 Python
解释器正跑着文档站，往 conda base 里装 FastAPI 有连带风险。

Caddy 把 https://mind-city.com/judge/api/* 反代到这里（127.0.0.1:9100）。
"""

from __future__ import annotations

import datetime as dt
import hmac
import json
import logging
import secrets
import sqlite3
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from . import config, db, verdict as V
from .identity import FORMAT_HINT, STUDENT_ID_RE, extract_student_id
from .gitstore import GitStore
from .isolate_runner import judge_ready
from .problem import ProblemError, list_problems, load_problem
from .roster import Roster
from .worker import JudgeWorker

log = logging.getLogger("judge.server")


# ---------------------------------------------------------------- 应用状态


class App:
    """进程内的共享状态。HTTP 线程和判题线程都从这里拿东西。"""

    def __init__(self) -> None:
        self.db_path = config.DB_PATH
        self.conn = db.connect(self.db_path)
        db.init_db(self.conn)
        self.lock = threading.RLock()

        self.roster = Roster(config.ROSTER_PATH)
        if not self.roster.reload_or_keep():
            raise SystemExit(f"花名册加载失败：{config.ROSTER_PATH}")

        self.admin_token = load_admin_token()
        self.git = GitStore()
        self.worker = JudgeWorker(self.db_path, self.roster, self.git)
        # 启动时拉一次花名册就跑完退出 —— 名单不再变，不需要常驻线程。
        # 成绩单不再自动推送，要推就调 POST /api/admin/sync。
        self._roster_pull = threading.Thread(
            target=self.git.pull_roster_at_startup,
            args=(self.roster.reload_or_keep,),
            name="roster-pull",
            daemon=True,
        )

    def start(self) -> None:
        self._roster_pull.start()
        self.worker.start()

    def stop(self) -> None:
        self.worker.stop()

    # ------------------------------------------------------------ 提交

    def submit(self, homework: str, code: str, client_ip: str | None) -> tuple[int, dict]:
        if not isinstance(code, str) or not code.strip():
            return 400, {"error": "代码是空的"}

        if len(code.encode("utf-8")) > config.MAX_SOURCE_BYTES:
            return 413, {"error": f"代码太长（上限 {config.MAX_SOURCE_BYTES // 1024} KB）"}

        student_id = extract_student_id(code)
        if student_id is None:
            return 400, {"error": FORMAT_HINT}

        name = self.roster.lookup(student_id)
        if name is None:
            return 403, {"error": f"学号 {student_id} 不在本课程名单里，请核对。"}

        try:
            problem = load_problem(homework)
        except ProblemError as exc:
            return 404, {"error": str(exc)}

        with self.lock:
            if db.queue_depth(self.conn) >= config.QUEUE_MAX:
                return 503, {"error": "判题队列已满，请过一会儿再交。"}

            since = _ago(config.RATE_LIMIT_WINDOW_S)
            if db.count_since(self.conn, homework, student_id, since) >= config.RATE_LIMIT_MAX_IN_WINDOW:
                # 文案跟着配置走，别写死「几分钟」——窗口一改就对不上了
                minutes = max(1, round(config.RATE_LIMIT_WINDOW_S / 60))
                return 429, {
                    "error": (
                        f"提交太频繁了，{minutes} 分钟最多交 {config.RATE_LIMIT_MAX_IN_WINDOW} 次，请稍后再试。"
                    )
                }

            last = db.last_submit_at(self.conn, homework, student_id)
            if last and _seconds_since(last) < config.MIN_SUBMIT_INTERVAL_S:
                return 429, {"error": "刚交过一份，请稍等几秒。"}

            sub_id = db.create_submission(
                self.conn,
                homework=homework,
                student_id=student_id,
                name=name,
                source=code,
                client_ip=client_ip,
            )
            row = db.get(self.conn, sub_id)
            payload = _submission_payload(self.conn, row, problem)

        self.worker.wake()
        return 200, payload

    # ------------------------------------------------------------ 查询

    def submission(self, sub_id: int, token: str | None, is_admin: bool) -> tuple[int, dict]:
        with self.lock:
            row = db.get(self.conn, sub_id)
            if row is None:
                return 404, {"error": "没有这份提交"}

            # 结果里带学生源码输出，凭 token 才能看，防止遍历 id 看同学的
            if not is_admin and not hmac.compare_digest(token or "", row["access_token"]):
                return 403, {"error": "查询码不对"}

            try:
                problem = load_problem(row["homework"])
            except ProblemError as exc:
                return 404, {"error": str(exc)}

            return 200, _submission_payload(self.conn, row, problem)

    def history(self, homework: str, student_id: str) -> tuple[int, dict]:
        with self.lock:
            rows = db.history(self.conn, homework, student_id)
        return 200, {
            "submissions": [
                {
                    "id": r["id"],
                    "status": r["status"],
                    "verdict": r["verdict"],
                    "verdict_label": V.LABELS.get(r["verdict"], ""),
                    "passed": r["passed_cases"],
                    "total": r["total_cases"],
                    "created_at": r["created_at"],
                }
                for r in rows
            ]
        }

    def grades(self) -> tuple[int, dict]:
        """作业完成情况：行是学生，列是作业。

        这个接口是**公开**的（页面要显示全班完成情况），所以只回传姓名和
        通过与否 —— 不给学号，也不给提交次数、耗时这些细节。姓名在本课程
        名单里是唯一的，扫一眼就能找到自己。
        """
        with self.lock:
            problems = list_problems()
            passed = {p.slug: db.passed_ids(self.conn, p.slug) for p in problems}

        return 200, self._grid(
            [(p.slug, p.title) for p in problems], passed
        )

    # ------------------------------------------------------------ 阅读登记

    def mark_read(self, page: str, student_id: str) -> tuple[int, dict]:
        """登记一次阅读。不计分，所以校验和判题一样是弱校验：学号在名单里就受理。

        挡得住抄错学号，挡不住冒用同学的学号 —— 这不是成绩，够用了。
        """
        if page not in dict(config.ALL_READ_PAGES):
            return 404, {"error": "没有这一页"}

        if not isinstance(student_id, str) or not STUDENT_ID_RE.fullmatch(student_id):
            return 400, {"error": "学号是 11 位数字，请检查一下。"}

        name = self.roster.lookup(student_id)
        if name is None:
            return 403, {"error": f"学号 {student_id} 不在本课程名单里，请核对。"}

        with self.lock:
            first, at = db.mark_read(self.conn, page=page, student_id=student_id)

        # 顺带把姓名回给前端：登记成功后要显示「张三 同学，恭喜…」，而页面手里只有学号。
        # 代价是这一个公开接口可以用学号换姓名（本来 403 和 200 就已经能试出学号在不在名单里）。
        return 200, {"page": page, "registered_at": at, "already": not first, "name": name}

    def read_status(self, page: str, student_id: str) -> tuple[int, dict]:
        """查一个人在这一页登记过没有。

        这里**不查花名册**：只回「登记过没有」，不区分「不在名单里」和「没登记」，
        接口就没法拿来试探学号是否属于本课程。
        """
        if page not in dict(config.ALL_READ_PAGES):
            return 404, {"error": "没有这一页"}

        with self.lock:
            at = db.read_at(self.conn, page, student_id)

        return 200, {"registered": at is not None, "registered_at": at}

    def reads(self, group: str = "") -> tuple[int, dict]:
        """阅读进度：行是学生，列是页面。和作业完成情况同构，也是公开接口。

        分两组：实验课文档（setup，默认）和教材习题（book）。两张总览页各取一组，
        否则一张表里会同时出现文档和习题的列。
        """
        pages = config.BOOK_PAGES if group == "book" else config.READ_PAGES
        with self.lock:
            read = {page: db.read_ids(self.conn, page) for page, _ in pages}

        return 200, self._grid(list(pages), read)

    def _grid(self, columns: list[tuple[str, str]], done: dict[str, set[str]]):
        """两个完成情况页共用的表格数据：行是学生、列是作业/页面。

        顺序就是花名册文件里的顺序（助教在前，其余按姓名拼音），页面上再排一遍
        反而会和助教看到的名单对不上。助教名字后面加「（助教）」—— 他们和同学
        用同一套系统，但不是这个班的学生。
        """
        roster = self.roster.all()
        return {
            "columns": [{"slug": slug, "title": title} for slug, title in columns],
            "students": [
                {
                    "name": name + ("（助教）" if sid in config.TUTORS else ""),
                    "done": {slug: sid in ids for slug, ids in done.items()},
                }
                for sid, name in roster.items()
            ],
        }

    def health(self) -> tuple[int, dict]:
        ready, reason = judge_ready()
        with self.lock:
            depth = db.queue_depth(self.conn)
        return 200, {
            "ok": True,
            "judge_ready": ready,
            "message": reason,
            "queue_depth": depth,
            "roster_size": len(self.roster),
        }

    # ------------------------------------------------------------ 管理端

    def admin_submissions(self, q: dict) -> tuple[int, dict]:
        with self.lock:
            rows = db.list_submissions(
                self.conn,
                homework=q.get("homework"),
                student_id=q.get("student_id"),
                verdict=q.get("verdict"),
                limit=min(int(q.get("limit", 200)), 1000),
                offset=int(q.get("offset", 0)),
            )
        return 200, {
            "submissions": [
                {
                    "id": r["id"],
                    "homework": r["homework"],
                    "student_id": r["student_id"],
                    "name": r["name"],
                    "status": r["status"],
                    "verdict": r["verdict"],
                    "verdict_label": V.LABELS.get(r["verdict"], ""),
                    "passed": r["passed_cases"],
                    "total": r["total_cases"],
                    "created_at": r["created_at"],
                }
                for r in rows
            ]
        }

    def admin_sync(self) -> tuple[int, dict]:
        """同步一次：拉花名册 + 推成绩单。

        成绩单不再定时推送（仓库里只有名单和成绩，没有学生代码），
        所以这是唯一的推送入口。
        """
        pulled = self.git.pull()
        if pulled:
            self.roster.reload_or_keep()
        committed = self.git.commit("成绩单")
        pushed = self.git.push()
        return 200, {"roster_pulled": pulled, "committed": committed, "pushed": pushed}

    def admin_export(self, homework: str) -> str:
        """导出成绩 CSV。没提交的人也会占一行，标「未提交」。"""
        with self.lock:
            rows = db.export_grades(self.conn, homework, self.roster.all())
        return "\n".join(rows) + "\n"


# ---------------------------------------------------------------- 工具


def _ago(seconds: int) -> str:
    return (dt.datetime.now() - dt.timedelta(seconds=seconds)).isoformat(timespec="seconds")


def _seconds_since(iso: str) -> float:
    try:
        then = dt.datetime.fromisoformat(iso)
    except ValueError:
        return 1e9
    return (dt.datetime.now() - then).total_seconds()


def _submission_payload(conn, row: sqlite3.Row, problem) -> dict:
    """一份提交的完整结果。这是学生看到的核心内容：每个测试点的输入、
    期望输出、自己的实际输出。"""
    cases = []
    if row["status"] == db.DONE and row["verdict"] != V.CE:
        by_index = {r["case_index"]: r for r in db.case_results(conn, row["id"])}
        for case in problem.cases:
            r = by_index.get(case.index)
            if r is None:
                continue
            cases.append(
                {
                    "index": case.index,
                    "verdict": r["verdict"],
                    "verdict_label": V.LABELS.get(r["verdict"], ""),
                    "reason": r["reason"],
                    "time_s": r["time_s"],
                    "memory_kb": r["memory_kb"],
                    "stdin": case.stdin,
                    "expected": case.expected,
                    "actual": r["actual_output"],
                }
            )

    payload = {
        "id": row["id"],
        "token": row["access_token"],
        "homework": row["homework"],
        "student_id": row["student_id"],
        "name": row["name"],
        "status": row["status"],
        "verdict": row["verdict"],
        "verdict_label": V.LABELS.get(row["verdict"], ""),
        "passed": row["passed_cases"],
        "total": row["total_cases"],
        "compile_error": row["compile_error"],
        "created_at": row["created_at"],
        "finished_at": row["finished_at"],
        "cases": cases,
    }
    if row["status"] in (db.PENDING, db.JUDGING):
        payload["queue_ahead"] = db.queue_ahead(conn, row["id"])
    return payload


# ---------------------------------------------------------------- 鉴权


def load_admin_token() -> str:
    path = config.ADMIN_TOKEN_PATH
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()

    token = secrets.token_urlsafe(32)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(token + "\n", encoding="utf-8")
    path.chmod(0o600)
    log.info("已生成管理端查询码：%s", path)
    return token


# ---------------------------------------------------------------- HTTP


def create_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        timeout = config.HANDLER_TIMEOUT_S
        server_version = "MindCityJudge"

        # 关掉 Nagle。wfile 是无缓冲的，响应头和响应体会分两次 write，
        # Nagle 会压住第二个包等对端的 ACK，而客户端又在延迟确认 ——
        # 实测每个响应因此多花约 40ms（正是延迟确认的定时器长度）。
        # 这个开关是 StreamRequestHandler 现成的，置 True 即设 TCP_NODELAY。
        disable_nagle_algorithm = True

        # ---------------------------------------------------- 入口

        def do_GET(self) -> None:
            self._handle("GET")

        def do_POST(self) -> None:
            self._handle("POST")

        def _handle(self, method: str) -> None:
            parsed = urlparse(self.path)
            path = parsed.path
            query = {k: v[0] for k, v in parse_qs(parsed.query).items()}

            if not path.startswith(config.BASE_PATH):
                return self._json(404, {"error": "not found"})
            route = path[len(config.BASE_PATH) :]

            try:
                status, payload = self._route(method, route, query)
            except Exception:
                log.exception("处理 %s %s 时异常", method, self.path)
                status, payload = 500, {"error": "服务器内部错误"}

            if isinstance(payload, str):
                self._send(status, payload.encode("utf-8"), "text/csv; charset=utf-8")
            else:
                self._json(status, payload)

        # ---------------------------------------------------- 路由

        def _route(self, method: str, route: str, query: dict):
            if route in ("/api/problems", "/api/problems/"):
                return 200, {
                    "problems": [
                        {"slug": p.slug, "title": p.title, "total_cases": p.total_cases}
                        for p in list_problems()
                    ]
                }

            if route in ("/api/health", "/api/health/"):
                return app.health()

            if route in ("/api/grades", "/api/grades/"):
                return app.grades()

            if route in ("/api/reads", "/api/reads/"):
                return app.reads(query.get("group", ""))

            if route == "/api/read" and method == "POST":
                body = self._read_json()
                return app.mark_read(body.get("page", ""), body.get("student_id", ""))

            if route in ("/api/read", "/api/read/"):
                return app.read_status(query.get("page", ""), query.get("sid", ""))

            if route == "/api/submit" and method == "POST":
                body = self._read_json()
                return app.submit(
                    body.get("homework", ""), body.get("code", ""), self._client_ip()
                )

            if route == "/api/history":
                return app.history(query.get("homework", ""), query.get("sid", ""))

            if route.startswith("/api/submissions/"):
                sub_id = _int_or_none(route.rsplit("/", 1)[-1])
                if sub_id is None:
                    return 404, {"error": "没有这份提交"}
                return app.submission(sub_id, query.get("token"), self._is_admin())

            # ---------------- 管理端 ----------------

            if route.startswith("/api/admin/"):
                if not self._is_admin():
                    return 403, {"error": "需要管理端查询码"}

                if route == "/api/admin/submissions":
                    return app.admin_submissions(query)

                if route == "/api/admin/export.csv":
                    return 200, app.admin_export(query.get("homework", ""))

                if route == "/api/admin/roster":
                    return 200, {"roster": app.roster.all()}

                # 没有「看源码」和「重判」接口：源码判完即抹，服务手里没有。
                # 这是「不保存学生提交」的直接代价。

                # 成绩单每两天才自动推一次，想立刻备份就手动触发
                if route == "/api/admin/sync" and method == "POST":
                    return app.admin_sync()

            return 404, {"error": "not found"}

        # ---------------------------------------------------- 辅助

        def _is_admin(self) -> bool:
            header = self.headers.get("Authorization", "")
            if not header.startswith("Bearer "):
                return False
            return hmac.compare_digest(header[7:].strip(), app.admin_token)

        def _client_ip(self) -> str | None:
            # Caddy 反代会带上 X-Forwarded-For，服务只监听回环所以可信
            forwarded = self.headers.get("X-Forwarded-For", "")
            if forwarded:
                return forwarded.split(",")[0].strip()
            return self.client_address[0] if self.client_address else None

        def _read_json(self) -> dict:
            if self.headers.get("Transfer-Encoding", "").lower() == "chunked":
                raise ValueError("不支持 chunked 请求体")

            length = int(self.headers.get("Content-Length") or 0)
            if length <= 0:
                return {}
            if length > config.MAX_SOURCE_BYTES + config.MAX_BODY_OTHER:
                raise ValueError("请求体太大")

            raw = self.rfile.read(length)
            try:
                data = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise ValueError("请求体不是合法 JSON") from exc
            return data if isinstance(data, dict) else {}

        def _json(self, status: int, payload: dict) -> None:
            self._send(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                       "application/json; charset=utf-8")

        def _send(self, status: int, body: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt: str, *args) -> None:
            log.info("%s - %s", self.address_string(), fmt % args)

    return Handler


def _int_or_none(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


# ---------------------------------------------------------------- main


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stdout,
    )

    app = App()
    app.start()

    server = ThreadingHTTPServer((config.BIND_HOST, config.BIND_PORT), create_handler(app))
    server.daemon_threads = True
    log.info("判题服务监听 http://%s:%d%s", config.BIND_HOST, config.BIND_PORT, config.BASE_PATH)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
        app.stop()
        app.worker.join(timeout=30)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
