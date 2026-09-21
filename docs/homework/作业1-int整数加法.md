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

## 1. 在线评测

把代码粘进下面的框里提交，几秒后就能看到哪几个测试点没过。**每个测试点的输入、期望输出和你的实际输出都会显示出来**，方便自己定位问题。全过就算完成。

!!! warning "代码第一行必须写学号"

    注释符后面只能有学号，多一个字都不行：

    ```c
    // 26113050003
    ```

    学号必须在本课程名单里，否则会被拒绝。姓名不用写——系统按学号从名单里查。

<div class="judge" id="judge" data-homework="作业1">
  <div class="judge__bar">
    <button id="judge-submit" type="button">提交</button>
    <a class="judge__last" id="judge-last" href="#" hidden>查看最近一次结果</a>
  </div>

  <div class="judge__editor">
    <pre class="judge__gutter" id="judge-gutter" aria-hidden="true"></pre>
    <pre class="judge__highlight" id="judge-highlight" aria-hidden="true"></pre>
    <textarea id="judge-code" class="judge__code" spellcheck="false" placeholder="// 26113050003&#10;#include &lt;stdio.h&gt;&#10;&#10;int main(void) {&#10;    ...&#10;}"></textarea>
  </div>

  <p class="judge__progress" id="judge-progress" hidden></p>
  <p class="judge__error" id="judge-error" hidden></p>
  <p class="judge-summary" id="judge-summary" hidden></p>

  <div class="judge__compile" id="judge-compile-error" hidden>
    <p>编译没有通过，编译器说：</p>
    <pre></pre>
  </div>

  <div id="judge-cases" hidden></div>
</div>

同一份代码重复提交不会重复判题，直接返回上次的结果；改了代码再交就会重新判。判题用的是服务器的 `isolate` 沙箱：编译参数固定 `-O2 -std=c11`，每个测试点限时 1 秒、限内存 256 MB，沙箱内没有网络。

## 2. 评分要点

程序能编译通过、对给定输入输出正确，就能满分。交之前请自己先编译运行一遍，确认输出和样例一致。

## 3. 交到 eLearning

在线评测只是自查工具，**正式提交仍然走 eLearning**：<https://elearning.fudan.edu.cn/courses/114551/assignments/137188>

提交单个 `.c` 源文件即可，不要交 `.exe`，也不要打包压缩。文件命名为 `学号-姓名-作业1.c`。

本作业不设截止时间，随时可以提交。

!!! tip "遇到问题怎么办"
    编译报错看不懂、环境装不上，都属正常，直接到课程群里问，或者联系助教。还没配好环境的同学，先看「实验课」一栏里的教程：

    - Windows：[WSL2 + VSCode](../setup/wsl2-vscode.md)（推荐）或 [Dev-C++](../setup/dev-cpp.md)（备选）
    - macOS：[VSCode + Apple clang](../setup/macos-vscode.md)
