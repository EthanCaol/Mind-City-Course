
# 小工具推荐

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>实验课时间：<strong>待定</strong></span></p>

| 工具      | 解决什么问题                     |
| --------- | -------------------------------- |
| PixPin    | 截图、贴图，以及从图片里取文字   |
| PicGo     | 把图片传上图床，直接拿到图片网址 |
| Ente Auth | 两步验证（2FA），给账号再加一道锁 |

## 1. PixPin：截图和取字

### 1.1 功能介绍

PixPin 免费，能干这几件事：

- 标注：截图时直接圈重点、打箭头、标序号、打马赛克。
- 长截图：一边往下滚，一边把整页拼成一张长图。
- 文字识别（OCR）：框住图片里的文字，直接复制出来。
- 贴图：把一张图「钉」在屏幕上。对着参考代码写自己的代码时，不用来回切窗口。

### 1.2 下载安装

在 Microsoft Store 里搜 `PixPin`，点「获取」装上就行：

![Microsoft Store 里的 PixPin 页面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922103014401.png)

### 1.3 快捷键按自己的习惯改

常用的截图动作就那么几个，绑到自己顺手、又不跟别的软件打架的键上，用起来会舒服很多。

在设置窗口左侧点「快捷键/动作」，右边一行就是一个动作：

![PixPin 设置窗口的「快捷键/动作」页](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922102459609.png)

图里这套绑的是截图 `Ctrl+1`、贴图 `Ctrl+2`、恢复上次关闭的贴图 `Ctrl+3`。每行右边三个控件分别是：

!!! warning "快捷键冲突"
    `Ctrl+1`、`Ctrl+2` 这种组合键很常见，别的软件可能也在用，撞上了的症状是「在某个程序里按了没反应」。

    最常撞的：浏览器用 `Ctrl+数字` 切标签页。真撞上了就换成 `Alt+数字`，或者多加一个 ++shift++。

### 1.4 相关视频

有一期评测把上面这几个功能都演示了一遍，是拿 PixPin 和另一款老牌截图工具 Snipaste 对着讲的：

- [《几乎完美的截图软件？怕不是冲着Snipaste来的 | PixPin - 贴图、离线OCR、长截图、GIF录制》](https://www.bilibili.com/video/BV1Vu4y1G7Uw)

## 2. PicGo：图床客户端

### 2.1 什么是图床，为什么需要

图床就是一个专门用来存图片的地方。你把图片传上去，它给你一个网址；之后在哪儿用这个网址，图片就在哪儿显示。

需要它的原因是：Markdown 里插图只能插网址，不能插自己电脑上的文件路径。

- 你写 `![](C:\Users\你\Desktop\截图.png)`，自己看是没问题的 —— 这台电脑上确实有这个文件
- 但这份文档发出去，别人的电脑上并没有 `C:\Users\你\Desktop\截图.png`，看到的就是一个空的图框

所以实验报告、GitHub 上的 README、博客这类要发给别人的文档，里面的图都得先传到图床，再把网址填进去。这个网站的截图就是这么来的：每张图都存在腾讯云 COS 上（网址都是 `image-1379176255.cos.ap-shanghai.myqcloud.com` 开头）。

### 2.2 PicGo 干什么

PicGo 本身不提供存储，它是图床的客户端，只负责两件事：

1. 把图片传到你在用的那个图床
2. 把图床返回的网址，按你选的格式放进剪贴板

所以整个流程是：截完图 → ++ctrl+shift+u++ → 回文档里 ++ctrl+v++，粘出来的已经是一条完整的 Markdown 图片语法了。

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

只用密码保护的账号，密码一旦泄露，账号就是别人的了。两步验证是登录时再要一个「只有你手上这台设备能算出来」的六位数字，密码泄露了也进不去。

它的英文缩写是 2FA（two-factor authentication），网站的账号设置里写的多半就是这个字样。本文下面也一律叫 2FA。

重要的账号都建议开。开启之后，登录时除了输密码，还要输一个 30 秒换一次的六位码 —— 这个码就是 Ente Auth 这类 App 算出来的。

### 3.2 为什么是 Ente Auth

Ente Auth 在这几件事上做得比较好：

- 端到端加密的云备份：换手机扫一次登录，所有账号的验证码就都回来了
- 全设备同步：电脑、手机、网页上都装得上，验证码在每台设备上都是同一份
- 完全离线也能用：不注册账号也行，数据纯本地存
- 批量导入：能从别的验证器一次性导进来，不用一个个重新扫

### 3.3 下载安装

官网：<https://ente.io/auth/>

网页版直接打开就能用：<https://auth.ente.com>。

手机上在谷歌应用商店里搜 `Ente Auth`，电脑上从官网下载。

添加账号有三种方式：

1. 扫二维码（最常用）
2. 手动输入网站给的密钥
3. 从其他验证器批量导入

![Ente Auth 的账号列表](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260922102319338.png)


