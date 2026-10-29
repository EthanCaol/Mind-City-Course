---
icon: material/pencil-outline
---

# 作业 14：矩阵乘法

从键盘读入两个矩阵 A 和 B，其中 A 是 m 行 k 列、B 是 k 行 n 列，输出它们的乘积 C。

### 示例 1

输入：

```text
2 4 2
14 27 6 35
9 21 12 8
12 8
5 31
24 17
3 19
```

输出：

```text
552 1716
525 1079
```

解析：

$$
\begin{bmatrix}14&27&6&35\\9&21&12&8\end{bmatrix}_{2\times 4}
\times
\begin{bmatrix}12&8\\5&31\\24&17\\3&19\end{bmatrix}_{4\times 2}
=\begin{bmatrix}552&1716\\525&1079\end{bmatrix}_{2\times 2}
$$



### 提示

- 第一行三个整数 m、k、n，范围都是 1 到 100
- 接着 m 行是矩阵 $A_{m\times k}$
- 再接着 k 行是矩阵 $B_{k\times n}$
- 矩阵乘法得到的结果是 $C_{m\times n}$
- $C[i][j] = \sum_{t=0}^{k-1} A[i][t] * B[t][j]$
- 三个矩阵都可以直接开 `[100][100]`
- 元素绝对值不超过 100，结果落在 `int` 能表示的范围内
- 输出 m 行，每行 n 个整数，用空格分隔，行末换行
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业14">
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

<script src="/assets/katex/katex.min.js"></script>
<script src="/assets/katex/auto-render.min.js"></script>
<script>renderMathInElement(document.querySelector('.md-content'));</script>
