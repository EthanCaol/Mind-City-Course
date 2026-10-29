---
icon: material/pencil-outline
---

# 作业 17：插入排序

从键盘读入 n 个整数，用插入排序把它们按从小到大的顺序排列后输出。

讲解视频：[插入排序｜动画演示 + 逐轮拆解](https://www.bilibili.com/video/BV1wznZ6sEzq)

以下为 Python 版本的插入排序示例，算法的可行性与复杂性证明见页面底部。

```py
def INSERTION_SORT(A):
    n = len(A)
    for i in range(1, n):
        key, k = A[i], i - 1

        # 将第i张牌 往前插入到 (i-1)的有序牌堆中
        while k >= 0 and A[k] > key:
            A[k + 1] = A[k]
            k = k - 1
        A[k + 1] = key
```

### 示例 1

输入：

```text
6
9 8 0 2 4 5
```

输出：

```text
0 2 4 5 8 9
```

### 示例 2

输入：

```text
5
-3 12 -3 7 0
```

输出：

```text
-3 -3 0 7 12
```

### 提示

- 第一行一个整数 n，范围是 1 到 1000
- 第二行 n 个整数，用空格分隔
- 输出一行 n 个整数，从小到大排列，用空格分隔，行末换行
- 判题只看输出的序列，用别的方法排出同样的结果也算通过
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业17">
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

## 插入排序-可行性与复杂性证明

更详细的证明讲解，见《算法导论（原书第3版）》的第2.1节部分

```py
def INSERTION_SORT(A):
    n = len(A)
    for i in range(1, n):
        key, k = A[i], i - 1

        # 将第i张牌 往前插入到 (i-1)的有序牌堆中
        while k >= 0 and A[k] > key:
            A[k + 1] = A[k]
            k = k - 1
        A[k + 1] = key
```

### 算法可行性证明

循环不变量：在每次循环开始时，子数组$\{0,\cdots,i-1\}$是有序的
1. 起始：外层循环从$i=1$开始，此时子数组只有一个元素，满足有序
2. 递推：已知$\{0,\cdots,i-1\}$有序，由算法过程可知，插入之后$\{0,\cdots,i\}$仍然有序
3. 结束：最后一轮$i=n-1$结束后，整个数组有序

------

### 最好情况复杂度

最好情况：如果输入数组已有序
那么对于每张牌，while循环都只需比较1次
因此时间复杂度 $n-1=\Theta(n)$

------

### 最坏情况复杂度

最坏情况：如果输入数组已反向排序
那么对于外层循环$i$，while循环需要比较$i$次
因此时间复杂度 $\sum_1^{n-1} i=\frac{n(n-1)}{2}=\Theta(n^2)$

------

### 平均复杂度

随机变量 $X_i=\{第i张牌需要比较的次数\}$
- 第i张牌 是前i张牌中最大的概率为 $1/i$
- 是第2大的概率为 $1/i$
- $\cdots$
- 是第i大的概率为 $1/i$

$$\begin{aligned}
E[X_i] &= 1\cdot\frac{1}{i} + 2\cdot\frac{1}{i} + \cdots + i\cdot\frac{1}{i} \\
       &= \sum_{k=1}^{i} k\cdot\frac{1}{i} \\
       &= \frac{(1+i)i}{2}\cdot\frac{1}{i} \\
       &= \frac{1+i}{2}
\end{aligned}$$

总比较次数的期望为
$$\begin{aligned}
E[X] &= \sum_{i=2}^{n} E[X_i] \\
     &= \sum_{i=2}^{n} \frac{1+i}{2} \\
     &= \frac{3+\cdots+(1+n)}{2} \\
     &= \frac{(4+n)(n-1)}{2\cdot 2} \\
     &= \Theta(n^2)
\end{aligned}$$

------

### 插入排序是稳定排序

插入排序稳定：while循环的条件为$A[k] > key$，相等时就不再移动
相等的两个元素不会跨过对方，相对次序保持不变



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
