
# Claude 与 AI 编程助手

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>实验课时间：<strong>待定</strong></span></p>

这套方案要解决的问题是：**用 Claude 的客户端，但跑 DeepSeek 的模型**。配好之后，你就有了一个随时能用的 AI 助手：查报错、讲代码、逐行解释程序都行。

!!! abstract "全程概览"
    1. 了解为什么用这套方案（可跳过）
    2. 在 DeepSeek 开放平台申请 API Key
    3. 安装 CC Switch
    4. 在 CC Switch 里配置 DeepSeek
    5. 打开路由开关
    6. 安装 Claude 桌面版
    7. 安装并配置 Claude Code

    全程只需要下载、点击和粘贴，**不需要任何前置知识**。

## 1. 为什么是这套方案

先分清两件事：**模型**和 **Harness**。这套方案就是各取所长：Harness 用 Claude 的，模型用 DeepSeek 的。

### 1.1 为什么要用 Claude 的 Harness

**Harness**（直译是「马具」，指套在模型外面的那一层程序）决定模型能看到什么信息、能调用哪些工具、怎么把一个大任务拆成若干步。

同一个模型，装进不同的 Harness 里，用起来的效果可以差很远。好的 Harness 让模型能自己读文件、跑命令、看报错、再改代码，几轮下来就把问题解决了，看上去就像「变聪明了」；差的 Harness 里，再强的模型也只能干巴巴地陪你聊天。

**Claude Desktop** 和 **Claude Code** 是目前评价最高的 Harness：

- **记忆功能**：Claude 会自行维护记忆文件，存放在专门的记忆文件夹中，新会话仍会保留该信息，无需重复说明背景。
- **上下文自动压缩**：上下文接近上限时，会话历史会被压缩为摘要。
- **Cowork 沙盒**：它运行在本机隔离的虚拟机中，用户指定一个文件夹作为工作区，读写范围限于该文件夹，网络访问受白名单管控。
- **编辑器集成**：在 VSCode 中选中代码后，该段内容会自动进入上下文，无需手动复制粘贴。

!!! warning "但 Anthropic 对国内用户封号很凶"
    Claude 官方不向中国大陆提供服务，账号被风控封禁是常事。**助教那个充了 100 美元的 Max 会员账号就被封了**，钱直接打水漂。

    这正是这套方案要绕开的东西：**只用 Claude 的 Harness，账号和模型都换成国内的。**

### 1.2 为什么模型换成 DeepSeek

既然 Anthropic 的模型用不了，就得找一个能力够强、国内能用、又不贵的替代：

- **便宜**：按量计费，用多少扣多少，不用担心每周 token 限额。
- **能力强**：在编程和 agent 类跑分上，DeepSeek V4.1-Flash 已经跻身第一梯队，平时写写代码，能力绰绰有余。
- **国内可用**：注册充值方便，无需科学上网，不用担心封号。

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




## 3. 安装 CC Switch

下载并运行安装包 `CC-Switch-v3.20.3-Windows.msi`：

- **直接下载**：<https://mind-city-1379176255.cos.ap-shanghai.myqcloud.com/CC-Switch-v3.20.3-Windows.msi>
- **官方最新版**：<https://github.com/farion1231/cc-switch/releases>

!!! tip "GitHub 访问"
    官方仓库有时需要科学上网才能打开。打不开就用上面的直接下载链接，助教已经传好了。

## 4. 在 CC Switch 里配置 DeepSeek

**CC Switch 是一个跑在本机的模型路由工具**，作用是让 AI 客户端连到你指定的模型服务上。

例如 Claude Desktop 默认只支持自家的模型服务，而 CC Switch 是作为中间层，让它把实际的请求转发到 DeepSeek 上。这样既能用上 Claude 的完整配套工具链，又能跑 DeepSeek 的高性价比模型。

### 4.1 选中 Claude Desktop

工具栏上那一排图标，对应的是不同的 AI 客户端。

**先点一下 Claude Desktop 那个图标**，切换到它的配置界面：

![在工具栏中选中 Claude Desktop](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914230823562.png)

### 4.2 添加供应商

点右上角的 **「+」**，会弹出「添加新供应商」窗口。

在上方的「预设供应商」里找到 **DeepSeek** 并选中：

![在预设供应商中选择 DeepSeek](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914220955308.png)

选中之后，窗口下方会出现 API Key 等字段，把第 2 步存下来的那个 Key 粘进去。

### 4.3 配置模型映射

同一个窗口往下滚，是「模型配置」这一栏。

Claude 桌面版只会按 `sonnet`、`opus`、`fable`、`haiku` 这几个固定的模型名去请求，所以要把这四档一一映射到 DeepSeek 实际提供的模型上 —— 每一行的「菜单显示名」和「实际请求模型」都填上 `deepseek-flash`。

图中的「声明支持 1M」也可以勾上。填完点右下角的 **「添加」**。

![配置模型映射，把各档模型指向 DeepSeek](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914220833355.png)


## 5. 打开路由开关

配置完成后回到主界面，**把左上角的开关打开**（绿色表示已经打开）。

![打开 CC Switch 的路由开关](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914230901561.png)

!!! warning "电脑每次重启，都要重新打开路由"
    CC Switch 关掉或者电脑重启之后，这个开关会自己关掉。**Claude 连不上时，第一件事就是回来看这个开关是不是又关了** —— 这是最常见的问题。

## 6. 安装 Claude 桌面版

最后一步，下载并安装 Claude 官方客户端：

- **直接下载**：<https://mind-city-1379176255.cos.ap-shanghai.myqcloud.com/Claude-1.52386.6.0.msix>
- **官方网站**：<https://claude.com/download>

装好后打开随便问个问题。如果能正常回答，说明整条链路已经通了。

!!! tip "出问题了先看这两处"

    - **Claude 连不上** → 先检查 CC Switch 的**路由开关**是不是关着（见第 5 步）
    - **提示 API Key 无效** → 回 CC Switch 检查 Key 有没有粘错，以及 DeepSeek 账户里还有没有余额


## 7. 安装并配置 Claude Code

桌面版日常聊天够用了，但是如果你想要在终端里直接让 AI 读代码、改代码，就需要再装一个 **Claude Code**。

!!! warning "这一步必须科学上网，而且不能用香港节点"

    前面六步全程国内直连，只有这一步是例外：

    - Claude Code 的安装脚本放在 `claude.ai` 上，国内打不开，**安装的时候必须挂着代理**
    - **节点不要选香港**。Anthropic 不向香港提供服务，用香港 IP 会被判定成「不支持的地区」，装上了也用不了。

### 7.1 Windows

安装：

```pwsh title="Windows 终端"
irm https://claude.ai/install.ps1 | iex
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
setx CLAUDE_CODE_USE_POWERSHELL_TOOL 1
```

后两行解释一下：

- **`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`**：放开 PowerShell 的脚本限制。Windows 默认策略是 `Restricted`，**默认不支持加载 `$PROFILE` 配置文件**。所以少了这一行，下一步写进 `$PROFILE` 的配置会毫无动静地失效。
  - `RemoteSigned` 表示本地脚本可以跑、从网上下载的必须有签名
  - `-Scope CurrentUser` 让它只对当前用户生效，**不需要管理员权限**
- **`setx CLAUDE_CODE_USE_POWERSHELL_TOOL 1`**：让 Claude Code 用 **PowerShell 原生工具**执行命令，而不是绕 Git Bash。好处是能直接跑 PowerShell 命令、管道传对象、用 Windows 原生路径。用 `setx` 而不是 `$env:`，是因为它要**写进用户环境变量来持久化**，只在当前终端窗口里设置不够用。

然后用 VSCode 编辑器打开 `$PROFILE`：

```pwsh title="Windows 终端"
code $PROFILE
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
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "deepseek-flash[1m]"
$env:CLAUDE_CODE_SUBAGENT_MODEL = "deepseek-flash[1m]"
```

### 7.2 Ubuntu

安装：

```bash title="Ubuntu 终端"
curl -fsSL https://claude.ai/install.sh | bash
```

然后用 vim 编辑器打开 `~/.bashrc`：

```bash title="Ubuntu 终端"
vi ~/.bashrc
```

把下面这段粘到文件**末尾**，注意把 Key 替换成你之前存下来的那个：

```bash title="~/.bashrc"
alias cc='claude --permission-mode auto'
export ANTHROPIC_AUTH_TOKEN="这里填上你的 DeepSeek API Key"

export PATH="$HOME/.local/bin:$PATH"
export ANTHROPIC_MODEL="deepseek-flash[1m]"
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-flash[1m]"
export CLAUDE_CODE_SUBAGENT_MODEL="deepseek-flash[1m]"
```

!!! warning "这个文件里存着你的 API Key"
    `~/.bashrc` 和 `$PROFILE` 现在是明文保存 Key 的。**不要把这个文件发给别人，也不要提交到 GitHub**。

### 7.3 验证

关掉终端重新开一个（让新配置生效），然后输入：

```bash title="任意终端"
cc
```

能正常对话就说明配好了。`cc` 是上面定义的快捷方式，等价于 `claude --permission-mode auto`，省得每次都打全名。


### 7.4 权限模式

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


