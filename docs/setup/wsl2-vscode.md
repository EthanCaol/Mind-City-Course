
# WSL2 + GCC + VSCode 环境搭建

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>实验课时间：<strong>2026-9-16</strong></span></p>

面向零基础、使用 Win11 操作系统的同学。全过程只需要在 Windows 终端里粘贴命令，**不需要任何前置知识**。中途遇到任何不懂的术语或者问题，请立即咨询 AI，或马上向助教求助。

!!! tip "课程推荐 AI 工具"
    可以参考 [LMArena](https://arena.ai/leaderboard/agent) 大模型实时排行榜

    - 排行榜第1名：[Claude](https://claude.ai/)（付费）
    - 排行榜第2名：[ChatGPT](https://chatgpt.com/)（付费）
    - 排行榜第11名：[腾讯元宝](https://yuanbao.tencent.com/)（国内，免费但限流）
    - 排行榜第12名：[DeepSeek-API](https://platform.deepseek.com/)（国内，收费但便宜）

!!! abstract "全程概览"
    本文按顺序做完这 8 步，你就有了一个完整的 C语言开发环境：

    1. 了解为什么用这套方案（可跳过）
    2. 启用 Windows 功能，安装 WSL2
    3. 安装 Ubuntu，创建 Linux 用户
    4. 配置国内网络，安装 GCC / GDB
    5. 写并运行第一个 C 程序
    6. 安装 VSCode，连接到 WSL
    7. （进阶）VSCode 详细配置视频
    8. （进阶）备份系统、迁移到 D 盘

## 1. 为什么推荐 VSCode + WSL 开发模式

### 1.1 为什么要在 Linux 里写代码

!!! quote "延伸阅读"
    想弄明白 Unix 和 Linux 的演化与关系，可以看这期视频：[《操作系统发展史｜仿生之旅》](https://www.bilibili.com/video/BV1Zc411D7sG/)

![《操作系统发展史》视频封面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913211826711.jpg)

C语言就是为了 Unix 操作系统而生的。它不是先被设计好一门语言、再找个操作系统来跑，而是为了重写 Unix 才被造出来的，之后几十年语言和系统一起演化，所以 C语言里到处是 Unix 的影子：

- `main(int argc, char *argv[])` 的参数形态、`stdin` / `stdout` / `stderr` 这三个流、`errno` 这套错误码，全都来自 Unix。
- 那些名字里带 unix 的头文件 —— `unistd.h`（unistd 就是 Unix standard 的缩写）、`sys/wait.h`、`sys/types.h` —— 声明的就是 Unix 那套操作系统接口。这套东西后来被写成了一份正式标准，叫 POSIX，现在的 Linux、macOS 都是照着它实现的。
- 计算机专业课上绕不开的 `fork()`、`pipe()`、`open()` / `read()` / `write()`、信号、文件描述符，全部是 Unix 的概念。
- 连 C语言编译器本身也是：`gcc` 出自 GNU 计划，这是一个为了做出自由版 Unix 而发起的项目。

!!! quote "延伸阅读"
    想了解 GNU 计划和自由软件运动是怎么来的，可以看这期视频：[《计算机博物志·最后的黑客：理查德·马修·斯托曼》](https://www.bilibili.com/video/BV11R4y1b7zc)

![GNU 计划与自由软件运动相关视频封面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913211923938.jpg)

并且 Unix 家族至今仍是世界上使用最广泛的操作系统：安卓手机的底层就是 Linux 内核，全世界的服务器跑的都是 Linux，路由器、机顶盒等所有智能设备里面也跑着它，包括 Mac 和 iPhone 的系统内核同样是 Unix 家族。

也就是说，**在 Linux 环境上写 C语言，用的是这门语言原生的环境**；在 Windows 环境上写 C语言，用的是后来才移植过去的版本，很多 Unix 侧的东西根本没有对应实现。

### 1.2 为什么要使用 WSL

WSL 的全称是 **Windows Subsystem for Linux**，中文叫**「适用于 Linux 的 Windows 子系统」**。它是微软官方提供的一个功能：让你在 Windows 里直接跑一个真正的 Linux 系统 —— 不用装虚拟机软件，也不用装双系统，在 Windows 的终端里敲 Linux 命令就能用。

现在的 WSL2 用的是微软自己编译的真正的 Linux 内核，跑在轻量虚拟化上。

- **工具链完整**：`gcc` / `g++` / `gdb` / `make` 这一整套都是 Linux 原生的，编译、调试、内存检查都有标准做法。
- **性能优异**：WSL2 是真正的 Linux 内核，不是模拟层，编译和运行速度跟原生 Linux 基本没差别，而不是像 VMware 之类的模拟器那样会慢一大截。
- **环境隔离**：Linux 开发环境和 Windows 主机互不干扰，环境搞坏了花几秒钟就能直接删掉重装，Windows 本身不受任何影响。
- **文件系统互通**：Windows 的文件资源管理器能直接看到 WSL 里的文件，反过来也一样。

### 1.3 为什么用 VSCode

VSCode 是目前世界上最主流的代码编辑器 —— 用的人最多、插件生态最丰富、社区最活跃。它本身又足够轻量：装完就能用，插件按需添加，老电脑也跑得动。

对零基础的同学来说，实际能感受到的好处是：

- **智能补全**：敲两三个字母，函数名、参数列表、结构体成员就自动列出来，不用背也不用完整敲出来。写 `str` 会提示 `strlen` / `strcpy` / `strcmp`，还附带参数说明和该引入哪个头文件。
- **写的时候就知道错**：拼错函数名、少个分号、参数类型对不上，编辑器当场画波浪线，不用等到编译才发现。
- **和各种 AI 工具无缝衔接**：GitHub Copilot、Claude Code、Codex 这类工具都有围绕 VSCode 生态做适配，装上插件就能在编辑器里直接对话、讲解代码、解释报错，学习效率完全不一样。
- **一套工具用到底**：C/C++、Python、Verilog、Java、JS/TS、Rust、Go，后面所有的课都能用同一个编辑器，不用每门课换一个工具。
- **调试体验完整**：断点、单步、看变量值、看调用栈，直接调试 WSL 里的 Linux 程序。

### 1.4 为什么 Dev-C++ 只适合暂时过渡

Dev-C++ 是个 2005 年就停止更新的老古董 IDE，内置的是 2004 年的 GCC-3.4.2 和 2002 年的 GDB-5.2.1，比同学们的岁数都大不少。它底层是一套跑在 Windows 上的 MinGW-w64 (GCC) 工具链，编译简单 C 程序没问题，但跑一些复杂偏底层的程序会踩到不少坑。

## 2. 启用 Windows 功能并安装 WSL2 工具

### 2.1 启用 Windows 功能

**按 ++win++ 键**，输入并打开「启用或关闭 Windows 功能」

![在开始菜单搜索「启用或关闭 Windows 功能」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913222107863.png)

在弹出的窗口中，勾选以下两个选项

- 「适用于 Linux 的 Windows 子系统」
- 「虚拟机平台」

确定后会开始安装，然后按提示重启电脑

![勾选「虚拟机平台」和「适用于 Linux 的 Windows 子系统」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914204140810.png)

!!! tip "补充：用命令行做同样的事"
    如果你更喜欢敲命令，上面的勾选框操作等价于在**管理员终端**里执行下面这两条命令：

    ```pwsh title="Windows 终端（管理员）"
    # 启用「适用于 Linux 的 Windows 子系统」
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```

    ```pwsh title="Windows 终端（管理员）"
    # 启用「虚拟机平台」
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

    - 右键开始菜单（或按 ++win+x++），选「**终端(管理员)**」，才能打开管理员终端
    - 两条命令都要看到 `操作成功完成` 才算生效，执行完同样按需要重启电脑


### 2.2 安装 WSL 本体

下载并运行安装包 `wsl.2.7.14.0.x64.msi`：

- **直接下载**：<https://mind-city-1379176255.cos.ap-shanghai.myqcloud.com/wsl.2.7.14.0.x64.msi>
- **官方最新版**：<https://github.com/microsoft/wsl/releases>

!!! warning "GitHub 访问"
    官方仓库有时需要科学上网才能打开。打不开就用上面的直接下载链接，助教已经传好了。

### 2.3 检查是否安装成功

打开终端（**开始菜单搜索「终端」**）

![在开始菜单搜索「终端」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913213618811.png)

!!! tip "如果搜不到「终端」"
    换一个办法打开：按 ++win+r++ 打开「运行」窗口，输入 `cmd`，回车。

输入下面这条命令：

```pwsh title="Windows 终端"
wsl --version
```

安装成功会显示类似下面的输出：

![wsl --version 的正常输出](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913213158133.png)


### 2.4 更新 WSL

安装包自带的是一个固定的版本，微软每隔几周就会发布新版本、加新功能。执行下面这条命令，让 WSL 更新到当前的最新版：

```pwsh title="Windows 终端"
wsl --update
```

## 3. 配置 Ubuntu

### 3.1 下载并安装 Ubuntu

在终端里执行下面这条命令，会**自动下载并安装** Ubuntu 26.04。

```pwsh title="Windows 终端"
wsl --install -d Ubuntu-26.04
```

!!! tip "下载很慢或者连接超时怎么办"
    先按 ++ctrl+c++ **终止下载**，然后再重新输入指令下载，多试几次通常就能成。

!!! tip "还是慢？用助教准备的离线安装包"
    助教已经提前把安装包传到了腾讯云存储桶，可以先下载到本地，再从本地安装：

    ```pwsh title="Windows 终端"
    # 先将 Ubuntu-26.04 的安装包下载到临时目录
    curl.exe -Lo $env:TEMP\ubuntu-26.04.wsl https://mind-city-1379176255.cos.ap-shanghai.myqcloud.com/ubuntu-26.04.1-wsl-amd64.wsl

    # 再从临时目录安装 Ubuntu-26.04
    wsl --install --from-file $env:TEMP\ubuntu-26.04.wsl --name Ubuntu-26.04
    ```

### 3.2 卸载刚才安装的 Ubuntu

既然学会了安装，就顺便学会卸载吧 —— 以后环境搞坏了，**重来一次就是这两条命令**。

```pwsh title="Windows 终端"
# 查看当前已经安装了哪些发行版
wsl --list

# 注销(卸载)刚才安装的 Ubuntu
wsl --unregister Ubuntu-26.04
```

!!! note "卸载不会删除你的代码文件"
    但如果文件放在 WSL 内部，卸载后会被一起删掉。重要代码记得备份到 Windows 侧或者 Git 仓库。

### 3.3 首次启动：创建你的 Linux 用户

![首次启动 Ubuntu 时的创建账号提示](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913222827482.png)

等安装好之后，会出现创建账号的提示。用户名那一栏已经预填好了你的 Windows 用户名，**推荐改成别的名字**（比如你的英文名）。

![设置 Linux 用户密码](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913223100271.png)

- **推荐使用 `123456`** 这种简单密码，或者想一个其他容易输入的密码
- 以后执行命令**经常要输好几遍密码**，如果密码太复杂，敲起来很麻烦
- 这是你自己电脑的子系统，不必担心安全性问题

!!! warning "输入密码时屏幕上不会有任何显示"
    连星号都没有。这是 Linux 密码程序的正常设计，**不是键盘坏了**，输入之后按回车就行。

当你看到类似下面这样的提示符，就说明装好了：

```text title="Ubuntu 终端"
ethan@Ethan-Asus:~$
```

恭喜你，你已经成功安装了属于自己的 Linux 系统！

以后在 Windows 终端里敲 `wsl` 或者 `wsl -d Ubuntu-26.04` 就能直接进入这个系统。

### 3.4 让 Ubuntu 关机

关掉 Ubuntu 的终端窗口之后，**过几秒钟**这套 Linux 系统就会自动停止运行。手动关机就是在 Windows 终端里执行：

```pwsh title="Windows 终端"
wsl --shutdown
```

### 3.5 让 Ubuntu 开机

以后每次要用 Linux，有两种方式把它打开。

=== "方式一：敲命令"

    在 Windows 终端里敲：

    ```pwsh title="Windows 终端"
    wsl
    ```

    不跟任何参数时，`wsl` 会进入**「默认发行版」**。如果你只装了 Ubuntu-26.04 这一个，那它本来就是默认的，敲 `wsl` 就够用了。

    如果以后装了不止一个发行版，可以用 `-d` 指定这次进哪一个：

    ```pwsh title="Windows 终端"
    wsl -d Ubuntu-26.04
    ```

    嫌每次都要多打一段 `-d Ubuntu-26.04` 麻烦的话，可以把它设成默认发行版：

    ```pwsh title="Windows 终端"
    # 设置 Ubuntu-26.04 为默认发行版
    wsl --set-default Ubuntu-26.04

    # 查看当前默认发行版
    wsl --list
    ```

=== "方式二：从开始菜单启动"

    按 ++win++ 键打开开始菜单，直接输入 `Ubuntu-26.04`。

    **推荐点上「固定到"开始"屏幕」**，以后点一下就能打开。

    ![在开始菜单中把 Ubuntu-26.04 固定到开始屏幕](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913231050196.png)

## 4. 配置网络并安装 GCC / GDB

Ubuntu 的软件都要从网上下载，所以这一步先把网络理顺，再更新软件列表，最后装编译工具。

- 如果你**不**熟悉科学上网 → 走 [4.1 切换镜像源](#41-切换镜像源可选)
- 如果你熟悉科学上网 → 走 [4.2 配置网络代理](#42-配置网络代理可选)

!!! tip "两个都做也可以"
    配了代理之后仍然推荐再配一下镜像源 —— 速度更快，还能省流量。以后用 `pip` 装大型 Python 包的时候体会更深。

上面的 4.1 / 4.2 **二选一**即可，走完任意一条就继续往下做 [4.3 更新软件列表](#43-更新软件列表)。

### 4.1 切换镜像源（可选）

Ubuntu 的 apt 软件管理工具默认会从国外的服务器下载软件，**速度很慢甚至超时**。如果不熟悉科学上网，可以先使用腾讯云的国内镜像源加速。

![腾讯云镜像源配置界面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913224450975.png)

```bash title="Ubuntu 终端" linenums="1"
# 记得要一次性完整复制下面这几行的内容
# 参见上图终端中显示的内容
# 从 sudo 命令开始，到 EOF 结束
sudo tee /etc/apt/sources.list.d/ubuntu.sources << 'EOF'
Types: deb deb-src
URIs: https://mirrors.tencent.com/ubuntu/
Suites: resolute resolute-updates resolute-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb deb-src
URIs: https://mirrors.tencent.com/ubuntu/
Suites: resolute-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
EOF
```

!!! tip "更多镜像站"
    官方有一个镜像站汇总平台：[MirrorZ](https://help.mirrorz.org/ubuntu/)。腾讯云镜像不可用时可以在这里换一家。

### 4.2 配置网络代理（可选）

如果你在 Windows 上已经装好了科学上网软件（比如 Clash），可以让 WSL 直接复用 Windows 的代理。这样在 WSL 里 `apt install` 下载软件时走的就是代理通道，不用再单独给 Linux 配一遍。

WSL 的全局配置存在 Windows 用户目录下的 `.wslconfig` 文件里。**默认是没有这个文件的，需要我们自己新建一个。**

---

#### 第 1 步：打开你的用户目录

打开文件资源管理器，进入你的用户目录，它的路径是：

```text
C:\Users\<你的用户名>
```

**如果懒得去找这个路径**，可以在资源管理器顶部的地址栏直接输入 `%UserProfile%` 再回车，就会跳转到你的用户目录。

![在资源管理器地址栏输入 %UserProfile%](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913230242391.png)

---

#### 第 2 步：让文件显示扩展名

点击窗口上方的「查看」菜单，在展开的「显示」子菜单里，**勾上「文件扩展名」**。

![在「查看 → 显示」中勾选「文件扩展名」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913225251762.png)

!!! warning "这一步不能跳过"
    Windows 默认会把扩展名藏起来，于是 `新建文本文档.txt` 在你眼里只显示成「新建文本文档」。

    不开这个开关，等下重命名时就会把它改成 `.wslconfig.txt`，而 WSL 只会读取文件名是 `.wslconfig` 的配置文件 —— 结果就是配置**看起来做了但完全不生效**。

---

#### 第 3 步：创建 `.wslconfig` 并粘贴配置

在文件夹的空白处点右键 → 新建 → 文本文档，把文件名（**连同 `.txt` 后缀一起**）改成：

```text
.wslconfig
```

改完回车，Windows 会弹一个「如果改变文件扩展名，文件可能不可用」的提示，**点「是」**。

改成功后，这个文件的类型一栏会显示成「WSLCONFIG 文件」，图标也变成一张白纸，跟图上一样。

然后双击打开 `.wslconfig`（如果问用什么程序打开，选「记事本」），把下面两行粘进去，**记得一定要 ++ctrl+s++ 保存**，然后再关掉：

```ini title=".wslconfig"
[wsl2]
autoProxy=true
networkingMode=mirrored
```

- `networkingMode=mirrored`：让 WSL 和 Windows **共用同一套网络**。
- `autoProxy=true`：让 WSL **自动读取并同步** Windows 当前的代理设置。

![改好后的 .wslconfig 文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913225359625.png)

---

#### 第 4 步：重启 WSL 让配置生效

`.wslconfig` **只在 WSL 启动时读取一次**，改完必须让 WSL 重启才能生效。打开 Windows 终端，执行命令先让 WSL 关机：

```pwsh title="Windows 终端"
wsl --shutdown
```

---

#### 第 5 步：验证代理是否打通

重新打开 Ubuntu-26.04，在 Ubuntu 窗口里执行：

```bash title="Ubuntu 终端"
echo $http_proxy
```

能打印出形如 `http://127.0.0.1:7890` 的地址，**就说明代理已经打通了**。

再尝试一下能不能真的访问谷歌：

```bash title="Ubuntu 终端"
curl google.com
```

如果显示下图结果，恭喜你成功让 WSL 复用了 Windows 的代理。

![curl google.com 成功返回的结果](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913231556126.png)

!!! tip "顺便把 pip 也加速一下"
    `pip` 是 Python 的包管理工具，默认也从国外服务器下载包，速度很慢。配好镜像源或代理之后，装大型包的时候会轻松很多。

### 4.3 更新软件列表

网络理顺之后，装任何软件之前都要先更新一下软件列表。

**不管你走的是 4.1 还是 4.2，这一步都要做。**

`apt` 按一份**软件版本列表**来知道服务器上现在有哪些软件、各自是什么版本。这份列表是装系统时缓存下来的，会越来越旧：有可能某个软件已经修了 bug、发了新版本，但你的机器还不知道。

所以要**先拉取**当前最新的软件版本列表：

```bash title="Ubuntu 终端"
sudo apt update
```

**再对照着**最新的软件列表，把系统里已经安装的软件升级到最新版本：

```bash title="Ubuntu 终端"
sudo apt upgrade -y
```

`-y` 的意思是对所有「是否继续」的询问都自动回答「是」，省得你还需要手动确认。

### 4.4 安装 GCC / GDB

先说说这几个东西是干什么的：

- **gcc**（GNU Compiler Collection，GNU 编译器套件）是 C语言的编译器：负责把 C 代码翻译成能跑的可执行程序
- **gdb**（GNU Debugger）是 C语言的调试器：负责单步执行、看变量的值如何变化、定位程序是怎么崩溃报错的
- **build-essential** 是一组基础编译工具的合集包：除了 gcc 和 g++，还包含 make 和 C 标准库的开发文件。只装 gcc 有时会因为缺头文件编译不过，装它一次到位，后面的《Make 构建工具》也要用它

!!! warning "装之前先确认你做过 4.3 的 `sudo apt update`"
    这是同学漏得最多的一步。跳过它直接装，`apt` 手上还是一份很旧的软件列表，经常直接报 `E: Unable to locate package gcc`，或者装上一个早该换掉的旧版本。

    不确定自己做过没有？**就当没做过，先补一条**（重复执行没有任何坏处）：

    ```bash title="Ubuntu 终端"
    sudo apt update
    ```

开始安装：

```bash title="Ubuntu 终端"
sudo apt install -y gcc gdb build-essential
```

验证一下是否安装成功：

```bash title="Ubuntu 终端"
gcc --version
```

![gcc --version 的输出](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913232920110.png)

## 5. 写第一个 C 程序

### 5.1 用记事本写代码

在 WSL 窗口里输入：

```bash title="Ubuntu 终端"
notepad.exe hello.c
```

会弹出 Windows 的记事本。

这里用到了 WSL 一个很方便的特性：**它能直接调用 Windows 里的程序**。`notepad.exe` 就是 Windows 自带的记事本，但它打开的 `hello.c` 是 WSL 里的那个文件 —— 你不用关心文件到底存在哪一边。

!!! tip "如果记事本提示找不到文件"
    问你要不要新建，点「是」就行。

把下面的代码粘进记事本，**++ctrl+s++ 保存**，然后关掉它：

```c title="hello.c"
--8<-- "code/hello.c"
```

!!! warning "要注意中文输入法的标点，不然代码很容易编译不过"

    这是初学者最容易踩的坑：**中文输入法打出来的引号、分号、括号是汉字全角的**，而 C语言只认英文半角标点。屏幕上看着差不多，编译器却会报一堆看不懂的错，盯半天都找不出问题。

    花一分钟按下面两步处理掉，之后再写代码会顺很多。

    ---

    **第一步：加一个英语输入法**

    中文输入法下，写代码时误触 ++shift++ 就会切到中文。更稳妥的做法是**单独添加一个英语输入法**，这样中英文各用各的，互不干扰。

    打开「设置 → 时间和语言 → 语言和区域」，在「首选语言」里点**「添加语言」**，搜索并添加**「英语(美国)」**。

    ![在「首选语言」中添加英语(美国)输入法](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914223505078.png)

    添加之后，按 ++alt+shift++ 就能在中文和英文输入法之间切换：
    
    写代码时切到英文，写注释时再切回中文。

    ---

    **第二步：如果还嫌切换麻烦，可以让中文输入法直接输出英文标点**

    进入「设置 → 时间和语言 → 语言和区域 → 微软拼音输入法 → 常规」，打开**「中文输入时使用英文标点」**：

    打开后，即使输入法处于中文状态，打出来的也是英文半角符号，不用再切来切去了。
    
    偶尔写作需要写中文标点时，再去设置里把开关临时关掉即可。

    ![在微软拼音输入法的常规设置中打开「中文输入时使用英文标点」](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914223321449.png)




回到 WSL 窗口，编译并运行刚才的代码：

```bash title="Ubuntu 终端"
gcc hello.c -o hello   # 编译代码，得到可执行文件 hello
./hello                # 运行可执行文件 hello
```

屏幕输出 `Hello, Fudan!`，**恭喜你的第一个程序成功跑起来了**。

!!! quote "延伸阅读：为什么需要学 vim"
    Linux 上最经典的编辑器是 vim，几乎所有服务器都预装了它，而别的编辑器多半没有。以后你连到服务器或者其他远程机器上时，往往就只有 vim 能用。

    想学习 vim，可以看这期视频：[《保姆级入门：Vim 编辑器》](https://www.bilibili.com/video/BV13t4y1t7Wg)

## 6. 安装 VSCode 及插件并连接到 WSL

### 6.1 安装 VSCode

下载 VSCode 的 Windows 版安装包，双击安装：

- **直接下载**：<https://mind-city-1379176255.cos.ap-shanghai.myqcloud.com/VSCodeUserSetup-x64-1.137.0.exe>
- **官方最新版**：<https://code.visualstudio.com/Download>

安装向导里的**「通过 Code 打开」**和**「添加到 PATH」**两个选项都勾上：

- 「通过 Code 打开」：能在 Windows 文件管理器里右键点击文件夹，直接用 VSCode 打开。
- 「添加到 PATH」：能在 Windows 终端里直接敲 `code` 命令来打开 VSCode。

![VSCode 安装向导中勾选这两个选项](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913233303957.png)

### 6.2 安装插件

![VSCode 左侧边栏的「扩展」按钮](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913233649921.png)

打开 VSCode，**点击左侧边栏的「扩展」**（Extensions，方块图标），搜索并安装下面这几个：

| 插件名                             | 说明                    | 是否必装 |
| ---------------------------------- | ----------------------- | ------ |
| WSL                                | 让 VSCode 能连进 WSL    | 是     |
| C/C++                              | C语言语法高亮、代码提示 | 是     |
| Code Runner                        | 一键运行代码的小插件    | 是     |
| Chinese (Simplified) Language Pack | 中文界面                | 可选   |

!!! tip "建议用英文界面"
    推荐大家尽量使用英文界面，这样之后修改配置文件会方便很多，也能和网上搜到的教程对得上。

### 6.3 连接到 WSL

在 WSL 窗口里输入：

```bash title="Ubuntu 终端"
# 注意 "code" 和 "." 之间需要加个空格
# 接触命令行之后就能知道，这里的 "." 是当前目录的意思
# 所以这条命令的意思就是「用 VSCode 打开当前目录」
code .
```

VSCode 会打开，并且**自动连上 WSL**。窗口标题和左下角都会变成 `WSL: Ubuntu-26.04`。

![VSCode 左下角显示 WSL: Ubuntu-26.04](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913234038421.png)

**首次连接时**，VSCode 会自动往 Ubuntu 里装一个服务端组件。

### 6.4 把插件再在 WSL 里装一遍

!!! warning "这里有个很容易踩的坑"
    6.2 节装的那几个插件，是装在你 **Windows 上的 VSCode** 里的，其中一部分在 WSL 里不会生效。

VSCode 其实是分两端的：界面跑在 Windows 上，但真正读写代码、执行命令的那一端在 Ubuntu 里。

插件也是分两端的：

- 像 **WSL** 这种负责「连接」的插件，装在 Windows 端就够了
- 但 **C/C++**、**Code Runner** 这种要调用编译器工具、真正跑起代码的插件，必须装进 WSL 那一端才能生效

所以回到左侧的「扩展」面板，你会看到刚才装过的插件下面多了一行小字：`Install in WSL: Ubuntu-26.04`。找到 **C/C++** 和 **Code Runner**，点这个按钮，把它们在 WSL 里再装一遍。

![扩展面板中出现的 Install in WSL 按钮](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913234609008.png)

!!! tip "记住这个规律"
    以后凡是 VSCode 弹窗提示某个插件需要 `Install in WSL`，直接点它就行。养成习惯之后，这一步花不了几秒钟，但能省掉后面一大堆莫名其妙的报错。

### 6.5 编辑并运行代码

左侧文件栏里应该能看到第 5 节写的 `hello.c`，**点开它**。

运行代码，两种方式任选：

=== "方式一：点击运行按钮"

    点右上角的 ▷ 三角按钮（由 Code Runner 插件提供）。

=== "方式二：在终端里运行"

    使用快捷键 ++ctrl+grave++（键盘 Esc 下面那个飘号键 `~`）打开终端，在里面敲：

    ```bash title="Ubuntu 终端"
    gcc hello.c -o hello && ./hello
    ```

## 7. 进阶补充：VSCode 详细配置（视频，强烈推荐）

第 6 节只讲了把第一个程序跑起来所必需的最精简配置。想让 VSCode 真正好用起来（界面外观、常用插件、C/C++ 的调试与构建），下面这两期视频讲得很细，**非常建议大家跟着做一遍**：

- [《VSCode 配置 | 外观 | 通用型扩展 | Minimal》](https://www.bilibili.com/video/BV1YW4y1M7uX)
- [《VSCode 配置 | C/C++ | MakeFile | CMake | Minimal》](https://www.bilibili.com/video/BV1H24y1D7Kn)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914214817142.jpg)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914214845964.jpg)


## 8. 进阶补充：备份操作系统，以及迁移到 D 盘

WSL 里的 Ubuntu 说到底就是一堆文件。WSL 为此提供了一对命令：可以把整套系统原样打包成一个 tar 文件，也可以把这个 tar 文件还原成一套能直接跑的系统。

- **备份与还原**：装好的软件、写的代码、改过的配置，全部都在这个包里。系统哪天玩坏了、或者想推倒重来，一条命令就能还原回去，不用从头再装一遍。
- **拷给别人直接用**：把 tar 包发给同学，对方导入之后，得到的就是和你一模一样的环境 —— 一样的 gcc、一样的 apt 源、连你装过的插件配置都在。省掉了从头配一遍的全部时间。
- **搬到别的盘**：WSL 的 Ubuntu 默认装在 C 盘。如果 C 盘吃紧，把系统还原到 D 盘就行，别的什么都不用改。

下面以「迁移到 D 盘」为例走一遍完整流程。**打包和还原这两步在三种用途里是完全一样的**，区别只在于 tar 包最终放到哪里 —— 备份就放到移动硬盘，发给别人就传过去。

先看一眼当前装了哪些发行版：

```pwsh title="Windows 终端"
wsl --list
```

导出之前**必须先关掉 WSL**，否则文件正在被占用：

```pwsh title="Windows 终端"
# 关掉 WSL
wsl --shutdown

# 导出 Ubuntu-26.04 并打包成为 D 盘的压缩包
wsl --export Ubuntu-26.04 D:\Ubuntu-26.04.tar
```

然后把导出好的系统重新导入到 D 盘：

```pwsh title="Windows 终端"
# 先注销掉默认跑在 C 盘上的 Ubuntu-26.04
wsl --unregister Ubuntu-26.04

# 重新导入到 D 盘上
# --import 的三个参数依次是：发行版名字、新的安装目录、压缩包的路径
wsl --import Ubuntu-26.04 D:\Ubuntu-26.04 D:\Ubuntu-26.04.tar
```

!!! warning "C 盘和 D 盘可能只是同一块物理硬盘"
    如果电脑实际只插了一块物理硬盘，C 盘和 D 盘只是同一块盘上的两个虚拟分区，并且 C 盘空间快炸了，那「把系统搬到 D 盘」就只是把左手倒右手。

    这种情况下的重点不是搬文件，而是应该去合并分区。
