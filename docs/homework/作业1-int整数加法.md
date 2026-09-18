---
icon: material/pencil-outline
---

# 作业 1：int 整数加法

<p class="doc-meta"><span>负责助教：<strong>曹奕伦</strong></span><span>提交平台：<strong>eLearning</strong></span></p>

写一个 C 程序，从键盘读入两个整数，计算并输出它们的和。

!!! abstract "题目要求"
    输入一行，两个整数，中间用空格分隔。保证这两个整数以及它们的和都在 `int` 能表示的范围内。

    输出一行，一个整数，即两数之和，行末换行。程序不要输出「请输入两个整数」之类的提示文字，除结果外不要输出任何内容。

样例：

| 输入    | 输出 |
| ------- | :--: |
| `3 5`   | `8`  |
| `-7 2`  | `-5` |

!!! tip "几个容易踩的坑"
    - 两个加数都用 `int` 类型存放，变量名自己取，取成能一眼看懂的。
    - 用 `scanf` 读入，注意取地址符 `&` 不要漏。
    - 代码要有缩进，关键的地方写上行注释。

## 1. 评分要点

程序能编译通过、对给定输入输出正确，就能拿到大部分分数；剩下的看代码是否整洁，也就是缩进、命名和注释。编译不过的代码扣分会比较重，交之前请自己先编译运行一遍，确认输出和样例一致。

## 2. 提交方式

在 eLearning 上提交：<https://elearning.fudan.edu.cn/courses/114551/assignments/137188>

交一个 `.c` 源文件即可，不要交 `.exe`，也不要打包压缩。截止时间和文件命名要求以 eLearning 页面为准。

!!! tip "遇到问题怎么办"
    编译报错看不懂、环境装不上，都属正常，直接到课程群里问，或者联系助教。还没配好环境的同学，先看「实验课」一栏里的教程：

    - Windows：[WSL2 + VSCode](../setup/wsl2-vscode.md)（推荐）或 [Dev-C++](../setup/dev-cpp.md)（备选）
    - macOS：[VSCode + Apple clang](../setup/macos-vscode.md)
