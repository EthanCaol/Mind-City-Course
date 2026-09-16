
# macOS + GCC + VSCode 环境搭建

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>实验课时间：<strong>2026-9-16</strong></span></p>

!!! warning "本篇内容由 AI 生成"
    助教没有使用过 Mac，所以本文的内容是由 AI 生成的，助教只做了**语法和逻辑上的初步校对**。

    如果你在 Mac 上遇到问题，请**优先向 AI 咨询**，或者向助教求助。

面向零基础、使用 Mac 的同学。Mac 上要装的东西比 Windows 少得多 —— 编译器本来就是系统自带的，全过程只需要在终端里粘几条命令，**不需要任何前置知识**。中途遇到任何不懂的术语或者问题，请立即咨询 AI，或马上向助教求助。

!!! tip "如果你用的是 Windows"
    请改看 [(0) WSL2 环境搭建](wsl2-vscode.md)，那边的步骤和本文完全不一样。

!!! tip "课程推荐 AI 工具"
    可以参考 [LMArena](https://arena.ai/leaderboard/agent) 大模型实时排行榜

    - 排行榜第1名：[Claude](https://claude.ai/)（付费）
    - 排行榜第2名：[ChatGPT](https://chatgpt.com/)（付费）
    - 排行榜第11名：[腾讯元宝](https://yuanbao.tencent.com/)（国内，免费但限流）
    - 排行榜第12名：[DeepSeek-API](https://platform.deepseek.com/)（国内，收费但便宜）

!!! abstract "全程概览"
    本文按顺序做完这 6 步，你就有了一个完整的 C语言开发环境：

    1. 了解 Mac 上为什么这样配（可跳过）
    2. 安装 Xcode Command Line Tools，也就是编译器
    3. 安装 VSCode 及插件
    4. 写并运行第一个 C 程序
    5. 学会用 lldb 调试程序
    6. （进阶）在 VSCode 里图形化调试

## 1. 为什么 Mac 上这样配

### 1.1 macOS 本身就是 Unix

WSL 篇里说过，C语言是为了 Unix 而生的。而 macOS 的内核 Darwin 正是从 BSD Unix 演化来的，还是通过了正式 UNIX 认证的系统 —— 也就是说，**在 Mac 上写 C语言，用的同样是这门语言原生的环境**。

最直接的体现就是：终端里敲的 `ls`、`cd`、`gcc`、`./hello` 这些命令，和 Linux 里几乎一模一样。以后你在 WSL 篇或者网上看到的 Linux 命令，在 Mac 上大多能直接照着敲。

少数几个习惯上的差异，先混个眼熟，遇到再回来查：

| 想干的事       | Ubuntu（Linux）         | macOS                              |
| -------------- | ----------------------- | ---------------------------------- |
| 家目录在哪里   | `/home/ethan`           | `/Users/ethan`                     |
| 装一个软件     | `sudo apt install 软件` | `brew install 软件`（要另装 Homebrew） |
| 用默认程序打开 | `xdg-open 文件`         | `open 文件`                        |
| 默认的 shell   | bash                    | zsh                                |

### 1.2 为什么不用装 WSL 或者虚拟机

WSL 是 Windows 独有的功能，Mac 上用不了，**也不需要** —— Mac 自己就是 Unix 家族的系统。

在 Mac 上装虚拟机（Parallels、VMware）再跑一个 Linux 当然也可以，但那要多占几十 GB 硬盘和一大块内存，还会让电脑变烫变卡。对只想写 C 作业的同学来说，这是纯负担。

### 1.3 Mac 上的 `gcc` 其实是 clang

这一点必须说清楚，否则你敲 `gcc --version` 时会以为自己装错了。

- **真正的 GNU GCC** 在 Mac 上没有预装，要用的话得另外装（见 [第 7 节](#7-进阶补充想装真正的-gnu-gcc可选)）。
- **Mac 自带的是 Apple clang** —— 它是 LLVM 项目出品的 C/C++ 编译器，由苹果随 Xcode 一起提供。
- clang 和 GCC 是**两个独立实现**，但都完整实现了同一套 C 语言标准。写课程里的程序，用哪个都没有区别。
- 为了让大家能直接抄课程里的命令，Mac 上同样保留了 `gcc` 这个名字：敲 `gcc hello.c -o hello` 照样能跑，只是背后干活的其实是 clang。

所以待会儿看到 `gcc --version` 打印出 `Apple clang version ...`，**这是正常的，不是装错了**。

### 1.4 调试器：Mac 上讲 lldb，不是 gdb

同样地，gdb 在 Mac 上能装，但**开箱跑不起来**：苹果对「调试别的进程」这件事做了权限限制，装完还得用 `codesign` 给 gdb 签一个特殊权限、再去「系统设置 → 隐私与安全性」里手动授权，才肯干活。这一步非常容易卡住，而且没有什么教学价值。

Mac 上原生的调试器是 **lldb**，它和 gdb 是同一类工具（同一个 LLVM 项目出品），功能一样，**常用命令可能连名字都一样**（`run`、`next`、`break`、`print`）。

所以本文第 5 节讲 lldb。以后你在网上搜到 gdb 的教程，[5.3 节](#53-和-gdb-的命令对照表)给了一张对照表，照着换一下就能用。

## 2. 安装 Xcode Command Line Tools

编译器不用自己装，但要让 Mac 把它交出来 —— 苹果把这套命令行工具单独打了一个包，叫 **Xcode Command Line Tools**（简称 CLT）。

### 2.1 安装

先打开终端：按 ++cmd+space++ 打开聚焦搜索，输入 `终端` 或 `Terminal`，回车。

然后在终端里输入这条命令：

```bash title="终端"
xcode-select --install
```

回车后会弹出一个对话框，点「**安装**」，同意许可协议，然后等它下载完。

!!! warning "只装命令行工具，不要装完整的 Xcode"
    完整的 Xcode 是给 iOS/macOS 开发用的，十几 GB，而你要的编译器只是里面的一小部分。

    - 在弹出的对话框里点「安装」（安装命令行工具）就够了
    - **不要**去 App Store 搜 Xcode 然后装它
    - 如果弹出的对话框里只有「获取 Xcode」而没有「安装」，说明你的系统版本比较特殊，直接来找助教

<!-- 待补图：xcode-select --install 弹出的「安装命令行工具」对话框 -->
<!-- 待补图：安装进度窗口 -->

几点补充：

- 这个包有几百 MB，视网速要几分钟到十几分钟，**期间终端会一直没有反应，这是正常的**。
- 如果命令直接返回 `command line tools are already installed`，说明之前已经装过了，不用再装，直接做下面的验证。
- 如果装完之后系统提示你需要同意许可协议，执行 `sudo xcodebuild -license accept`，然后一路回车。

### 2.2 验证

```bash title="终端"
gcc --version
```

只要输出里出现 **`Apple clang version`** 和 **`Target: ...-apple-darwin...`** 这两行，就说明装好了：

```text title="输出示例"
Apple clang version 17.0.0 (clang-1700.0.13.3)
Target: arm64-apple-darwin25.0.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```

**版本号跟你看到的不一样很正常**，不用管。另外不用去纠结 `Target` 里是 `arm64` 还是 `x86_64` —— 那只是说明你的 Mac 是 Apple 芯片还是 Intel 芯片，对写 C 程序没有任何影响。

敲 `clang --version` 会打印出完全一样的内容，因为它们本来就是同一个东西。

## 3. 安装 VSCode 及插件

### 3.1 下载并安装 VSCode

打开下载页：<https://code.visualstudio.com/Download>

页面上有**两个** Mac 版本，选错了通常也能跑起来（系统会自动装一个翻译层），但会明显变慢，所以先确认自己该下哪个：

- 点屏幕左上角的苹果菜单 →「**关于本机**」，看「芯片」（或「处理器」）那一行
- 写着 **Apple M1 / M2 / M3 …** 的 → 下 **Apple silicon** 版
- 写着 **Intel** 的 → 下 **Intel chip** 版

下载下来是一个 `.zip`，双击解压，会得到一个 `Visual Studio Code.app`。

!!! warning "一定要把它拖进「应用程序」文件夹"
    不要把 `.app` 留在「下载」文件夹里直接双击使用。

    VSCode 有一个「把 `code` 命令装进终端」的功能，它会记住这个 `.app` **当前所在的位置**。如果你现在从「下载」里打开，那个命令就永久指向了下载目录 —— 哪天你清理下载文件夹，`code` 命令就莫名其妙地失灵了。

    正确做法：在访达里把 `Visual Studio Code.app` **拖到左侧边栏的「应用程序」**里。以后从启动台打开它。

第一次打开时会提示「这是从互联网下载的，确定要打开吗」，点「**打开**」即可。

### 3.2 把 `code` 命令装进终端

装好之后，在终端里敲 `code .` 就能用 VSCode 打开当前文件夹 —— 这个命令要手动开一下。

在 VSCode 里按 ++cmd+shift+p++ 打开命令面板，输入 `shell command`，选中 **Shell Command: Install 'code' command in PATH**。

装好之后**要把终端窗口关掉重新开一个**才会生效（终端只在启动时读一次 PATH）。验证一下：

```bash title="终端"
code --version
```

有版本号输出就成功了。

### 3.3 安装插件

![VSCode 左侧边栏的「扩展」按钮](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260913233649921.png)

打开 VSCode，**点击左侧边栏的「扩展」**（Extensions，方块图标），搜索并安装下面这几个：

| 插件名                             | 说明                          | 是否必装 |
| ---------------------------------- | ----------------------------- | -------- |
| C/C++                              | C语言语法高亮、代码提示       | 是       |
| Code Runner                        | 一键运行代码的小插件          | 是       |
| CodeLLDB                           | 图形化调试（第 6 节要用）     | 是       |
| Chinese (Simplified) Language Pack | 中文界面                      | 可选     |

!!! tip "建议用英文界面"
    推荐大家尽量使用英文界面，这样之后修改配置文件会方便很多，也能和网上搜到的教程对得上。

!!! note "Mac 上没有「装两遍插件」这回事"
    WSL 篇里提醒过一个坑：插件要装在 WSL 那一端才生效。**那是 WSL 特有的**，因为那里分了「Windows 端」和「Linux 端」两个部分。

    Mac 上界面和编译器都在同一台机器里，装一遍就是装好了，不用管这回事。

## 4. 写并运行第一个 C 程序

### 4.1 建一个放代码的文件夹

回到终端，把下面三行依次粘贴进去：

```bash title="终端"
mkdir -p ~/CppPractice/lesson01   # 在家目录下建好这几层文件夹
cd ~/CppPractice/lesson01         # 进入这个文件夹
code .                            # 用 VSCode 打开当前文件夹
```

三个东西解释一下：

- `~` 是**家目录**的意思，也就是 `/Users/你的用户名`。`mkdir -p` 会一次把中间缺的文件夹都建好。
- `cd` 是 change directory，切换当前所在目录。
- `code` 后面的 `.` 是**当前目录**的意思，所以这条命令就是「用 VSCode 打开当前目录」。

!!! tip "如果提示 `code: command not found`"
    说明 3.2 那一步没成功，或者终端没重开。回去重做一遍即可。

VSCode 打开后，左侧文件栏会显示这个文件夹（现在是空的）。

### 4.2 写代码

在左侧文件栏里点「新建文件」图标，把文件名填成 `hello.c`（**注意扩展名是 `.c`，不是 `.txt`**）。

然后把下面的代码粘进去：

```c title="hello.c"
--8<-- "code/hello.c"
```

!!! warning "要注意中文输入法的标点，不然代码很容易编译不过"

    这是初学者最容易踩的坑：**中文输入法打出来的引号、分号、括号是汉字全角的**，而 C语言只认英文半角标点。屏幕上看着差不多，编译器却会报一堆看不懂的错，盯半天都找不出问题。

    Mac 上切换中英文输入法，默认是**按 ++caps lock++ 键**（也可以按 ++ctrl+space++）。写代码时就切到英文，写注释时再切回中文。

    嫌切来切去麻烦的话，也可以换一个第三方中文输入法（搜狗、微信输入法之类），它们一般都有「中文状态下使用英文标点」的开关。

按 ++cmd+s++ 保存。**养成习惯：写几行就保存一次**，编译的永远是你保存过的那个版本。

### 4.3 编译并运行

打开 VSCode 内置的终端：按 ++ctrl+grave++（键盘左上角 Esc 下面那个飘号键 `` ` ``）。

!!! warning "这里用的是 ++ctrl++，不是 ++cmd++"
    VSCode 的内置终端快捷键在所有系统上都是 ++ctrl+grave++，Mac 上也一样。这是少数几个 Mac 上不用把 ctrl 换成 cmd 的地方。

这个终端**直接就开在你刚才那个文件夹里**，不用再 `cd`。输入：

```bash title="VSCode 终端"
gcc hello.c -o hello   # 编译代码，得到可执行文件 hello
./hello                # 运行可执行文件 hello
```

屏幕输出 `Hello, Fudan!`，**恭喜你的第一个程序成功跑起来了**。

两个细节：

- `-o hello` 是「output」的意思，指定编译出来的可执行文件叫什么名字。不写的话会默认叫 `a.out`。
- `./hello` 前面的 `./` 表示「当前目录下的」。Mac 和 Linux 出于安全考虑，**不会自动去当前目录里找程序来执行**，所以这个 `./` 不能省。

顺带一提，VSCode 右上角那个 ▷ 三角按钮（由 Code Runner 插件提供）也能一键运行代码。但**刚开始建议老老实实敲命令**，知道背后发生了什么，出了问题才有办法排查。

!!! quote "延伸阅读：为什么需要学 vim"
    Linux 上最经典的编辑器是 vim，几乎所有服务器都预装了它，而别的编辑器多半没有。以后你连到服务器或者其他远程机器上时，往往就只有 vim 能用。

    想学习 vim，可以看这期视频：[《保姆级入门：Vim 编辑器》](https://www.bilibili.com/video/BV13t4y1t7Wg)

## 5. 用 lldb 调试程序

程序跑不出预期结果是常态，这时候就需要调试器。**调试器能让你把程序的执行按暂停键**，一行一行地看着变量怎么变、程序是怎么走到崩溃的那一步的。

为了有东西可看，这一节换一个稍微长一点的程序：算 1 到 5 的和。

在 VSCode 里新建文件 `sum.c`，粘进去：

```c title="sum.c"
--8<-- "code/sum.c"
```

### 5.1 编译时加上 `-g`

```bash title="VSCode 终端"
gcc -g sum.c -o sum
```

`-g` 的意思是让编译器把**变量名、行号**这些调试信息一起写进可执行文件里。不加 `-g` 也能调试，但你在调试器里只能看到一堆内存地址和汇编指令，看不见 `sum` 和 `i` 这些名字。

### 5.2 启动 lldb

```bash title="VSCode 终端"
lldb ./sum
```

回车之后会进入 lldb 自己的提示符 `(lldb)`，接下来输入的都是 lldb 的命令，**不是 shell 命令**了。

下面这段会话就是这一节要做的事：在 `main` 开头和循环体里各下一个断点，然后一次次继续运行，看着 `sum` 一轮轮变大。

```text title="lldb 会话（地址、进程号每次都不同，对不上是正常的）"
$ lldb ./sum
(lldb) breakpoint set --name main
Breakpoint 1: where = sum`main + 20 at sum.c:4:14, address = 0x100003f74
(lldb) breakpoint set --file sum.c --line 6
Breakpoint 2: where = sum`main + 84 at sum.c:6:9, address = 0x100003fb4
(lldb) run
Process 4321 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x100003f74 sum`main at sum.c:4:14
   1   	#include <stdio.h>
   2   	
   3   	int main() {
-> 4   	    int sum = 0;
(lldb) continue
Process 4321 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 2.1
    frame #0: 0x100003fb4 sum`main at sum.c:6:9
   4   	    int sum = 0;
   5   	    for (int i = 1; i <= 5; i++) {
-> 6   	        sum += i;
(lldb) frame variable
(int) sum = 0
(int) i = 1
(lldb) continue
(lldb) frame variable
(int) sum = 1
(int) i = 2
(lldb) continue
(lldb) frame variable
(int) sum = 3
(int) i = 3
(lldb) continue
(lldb) frame variable
(int) sum = 6
(int) i = 4
(lldb) continue
(lldb) frame variable
(int) sum = 10
(int) i = 5
(lldb) continue
sum = 15
Process 4321 exited with status = 0 (0x00000000)
(lldb) quit
```

看明白这段会话，你就掌握调试的核心思路了：

1. **下断点**：告诉调试器「执行到这一行就停下来」。这里下了两个：一个在 `main` 开头，一个在循环体第 6 行。
2. **运行**：`run` 让程序跑起来，停在第一个断点处。箭头 `->` 指着当前停在哪一行。
3. **继续到下一个断点**：`continue` 让它接着跑，这次停在了循环体里第 6 行。
4. **看变量**：`frame variable` 打印出当前函数里所有变量的值 —— `sum` 是 0，`i` 是 1。因为断点停在这一行**执行之前**，所以此时 `i` 还没加进 `sum`。
5. **反复继续**：每 `continue` 一次，就停到下一轮循环。`sum` 依次变成 1、3、6、10 —— **循环原来是这样一轮轮加上去的，一眼就能看明白**。
6. **跑完**：最后一次 `continue` 加上了 5，循环结束，打印出 `sum = 15`（1+2+3+4+5）。
7. **退出**：`quit` 离开 lldb。

!!! tip "想看每一行是怎么执行的，把 `continue` 换成 `next`"
    `next` 就是**单步**：每敲一次，只执行一行，然后立刻停下来。上面这段会话里，如果把 `continue` 都换成连续敲 `next`，你就能看到 `sum` 是怎么从 0 变成 1、又从 1 变成 3 的 —— 每一步都不会漏掉。

    自己动手试试，比看文档有用得多。

!!! note "为什么能看到变量名"
    因为 5.1 节编译时加了 `-g`。注意看会话里 `frame variable` 打印的是 `(int) sum = 0` —— 连类型都告诉你了。要是忘了加 `-g`，这里只会打印出一串地址。


### 5.3 和 gdb 的命令对照表

以后你在网上搜到 gdb 的教程（或者问了 AI，它默认按 gdb 回答你），照着这张表换一下就能在 Mac 上用：

| 想干的事             | gdb                      | lldb                                  |
| -------------------- | ------------------------ | ------------------------------------- |
| 启动调试             | `gdb ./sum`              | `lldb ./sum`                          |
| 在 main 开头下断点   | `break main`             | `breakpoint set --name main`（或 `b main`） |
| 在第 6 行下断点      | `break 6`                | `breakpoint set --file sum.c --line 6` |
| 开始运行             | `run`                    | `run`                                 |
| 单步，不进入函数     | `next`                   | `next`                                |
| 单步，进入函数       | `step`                   | `step`                                |
| 打印变量的值         | `print sum`              | `print sum`（或 `frame variable sum`） |
| 看当前函数所有变量   | `info locals`            | `frame variable`                      |
| 继续运行             | `continue`               | `continue`                            |
| 看函数调用栈         | `backtrace`              | `bt`                                  |
| 退出                 | `quit`                   | `quit`                                |

!!! tip "大部分简写是通用的"
    `run` / `next` / `step` / `continue` / `print` / `quit` 这六个命令，**在 gdb 和 lldb 里连拼写都一样**，而且都能缩写成首字母（`r` / `n` / `s` / `c` / `p` / `q`）。只有下断点的方式差别比较大。

## 6. 进阶：在 VSCode 里一键编译和调试

第 5 节那套 lldb 命令用熟了很快，但每次都要手动敲、手动看变量，还是不够顺手。VSCode 可以把同样的流程变成一个图形界面：**在行号旁边点一下就是断点，鼠标点按钮就是单步，变量在左侧面板里实时显示**。

这需要两个配置文件。配置文件放在项目里的 `.vscode` 文件夹下，**这样配置跟着代码走**，换台电脑也算数。

### 6.1 创建配置文件

在 VSCode 的左侧文件栏里：

1. 点「新建文件夹」图标，文件夹名叫 `.vscode`（**前面的点不能少**，这样它在 Mac 上会变成隐藏文件夹，VSCode 里照常显示）。
2. 在 `.vscode` 上右键 → 新建文件，叫 `tasks.json`，把下面内容粘进去：

```json title=".vscode/tasks.json"
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "clang 编译",
      "type": "shell",
      "command": "clang",
      "args": ["-g", "${file}", "-o", "${fileDirname}/${fileBasenameNoExtension}"],
      "group": { "kind": "build", "isDefault": true }
    }
  ]
}
```

这个文件告诉 VSCode **怎么编译**。几个占位符是 VSCode 自己会替换的：`${file}` 是当前打开的文件，`${fileDirname}` 是它所在的文件夹，`${fileBasenameNoExtension}` 是去掉 `.c` 后缀的文件名。

3. 同样在 `.vscode` 里新建 `launch.json`：

```json title=".vscode/launch.json"
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "调试 C 程序",
      "type": "lldb",
      "request": "launch",
      "program": "${fileDirname}/${fileBasenameNoExtension}",
      "args": [],
      "cwd": "${fileDirname}",
      "preLaunchTask": "clang 编译"
    }
  ]
}
```

这个文件告诉 VSCode **怎么调试**：用 lldb 调试编译出来的那个程序。

!!! warning "`preLaunchTask` 的名字必须和上面那个 `label` 一模一样"
    也就是 `clang 编译` 这个词。对不上，VSCode 会找不到该执行的编译任务，调试根本起不来。

!!! note "为什么要装 CodeLLDB"
    `"type": "lldb"` 就是 CodeLLDB 插件提供的。不装它，VSCode 会提示「找不到调试类型 lldb」。

### 6.2 开始调试

打开 `sum.c`，在**第 6 行 `sum += i;` 的行号左边点一下**，会出现一个红点 —— 这就是断点。

然后按 ++f5++。VSCode 会自动先编译、再启动调试，程序停在红点那一行。

!!! warning "Mac 上按不出 ++f5++ 怎么办"
    MacBook 键盘最上面那排默认是**多媒体键**（亮度、音量），按 F5 可能没反应。
    两个办法：按住 ++fn++ 再按 ++f5++；或者去「系统设置 → 键盘 → 键盘快捷键 → 功能键」里打开「**将 F1、F2 等键用作标准功能键**」，之后 F5 就正常了。

按 ++f5++ 之后，界面上会出现这些小东西：

| 位置           | 是什么                                                   |
| -------------- | -------------------------------------------------------- |
| 顶部悬浮小工具条 | 调试控制按钮，从左到右大致是：继续、单步跳过、单步进入、重启、停止 |
| 左侧「变量」面板 | 当前函数里所有变量的实时值，**点开就能看见 `sum` 和 `i` 在变** |
| 左侧「调用栈」面板 | 现在停在哪一层函数里，以后程序复杂了靠它找路径          |

对应的快捷键（**和 lldb 的命令一一对应**）：

| 功能               | 快捷键         | 对应 lldb 命令 |
| ------------------ | -------------- | -------------- |
| 开始 / 继续运行    | ++f5++         | `run` / `continue` |
| 单步，不进入函数   | ++f10++        | `next`         |
| 单步，进入函数     | ++f11++        | `step`         |
| 停止调试           | ++shift+f5++   | `quit`         |
| 在某行加 / 取消断点 | ++f9++        | `breakpoint set` |

多练几遍就会发现：**图形界面和 lldb 命令是同一件事的两种操作方式**。想做更细的事（比如看指针指向的内存、按条件断下来），还是得回到命令行，或者去查 lldb 的文档。

## 7. 进阶补充：想装真正的 GNU GCC（可选）

第 1.3 节说了，Mac 自带的 `gcc` 其实是 clang。对**本课程来说，clang 完全够用**，这一节可以跳过。

如果你出于好奇，或者以后某门课明确要求 GNU GCC，可以先装 [Homebrew](https://brew.sh/zh-cn/)（Mac 上的包管理器，相当于 Ubuntu 的 `apt`），然后：

```bash title="终端"
brew install gcc
```

装完之后敲 `gcc --version`，会发现**打印的还是 Apple clang** —— 这不是没装上。Homebrew 装出来的命令名是带版本号的，比如 `gcc-15`：

```bash title="终端"
gcc-15 --version   # 这里输出才是真正的 GNU GCC（版本号填你实际装上的那个）
```

因为系统里 `gcc` 这个名字已经被占用了，Homebrew 只能另起一个名字，免得把系统自带的编译器覆盖掉。想让它响应 `gcc` 这个名字，可以在 `~/.zshrc` 里加一行别名：

```bash title="终端"
echo "alias gcc='gcc-15'" >> ~/.zshrc   # 版本号换成你实际装的那个
source ~/.zshrc
```

!!! warning "改完别名如果编译报奇怪的错，先把这行删掉试试"
    两套编译器混用，有时会踩到一些奇怪的问题。课程里遇到想不明白的编译错误，第一件事就是确认自己到底在用哪个编译器：`which gcc`。

## 8. 自检清单

全部做完之后，逐条对一遍。**每一条都能勾上，你的环境就没问题了**：

- [ ] `gcc --version` 输出的第一行里有 `Apple clang version`
- [ ] `code --version` 有版本号输出
- [ ] VSCode 里打开 `hello.c`，代码有颜色（语法高亮）、能补全
- [ ] 在终端里敲 `gcc hello.c -o hello && ./hello`，打印出 `Hello, Fudan!`
- [ ] 终端里敲 `lldb ./sum`，`b main` 加 `run` 能停得下来，`frame variable` 能看到变量的值
- [ ] 按 ++f5++ 能启动调试，程序停在红点上，左侧「变量」面板能看到变量的值

有哪条勾不上，或者中间哪一步卡住了，直接在微信群里问，或者把报错信息发给助教。
