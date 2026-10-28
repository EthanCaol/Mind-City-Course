---
icon: material/pencil-outline
---

# 作业 16：选择排序

从键盘读入 n 个整数，用选择排序把它们按从小到大的顺序排列后输出。

讲解视频：[选择排序｜动画演示 + 逐轮拆解](https://www.bilibili.com/video/BV1CZHg6fEJ7)

以下为 Python 版本的选择排序示例，算法的可行性与复杂性证明见页面底部。

```py
def SELECTION_SORT(A):
    n = len(A)
    for i in range(n - 1):
        minI = i

        # 在未排序部分中找最小值
        for j in range(i + 1, n):
            if A[j] < A[minI]:
                minI = j

        # 把最小值交换到未排序部分的首位
        if minI != i:
            A[i], A[minI] = A[minI], A[i]
```

### 示例 1

输入：

```text
7
4 2 9 1 7 6 3
```

输出：

```text
1 2 3 4 6 7 9
```

### 示例 2

输入：

```text
4
0 -5 0 8
```

输出：

```text
-5 0 0 8
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

<div class="judge" id="judge" data-homework="作业16">
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

## 选择排序-可行性与复杂性证明

```py
def SELECTION_SORT(A):
    n = len(A)
    for i in range(n - 1):
        minI = i

        # 在未排序部分中找最小值
        for j in range(i + 1, n):
            if A[j] < A[minI]:
                minI = j

        # 把最小值交换到未排序部分的首位
        if minI != i:
            A[i], A[minI] = A[minI], A[i]
```

### 算法可行性证明

循环不变量：在每次循环开始时，前$i$个元素有序，且是整个数组中最小的部分
1. 起始：当$i=0$时，前0个元素为空，结论成立
2. 递推：已知前$i$个元素已就位，内层循环在剩余元素中找到最小值
    并交换到数组的第$i+1$位置，保持前$i+1$个最小且有序
3. 结束：当$i=n-1$时，前$n-1$个元素最小且有序
    剩下的元素就是最大值，因此整个数组有序

------

### 最好情况复杂度

最好情况：如果输入数组已有序
内层循环仍要扫描整个未排序部分才能确定最小值
因此比较次数是 $\frac{n(n-1)}{2}=\Theta(n^2)$
交换次数为0，总时间复杂度仍为$\Theta(n^2)$

------

### 最坏情况复杂度

最坏情况：如果输入数组已反向有序
内层循环要扫描整个未排序部分才能确定最小值
因此比较次数是 $\frac{n(n-1)}{2}=\Theta(n^2)$
交换次数为$n-1$，总时间复杂度仍为$\Theta(n^2)$

------

### 平均复杂度

比较次数与输入无关，恒为$\frac{n(n-1)}{2}=\Theta(n^2)$
交换次数：当外层循环为$i$时，未排序部分有$n-i$个元素
最小值恰在首位的概率为$\frac{1}{n-i}$，所以该轮发生交换的概率为$1-\frac{1}{n-i}$

记调和数为 $H_n=\sum_{m=1}^{n}\frac{1}{m}$

$$
\begin{aligned}
E[X]
&= \sum_{i=0}^{n-2}\left(1-\frac{1}{n-i}\right) \\
&= \sum_{i=0}^{n-2}1 - \sum_{i=0}^{n-2}\frac{1}{n-i} \\
&= (n-1) - \left(\frac{1}{n}+\frac{1}{n-1}+\cdots+\frac{1}{2}\right) \\
&= (n-1) - (H_n - 1) \\
&= n - H_n \\
&= \Theta(n)
\end{aligned}
$$

故总时间复杂度为 $\Theta(n^2)+\Theta(n)=\Theta(n^2)$

------

### 选择排序是不稳定排序

选择排序不稳定：交换会把后面的相等元素跨到前面
例如：$[2_a,2_b,1]$ 在第一轮交换首尾，得到 $[1,2_b,2_a]$，两个$2$的次序颠倒



!!! note "判题环境"

    判题用的是服务器的 `isolate` 沙箱：

    - 操作系统：Ubuntu-26.04
    - 编译器：GCC 15.2.0
    - 编译参数：`-O2 -std=gnu23`
    - 每个测试点限时 1 秒
    - 每个测试点限制内存 256 MB
