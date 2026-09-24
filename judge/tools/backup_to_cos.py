#!/usr/bin/env python3
"""把判题数据同步到 COS（覆盖式，由 mind-city-backup.timer 每周一 04:00 调用）。

    python3 judge/tools/backup_to_cos.py

传三样，都落在桶里 `backup/` 下面，每次覆盖同名对象：

    backup/judge.sqlite3    数据库快照
    backup/roster.csv       花名册
    backup/grades/*.csv     成绩单

**数据库不能直接 cp。** 这个库是 WAL 模式，主文件可能只有几十 KB，绝大部分数据还在
`judge.sqlite3-wal` 里（实测主文件 48 KB / WAL 4.1 MB，直接拷主文件等于只备份了个壳）。
所以走 sqlite3 的在线备份 API，源库正在被写也能拿到一致的一份。

**每个对象都显式带私有 ACL。** 桶是公开读的（站点的图就挂在上面），漏了这个头就等于
把学生姓名、学号和提交记录摊在公网上。
"""

from __future__ import annotations

import logging
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from judge import config

log = logging.getLogger("backup")

ACL_HEADER = "x-cos-acl: private"


def snapshot_db(dest: Path) -> float:
    """取一份一致的数据库快照，返回 MB 数。"""
    src = sqlite3.connect(f"file:{config.DB_PATH}?mode=ro", uri=True)
    try:
        out = sqlite3.connect(dest)
        try:
            src.backup(out)
        finally:
            out.close()
    finally:
        src.close()
    return dest.stat().st_size / 1e6


def upload(local: Path, key: str, recursive: bool = False) -> None:
    cmd = [config.COS_BIN, "-b", config.COS_BACKUP_BUCKET, "upload", "-f",
           "-H", ACL_HEADER]
    if recursive:
        cmd.append("-r")
    cmd += [str(local), key]

    done = subprocess.run(cmd, capture_output=True, text=True)
    if done.returncode != 0:
        log.error("上传失败：%s → %s\n%s%s", local, key, done.stdout, done.stderr)
        raise SystemExit(f"coscmd 退出码 {done.returncode}")
    log.info("已上传 %s → %s/", local.name, key)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

    grades = config.DATA_DIR / "grades"
    if not config.ROSTER_PATH.exists():
        raise SystemExit(f"花名册不存在：{config.ROSTER_PATH}")

    with tempfile.TemporaryDirectory(prefix="judge-backup-") as tmp:
        snap = Path(tmp) / "judge.sqlite3"
        size = snapshot_db(snap)
        log.info("数据库快照 %.2f MB（主文件只有 %.0f KB，其余都在 WAL 里）",
                 size, config.DB_PATH.stat().st_size / 1e3)

        upload(snap, f"{config.COS_BACKUP_PREFIX}/judge.sqlite3")
        upload(config.ROSTER_PATH, f"{config.COS_BACKUP_PREFIX}/roster.csv")

        # 成绩单是助教导出后才有的，平时这个目录是空的 —— 空目录不上传，
        # 反正数据库快照里什么都有，成绩单随时能从它重新导出。
        if grades.is_dir() and any(grades.iterdir()):
            upload(grades, f"{config.COS_BACKUP_PREFIX}/grades", recursive=True)
        else:
            log.info("成绩单目录是空的，跳过")

    log.info("备份完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
