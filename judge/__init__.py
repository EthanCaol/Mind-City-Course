"""Mind City Course 在线测评判题后端。

模块划分：

    config          全部可调常量与路径（单一来源）
    identity        从源码注释里提取学号
    roster          花名册读取与匹配
    compare         输出归一化与比对
    problem         题目与测试点加载
    db              SQLite 读写
    isolate_runner  isolate 子进程编排（BoxPool / Box / meta 解析）
    verdict         meta → AC/WA/TLE/MLE/RE/CE/OLE/SYSTEM
    worker          单 worker 线程、队列、重启恢复
    gitstore        私有数据仓库的 pull / push
    api / server    HTTP 接口
"""

__all__ = ["config"]
