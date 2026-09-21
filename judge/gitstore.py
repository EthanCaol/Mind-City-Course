"""私有数据仓库的同步：拉花名册、存提交记录。

仓库是 `EthanCaol/Mind-City-Course-OJ`（private），工作副本就是 `judge/data/`
—— 它同时被外层公开仓库 gitignore 掉。这一点很关键：数据一旦提交进外层仓库，
本地就有未推送的 commit，部署脚本的 `git pull --ff-only` 会失败，整个文档站静默停止更新。

**SQLite 是权威数据源，这个仓库只是耐久备份。** 所以推送失败不影响判题：
worker 只调这里的本地磁盘操作（微秒级），联网的 push 交给独立的 sync 线程，
失败就退避重试。
"""

from __future__ import annotations

import fcntl
import json
import logging
import subprocess
import threading
import time
from pathlib import Path

from . import config

log = logging.getLogger("judge.git")

# 永不挂在交互式认证上：没有 TTY 时 git 会一直等密码，把线程卡死。
GIT_ENV = {
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_SSH_COMMAND": "ssh -o BatchMode=yes -o ConnectTimeout=10",
    "GIT_AUTHOR_NAME": "Mind City Judge",
    "GIT_AUTHOR_EMAIL": "judge@mind-city.com",
    "GIT_COMMITTER_NAME": "Mind City Judge",
    "GIT_COMMITTER_EMAIL": "judge@mind-city.com",
}

RECORDS = "records/submissions.jsonl"
# JSONL 里截断输出：全量文本留在 SQLite 里，不然仓库会被撑到几百 MB
TRUNCATE = 1024


class GitStore:
    def __init__(self, repo_dir: Path = config.DATA_DIR) -> None:
        self.dir = Path(repo_dir)
        self.lock_path = self.dir / ".sync.lock"

    # ------------------------------------------------------------ 基础

    def _git(self, args: list[str], timeout: float) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["git", "-C", str(self.dir), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**GIT_ENV, "PATH": "/usr/bin:/bin:/usr/local/bin"},
        )

    def _locked(self):
        """把 git 操作串行化。多个线程同时 pull/push 会互相打架。"""
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        handle = open(self.lock_path, "w")
        fcntl.flock(handle, fcntl.LOCK_EX)
        return handle

    def ensure(self) -> bool:
        """确认工作副本是个配置好远端的 git 仓库。"""
        if not (self.dir / ".git").is_dir():
            log.warning("%s 不是 git 仓库，跳过同步", self.dir)
            return False
        return True

    # ------------------------------------------------------------ 拉

    def pull(self) -> bool:
        """拉花名册。助教只改 roster.csv，服务从不写它，所以不会冲突。"""
        if not self.ensure():
            return False
        handle = self._locked()
        try:
            result = self._git(
                ["pull", "--rebase", "--autostash", config.GIT_REMOTE, config.GIT_BRANCH],
                config.GIT_PULL_TIMEOUT_S,
            )
        except subprocess.TimeoutExpired:
            log.warning("拉取数据仓库超时")
            return False
        finally:
            handle.close()

        if result.returncode != 0:
            log.warning("拉取数据仓库失败：%s", result.stderr.strip()[:200])
            return False
        return True

    # ------------------------------------------------------------ 写（纯本地）

    def archive_source(self, homework: str, student_id: str, sha: str, source: str) -> Path:
        """按内容 sha 命名存源码。同一份代码重复交只会有一个文件。"""
        path = self.dir / "submissions" / homework / student_id / f"{sha[:12]}.c"
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file():
            path.write_text(source, encoding="utf-8")
        return path

    def append_record(self, record: dict) -> None:
        """追加一行 JSONL。追加式写入，助教和服务同时推也不会冲突
        （.gitattributes 里给这个文件配了 merge=union）。"""
        path = self.dir / RECORDS
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def commit(self, message: str) -> bool:
        """纯本地提交，不联网。返回是否产生了一个新提交。"""
        if not self.ensure():
            return False
        handle = self._locked()
        try:
            # 用 -A 而不是列路径：judge.sqlite3 和 work/ 都在 .gitignore 里，
            # 而列路径时只要有一个目录还不存在（比如 grades/），git add 就会报错。
            self._git(["add", "-A"], 30)
            result = self._git(["commit", "-m", message, "--no-verify"], 30)
        except subprocess.TimeoutExpired:
            log.warning("提交数据仓库超时")
            return False
        finally:
            handle.close()

        if result.returncode != 0:
            # 没有改动时 git commit 会返回非 0，这是正常的
            if "nothing to commit" not in result.stdout:
                log.warning("提交数据仓库失败：%s", (result.stderr or result.stdout).strip()[:200])
            return False
        return True

    # ------------------------------------------------------------ 推

    def push(self) -> bool:
        if not self.ensure():
            return False
        handle = self._locked()
        try:
            self._git(
                ["pull", "--rebase", "--autostash", config.GIT_REMOTE, config.GIT_BRANCH],
                config.GIT_PULL_TIMEOUT_S,
            )
            result = self._git(
                ["push", config.GIT_REMOTE, config.GIT_BRANCH], config.GIT_PUSH_TIMEOUT_S
            )
        except subprocess.TimeoutExpired:
            log.warning("推送数据仓库超时")
            return False
        finally:
            handle.close()

        if result.returncode != 0:
            log.warning("推送数据仓库失败：%s", result.stderr.strip()[:200])
            return False

        self._push_failures = 0
        return True

    # ------------------------------------------------------------ 后台线程

    def sync_loop(self, stop_event: threading.Event, on_change=None) -> None:
        """定时同步：花名册勤拉，提交记录一周推一次。

        独立线程，判题 worker 不碰网络 —— 网络再慢再断也不影响判题。
        """
        next_pull = 0.0  # 启动时立刻拉一次
        next_push = time.monotonic() + config.PUSH_INTERVAL_S

        while not stop_event.is_set():
            now = time.monotonic()

            if now >= next_pull:
                next_pull = now + config.ROSTER_PULL_INTERVAL_S
                if self.pull() and on_change is not None:
                    on_change()

            if now >= next_push:
                # 正常情况下 worker 每判一份就已经本地 commit 了，
                # 这里只是兜底，顺手把可能漏掉的改动一起提上
                self.commit("判题记录")
                if self.push():
                    next_push = now + config.PUSH_INTERVAL_S
                else:
                    # 不能真等一周才重试
                    next_push = now + config.PUSH_RETRY_S

            stop_event.wait(30)
