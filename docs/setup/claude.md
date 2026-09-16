
# Claude 和 DeepSeek 配置

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>实验课时间：<strong>待定</strong></span></p>

!!! warning "开始之前：整篇教程的前置基础是科学上网"

    Claude 的母公司 Anthropic **不向中国大陆和中国香港特别行政区提供服务**，直连一律返回 `App unavailable in region`。所以这篇教程**从头到尾都建立在科学上网的基础上** —— 下载客户端、安装 Claude Code 走的都是官方渠道。

    另外两点要注意：

    - **代理节点不要选香港** —— 香港同样会被判定为「不受支持的地区」，挂上去照样打不开。
    - Anthropic **对国内用户的风控封号很凶**，账号被封是常事。**助教那个充了好几个月的尊贵 Max 会员账号就被封了**，钱直接打水漂。所以这套方案**一分钱都不付给 Anthropic**：只借用它的客户端（Harness），模型全部换成国内的平台。

!!! tip "搞不定科学上网的同学，换成看另外一篇"

    **整篇教程的前置条件是科学上网**，没弄过代理的同学光这一步就可能卡很久。

    这种情况可以直接看 [DeepSeek 工具链配置](deepseek-harness.md)：那篇装的是社区封装的 **DeepSeek Harness 桌面版**，下载、安装、调用模型全程都在国内完成，**不需要任何代理**，装完把 API Key 填进去就能用，少了一大堆配置步骤。唯一的代价是它还是个较新的项目，偶尔会踩到 bug。

    两套方案**互不影响**，可以都装着；先把哪个跑通都行。

这套方案要解决的问题是：**用 Claude 的客户端，但跑 DeepSeek 的模型**。配好之后，你就有了一个随时能用的 AI 助手：查报错、讲代码、逐行解释程序都行。

!!! abstract "全程概览"
    1. 了解为什么用这套方案（可跳过）
    2. 在 DeepSeek 开放平台申请 API Key
    3. 安装 Claude 桌面版，并启动一次
    4. 安装 CC Switch
    5. 回 CC Switch 里配置 DeepSeek
    6. 打开路由开关
    7. 完全退出桌面版，再重新打开
    8. 安装并配置 Claude Code

    全程只需要下载、点击和粘贴，**不需要任何前置知识**（代理除外，见文首警告）。

    **第 3 步和第 5 步的顺序不能反**：CC Switch 是往桌面版自己的配置目录里写配置的，桌面版没装、没启动过，这份配置就没有地方可写。

## 1. 为什么是这套方案

### 1.1 为什么要用 Claude 的 Harness

**Harness**（直译是「马具」，指围绕模型搭建的一整套工具链）决定模型能看到什么信息、能调用哪些工具、怎么把一个大任务拆成若干步。

同一个模型，装进不同的 Harness 里，用起来的效果可以差很非常远。

好的 Harness 能让模型自己读文件、跑命令、看报错、再改代码，几轮下来就把问题解决了，看上去就像「变聪明了」；而使用了差的 Harness，就算内置再强的模型也无法完成你想要的任务。

**Claude Desktop** 和 **Claude Code** 是目前公认能力最强的 Harness：

- **记忆功能**：Claude 会自行维护记忆文件，存放在专门的记忆文件夹中，新会话仍会保留该信息，无需重复说明背景。
- **上下文自动压缩**：上下文接近上限时，会话历史会被压缩为摘要。
- **Cowork 沙盒**：它运行在本机隔离的虚拟机中，用户指定一个文件夹作为工作区，读写范围限于该文件夹，网络访问受白名单管控。
- **编辑器集成**：在 VSCode 中选中代码后，该段内容会自动进入上下文，无需手动复制粘贴。

但正如文首警告所说，Anthropic 对国内用户封号很凶，官方模型既贵又随时可能用不了。所以这套方案**一分钱都不付给 Anthropic**：只借它的 Harness，内置的模型全部换成国内的平台。

### 1.2 为什么模型换成 DeepSeek

既然 Anthropic 的模型用不了，就得找一个能力够强、国内能用、又不贵的替代：

- **便宜**：按量计费，用多少扣多少，不用担心每周 token 限额。
- **能力强**：在编程和 agent 类跑分上，DeepSeek V4.1-Flash 已经跻身第一梯队，平时写写代码，能力绰绰有余。
- **国内可用**：注册、充值都方便，API 本身国内直连，也不存在封号问题。

![DeepSeek V4.1-Flash 与主流模型的跑分对比](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914231741845.jpg)

## 2. 申请 DeepSeek API Key

### 2.1 注册并登录

打开 DeepSeek 开放平台，注册并登录：

<https://platform.deepseek.com/>

### 2.2 充值

DeepSeek 的**网页版和 App 对话是免费的**，但我们这套方案走的是 **API**，API 按量计费，所以账户里得先有余额。

在左侧栏点 **「充值」**，选一个金额，支付方式用支付宝或微信都行：

![DeepSeek 开放平台的充值页面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914233810239.png)

!!! tip "充多少合适"
    先充 ¥1 试水就够，用完了随时再充。

    页面上的单价分**空闲时段**和**高峰时段**两档，高峰时段是空闲时段的 2 倍。具体单价点旁边的「查看价格」看。

### 2.3 创建 API Key

回到左侧栏，点 **「API keys」**，再点 **「创建 API key」**。名称随便写一个（比如 `claude`），然后点「创建」：

![在 DeepSeek 开放平台创建 API key](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914231206951.png)

!!! warning "API Key 只在创建时完整显示一次"
    弹窗关掉之后就再也看不到了。**创建完立刻复制下来**，先粘到记事本里存着，下一步马上要用。

!!! warning "API Key 泄露等于账户被盗刷"

    任何拿到这个 Key 的人，都能直接花你账户里的钱。请务必做到：

    - **不要**把它粘到聊天群、论坛或者作业提交里，也不要截图发出去
    - **不要**写进代码或配置文件之后提交到 GitHub —— 公开仓库有爬虫盯着，泄露的 Key 往往几个小时内就会被刷光
    - 万一怀疑泄露，立刻回「API keys」页面把它删掉，重新建一个

    同样地，**充值尽量用多少充多少**，不要在账户里留大额余额。这样即使 Key 真出了问题，损失也是可控的。


### 2.4 选择合适的模型

DeepSeek 目前提供两个模型，**它们的模型名要一字不差地填进后面的配置**，所以先在这里确认好：

| 2026年9月14日 | `deepseek-flash`    | `deepseek-v4-pro`    |
| ------------- | ------------------- | -------------------- |
| 模型版本      | DeepSeek-V4.1-Flash | DeepSeek-V4-Pro-0813 |
| 上下文长度    | 1M                  | 1M                   |
| 最大输出长度  | 384K                | 384K                 |
| 图像理解      | 支持                | 不支持               |
| 并发限制      | 2500                | 500                  |

**平时写代码用 `deepseek-flash` 就完全足够了**。


| 模型                       | 输入（缓存命中） | 输入（缓存未命中） | 输出 |
| -------------------------- | ---------------- | ------------------ | ---- |
| `deepseek-flash` 空闲时段  | 0.02             | 1                  | 4    |
| `deepseek-flash` 高峰时段  | 0.04             | 2                  | 8    |
| `deepseek-v4-pro` 空闲时段 | 0.15             | 4.5                | 13.5 |
| `deepseek-v4-pro` 高峰时段 | 0.30             | 9.0                | 27.0 |




!!! tip "实际跑下来，接近 99% 的输入都会命中缓存"

    助教在 2026-09-14 单日的真实用量(工作量大)，按 `deepseek-flash` 空闲时段计算：

    | 项目               | tokens      | 占输入比例 | 费用（元） |
    | ------------------ | ----------- | ---------- | ---------- |
    | 输入（命中缓存）   | 223,619,262 | 98.8%      | 4.47       |
    | 输入（未命中缓存） | 2,775,889   | 1.2%       | 2.78       |
    | 输出               | 1,082,867   |            | 4.33       |
    | **合计**           | 227,478,018 |            | **11.58**  |


!!! warning "高峰时段的价格是空闲时段的两倍"
    **高峰时段是北京时间周一至周五的 9:00-12:00 和 14:00-18:00**，其余时间（包括整个周末）都算空闲时段。

    所以同样的活儿，**放在晚上或者周末跑，费用只要一半**。要跑大批量的任务，尽量避开高峰。




## 3. 安装 Claude 桌面版

**这一步要排在配置 CC Switch 之前**，原因见下面的提示框。

从官网下载并安装 Claude 官方客户端（**需要科学上网**）：

<https://claude.com/download>

装好之后**先打开一次**（现在还连不通模型，能启动到界面就算成功），然后关掉。

!!! warning "为什么必须「先装桌面版，再配 CC Switch」"

    CC Switch 接管桌面版的办法，是**往桌面版自己的配置目录里写配置文件**。这带来两个绕不开的先后关系：

    - 桌面版还没装，CC Switch 要写的那个目录**根本不存在**，配置无处可写；
    - 桌面版**第一次启动时会做一次配置迁移**，把配置搬进自己的容器路径。要是先配了 CC Switch 再装桌面版，这份配置会被这次迁移挤掉，桌面版读到的仍然是内置的官方模型。

    所以正确的顺序是：**装好桌面版 → 让它至少完整启动过一次 → 再回 CC Switch 写配置**

!!! tip "顺序弄反了的话，会看到这个报错"

    顺序反了、配置被桌面版首次启动时的迁移挤掉之后，桌面版发消息会报 `Host Claude Code binary not available. Check that the download completed.`：

    ![桌面版提示 Host Claude Code binary not available](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260916132341531.png)

    **不用重装**。回 CC Switch 的 Claude Desktop 面板，**重新加一个 DeepSeek 供应商配置**（把 [5.2 添加供应商](#52-添加供应商) 再做一遍），用它覆盖掉出错的那份，再按第 7 步退出重启桌面版就好了。

## 4. 安装 CC Switch

从官方仓库下载安装包（**需要科学上网**）：

<https://github.com/farion1231/cc-switch/releases>

打开最新的一版 Release，在下面的 **Assets** 里找到 Windows 的 `.msi`（文件名形如 `CC-Switch-v3.20.3-Windows.msi`），下载后运行安装。

## 5. 在 CC Switch 里配置 DeepSeek

**CC Switch 是一个跑在本机的模型路由工具**，作用是让 AI 客户端连到你指定的模型服务上。

例如 Claude Desktop 默认只支持自家的模型服务，而 CC Switch 是作为中间层，让它把实际的请求转发到 DeepSeek 上。这样既能用上 Claude 的完整配套工具链，又能跑 DeepSeek 的高性价比模型。

### 5.1 选中 Claude Desktop

工具栏上那一排图标，对应的是不同的 AI 客户端。

**先点一下 Claude Desktop 那个图标**，切换到它的配置界面：

![在工具栏中选中 Claude Desktop](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914230823562.png)

### 5.2 添加供应商

点右上角的 **「+」**，会弹出「添加新供应商」窗口。

在上方的「预设供应商」里找到 **DeepSeek** 并选中：

![在预设供应商中选择 DeepSeek](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914220955308.png)

选中之后，窗口下方会出现 API Key 等字段，把第 2 步存下来的那个 Key 粘进去。

### 5.3 配置模型映射

同一个窗口往下滚，是「模型配置」这一栏。

Claude 桌面版只会按 `sonnet`、`opus`、`fable`、`haiku` 这几个固定的模型名去请求，所以要把这四档一一映射到 DeepSeek 实际提供的模型上 —— 每一行的「菜单显示名」和「实际请求模型」都填上 `deepseek-flash`。

图中的「声明支持 1M」**要勾上** —— `deepseek-flash` 本身就是 1M 上下文，勾了才对得上。填完点右下角的 **「保存」**。

![配置模型映射，把各档模型指向 DeepSeek](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260915004736226.png)

## 6. 打开路由开关

配置完成后回到主界面，**把左上角的开关打开**（绿色表示已经打开）。

![打开 CC Switch 的路由开关](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914230901561.png)

!!! warning "这个开关要一直开着，不是在配置时打开一下就行"

    桌面版发出去的请求并不是直接去 DeepSeek，而是**先发给 CC Switch 在本机开的代理**（`http://127.0.0.1:15721`），由它把模型名换好、再转发出去。所以只要 CC Switch 没在跑、或者这个开关被关掉，**整条链路就断了**，桌面版立刻连不上。

    CC Switch 退出、电脑重启之后，这个开关会自己关掉。
    
    **Claude 连不上时，第一件事就是回来看这个开关是不是又关了** —— 这是最常见的问题。

## 7. 完全退出桌面版，再重新打开

配置已经写好了，但**桌面版不会自己读**，桌面版只会在**自己启动的那一刻**读一次。

所以现在要把桌面版**彻底退干净，再重新打开**：

1. 关掉桌面版的窗口
2. 在**系统托盘**里找到 Claude 图标（右下角时钟旁边，点 `^` 展开），右键 → **退出**（英文菜单里是 **Exit**）

![在系统托盘右键 Claude 图标，选 Exit](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260916130629134.png)

!!! warning "只关窗口是不够的"
    关掉聊天窗口只是把界面收起来了，**进程还在后台跑着**，用着的仍然是启动时读到的那份旧配置。必须退到进程真的结束，重新打开才会重新读一遍。

重新打开桌面版，随便问一个问题。能正常回答，说明整条链路已经通了。


## 8. 安装并配置 Claude Code

桌面版日常聊天够用了，但是如果你想要在终端里直接让 AI 读代码、改代码，就需要再装一个 **Claude Code**。

!!! warning "安装前先确认代理是通的"

    官方的安装脚本放在 `claude.ai` 上，而 Anthropic 不对**中国大陆**和**中国香港特别行政区**提供服务，直连会返回 `App unavailable in region`。**挂上代理再往下走**，并且**节点不要选香港**。

    走官方渠道安装还有个附带好处：Claude Code 自带的自动更新同样指向官方地址，装完之后能跟着官方一起升级，不会一直停在某个旧版本上。

!!! quote "延伸阅读：为什么建议顺手学一下 vim"

    下面两个小节给的都是 VSCode 和记事本，是为了照顾还没学过 vim 的同学。但**练熟之后 vim 反而是最快的**：不用切窗口，手不离键盘，改两行配置几秒钟就完事。

    Linux 上最经典的编辑器就是 vim，几乎所有服务器都预装了它，而别的编辑器多半没有。以后你连到服务器或者其他远程机器上时，往往**只有 vim 能用**。

    想学习 vim，可以看这期视频：[《保姆级入门：Vim 编辑器》](https://www.bilibili.com/video/BV13t4y1t7Wg)

### 8.1 在 Windows 终端里安装 Claude Code

!!! warning "这几行要在 PowerShell 里跑，不能粘到 cmd 里"
    下面用到的 `irm` 和 `iex` 都是 PowerShell 的命令（`Invoke-RestMethod` / `Invoke-Expression` 的缩写），**命令提示符（cmd）里没有这两个东西**，粘进去只会报 `'irm' 不是内部或外部命令`。这一节后面的 `Set-ExecutionPolicy`、`$PROFILE` 也是 PowerShell 的语法，同样不能在 cmd 里跑。

    打开 PowerShell的两种方法：

    - 按 ++win++ 键，搜索 `PowerShell`
    - 或者按 ++win+r++，输入 `powershell`，回车

    **怎么知道自己开对了**：PowerShell 的提示符前面有个 `PS`，长这样 `PS C:\Users\你的用户名>`；cmd 的提示符没有 `PS`。

安装（**需要科学上网**）：

```pwsh title="Windows 终端"
irm https://claude.ai/install.ps1 | iex
```

装完需要**接着再跑这两行**：

```pwsh title="Windows 终端"
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
setx CLAUDE_CODE_USE_POWERSHELL_TOOL 1
```

这两行解释一下：

- **`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`**：放开 PowerShell 的脚本限制。Windows 默认策略是 `Restricted`，**默认不支持加载 `$PROFILE` 配置文件**。所以少了这一行，下一步写进 `$PROFILE` 的配置会毫无动静地失效。
    - `RemoteSigned` 表示本地脚本可以跑、从网上下载的必须有签名
    - `-Scope CurrentUser` 让它只对当前用户生效，**不需要管理员权限**
- **`setx CLAUDE_CODE_USE_POWERSHELL_TOOL 1`**：让 Claude Code 用 **PowerShell 原生工具**执行命令，而不是绕 Git Bash。
    - 好处是能直接跑 PowerShell 命令、管道传对象、用 Windows 原生路径。
    - 用 `setx` 而不是 `$env:`，是因为它要**写进用户环境变量来持久化**，只在当前终端窗口里设置不够用。

然后用编辑器打开 `$PROFILE`（两种方式选一种）：

=== "VSCode"

    ```pwsh title="Windows 终端"
    code $PROFILE
    ```

=== "记事本"

    ```pwsh title="Windows 终端"
    notepad $PROFILE
    ```

把下面这段粘到文件**末尾**，注意把 Key 替换成你之前存下来的那个：

```pwsh title="$PROFILE"
function cc { claude --permission-mode auto @args }
$env:ANTHROPIC_AUTH_TOKEN = "这里填上你的 DeepSeek API Key"

$env:Path += ";$env:USERPROFILE\.local\bin"
$env:ANTHROPIC_MODEL = "deepseek-flash[1m]"
$env:ANTHROPIC_BASE_URL = "https://api.deepseek.com/anthropic"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL = "deepseek-flash[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL = "deepseek-flash[1m]"
$env:ANTHROPIC_DEFAULT_FABLE_MODEL = "deepseek-flash[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "deepseek-flash[1m]"
$env:CLAUDE_CODE_SUBAGENT_MODEL = "deepseek-flash[1m]"
```

### 8.2 在 Ubuntu 中安装 Claude Code

安装（**需要科学上网**）：

```bash title="Ubuntu 终端"
curl -fsSL https://claude.ai/install.sh | bash
```

然后用编辑器打开 `~/.bashrc`（两种方式选一种）：

=== "VSCode"

    ```bash title="Ubuntu 终端"
    code ~/.bashrc
    ```

=== "记事本"

    ```bash title="Ubuntu 终端"
    notepad.exe ~/.bashrc
    ```

!!! tip "`code` 提示找不到命令"
    这个命令要装了 VSCode **并且连上 WSL** 之后才生效（见 [WSL2 环境搭建](wsl2-vscode.md) 第 6 步）。没装上就直接用记事本那条 —— WSL 能直接调用 Windows 的程序，记事本打开的确实就是 WSL 里的那份 `~/.bashrc`。

把下面这段粘到文件**末尾**，注意把 Key 替换成你之前存下来的那个：

```bash title="~/.bashrc"
alias cc='claude --permission-mode auto'
export ANTHROPIC_AUTH_TOKEN="这里填上你的 DeepSeek API Key"

export PATH="$HOME/.local/bin:$PATH"
export ANTHROPIC_MODEL="deepseek-flash[1m]"
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_FABLE_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-flash[1m]"
export CLAUDE_CODE_SUBAGENT_MODEL="deepseek-flash[1m]"
```

!!! warning "这个文件里存着你的 API Key"
    `~/.bashrc` 和 `$PROFILE` 现在是明文保存 Key 的。**不要把这个文件发给别人，也不要提交到 GitHub**。

### 8.3 验证

关掉终端重新开一个（让新配置生效），然后输入：

```bash title="任意终端"
cc
```

能正常对话就说明配好了。`cc` 是上面定义的快捷方式，等价于 `claude --permission-mode auto`，省得每次都打全名。


### 8.4 权限模式

上面定义的 `cc` 带了一个参数 `--permission-mode auto`。**权限模式**决定 Claude Code 做哪些事情之前要先问你。

会话里按 ++shift+tab++ 可以循环切换（终端底部会显示当前模式）：


| 模式         | 名称                | 权限                                   | 适合任务                     |
| ------------ | ------------------- | -------------------------------------- | ---------------------------- |
| 手动模式     | `manual`            | 只能读                                 | 想逐步确认每一步、改敏感代码 |
| 接受编辑     | `acceptEdits`       | 读、改文件，以及常见文件操作           | 边看边改的迭代               |
| 计划模式     | `plan`              | 读，加上分类器放行的少量命令           | 动手前先列出详细计划书       |
| 自动模式     | `auto`              | 全部，但背后有安全检查                 | 长任务、不想被反复打断       |
| 不询问       | `dontAsk`           | 只做读取和预先批准的工具，其余直接拒绝 | 无人值守的脚本和 CI          |
| 绕过所有权限 | `bypassPermissions` | 全部                                   | 助教这样的懒人               |


- 本教程的 `cc` 用的是**自动（`auto`）**：大部分操作直接放行，另有独立的分类器模型在后台审查，拦下越界或来路不明的动作。
- **计划（`plan`）模式不动你的代码**：只读、只查、只写方案，等你点头才开工。拿不准该怎么做时先用它。


