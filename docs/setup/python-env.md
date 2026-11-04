# Python 环境配置

这篇给需要在同一台机器上同时使用 Miniconda 和 uv 的读者参考。

## 1. 两者的分工

| 工具      | 安装方式                        | 用途                                                     |
| --------- | ------------------------------- | -------------------------------------------------------- |
| Miniconda | 单独安装，保留一个 base 环境    | base 环境负责安装日常使用的库，老项目另建 conda 独立环境 |
| uv        | 直接装到 Miniconda 的 base 环境 | 现在的新项目都用 uv 创建环境和安装依赖，速度比 conda 快    |

## 2. Windows 操作系统的环境配置

### 2.1 安装 Miniconda

在 PowerShell 里执行：

```powershell
winget install Anaconda.Miniconda3
```

### 2.2 初始化 PowerShell

```powershell
& "$env:USERPROFILE\miniconda3\Scripts\conda.exe" init powershell
```

这条命令往 PowerShell 配置文件里写入 conda 的初始化脚本。执行完关闭终端重新打开，提示符前面出现 `(base)` 表示生效。

如果懒得重开终端，也可以在当前终端里，手动加载更新后的配置文件：

```powershell
. $PROFILE.CurrentUserAllHosts
```

### 2.3 安装 uv

```powershell
pip install uv
```

### 2.4 测速并配置镜像源

把下面一行命令发给 Claude Code：

```text
对比各个 pip 镜像源的下载速度，然后写入 conda-pip 和 uv 的配置（tencent aliyun huaweicloud tuna ustc sjtug pypi）
```

### 2.5 安装常用库

```powershell
pip install numpy pandas matplotlib jupyter
```

## 3. Linux 操作系统的环境配置

### 3.1 安装 Miniconda

在终端里执行：

```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -u -p ~/miniconda3
rm Miniconda3-latest-Linux-x86_64.sh
```

`-b` 表示接受许可协议并静默安装，`-p` 指定安装目录。

### 3.2 初始化 bash

```bash
~/miniconda3/bin/conda init bash
```

这条命令往 `~/.bashrc` 里写入 conda 的初始化脚本。执行完关闭终端重新打开，提示符前面出现 `(base)` 表示生效。

如果懒得重开终端，也可以在当前终端里，手动加载更新后的配置文件：

```bash
source ~/.bashrc
```

### 3.3 安装 uv

```bash
pip install uv
```

### 3.4 测速并配置镜像源

把下面一行命令发给 Claude Code：

```text
对比各个 pip 镜像源的下载速度，然后写入 conda-pip 和 uv 的配置（tencent aliyun huaweicloud tuna ustc sjtug pypi）
```

### 3.5 安装常用库

```bash
pip install numpy pandas matplotlib jupyter
```

## 4. 验收

Windows 和 Linux 下命令相同，依次执行，三步都正常输出就表示配置完成：

```bash
conda --version
uv --version
python -c "import numpy, pandas, matplotlib; print('ok')"
```

## 5. 常用操作

下表列出的命令不需要记住，环境管理的繁琐操作，直接交给 Claude Code 即可。

| 需求             | 命令                                 |
| ---------------- | ------------------------------------ |
| 老项目：创建环境 | `conda create -n 项目名 python=3.12` |
| 老项目：进入环境 | `conda activate 项目名`              |
| 老项目：退出环境 | `conda deactivate`                   |
| 新项目：初始化   | `uv init`                            |
| 新项目：安装依赖 | `uv add 包名`                        |
| 新项目：运行脚本 | `uv run 脚本.py`                     |

---

!!! todo "文档完成登记：完成本文全部流程后告知助教"

    <div class="read" id="read" data-page="python-env">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
