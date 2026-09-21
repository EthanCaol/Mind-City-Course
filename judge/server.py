"""HTTP 接口。

用标准库 `http.server`，不引第三方框架：现有 webhook 服务（同样的
ThreadingHTTPServer 写法）常驻内存只有 8 MB，证明这条路够用；而同一个 Python
解释器正跑着文档站，往 conda base 里装 FastAPI 有连带风险。

Caddy 把 https://mind-city.com/judge/api/* 反代到这里（127.0.0.1:9100）。
"""

from __future__ import annotations

import datetime as dt
import hashlib
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
from .identity import FORMAT_HINT, extract_student_id
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
        self._stop = threading.Event()
        self._syncer = threading.Thread(
            target=self.git.sync_loop,
            args=(self._stop, self.roster.reload_or_keep),
            name="git-sync",
            daemon=True,
        )

    def start(self) -> None:
        self.worker.start()
        self._syncer.start()

    def stop(self) -> None:
        self._stop.set()
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
                return 429, {"error": "提交太频繁了，请等几分钟再试。"}

            last = db.last_submit_at(self.conn, homework, student_id)
            if last and _seconds_since(last) < config.MIN_SUBMIT_INTERVAL_S:
                return 429, {"error": "刚交过一份，请稍等几秒。"}

            sha = hashlib_sha256(code)
            dup = db.find_duplicate(self.conn, homework, student_id, sha)
            if dup is not None and dup["status"] != db.SYSTEM_ERROR:
                return 200, _submission_payload(self.conn, dup, problem, duplicate=True)

            sub_id = db.create_submission(
                self.conn,
                homework=homework,
                student_id=student_id,
                name=name,
                source=code,
                sha256=sha,
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
            "roster_stale": self.roster.is_stale,
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

    def admin_source(self, sub_id: int) -> tuple[int, dict]:
        with self.lock:
            row = db.get(self.conn, sub_id)
        if row is None:
            return 404, {"error": "没有这份提交"}
        return 200, {
            "id": row["id"],
            "student_id": row["student_id"],
            "name": row["name"],
            "source": row["source"],
        }

    def admin_rejudge(self, sub_id: int) -> tuple[int, dict]:
        with self.lock:
            if db.get(self.conn, sub_id) is None:
                return 404, {"error": "没有这份提交"}
            db.requeue(self.conn, sub_id)
        self.worker.wake()
        return 200, {"ok": True}

    def admin_export(self, homework: str) -> str:
        """导出成绩 CSV：每人一行，第一次通过的时间。"""
        roster = self.roster.all()
        with self.lock:
            passed = db.passed_students(self.conn, homework)

        lines = ["学号,姓名,是否通过,首次通过时间,最好成绩"]
        for sid, name in sorted(roster.items()):
            row = passed.get(sid)
            if row:
                lines.append(
                    f"{sid},{name},是,{row['finished_at']},"
                    f"{row['passed_cases']}/{row['total_cases']}"
                )
            else:
                lines.append(f"{sid},{name},否,,")
        return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- 工具


def hashlib_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _ago(seconds: int) -> str:
    return (dt.datetime.now() - dt.timedelta(seconds=seconds)).isoformat(timespec="seconds")


def _seconds_since(iso: str) -> float:
    try:
        then = dt.datetime.fromisoformat(iso)
    except ValueError:
        return 1e9
    return (dt.datetime.now() - then).total_seconds()


def _submission_payload(conn, row: sqlite3.Row, problem, duplicate: bool = False) -> dict:
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
    if duplicate:
        payload["duplicate"] = True
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

                if route.startswith("/api/admin/source/"):
                    sub_id = _int_or_none(route.rsplit("/", 1)[-1])
                    return (
                        app.admin_source(sub_id)
                        if sub_id is not None
                        else (404, {"error": "没有这份提交"})
                    )

                if route.startswith("/api/admin/rejudge/") and method == "POST":
                    sub_id = _int_or_none(route.rsplit("/", 1)[-1])
                    return (
                        app.admin_rejudge(sub_id)
                        if sub_id is not None
                        else (404, {"error": "没有这份提交"})
                    )

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
