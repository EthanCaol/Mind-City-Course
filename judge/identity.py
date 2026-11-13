"""学号与验证凭据的形状。

判题提交和阅读登记都只认「11 位数字」这一条，两边共用这个正则。

成绩查询除了学号还要一个凭据：学生首次查询时，用复旦学邮寄来的验证码换一个
签名串，之后浏览器带着它就不再要验证码。凭据是无状态的 —— 签名里带着学号，
不建表、服务重启也不用重新验证。
"""

import hashlib
import hmac
import re

STUDENT_ID_RE = re.compile(r"[0-9]{11}")


def code_for(student_id: str, secret: str) -> str:
    """学号对应的固定六位验证码。和签名共用密钥，同一个学号每次都一样。"""
    digest = hmac.new(secret.encode(), student_id.encode(), hashlib.sha256).hexdigest()
    return f"{int(digest[:8], 16) % 1_000_000:06d}"


def issue_token(student_id: str, secret: str) -> str:
    """学号 + 签名。格式 `学号.签名前32位`。"""
    sig = hmac.new(secret.encode(), student_id.encode(), hashlib.sha256).hexdigest()
    return f"{student_id}.{sig[:32]}"


def check_token(token: str | None, secret: str) -> str | None:
    """凭据有效就返回其中的学号，否则 None。"""
    if not token or "." not in token:
        return None
    student_id, _, sig = token.partition(".")
    if not STUDENT_ID_RE.fullmatch(student_id):
        return None
    expected = issue_token(student_id, secret).partition(".")[2]
    return student_id if hmac.compare_digest(sig, expected) else None
