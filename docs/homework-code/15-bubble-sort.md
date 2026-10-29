---
icon: material/pencil-outline
---

# 作业 15：冒泡排序

从键盘读入 n 个整数，用冒泡排序把它们按从小到大的顺序排列后输出。

讲解视频：[冒泡排序｜动画演示 + 逐轮拆解](https://www.bilibili.com/video/BV1DbHw62EMM)

以下为 Python 版本的冒泡排序示例，算法的可行性与复杂性证明见页面底部。

```py
def BUBBLE_SORT(A):
    n = len(A)
    for i in range(n - 1):
        swapped = False

        # 每轮把未排序部分的最大值 冒泡到末尾部分
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        # 本轮没有发生交换, 说明已经有序
        if not swapped:
            break
```

### 示例 1

输入：

```text
5
3 1 2 5 4
```

输出：

```text
1 2 3 4 5
```

### 示例 2

输入：

```text
4
-2 8 -2 0
```

输出：

```text
-2 -2 0 8
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

<div class="judge" id="judge" data-homework="作业15">
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

## 冒泡排序-可行性与复杂性证明

```py
def BUBBLE_SORT(A):
    n = len(A)
    for i in range(n - 1):
        swapped = False

        # 每轮把未排序部分的最大值 冒泡到末尾部分
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        # 本轮没有发生交换, 说明已经有序
        if not swapped:
            break
```

### 算法可行性证明

循环不变量：在每次循环开始时，末尾部分的子数组 $\{n-i,\cdots,n-1\}$ 是有序的
1. 起始：当$i=0$时，末尾含0个元素，子数组为空，结论成立
2. 递推：已知末尾 $i$个元素有序，内层循环时，依次对相邻元素进行比较，其中的最大元素会一直后移
    所以外层循环$i$ 结束时，$A[n-1-i]$成为该次循环的最大值，保证末尾$i+1$个元素始终有序
3. 结束：当$i=n-1$时，末尾$n-1$个元素都保证有序，剩下的第一个元素即是数组的最小值，因此整个数组有序

------

### 最好情况复杂度

最好情况：如果输入数组已有序
那么第一轮内层循环比较$n-1$次，没有发生交换，直接退出
比较次数为 $n-1=\Theta(n)$

------

### 最坏情况复杂度

最坏情况：如果输入数组已反向有序
那么当外层循环为$i$时，未排序部分有$n-i$个元素
内层循环需要做 $n-i-1$次相邻比较，每对都要交换

总的比较次数为 $\sum_{i=0}^{n-2}(n-1-i)=\frac{n(n-1)}{2}=\Theta(n^2)$
交换次数与比较次数相同，也是$\frac{n(n-1)}{2}=\Theta(n^2)$

------

### 平均复杂度

构造随机变量 $X_{ij}:=\{A[i]和A[j]是否逆序\}$
输入为随机排列时，对应概率为 $P(X_{ij}=1)=1/2$
得到期望为 $E[X_{ij}]=1\cdot1/2+0\cdot1/2=1/2$

总交换次数 $X=\sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1}X_{ij}$
总交换次数的期望为
$$\begin{aligned}
E[X] &= E[\ \sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1} X_{ij}\ ] \\
     &= \sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1} E[X_{ij}] \\
     &= \binom{n}{2}\cdot\frac{1}{2} \\
     &= \frac{n(n-1)}{4} \\
     &= \Theta(n^2)
\end{aligned}$$

------

### 冒泡排序是稳定排序

冒泡排序稳定：相邻比较用严格大于，相等时不交换
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
