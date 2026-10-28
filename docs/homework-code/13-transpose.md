---
icon: material/pencil-outline
---

# 作业 13：矩阵转置

从键盘读入一个 m 行 n 列的整数矩阵，输出它的转置。

### 示例 1

输入：

```text
2 3
1 2 3
4 5 6
```

输出：

```text
1 4
2 5
3 6
```

### 示例 2

输入：

```text
1 4
7 8 9 10
```

输出：

```text
7
8
9
10
```

### 提示

- 第一行两个整数 m 和 n，范围都是 1 到 100
- 之后 m 行，每行 n 个整数，用空格分隔
- 转置后是 n 行 m 列，原来第 i 行第 j 列的元素，转置后位于第 j 行第 i 列
- 二维数组的两个维度都要写成常量，直接开 `a[100][100]` 即可，实际只用前 m 行、前 n 列
- 输出 n 行，每行 m 个整数，用空格分隔，行末换行
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业13">
  <div class="judge__bar">
    <label class="judge__label" for="judge-id">你的学号：</label>
    <input id="judge-id" class="judge__id" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="11位学号">
    <button id="judge-submit" type="button">提交</button>
  </div>

  <div class="judge__editor">
    <pre class="judge__gutter" id="judge-gutter" aria-hidden="true"></pre>
    <pre class="judge__highlight" id="judge-highlight" aria-hidden="true"></pre>
    <textarea id="judge-code" class="judge__code" spellcheck="false" placeholder="// 在这里粘贴你的代码"></textarea>
  </div>

  <p class="judge__progress" id="judge-progress" hidden></p>
  <p class="judge__error" id="judge-error" hidden></p>
  <p class="judge-summary" id="judge-summary" hidden></p>

  <div class="judge__compile" id="judge-compile-error" hidden>
    <p>编译未通过，报错信息如下：</p>
    <pre></pre>
  </div>

  <div id="judge-cases" hidden></div>
</div>


!!! note "判题环境"

    判题用的是服务器的 `isolate` 沙箱：

    - 操作系统：Ubuntu-26.04
    - 编译器：GCC 15.2.0
    - 编译参数：`-O2 -std=gnu23`
    - 每个测试点限时 1 秒
    - 每个测试点限制内存 256 MB
