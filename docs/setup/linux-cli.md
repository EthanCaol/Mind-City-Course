# Linux 命令行基础

| 教程                                 | 内容描述                                       |
| ------------------------------------ | ---------------------------------------------- |
| 黑马程序员入门课程                   | 视频课，从命令基础讲到用户权限和日常操作       |
| 零基础最小入门在线文档               | 图文教程，只保留最核心的命令，另有一期配套视频 |
| 书籍：Linux命令行与shell脚本编程大全 | 命令行和 shell 脚本的系统教程，比文档讲得细    |
| 编辑器学习：vim                      | Linux 上的编辑器                               |

## 黑马程序员入门课程

!!! quote "视频"

    [《黑马程序员新版 Linux 零基础快速入门到精通》](https://www.bilibili.com/video/BV1n84y1i7td)

    ![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260928192840453.jpg)

这是一套成体系的入门视频课，按章节推进：

- 第一章：操作系统概述，因为已经配置好了wsl，这里可以直接跳过虚拟机安装
- 第二章：命令基础，从 `ls`、`cd` 讲到 `cp`、`mv`、`grep`、管道符、重定向和 vi
- 第三章：用户、用户组和权限
- 第四章：日常操作，软件安装、软链接、日期时区、IP 和主机名、端口、进程管理、环境变量、压缩解压


## 零基础最小入门在线文档

!!! quote "文档"

    [《只学够用的 Linux：零基础最小入门教程》](https://zouht.com/4399.html)

    ![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260924145737281.png)

------

该文作者自己也给文档录了一期视频：

!!! quote "视频"

    [《只学够用的 Linux：长度正好的零基础入门教程》](https://www.bilibili.com/video/BV13ctf6RECM)

    ![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260924145245076.png)

这篇教程的写法是「最小但够用」：只保留最核心的知识，面向完全没有接触过 Linux 的读者。内容大致包括：

- 内核与发行版、Shell 与命令的基本结构
- 目录、文件和路径，以及 Linux 的目录结构约定
- 复制、移动、重命名和删除
- 文本的查看与编辑
- 通配符、重定向、命令连接、变量、引号与转义
- 用户、用户组和权限
- 软件包管理
- 远程连接和文件传输

## 书籍：Linux命令行与shell脚本编程大全

在线文档为了「够用」删去了不少内容。

想要完整学习，可以同时看这本：

- [《Linux命令行与shell脚本编程大全》（第4版）](https://mind-city.com/downloads/Linux%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%B8%8Eshell%E8%84%9A%E6%9C%AC%E7%BC%96%E7%A8%8B%E5%A4%A7%E5%85%A8-%E7%AC%AC4%E7%89%88.pdf)

书籍内容分两部分：

- 前半部分讲命令行的使用，主题和文档里大致相同，但选项、例子和排错提示都更全；
- 后半部分讲 shell 脚本，从变量、条件判断、循环、函数讲到正则表达式、`sed` 和 `awk`，最后给了一批实用脚本。

## 编辑器学习：vim

[《保姆级入门：Vim 编辑器》](https://www.bilibili.com/video/BV13t4y1t7Wg)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260924173435000.jpg)

---

!!! todo "文档完成登记：完成本文全部流程后告知助教"

    <div class="read" id="read" data-page="linux-cli">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
