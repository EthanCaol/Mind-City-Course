"""SQLite 读写。

两张表：`submissions` 每份提交一行，`case_results` 每个测试点一行。
测试点的输入和期望**不入库** —— 展示的时候直接从题目文件读，它们本来就是公开的。
只存学生程序的实际输出。

SQLite 是权威数据源；private 仓库里的 JSONL 只是它的耐久备份，推送失败不影响判题。
"""

from __future__ import annotations

import datetime as dt
import secrets
import sqlite3
from pathlib import Path

PENDING = "PENDING"
JUDGING = "JUDGING"
DONE = "DONE"
SYSTEM_ERROR = "SYSTEM_ERROR"

SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    homework      TEXT    NOT NULL,
    student_id    TEXT    NOT NULL,
    name          TEXT    NOT NULL,
    source        TEXT    NOT NULL,
    access_token  TEXT    NOT NULL,
    status        TEXT    NOT NULL,
    verdict       TEXT,
    passed_cases  INTEGER NOT NULL DEFAULT 0,
    total_cases   INTEGER NOT NULL DEFAULT 0,
    compile_error TEXT,
    worst_time_s  REAL,
    worst_mem_kb  INTEGER,
    attempts      INTEGER NOT NULL DEFAULT 0,
    client_ip     TEXT,
    created_at    TEXT    NOT NULL,
    started_at    TEXT,
    finished_at   TEXT
);

-- 不做去重：同一份代码重复提交会重新判一次。
-- 「重判」这个功能已经没了（源码不存），重交一份相同的代码是学生唯一的
-- 重新判题途径。防刷由速率限制负责（见 config 里的几个 RATE_LIMIT）。
CREATE INDEX IF NOT EXISTS idx_queue ON submissions(status, id);
CREATE INDEX IF NOT EXISTS idx_student ON submissions(homework, student_id, id DESC);

CREATE TABLE IF NOT EXISTS case_results (
    submission_id INTEGER NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    case_index    INTEGER NOT NULL,
    verdict       TEXT    NOT NULL,
    reason        TEXT,
    time_s        REAL,
    memory_kb     INTEGER,
    actual_output TEXT,
    PRIMARY KEY (submission_id, case_index)
);
"""


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def connect(path: Path) -> sqlite3.Connection:
    """开一个连接。HTTP 线程和判题线程都会用，所以关掉同线程检查，
    由一把锁串行化（这台机器的流量用不上连接池）。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=5000")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    with conn:
        conn.executescript(SCHEMA)


# ---------------------------------------------------------------- 提交


def create_submission(
    conn: sqlite3.Connection,
    *,
    homework: str,
    student_id: str,
    name: str,
    source: str,
    client_ip: str | None,
) -> int:
    with conn:
        cur = conn.execute(
            """INSERT INTO submissions
               (homework, student_id, name, source, access_token,
                status, created_at, client_ip)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                homework,
                student_id,
                name,
                source,
                secrets.token_urlsafe(16),
                PENDING,
                now(),
                client_ip,
            ),
        )
        return int(cur.lastrowid)


def claim_next(conn: sqlite3.Connection) -> sqlite3.Row | None:
    """取下一份待判的提交并标记为 JUDGING。

    `UPDATE ... RETURNING` 放在事务里，天然原子 —— 将来开两个 worker 也不会
    重复领到同一份。
    """
    with conn:
        row = conn.execute(
            """UPDATE submissions
                  SET status=?, started_at=?, attempts=attempts+1
                WHERE id = (SELECT id FROM submissions
                             WHERE status=? ORDER BY id LIMIT 1)
            RETURNING *""",
            (JUDGING, now(), PENDING),
        ).fetchone()
    return row


def reset_stuck(conn: sqlite3.Connection) -> int:
    """把服务重启时卡在 JUDGING 的提交退回队列。

    判题是幂等的，重判一遍即可；不然这些提交会永远停在「判题中」。
    """
    with conn:
        cur = conn.execute(
            "UPDATE submissions SET status=? WHERE status=?", (PENDING, JUDGING)
        )
    return cur.rowcount


def add_case_result(
    conn: sqlite3.Connection,
    submission_id: int,
    *,
    case_index: int,
    verdict: str,
    reason: str = "",
    time_s: float = 0.0,
    memory_kb: int = 0,
    actual_output: str = "",
) -> None:
    with conn:
        conn.execute(
            """INSERT OR REPLACE INTO case_results
               (submission_id, case_index, verdict, reason, time_s, memory_kb, actual_output)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (submission_id, case_index, verdict, reason, time_s, memory_kb, actual_output),
        )


def clear_case_results(conn: sqlite3.Connection, submission_id: int) -> None:
    with conn:
        conn.execute("DELETE FROM case_results WHERE submission_id=?", (submission_id,))


def finish(
    conn: sqlite3.Connection,
    submission_id: int,
    *,
    verdict: str,
    passed: int,
    total: int,
    worst_time_s: float = 0.0,
    worst_mem_kb: int = 0,
    compile_error: str | None = None,
) -> None:
    with conn:
        conn.execute(
            """UPDATE submissions
                  SET status=?, verdict=?, passed_cases=?, total_cases=?,
                      worst_time_s=?, worst_mem_kb=?, compile_error=?, finished_at=?
                WHERE id=?""",
            (
                DONE,
                verdict,
                passed,
                total,
                worst_time_s,
                worst_mem_kb,
                compile_error,
                now(),
                submission_id,
            ),
        )


def mark_system_error(conn: sqlite3.Connection, submission_id: int, reason: str) -> None:
    with conn:
        conn.execute(
            """UPDATE submissions
                  SET status=?, verdict='SYSTEM', compile_error=?, finished_at=?
                WHERE id=?""",
            (SYSTEM_ERROR, reason, now(), submission_id),
        )


def requeue(conn: sqlite3.Connection, submission_id: int) -> None:
    """把提交退回队列（重判，或撞上判题机故障后重排）。"""
    with conn:
        conn.execute(
            "UPDATE submissions SET status=?, verdict=NULL, finished_at=NULL WHERE id=?",
            (PENDING, submission_id),
        )


def clear_source(conn: sqlite3.Connection, submission_id: int) -> None:
    """判完立刻把源码抹掉。

    源码只在排队期间存在 —— 不这么做 worker 就没法异步取件，但留着就等于
    把学生一学期的代码全存档了。判完即清，谁都不留。
    """
    with conn:
        conn.execute("UPDATE submissions SET source='' WHERE id=?", (submission_id,))


# ---------------------------------------------------------------- 查询


def get(conn: sqlite3.Connection, submission_id: int) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM submissions WHERE id=?", (submission_id,)
    ).fetchone()


def case_results(conn: sqlite3.Connection, submission_id: int) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM case_results WHERE submission_id=? ORDER BY case_index",
        (submission_id,),
    ).fetchall()


def history(conn: sqlite3.Connection, homework: str, student_id: str) -> list[sqlite3.Row]:
    return conn.execute(
        """SELECT id, status, verdict, passed_cases, total_cases, created_at
             FROM submissions WHERE homework=? AND student_id=?
            ORDER BY id DESC LIMIT 20""",
        (homework, student_id),
    ).fetchall()


def queue_ahead(conn: sqlite3.Connection, submission_id: int) -> int:
    """排在这份提交前面的还有几份（含正在判的那份）。"""
    row = conn.execute(
        """SELECT COUNT(*) AS n FROM submissions
            WHERE status IN (?, ?) AND id < ?""",
        (PENDING, JUDGING, submission_id),
    ).fetchone()
    return int(row["n"])


def queue_depth(conn: sqlite3.Connection) -> int:
    row = conn.execute(
        "SELECT COUNT(*) AS n FROM submissions WHERE status IN (?, ?)",
        (PENDING, JUDGING),
    ).fetchone()
    return int(row["n"])


def count_since(
    conn: sqlite3.Connection, homework: str, student_id: str, since: str
) -> int:
    row = conn.execute(
        """SELECT COUNT(*) AS n FROM submissions
            WHERE homework=? AND student_id=? AND created_at >= ?""",
        (homework, student_id, since),
    ).fetchone()
    return int(row["n"])


def last_submit_at(
    conn: sqlite3.Connection, homework: str, student_id: str
) -> str | None:
    row = conn.execute(
        """SELECT created_at FROM submissions
            WHERE homework=? AND student_id=? ORDER BY id DESC LIMIT 1""",
        (homework, student_id),
    ).fetchone()
    return row["created_at"] if row else None


def best_passed(conn: sqlite3.Connection, homework: str, student_id: str) -> int:
    """该学生在这一题上通过过的最多测试点数（用来判断是否登记为通过）。"""
    row = conn.execute(
        """SELECT MAX(passed_cases) AS n FROM submissions
            WHERE homework=? AND student_id=? AND verdict='AC'""",
        (homework, student_id),
    ).fetchone()
    return int(row["n"] or 0)


def has_passed(conn: sqlite3.Connection, homework: str, student_id: str) -> bool:
    row = conn.execute(
        """SELECT 1 FROM submissions
            WHERE homework=? AND student_id=? AND verdict='AC' LIMIT 1""",
        (homework, student_id),
    ).fetchone()
    return row is not None


def list_submissions(
    conn: sqlite3.Connection,
    *,
    homework: str | None = None,
    student_id: str | None = None,
    verdict: str | None = None,
    limit: int = 200,
    offset: int = 0,
) -> list[sqlite3.Row]:
    where, params = [], []
    if homework:
        where.append("homework=?")
        params.append(homework)
    if student_id:
        where.append("student_id=?")
        params.append(student_id)
    if verdict == "PASSED":
        where.append("verdict='AC'")
    elif verdict:
        where.append("verdict=?")
        params.append(verdict)

    clause = f"WHERE {' AND '.join(where)}" if where else ""
    params.extend([limit, offset])
    return conn.execute(
        f"""SELECT id, homework, student_id, name, status, verdict,
                   passed_cases, total_cases, worst_time_s, worst_mem_kb,
                   created_at, finished_at, client_ip
              FROM submissions {clause}
             ORDER BY id DESC LIMIT ? OFFSET ?""",
        params,
    ).fetchall()


def passed_students(conn: sqlite3.Connection, homework: str) -> dict[str, sqlite3.Row]:
    """该题目下每个学号最好的一次 AC 记录，用于导出成绩。"""
    rows = conn.execute(
        """SELECT s.* FROM submissions s
             JOIN (SELECT student_id, MIN(id) AS first_id FROM submissions
                    WHERE homework=? AND verdict='AC' GROUP BY student_id) t
               ON s.id = t.first_id""",
        (homework,),
    ).fetchall()
    return {r["student_id"]: r for r in rows}


def passed_ids(conn: sqlite3.Connection, homework: str) -> set[str]:
    """该题目下通过过的学号。用于「作业完成情况」页。"""
    return {
        r["student_id"]
        for r in conn.execute(
            "SELECT DISTINCT student_id FROM submissions WHERE homework=? AND verdict='AC'",
            (homework,),
        )
    }


def export_grades(
    conn: sqlite3.Connection, homework: str, roster: dict[str, str]
) -> list[str]:
    """成绩单的 CSV 行。`roster` 是 学号→姓名。

    没交的人也要占一行，助教一眼能看出谁还没交 —— 只列交过的人，"谁没交"
    反而得自己比对名单。
    """
    passed = passed_students(conn, homework)
    submitted = {
        r["student_id"]
        for r in conn.execute(
            "SELECT DISTINCT student_id FROM submissions WHERE homework=?", (homework,)
        )
    }

    rows = ["学号,姓名,是否通过,首次通过时间,通过测试点"]
    for sid, name in sorted(roster.items()):
        row = passed.get(sid)
        if row:
            rows.append(
                f"{sid},{name},是,{row['finished_at']},"
                f"{row['passed_cases']}/{row['total_cases']}"
            )
        elif sid in submitted:
            rows.append(f"{sid},{name},否,,")
        else:
            rows.append(f"{sid},{name},未提交,,")
    return rows


def counts_by_verdict(conn: sqlite3.Connection, homework: str | None = None) -> dict[str, int]:
    sql = "SELECT verdict, COUNT(*) AS n FROM submissions"
    params: tuple = ()
    if homework:
        sql += " WHERE homework=?"
        params = (homework,)
    sql += " GROUP BY verdict"
    return {r["verdict"] or "": int(r["n"]) for r in conn.execute(sql, params)}
