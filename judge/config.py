"""判题服务的全部可调常量与路径。

这里是**单一来源**：其他模块一律 `from . import config` 后读 `config.XXX`。

尤其不要把 isolate 参数散落到各处 —— `--init` 和 `--run` 的 `--cg` 一旦不一致，
isolate 会报 `status:XX` 并以退出码 2 失败，而报错信息看起来像是配置写错了。
所以 `--cg` 由 `isolate_runner` 内部统一拼装，调用方没有机会漏传。
"""

from __future__ import annotations

import dataclasses
from pathlib import Path

# ---------------------------------------------------------------- 路径

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
PROBLEMS_DIR = BASE_DIR / "problems"

DB_PATH = DATA_DIR / "judge.sqlite3"
ROSTER_PATH = DATA_DIR / "roster.csv"
WORK_DIR = DATA_DIR / "work"

ADMIN_TOKEN_PATH = Path.home() / ".config" / "mind-city" / "judge-admin-token"

# 助教。他们和同学用同一套判题，也出现在花名册里，但不是这个班的学生。
# 「作业完成情况」页把他们排在最前面，名字后面加「（助教）」。
# 顺序就是这里的顺序；姓名仍然从花名册查，名单改了不用动这里。
TUTORS = ("26113050003", "26113050344")

# 带「阅读登记」栏的实验课页面。slug 就是页面里 `data-page` 的值，也是总览页的列名；
# title 只用在悬停提示上。顺序就是总览页列的顺序，这里跟侧边栏「实验课文档」一致。
#
# 这里**手工维护**，不去扫 docs 目录：服务只认这几个 slug，多一个少一个都由这份清单说了算。
# 加了新的实验课页面就在对应位置补一条，否则总览页不会出现那一列（页面上的登记栏会报「没有这一页」）。
#
# 「文档阅读进度」和「实用工具推荐」不在里面 —— 前者是总览页自己，后者是查资料用的，
# 都不属于「按顺序读下来」的进度。
READ_PAGES: tuple[tuple[str, str], ...] = (
    ("claude", "Claude 工具链配置"),
    ("dsh", "DSH 工具链配置"),
    ("dev-cpp", "Dev-C++ 环境搭建"),
    ("wsl2", "WSL2 环境搭建"),
    ("macos", "macOS 环境搭建"),
    ("vscode", "VSCode 入门教程"),
    ("linux-cli", "Linux 命令行基础"),
    ("git-github", "Git-GitHub 基础操作"),
)

# ---------------------------------------------------------------- isolate

ISOLATE_BIN = "/usr/local/bin/isolate"
BOX_ROOT = Path("/var/local/lib/isolate")

# 就绪探针读这个文件拿 cgroup 路径。注意 isolate.service 停掉之后
# 这个文件**不会**跟着清理，它会留着一条已经不存在了的路径
# （见根目录 README 的「三个坑」②），所以必须再去检查该路径是否真的有 cgroup.procs。
CGROUP_FILE = Path("/run/isolate/cgroup")

# --cg 必须始终打开。不加就等于没做内存隔离：--mem 只落到 RLIMIT_AS，
# 没有 cgroup 记账，meta 里也不会出现 cg-mem。
USE_CG = True

# 判题串行，所以只用一个 box。将来若开 2 并发，这里改成 (0, 1) 即可，
# 调用方（BoxPool）不用动。
BOX_IDS: tuple[int, ...] = (0,)

# 编译必须显式传 PATH，否则沙箱内环境被清空、gcc 找不到 ld
# （报 `collect2: fatal error: cannot find 'ld'`）。
SANDBOX_PATH = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# 每个 isolate 子进程调用的硬超时 = 该步的 --wall-time + 这个余量。
# 没有这层保护的话，isolate 自己卡住会把整条判题队列拖死。
SUBPROCESS_SLACK_S = 10.0

# ---------------------------------------------------------------- 判题

# 判题必须串行。2 核机器上并发 gcc 会打爆内存。
# 生产环境（claude / VSCode 都不开）内存是够跑 2 个的，但 2 核的 CPU 仍是瓶颈，
# 除非确有必要，否则别动这个值。
JUDGE_WORKERS = 1

# 内存闸门：开判前 MemAvailable 低于这个值就暂缓。
# 这是本机特有的保命措施 —— 判题服务一旦把机器打进 swap 会很难恢复。
MEM_AVAILABLE_FLOOR_KB = 400 * 1024

# 队列深度超过这个值就拒绝新提交（503），防止截止前雪崩。
QUEUE_MAX = 200

# 队列 ETA 用的 EWMA 平滑系数
EWMA_ALPHA = 0.3

# MLE 判据（isolate 本身没有 MLE 状态码，只能推断）
MLE_CGMEM_RATIO = 0.9  # cg-mem 达到上限的 90% 且进程被杀 → MLE
MLE_MAXRSS_RATIO = 0.8  # 兜底：rlimit 口径的峰值内存也接近上限


@dataclasses.dataclass(frozen=True)
class Limits:
    """一次 isolate --run 的资源限制。时间单位为秒，其余为 KB。"""

    time_s: float
    wall_time_s: float
    extra_time_s: float
    mem_kb: int  # → RLIMIT_AS（地址空间）
    cg_mem_kb: int  # → cgroup memory.max（真实 RSS）
    processes: int
    fsize_kb: int
    open_files: int
    stack_kb: int


# 编译：给足时间和内存，但仍在沙箱内跑 —— 学生代码在编译期也能作恶
# （超大全局数组、递归宏、#include 巨型文件）。
COMPILE_LIMITS = Limits(
    time_s=10,
    wall_time_s=20,
    extra_time_s=0.5,
    mem_kb=524288,
    cg_mem_kb=524288,
    processes=64,  # gcc 要 cc1 + as + collect2，64 够用且能挡住编译期 fork 炸弹
    fsize_kb=65536,
    open_files=128,
    stack_kb=65536,
)

# 运行：入门 C 作业的默认值，每题可在 problem.json 里覆盖。
#
# 注意 mem_kb 刻意取 cg_mem_kb 的 2 倍，与「两者同值」的
# 建议不同。原因：RLIMIT_AS >= RSS 恒成立，两者同值时 RLIMIT_AS 必然先触发，
# 程序 malloc 返回 NULL 后段错误，而 cg-mem 停在低位达不到阈值 ——
# 于是「cg-mem 接近上限」这条 MLE 判据永远不会成立，MLE 会被误判成 RE。
# 抬高 mem_kb 后真实内存先撞 cgroup，cg-mem ≈ memory.max，MLE 可以无歧义判定；
# 同时 mem_kb 仍守住「mmap 几十 GB 但不 touch」那一类地址空间炸弹。
#
# 2026-09-21 实测确认：同一个只申请 400 MB 的程序，同值配法判成 RE（cg-mem 停在
# 24 MB），2 倍配法判成 MLE（cg-mem = 262144）。见 judge/tools/selfcheck.py 的对比项。
RUN_LIMITS = Limits(
    time_s=1,
    wall_time_s=3,
    extra_time_s=0.5,
    mem_kb=524288,
    cg_mem_kb=262144,
    processes=8,
    fsize_kb=1024,  # 顺带把 stdout 也限到 1 MB，输出超限得到 SIGXFSZ(25)
    open_files=64,
    stack_kb=65536,
)

# ---------------------------------------------------------------- HTTP

BIND_HOST = "127.0.0.1"
BIND_PORT = 9100
BASE_PATH = "/judge"

MAX_SOURCE_BYTES = 64 * 1024
MAX_BODY_OTHER = 4 * 1024
MAX_CONCURRENCY = 16  # ThreadingHTTPServer 的无界线程会被这个信号量兜住
HANDLER_TIMEOUT_S = 15  # 挡 slowloris

# ---------------------------------------------------------------- 限流

MIN_SUBMIT_INTERVAL_S = 3  # 两次提交的最小间隔，防连点
# 每学生每作业，2 分钟内最多交 5 次。
# 窗口开得小是有意的：重复提交不去重，学生改一版交一版是正常操作，
# 卡太久会挡着人改错。作业页的提示文字里也写了这个数，改这里记得同步改。
RATE_LIMIT_WINDOW_S = 120
RATE_LIMIT_MAX_IN_WINDOW = 5

# ---------------------------------------------------------------- git

GIT_REMOTE = "origin"
GIT_BRANCH = "main"
GIT_PULL_TIMEOUT_S = 30
GIT_PUSH_TIMEOUT_S = 60

# 花名册不再变了，只在服务启动时从数据仓库拉一次。想手动刷就调
# POST /api/admin/sync，或者重启服务。
#
# 成绩单**不自动推送** —— 仓库里只有名单和成绩，没有学生代码，没有定时
# 备份的必要。想推就调 POST /api/admin/sync。
