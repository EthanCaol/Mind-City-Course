#!/usr/bin/env python3
"""真沙箱自测：直接调判题内核，不经过 HTTP。

    python3 judge/tools/selfcheck.py

需要 `isolate.service` 在运行（`sudo systemctl enable --now isolate`），
不然 `--cg` 模式起不来。脚本开头会先探测并给出提示。

覆盖 AC / WA / CE / TLE / RE / OLE / MLE 七种结论，最后做一个
`--mem` 取值对比 —— 那条 MLE 判据是推断出来的，必须实测确认。
"""

from __future__ import annotations

import dataclasses
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from judge import config  # noqa: E402
from judge.config import Limits  # noqa: E402
from judge.isolate_runner import BoxPool, judge_ready  # noqa: E402
from judge.judger import judge_submission  # noqa: E402
from judge.problem import load_problem  # noqa: E402

PROBLEM = "作业1"

HEAD = "// 26803070224\n"

PROGRAMS = {
    "正确": HEAD
    + "#include <stdio.h>\n"
    "int main(void){int a,b;scanf(\"%d %d\",&a,&b);printf(\"%d\\n\",a+b);return 0;}\n",
    "差一": HEAD
    + "#include <stdio.h>\n"
    "int main(void){int a,b;scanf(\"%d %d\",&a,&b);printf(\"%d\\n\",a+b+1);return 0;}\n",
    "编译错误": HEAD + "#include <stdio.h>\nint main(void){this is not C}\n",
    "死循环": HEAD + "int main(void){for(;;);}\n",
    "除零": HEAD
    + "#include <stdio.h>\n"
    "int main(void){int a,b;scanf(\"%d %d\",&a,&b);a=a/(b-b);printf(\"%d\\n\",a);return 0;}\n",
    "狂打印": HEAD
    + "#include <stdio.h>\n"
    "int main(void){int i=0;while(i++<100000000)printf(\"aaaaaaaaaaaaaaaaaaaa\\n\");return 0;}\n",
    # 一次性申请 400 MB，写满后还要读一遍 —— 不读回来的话 -O2 会把 memset
    # 当死代码整个删掉，程序就根本没碰内存，测不出任何东西。
    "吃内存": HEAD
    + "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
    "int main(void){size_t n=400u*1024*1024;char*p=malloc(n);"
    "if(!p){printf(\"malloc NULL\\n\");return 1;}memset(p,1,n);"
    "volatile long s=0;for(size_t i=0;i<n;i+=4096)s+=p[i];"
    "printf(\"sum=%ld\\n\",s);return 0;}\n",
}

EXPECTED = {
    "正确": "AC",
    "差一": "WA",
    "编译错误": "CE",
    "死循环": "TLE",
    "除零": "RE",
    "狂打印": "OLE",
    "吃内存": "MLE",
}

_failures: list[str] = []


def run_all(pool: BoxPool, problem) -> dict[str, tuple[str, str]]:
    """跑一遍全部程序，返回 {名字: (结论, 说明)}。"""
    results: dict[str, tuple[str, str]] = {}

    for name, source in PROGRAMS.items():
        with pool.acquire() as box:
            box.init()
            outcome = judge_submission(box, source, problem)

        detail = outcome.compile_error.splitlines()[0] if outcome.compile_error else ""
        if not detail and outcome.cases:
            bad = next((c for c in outcome.cases if c.verdict != "AC"), None)
            if bad:
                detail = bad.reason

        results[name] = (outcome.verdict, detail)
        mark = "OK " if outcome.verdict == EXPECTED[name] else "!! "
        print(f"  {mark}{name:<8} {outcome.verdict:<7} {outcome.passed}/{outcome.total}  {detail}")
        if outcome.verdict != EXPECTED[name]:
            _failures.append(
                f"{name}：期望 {EXPECTED[name]}，实际 {outcome.verdict}（{detail}）"
            )

    return results


def compare_mem_configs(pool: BoxPool, problem) -> None:
    """对 `--mem` 的两种取值各跑一次「吃内存」，看 MLE 判据成不成立。

    这是我们和 isolate.md 建议值唯一的偏离点，必须实测确认：
    两者同值时 RLIMIT_AS 会先触发，cg-mem 达不到阈值，MLE 会被误判成 RE。
    """
    print("\n--mem / --cg-mem 取值对比（都在判「吃内存」那个程序）")

    same = dataclasses.replace(problem.run_limits, mem_kb=problem.run_limits.cg_mem_kb)
    variants = [
        ("同值（isolate.md 的建议）", same),
        ("2 倍（本项目的选择）", problem.run_limits),
    ]

    for label, limits in variants:
        variant = dataclasses.replace(problem, run_limits=limits)
        with pool.acquire() as box:
            box.init()
            outcome = judge_submission(box, PROGRAMS["吃内存"], variant)

        first = outcome.cases[0] if outcome.cases else None
        print(
            f"  {label:<24} → {outcome.verdict:<6} "
            f"memory={first.memory_kb if first else 0} KB  "
            f"{first.reason if first else outcome.compile_error}"
        )


def main() -> int:
    ready, message = judge_ready()
    if not ready:
        print(message)
        return 2

    problem = load_problem(PROBLEM)
    pool = BoxPool()

    print("回收遗留 box：", pool.reclaim_all())
    print(f"\n题目 {problem.slug}：{problem.total_cases} 个测试点")
    print(f"运行限制：{dataclasses.asdict(problem.run_limits)}\n")

    print("各状态判定")
    run_all(pool, problem)

    compare_mem_configs(pool, problem)

    leftover = sorted(p.name for p in config.BOX_ROOT.iterdir()) if config.BOX_ROOT.is_dir() else []
    print(f"\n清理后 /var/local/lib/isolate 下剩：{leftover or '空'}")
    if leftover:
        _failures.append(f"box 泄漏：{leftover}")

    if _failures:
        print(f"\n失败 {len(_failures)} 项：")
        for f in _failures:
            print(f"  · {f}")
        return 1

    print("\n全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
