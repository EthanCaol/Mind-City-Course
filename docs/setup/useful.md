
# 实用小工具推荐

| 工具      | 解决什么问题                     |
| --------- | -------------------------------- |
| PixPin    | 截图、贴图，以及从图片里取文字   |
| PicGo     | 把图片传上图床，直接拿到图片网址 |
| Ente Auth | 两步验证（2FA），给账号加一层保护 |

## 1. PixPin：截图和取字

### 1.1 功能介绍

PixPin 免费，主要功能有：

- 标注：截图时直接圈重点、打箭头、标序号、打马赛克。
- 长截图：一边往下滚，一边把整页拼成一张长图。
- 文字识别（OCR）：框住图片里的文字，直接复制出来。
- 贴图：把一张图固定在屏幕上，对着参考代码写自己的代码时不用来回切窗口。

### 1.2 下载安装

在 Microsoft Store 里搜索 `PixPin`，点「获取」安装：

![Microsoft Store 里的 PixPin 页面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922103014401.png)

### 1.3 修改快捷键

常用的截图动作只有几个，可以把快捷键改到自己顺手的位置，同时避开其他软件已经占用的按键。

在设置窗口左侧点「快捷键/动作」，右侧每一行对应一个动作：

![PixPin 设置窗口的「快捷键/动作」页](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922102459609.png)

图中截图、贴图、恢复上次关闭的贴图分别绑定在 `Ctrl+1`、`Ctrl+2`、`Ctrl+3`。

!!! warning "快捷键冲突"
    `Ctrl+1`、`Ctrl+2` 这类组合键被很多软件占用。如果在某个程序里按下后没有反应，说明这个组合已经被占用了。

    最常见的是浏览器：`Ctrl+数字` 用来切换标签页。冲突时可以改成 `Alt+数字`，或者加上 ++shift++。

### 1.4 相关视频

下面这期视频把上面这些功能都演示了一遍，同时和 Snipaste 做了对比：

- [《几乎完美的截图软件？怕不是冲着Snipaste来的 | PixPin - 贴图、离线OCR、长截图、GIF录制》](https://www.bilibili.com/video/BV1Vu4y1G7Uw)

## 2. PicGo：图床客户端

### 2.1 什么是图床，为什么需要

图床是专门用来存放图片的地方。图片传上去之后会得到一个固定的网址，在哪儿引用这个网址，图片就在哪儿显示。

需要它的原因是：Markdown 里插图只能插网址，不能插自己电脑上的文件路径。

- 写成 `![](C:\Users\你\Desktop\截图.png)`，你自己能看到，因为这台电脑上确实有这个文件
- 但文档发给别人之后，对方电脑上没有这个文件，看到的就是一个空的图框

所以实验报告、GitHub 上的 README、博客这类要发给别人的文档，里面的图都得先传到图床，再把网址填进去。这个网站的截图就是这么处理的：每张图都存放在腾讯云 COS 上（网址都以 `image-1379176255.cos.ap-shanghai.myqcloud.com` 开头）。

### 2.2 PicGo 干什么

PicGo 本身不提供存储，它是图床的客户端，只负责两件事：

1. 把图片传到你在用的那个图床
2. 把图床返回的网址，按你选的格式放进剪贴板

整个流程是：截图之后按 ++ctrl+shift+u++ 上传，回到文档里按 ++ctrl+v++，粘贴出来的就是一条完整的 Markdown 图片语法。

![PicGo 主界面上传区](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922102341182.png)

### 2.3 下载安装

从 GitHub Releases 下载：

<https://github.com/Molunerfinn/PicGo/releases>

国内下载慢的话有个镜像站：<https://mirrors.sdu.edu.cn/github-release/Molunerfinn_PicGo>

### 2.4 图床选哪个

- 《从零开始搭建你的免费图床系统（Cloudflare R2 + WebP Cloud + PicGo）》：<https://sspai.com/post/90170>
- 《个人图床最佳方案：Cloudflare R2 + PicGo》：<https://tyxiaoming.xin/2025/01/12/%E6%90%AD%E5%BB%BA%E5%9B%BE%E5%BA%8A/>
- 《腾讯云存储桶》：<https://cloud.tencent.com/document/product/436/14106>

## 3. Ente Auth：两步验证（2FA）

### 3.1 为什么要开两步验证（2FA）

只靠密码保护的账号，一旦密码泄露，账号就有被别人登录的风险。两步验证要求登录时再输入一个六位数字，这个数字由你自己的设备生成，密码泄露了也进不去。

它的英文缩写是 2FA（two-factor authentication），网站的账号设置里写的通常就是这个字样。下面一律写作 2FA。

重要的账号都建议开启。开启之后，登录时除了密码，还要输入一个 30 秒变化一次的六位码，这个码由 Ente Auth 这类 App 生成。

### 3.2 为什么是 Ente Auth

Ente Auth 主要有这几个优点：

- 端到端加密的云备份：换手机后登录一次，所有账号的验证码都会同步回来
- 全设备同步：电脑、手机、网页上都可用，验证码在所有设备上保持一致
- 完全离线也能用：不注册账号也可以，数据只保存在这台设备上
- 批量导入：可以从其他验证器一次性导入，不用逐个重新扫描

### 3.3 下载安装

官网：<https://ente.io/auth/>

网页版直接打开就能用：<https://auth.ente.com>。

手机上在谷歌应用商店里搜索 `Ente Auth`，电脑上从官网下载。

添加账号有三种方式：

1. 扫二维码（最常用）
2. 手动输入网站给的密钥
3. 从其他验证器批量导入

![Ente Auth 的账号列表](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922102319338.png)

