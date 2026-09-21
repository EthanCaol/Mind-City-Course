# 在线测评判题后端

学生把 C 代码粘进网页 → 在 isolate 沙箱里编译运行 → 把每个测试点的输入、期望输出、
实际输出告诉他。全过就登记为通过。

## 运行方式

```
浏览器  https://mind-city.com/homework/在线评测/
   │       页面由 MkDocs 构建，JS 调站内 API
   ▼
Caddy   handle /judge/api/*  → 127.0.0.1:9100
   ▼
mind-city-judge.service（systemd --user，标准库 http.server）
   ├─ SQLite 当队列 + 单 worker 线程（2 核机器，判题必须串行）
   ├─ isolate box：写 main.c → 编译 → 逐测试点 run → cleanup
   └─ judge/data/（独立 private 仓库，git 推送由单独线程去抖批量做）
```

服务是 user 级 unit，`Linger=yes` 已开，开机自启：

```bash
systemctl --user status mind-city-judge
systemctl --user restart mind-city-judge
journalctl --user -u mind-city-judge -f
```

**`isolate.service` 必须常驻**（`sudo systemctl enable --now isolate`）。它是 system 级
unit，user 级 unit 引用不到，所以没法靠 `After=` 保证顺序——服务是在每次开判前用
`judge_ready()` 主动探测的。没起时提交会留在队列里，学生看到「判题机维护中」而不是报错。

## 目录

| 路径 | 说明 |
|---|---|
| `config.py` | 全部可调常量与路径。isolate 参数只在这里定义，别散到各处 |
| `identity.py` | 从代码第一行注释取学号 |
| `roster.py` | 花名册读取与匹配 |
| `compare.py` | 输出归一化与比对 |
| `problem.py` | 题目与测试点加载 |
| `db.py` | SQLite 读写（两张表） |
| `isolate_runner.py` | isolate 子进程编排、meta 解析、就绪探测 |
| `verdict.py` | meta → AC/WA/TLE/MLE/RE/CE/OLE |
| `judger.py` | 判一份提交：编译一次 + 跑 N 个测试点 |
| `worker.py` | 单 worker 线程、队列消费、重启恢复、内存闸门 |
| `gitstore.py` | 私有数据仓库的拉取与推送 |
| `server.py` | HTTP 接口 |
| `problems/<作业>/` | 题面参数 + 测试点（公开仓库，随代码一起版本管理） |
| `data/` | **独立 private 仓库**，见下 |

## 数据在哪

- **SQLite（`data/judge.sqlite3`）是权威数据源**，所有判题结果先写这里。
- `data/` 同时是一个**独立的 private git 仓库**（`EthanCaol/Mind-City-Course-OJ`），
  里面是花名册、学生源码存档、提交记录 JSONL。它是耐久备份，不是权威源——
  推送失败不影响判题，worker 只做本地磁盘操作，联网推送交给单独的线程按退避重试。
- `data/` 在外层公开仓库里被 **gitignore** 掉。这一点是硬要求：里面有学生姓名学号。
  而且数据一旦提交进外层仓库，本地就有未推送的 commit，部署脚本的
  `git pull --ff-only` 会失败，**整个文档站静默停止更新**。

同步节奏（`config.py` 里可调）：花名册每 5 分钟拉一次，提交记录**每两天推一次**
（推送失败 30 分钟后重试）。想立刻备份就手动触发：

```bash
TOKEN=$(cat ~/.config/mind-city/judge-admin-token)
curl -X POST -H "Authorization: Bearer $TOKEN" https://mind-city.com/judge/api/admin/sync
```

判断该不该推，看的是**最老的未推送提交有多久了**（`unpushed_age_s()`），
而不是「服务启动后过了多久」—— 后者的话，服务只要重启得比两天勤，
推送就永远不会发生。

代价是这台机器整个坏掉的话最多丢两天记录，异地备份的意义仅此而已。

## 加一份新作业

1. 建 `problems/<作业名>/problem.json`：

   ```json
   {
     "title": "作业 2：xxx",
     "compile_flags": ["-O2", "-std=c11", "-Wall", "-DONLINE_JUDGE"],
     "run_limits": { "time_s": 1, "wall_time_s": 3, "cg_mem_kb": 262144, "mem_kb": 524288 }
   }
   ```

2. 放测试点：`problems/<作业名>/cases/public/01.in`、`01.out`、`02.in`…（按文件名排序）

3. 重启服务：`systemctl --user restart mind-city-judge`

前端会自动从 `/judge/api/problems` 拿到新题目，不用改页面。

想加隐藏测试点：把文件放到 `cases/hidden/`，接口层会自动抹掉它们的输入输出，
学生只看到「未通过」。现在还没用上，但字段和加载逻辑都留好了。

## 几个容易踩的地方

- **`--mem` 是 `--cg-mem` 的 2 倍，不要改成同值。** 两者同值时 `RLIMIT_AS` 必然先触发，
  程序 `malloc` 返回 NULL、`cg-mem` 达不到阈值，**MLE 会被误判成 RE**。实测数据见
  仓库根目录的 `isolate.md` 第 4 节。
- **编译也在沙箱里跑**，因为学生代码在编译期也能作恶（超大全局数组、递归宏）。
- **每个 isolate 子进程调用都带硬超时**，否则 isolate 自己卡住会把整条队列拖死。
- **box 池在 worker 启动时会无条件 `reclaim_all()`**，回收上次崩溃留下的残骸。
  `--cleanup` 对不存在的 box 是安全的，所以可以无脑调用。
- **meta 文件是宿主侧路径，`--stdin/--stdout/--stderr` 是 box 内相对路径**，
  而且都必须在 `--cleanup` 之前读完。
- **内存闸门**：开判前读 `/proc/meminfo`，`MemAvailable` 低于 400 MB 就暂缓。
  这台机器只有 2 GB，判题服务把机器打进 swap 会很难恢复。

## 身份校验的强度

**这是弱校验。** 学号写在代码第一行注释里，只要能对上花名册就受理——挡得住抄错学号，
挡不住「故意冒用同学学号且知道其姓名」。课程练习场景下够用，成绩敏感的话要另加提交码。

代码里也不会去读姓名：记录里的姓名一律从花名册查，学生写什么都不影响。
