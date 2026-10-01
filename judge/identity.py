"""学号的形状。

判题提交和阅读登记都只认「11 位数字」这一条，两边共用这个正则。
"""

import re

STUDENT_ID_RE = re.compile(r"[0-9]{11}")
