"""发验证码邮件。

走 QQ 邮箱的 SMTP（SSL 465），账号和授权码从 `~/.config/mind-city/mail.json` 读，
不进仓库。用标准库 smtplib，不引第三方。

发信是阻塞的，一次几秒 —— 调用方是 HTTP 线程，ThreadingHTTPServer 下不影响别的请求。
"""

from __future__ import annotations

import json
import logging
import smtplib
from email.message import EmailMessage

from . import config

log = logging.getLogger("judge.mailer")


class MailError(Exception):
    pass


def _settings() -> dict:
    path = config.MAIL_CONFIG_PATH
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise MailError(f"没有邮件配置：{path}")
    except (OSError, json.JSONDecodeError) as exc:
        raise MailError(f"邮件配置读不了：{exc}")

    for key in ("user", "password"):
        if not data.get(key):
            raise MailError(f"邮件配置缺少 {key}：{path}")
    return data


def send_code(student_id: str, code: str) -> None:
    """把验证码发到学生的复旦学邮。失败抛 MailError。"""
    cfg = _settings()
    address = f"{student_id}@{config.STUDENT_MAIL_DOMAIN}"
    minutes = config.CODE_TTL_S // 60

    msg = EmailMessage()
    msg["Subject"] = f"成绩查询验证码：{code}"
    msg["From"] = f"{config.MAIL_FROM_NAME} <{cfg['user']}>"
    msg["To"] = address
    msg.set_content(
        "同学你好：\n\n"
        "有人正在查询你的成绩，验证码如下：\n\n"
        f"    {code}\n\n"
        f"{minutes} 分钟内有效。不是你本人操作的，忽略这封邮件即可。\n\n"
        "复旦大学《程序设计》课程\n"
    )

    try:
        with smtplib.SMTP_SSL(
            cfg.get("host", "smtp.qq.com"), int(cfg.get("port", 465)), timeout=10
        ) as smtp:
            smtp.login(cfg["user"], cfg["password"])
            smtp.send_message(msg)
    except (smtplib.SMTPException, OSError) as exc:
        raise MailError(str(exc)) from exc

    log.info("验证码已发往 %s", address)
