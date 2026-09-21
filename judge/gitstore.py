"""私有数据仓库的同步：拉花名册、推成绩单。

仓库是 `EthanCaol/Mind-City-Course-OJ`（private），工作副本就是 `judge/data/`
—— 它同时被外层公开仓库 gitignore 掉。这一点很关键：数据一旦提交进外层仓库，
本地就有未推送的 commit，部署脚本的 `git pull --ff-only` 会失败，整个文档站静默停止更新。

**仓库里只有花名册和成绩单，没有学生代码。** 学生源码判完即从数据库抹掉，
一行都不落盘（见 db.clear_source）。

**SQLite 是权威数据源，这个仓库只是耐久备份。** 所以推送失败不影响判题：
worker 只调这里的本地写文件（微秒级），联网的 push 交给独立的 sync 线程。
"""

from __future__ import annotations

import fcntl
import logging
import subprocess
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

    def write_grades(self, homework: str, rows: list[str]) -> Path:
        """整份重写成绩单。服务是唯一写者，不会有冲突。"""
        path = self.dir / "grades" / f"{homework}.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")
        return path

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

    # ------------------------------------------------------------ 启动时

    def pull_roster_at_startup(self, on_change=None) -> None:
        """服务启动时拉一次花名册，然后就不管了。

        名单不再变，所以没有轮询的必要。拉不到就用本地已有的那份。
        放在独立线程里做，万一张网络慢也不至于拖住服务启动。
        """
        if self.pull() and on_change is not None:
            on_change()
