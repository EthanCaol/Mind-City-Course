


## 实数系

数系的扩充
- 自然数集 $N$: 对加法与乘法封闭, 对减法不封闭
- 整数集 $Z$: 对加法, 减法, 乘法封闭, 对除法不封闭
- 有理数集 $Q=\left\{x\mid x=\frac{q}{p},p\in N^*,q\in Z\right\}$: 对加法,
  减法, 乘法, 除法都封闭

数轴: 取一条水平直线, 定一点 $O$ 为原点, 取线段 $OA$ 为单位长度
$Z$ 的元素对应数轴上的整数点, 相邻两点间隔为 $1$, $Z$ 具有离散性
$Q$ 的元素对应数轴上的有理点, 任意长度大于 $0$ 的线段上都有无穷多个有理点, $Q$ 具有稠密性

[有理数集 $Q$ 是稠密的, 但没有填满整条数轴, 中间留有许多空隙]

------

边长为 $1$ 的正方形的对角线长度 $c$ 不能用有理数表示

证明: 由勾股定理 $c^2=2$, 反证法设 $c=\frac{q}{p}$,
其中 $p,q\in N^*$ 且 $p,q$ 互素

由 $\frac{q^2}{p^2}=2$ 得 $q^2=2p^2$, 奇数的平方是奇数, 故 $q$ 是偶数
设 $q=2r$, 代入得 $p^2=2r^2$, 故 $p$ 也是偶数, 与 $p,q$ 互素矛盾

所以 $c$ 不是有理数, 有理数集 $Q$ 对开方运算不封闭

------

实数集: $R=\{x\mid x\text{是有理数或无理数}\}$

无理数: 无限不循环小数
无理点填补了有理点在数轴上的所有空隙, 数轴上的每个点都对应唯一一个实数
[这一性质称为实数系 $R$ 的连续性, $R$ 称为实数连续统, 表示实数全体的坐标轴称为数轴]
[实数系的连续性是分析学的基础, 从分析学角度的表述之一是确界存在定理]

图2-1: 与单位正方形对角线长度 $c$ 对应的点位于有理点集合的空隙中

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192949000.png =600x)


## 最大数与最小数

$\exists$ 表示存在, $\forall$ 表示对于任意
$A\subseteq B\iff\forall x\in A$, 有 $x\in B$
$A\subsetneq B\iff\exists x\in A$, 使得 $x\in B$

------

最大数: 若 $\exists\xi\in S$, 使得 $\forall x\in S$,
有 $x\leq\xi$, 则称 $\xi$ 是数集 $S$ 的最大数,
记为 $\xi=\max S$

最小数: 若 $\exists\eta\in S$, 使得 $\forall x\in S$,
有 $x\geq\eta$, 则称 $\eta$ 是数集 $S$ 的最小数,
记为 $\eta=\min S$

非空有限集一定存在 $\max S$ 与 $\min S$
[无限集的最大数与最小数可能不存在]

------

> 例2-1: 集合 $A=\{x\mid x\geq0\}$ 没有最大数, 但有最小数, $\min A=0$

> 例2-2: 证明集合 $B=\{x\mid 0<x<1\}$ 没有最大数
>
> 证: 反证法, 设 $B$ 有最大数 $\beta$
> 由 $\beta\in(0,1)$ 知 $\beta'=\frac{1+\beta}{2}\in(0,1)$
> 但 $\beta'>\beta$, 与 $\beta$ 是 $B$ 的最大数矛盾


## 上确界与下确界

上界: 设 $S$ 是非空数集, 若 $\exists M\in R$,
使得 $\forall x\in S$, 有 $x\leq M$,
则称 $M$ 是 $S$ 的一个上界

下界: 若 $\exists m\in R$, 使得 $\forall x\in S$,
有 $x\geq m$, 则称 $m$ 是 $S$ 的一个下界

有界集: 既有上界又有下界的数集
$S$ 为有界集 $\iff\exists X>0$, 使得 $\forall x\in S$,
有 $|x|\leq X$

------

上确界 $\beta=\sup S$: 设 $S$ 有上界, 其上界全体构成的集合 $U$ 的最小数为 $\beta$
$\beta$ 满足
1. $\forall x\in S$, 有 $x\leq\beta$
2. $\forall\varepsilon>0$, $\exists x_0\in S$,
   使得 $x_0>\beta-\varepsilon$

下确界 $\alpha=\inf S$: 设 $S$ 有下界,
其下界全体构成的集合 $L$ 的最大数为 $\alpha$
$\alpha$ 满足
1. $\forall x\in S$, 有 $x\geq\alpha$
2. $\forall\varepsilon>0$, $\exists x_0\in S$,
   使得 $x_0<\alpha+\varepsilon$

------

定理(确界存在定理): 非空有上界的数集必有上确界, 非空有下界的数集必有下确界
[又称实数系连续性定理]

证: 任一实数 $x$ 可表示为 $x=[x]+(x)$, $[x]$ 是 $x$ 的整数部分,
$(x)$ 是 $x$ 的非负小数部分
$(x)$ 写成无限小数的形式 $(x)=0.a_1a_2\cdots a_n\cdots$

设 $S$ 有上界, 令 $a_0$ 为 $S$ 中元素整数部分的最大者,
记 $S_0=\{x\mid x\in S\text{且}[x]=a_0\}$
令 $a_1$ 为 $S_0$ 中元素第一位小数的最大者,
记 $S_1=\{x\mid x\in S_0\text{且}x\text{的第一位小数为}a_1\}$

一般地, 令 $a_n$ 为 $S_{n-1}$ 中元素第 $n$ 位小数的最大者,
记 $S_n=\{x\mid x\in S_{n-1}\text{且}x\text{的第}n\text{位小数为}a_n\}$
$S_n$ 非空, 且对任意 $x\in S_n$, 有 $x<a_0+0.a_1a_2\cdots a_n$

令 $\beta=a_0+0.a_1a_2\cdots a_n\cdots$,
下证 $\beta$ 是 $S$ 的上确界

1. 设 $x\in S$, 或存在整数 $n_0\geq0$ 使 $x\in S_{n_0}$,
   或对一切 $n\geq0$ 有 $x\in S_n$
   若 $x\in S_{n_0}$,
   有 $x<a_0+0.a_1a_2\cdots a_{n_0}\leq\beta$
   若 $x\in S_n(n\in N)$, 由 $S_n$ 的定义逐位比较知 $x=\beta$
   所以对一切 $x\in S$ 有 $x\leq\beta$, $\beta$ 是 $S$ 的上界

2. 对任意 $\varepsilon>0$,
   取 $n_0$ 充分大使 $\frac{1}{10^{n_0}}<\varepsilon$
   取 $x_0\in S_{n_0}$,
   则 $\beta-x_0\leq\frac{1}{10^{n_0}}<\varepsilon$,
   即 $x_0>\beta-\varepsilon$
   所以小于 $\beta$ 的数 $\beta-\varepsilon$ 不是 $S$ 的上界

同理可证非空有下界的数集必有下确界

------

定理: 非空有界数集的上确界与下确界唯一

------

> 例2-3: 设 $T=\{x\mid x\in Q\text{且}x>0,x^2<2\}$,
> 证明 $T$ 在 $Q$ 内没有上确界
>
> 证: 反证法, 设 $T$ 在 $Q$ 内有上确界 $\sup T=\frac{n}{m}$,
> 其中 $m,n\in N^*$ 且 $m,n$ 互素
> 则 $1<\left(\frac{n}{m}\right)^2<3$, 于是只有两种可能
>
> 1. $1<\left(\frac{n}{m}\right)^2<2$: 记 $2-\frac{n^2}{m^2}=t$,
>    则 $0<t<1$
>    令 $r=\frac{t}{6m}$, 显然 $\frac{n}{m}+r>0$,
>    $\frac{n}{m}-r>0$
>    由 $r^2=\frac{n^2t^2}{36m^4}<\frac{t}{18}$ 及 $\frac{2n}{m}r=\frac{n^2t}{3m^2}<\frac{t}{2}$ 可得
>    $\left(\frac{n}{m}+r\right)^2-2=r^2+\frac{2n}{m}r-t<0$
>    这说明 $\frac{n}{m}+r\in T$, 与 $\frac{n}{m}$ 是 $T$ 的上确界矛盾
>
> 2. $2<\left(\frac{n}{m}\right)^2<3$: 记 $\frac{n^2}{m^2}-2=t$,
>    则 $0<t<1$
>    令 $r=\frac{t}{6m}$,
>    由 $\frac{2n}{m}r=\frac{n^2t}{3m^2}<t$ 可得
>    $\left(\frac{n}{m}-r\right)^2-2=r^2-\frac{2n}{m}r+t>0$
>    这说明 $\frac{n}{m}-r$ 也是 $T$ 的上界,
>    与 $\frac{n}{m}$ 是 $T$ 的上确界矛盾
>
> 所以 $T$ 在 $Q$ 内没有上确界


## Dedekind 切割定理

切割: 设两个非空有理数集合 $A$ 和 $B$ 满足 $Q=A\cup B$,
且对任意 $a\in A$ 与 $b\in B$ 成立 $a<b$,
则称 $A$ 和 $B$ 构成 $Q$ 的一个切割, 记为 $A/B$

------

有理数集合 $Q$ 的任一切割 $A/B$ 有且仅有以下情况之一
1. $A$ 有最大数 $a_0$, $B$ 没有最小数
2. $A$ 没有最大数, $B$ 有最小数 $b_0$
3. $A$ 没有最大数, $B$ 没有最小数
4. $A$ 有最大数 $a_0$, $B$ 有最小数 $b_0$

情况 4 不可能发生: 由定义 $a_0<b_0$,
而 $\frac{a_0+b_0}{2}$ 也是 $Q$ 中的有理数,
与 $Q=A\cup B$ 矛盾

------

无理数: 有理数集 $Q$ 的切割 $A/B$ 中, 若 $A$ 没有最大数, $B$ 没有最小数,
则称该切割确定一个无理数 $c$, $c$ 大于 $A$ 中任何有理数, 小于 $B$ 中任何有理数
例: $A=\{x\mid x\in Q,x>0,x^2<2\}$ 没有最大数,
$B=\{x\mid x\in Q,x>0,x^2>2\}$ 有最小数,
该切割确定无理数 $\sqrt2$

实数集: 由有理数全体与由切割确定的全体无理数所构成的集合, 记为 $R$
[有理数中的四则运算与大小关系可移植到实数集 $R$, 如 $c,d\in R$
由切割 $A_1/B_1$, $A_2/B_2$ 确定, 则 $c+d$
由 $A=\{x_1+x_2\mid x_1\in A_1,x_2\in A_2\}$,
$B=Q-A$ 确定]

------

实数切割: 设两个非空实数集合 $\tilde A$ 和 $\tilde B$ 满足 $R=\tilde A\cup\tilde B$,
且对任意 $a\in\tilde A$ 与 $b\in\tilde B$ 成立 $a<b$,
则称 $\tilde A$ 和 $\tilde B$ 构成 $R$ 的一个切割,
记为 $\tilde A/\tilde B$

------

定理(Dedekind 切割定理): 设 $\tilde A/\tilde B$ 是实数集 $R$ 的一个切割,
则或者 $\tilde A$ 有最大数, 或者 $\tilde B$ 有最小数

证: 设 $\tilde A$ 中全体有理数构成 $A$,
$\tilde B$ 中全体有理数构成 $B$, 则 $A/B$ 是 $Q$ 的一个切割

1. $A$ 有最大数 $a_0$, $B$ 没有最小数: 则 $a_0$ 也是 $\tilde A$ 的最大数
2. $A$ 没有最大数, $B$ 有最小数 $b_0$: 则 $b_0$ 也是 $\tilde B$ 的最小数
3. $A$ 没有最大数, $B$ 没有最小数: 则该切割确定无理数 $c$,
   $c$ 属于 $\tilde A$ 或 $\tilde B$
   若 $c\in\tilde A$, 则 $c$ 是 $\tilde A$ 的最大数;
   若 $c\in\tilde B$, 则 $c$ 是 $\tilde B$ 的最小数

所以 Dedekind 定理成立

------

由 Dedekind 定理可给出确界存在定理的另一证明

证: 设非空实数集 $S$ 有上界,
令 $S$ 的上界全体构成的集合为 $\tilde B=\{y\mid y\geq t,\forall t\in S\}$
并令 $\tilde B$ 的补集为 $\tilde A=R\setminus\tilde B$
于是 $\tilde A/\tilde B$ 构成实数集 $R$ 的一个切割,
由 Dedekind 定理, 或 $\tilde A$ 有最大数,
或 $\tilde B$ 有最小数

对任意 $x\in\tilde A$, $x$ 不是 $S$ 的上界, 即存在 $t\in S$ 使得 $x<t$
令 $x'=\frac{x+t}{2}$, 则 $x<x'<t$,
由 $x'<t$ 知 $x'$ 也不是 $S$ 的上界, 于是 $x'\in\tilde A$
再由 $x<x'$ 知 $x$ 不是 $\tilde A$ 的最大数, 所以 $\tilde A$ 没有最大数

由此证得 $\tilde B$ 有最小数, 即集合 $S$ 必有最小上界, 即上确界


## 数列与数列极限

数列: 按正整数编了号的一串数 $x_1,x_2,\cdots,x_n,\cdots$
$x_n$ 称为数列的通项, 第 $n$ 项, 记数列为 $\{x_n\}$

例
- $\left\{\frac{1}{n}\right\}:1,\frac{1}{2},\frac{1}{3},\cdots,\frac{1}{n},\cdots$
- $\left\{\frac{n}{n+3}\right\}:\frac{1}{4},\frac{2}{5},\frac{3}{6},\cdots,\frac{n}{n+3},\cdots$
- $\{n^2\}:1,4,9,\cdots,n^2,\cdots$
- $\{(-1)^n\}:-1,1,-1,1,\cdots,(-1)^n,\cdots$

[数列与数集有区别: 数集中元素没有次序, 数列中各项有确定的编号, 前后次序不能颠倒, 重复出现的数不能随便舍去]
[常数列 $C,C,C,\cdots$ 反映一种特殊的变化规律]

------

定义(数列极限): 设 $\{x_n\}$ 是一给定数列, $a$ 是一个实常数
如果对于任意给定的 $\varepsilon>0$, 可以找到正整数 $N$,
使得当 $n>N$ 时成立 $|x_n-a|<\varepsilon$
则称数列 $\{x_n\}$ 收敛于 $a$, 称 $a$ 是数列 $\{x_n\}$ 的极限, 记为
$\lim\limits_{n\to\infty}x_n=a$
有时也记为 $x_n\to a\ (n\to\infty)$
若不存在实数 $a$ 使 $\{x_n\}$ 收敛于 $a$, 则称数列 $\{x_n\}$ 发散

符号表述: $\lim\limits_{n\to\infty}x_n=a\iff\forall\varepsilon>0,\ \exists N,\ \forall n>N:|x_n-a|<\varepsilon$

$\varepsilon$ 邻域: 开区间 $(a-\varepsilon,a+\varepsilon)$,
记为 $O(a,\varepsilon)=\{x\mid a-\varepsilon<x<a+\varepsilon\}$
$|x_n-a|<\varepsilon$ 表示数列从第 $N+1$ 项起的所有项都落在点 $a$ 的 $\varepsilon$ 邻域中,
即 $x_n\in O(a,\varepsilon)$, $n>N$

[$\varepsilon$ 既是任意的, 又是给定的,
只有 $\varepsilon$ 确定后才能找到相应的 $N$]
[数列收敛与否, 收敛于哪个数, 与数列前面的有限项无关]

图2-2: 数列极限 $\lim\limits_{n\to\infty}x_n=a$ 的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192949001.png =550x)

------

> 例2-4: 证明数列 $\left\{\frac{n}{n+3}\right\}$ 的极限为 $1$
>
> 证: 对任意给定的 $\varepsilon>0$,
> 要使 $\left|\frac{n}{n+3}-1\right|=\frac{3}{n+3}<\varepsilon$,
> 只须 $n>\frac{3}{\varepsilon}-3$
>
> 取 $N=\left[\frac{3}{\varepsilon}\right]+1$,
> 其中 $[x]$ 表示 $x$ 的整数部分
> 则当 $n>N$ 时成立 $\left|\frac{n}{n+3}-1\right|=\frac{3}{n+3}<\varepsilon$

------

数列 $\{n^2\}:1,4,9,\cdots,n^2,\cdots$ 与 $\{(-1)^n\}$ 是发散数列

无穷小量: 极限为 $0$ 的数列
例: $\left\{\frac{1}{n}\right\}$,
$\left\{\frac{(-1)^{n+1}}{n^2+1}\right\}$
常数列 $0,0,\cdots,0,\cdots$ 是一种特殊的无穷小量
$\lim\limits_{n\to\infty}x_n=a\iff\{x_n-a\}$ 是无穷小量

------

> 例2-5: 证明 $\{q^n\}(0<|q|<1)$ 是无穷小量
>
> 证: 对任意给定的 $\varepsilon>0$, 要使 $|q^n-0|=|q|^n<\varepsilon$
> 两边取对数, 即得 $n>\frac{\lg\varepsilon}{\lg|q|}$
>
> 取大于 $\frac{\lg\varepsilon}{\lg|q|}$ 的任意正整数即为 $N$
> 为保证 $N$ 是正整数,
> 取 $N=\max\left\{\left[\frac{\lg\varepsilon}{\lg|q|}\right],1\right\}$
> 则当 $n>N$ 时成立 $|q^n-0|=|q|^n<|q|^{\frac{\lg\varepsilon}{\lg|q|}}=\varepsilon$

[证明时常对 $|x_n-a|$ 适度放大, 是常用的技巧]

> 例2-6: 设 $a>1$, 证明 $\lim\limits_{n\to\infty}\sqrt[n]{a}=1$
>
> 证: 令 $\sqrt[n]{a}=1+y_n$, $y_n>0$, 应用二项式定理
> $a=(1+y_n)^n=1+ny_n+\frac{n(n-1)}{2}y_n^2+\cdots+y_n^n>1+ny_n$
> 得到 $|\sqrt[n]{a}-1|=y_n<\frac{a-1}{n}$
>
> 对任意给定的 $\varepsilon>0$,
> 取 $N=\left[\frac{a-1}{\varepsilon}\right]$,
> 当 $n>N$ 时成立 $|\sqrt[n]{a}-1|<\frac{a-1}{n}<\varepsilon$

> 例2-7: 证明 $\lim\limits_{n\to\infty}\sqrt[n]{n}=1$
>
> 证: 令 $\sqrt[n]{n}=1+y_n$, $y_n>0$, 应用二项式定理
> $n=(1+y_n)^n=1+ny_n+\frac{n(n-1)}{2}y_n^2+\cdots+y_n^n>1+\frac{n(n-1)}{2}y_n^2$
> 得到 $|\sqrt[n]{n}-1|=y_n<\sqrt{\frac{2}{n}}$
>
> 对任意给定的 $\varepsilon>0$,
> 取 $N=\left[\frac{2}{\varepsilon^2}\right]$,
> 当 $n>N$ 时成立 $|\sqrt[n]{n}-1|<\sqrt{\frac{2}{n}}<\varepsilon$
> 类似地可证 $\lim\limits_{n\to\infty}\sqrt[n]{n^k}=1\ (k\in N^*)$

> 例2-8: 证明 $\lim\limits_{n\to\infty}\frac{n^2+1}{2n^2-7n}=\frac{1}{2}$
>
> 证: $\left|\frac{n^2+1}{2n^2-7n}-\frac{1}{2}\right|=\left|\frac{7n+2}{2n(2n-7)}\right|$
> 当 $n>6$ 时,
> $\left|\frac{7n+2}{2n(2n-7)}\right|<\frac{8n}{2n^2}=\frac{4}{n}$
>
> 对任意给定的 $\varepsilon>0$,
> 取 $N=\max\left\{6,\left[\frac{4}{\varepsilon}\right]\right\}$
> 当 $n>N$ 时成立 $\left|\frac{n^2+1}{2n^2-7n}-\frac{1}{2}\right|<\frac{4}{n}<\varepsilon$
> [放大在条件 $n>6$ 下成立,
> 取 $N$ 时必须要求 $N\geq\left[\frac{4}{\varepsilon}\right]$ 与 $N\geq6$
> 同时成立]

> 例2-9: 证明: 若 $\lim\limits_{n\to\infty}a_n=a$,
> 则 $\lim\limits_{n\to\infty}\frac{a_1+a_2+\cdots+a_n}{n}=a$
>
> 证: 先设 $a=0$, 即 $\{a_n\}$ 是无穷小量
> 对任意给定的 $\varepsilon>0$, 有正整数 $N_1$,
> 当 $n>N_1$ 时 $|a_n|<\frac{\varepsilon}{2}$
> 现在 $a_1+a_2+\cdots+a_{N_1}$ 已经是固定数, 取 $N>N_1$,
> 使当 $n>N$ 时 $\left|\frac{a_1+a_2+\cdots+a_{N_1}}{n}\right|<\frac{\varepsilon}{2}$
>
> 利用三角不等式得到
> $\begin{aligned}\left|\frac{a_1+a_2+\cdots+a_n}{n}\right|&=\left|\frac{a_1+a_2+\cdots+a_{N_1}}{n}+\frac{a_{N_1+1}+a_{N_1+2}+\cdots+a_n}{n}\right|\\&\leq\left|\frac{a_1+a_2+\cdots+a_{N_1}}{n}\right|+\left|\frac{a_{N_1+1}+a_{N_1+2}+\cdots+a_n}{n}\right|\\&<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon\end{aligned}$
>
> 当 $a\neq0$ 时, $\{a_n-a\}$ 是无穷小量, 于是
> $\lim\limits_{n\to\infty}\left(\frac{a_1+a_2+\cdots+a_n}{n}-a\right)=\lim\limits_{n\to\infty}\frac{(a_1-a)+(a_2-a)+\cdots+(a_n-a)}{n}=0$


## 数列极限的性质

定理(极限的唯一性): 收敛数列的极限必唯一

证: 假设 $\{x_n\}$ 有极限 $a$ 与 $b$, 根据定义
$\forall\varepsilon>0$, $\exists N_1$,
$\forall n>N_1:|x_n-a|<\frac{\varepsilon}{2}$;
$\exists N_2$,
$\forall n>N_2:|x_n-b|<\frac{\varepsilon}{2}$

取 $N=\max\{N_1,N_2\}$, 利用三角不等式, 当 $n>N$ 时
$|a-b|=|a-x_n+x_n-b|\leq|x_n-a|+|x_n-b|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon$
由 $\varepsilon$ 的任意性知 $a=b$
[插项(加一项再减一项)并辅以三角不等式是常用技巧]

------

有界数列: 数列 $\{x_n\}$ 若存在实数 $M$ 使所有项满足 $x_n\leq M$, 则 $M$ 是上界
若存在实数 $m$ 使所有项满足 $m\leq x_n$, 则 $m$ 是下界
既有上界又有下界的数列称为有界数列

等价定义: 存在正数 $X$, 使所有项满足 $|x_n|\leq X$, $n=1,2,3,\cdots$

------

定理(收敛数列的有界性): 收敛数列必有界

证: 设数列 $\{x_n\}$ 收敛, 极限为 $a$, 取 $\varepsilon=1$,
则 $\exists N$, $\forall n>N:|x_n-a|<1$,
即 $a-1<x_n<a+1$

取 $M=\max\{x_1,x_2,\cdots,x_N,a+1\}$,
$m=\min\{x_1,x_2,\cdots,x_N,a-1\}$
则对 $\{x_n\}$ 所有的项成立 $m\leq x_n\leq M$
[逆命题不成立, 有界数列未必收敛, 如 $\{(-1)^n\}$ 有界但不收敛]

------

定理(保序性): 设数列 $\{x_n\}$, $\{y_n\}$ 均收敛,
$\lim\limits_{n\to\infty}x_n=a$,
$\lim\limits_{n\to\infty}y_n=b$, 且 $a<b$
则存在正整数 $N$, 当 $n>N$ 时成立 $x_n<y_n$

证: 取 $\varepsilon=\frac{b-a}{2}>0$
由 $\lim\limits_{n\to\infty}x_n=a$, $\exists N_1$,
$\forall n>N_1:|x_n-a|<\frac{b-a}{2}$,
即 $x_n<a+\frac{b-a}{2}=\frac{a+b}{2}$

由 $\lim\limits_{n\to\infty}y_n=b$, $\exists N_2$,
$\forall n>N_2:|y_n-b|<\frac{b-a}{2}$,
即 $y_n>b-\frac{b-a}{2}=\frac{a+b}{2}$

取 $N=\max\{N_1,N_2\}$,
$\forall n>N$: $x_n<\frac{a+b}{2}<y_n$

图2-3: 保序性的几何意义, 从某项开始 $x_n$ 与 $y_n$ 分别落在两个不相交的区间中

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192949002.png =600x)

由保序性可得下面的推论
1. 若 $\lim\limits_{n\to\infty}y_n=b>0$, 则存在正整数 $N$,
   当 $n>N$ 时 $y_n>\frac{b}{2}>0$
2. 若 $\lim\limits_{n\to\infty}y_n=b<0$, 则存在正整数 $N$,
   当 $n>N$ 时 $y_n<\frac{b}{2}<0$

[保序性的逆命题不成立: 由 $\lim x_n=a$, $\lim y_n=b$
且 $x_n<y_n$ 对 $n>N$ 成立, 不能得出 $a<b$]
[正确的结论: 若 $\lim\limits_{n\to\infty}x_n=a$,
$\lim\limits_{n\to\infty}y_n=b$,
且 $x_n\leq y_n$ 对 $n>N$ 成立, 则 $a\leq b$]

------

定理(夹逼性): 若三个数列 $\{x_n\}$, $\{y_n\}$,
$\{z_n\}$ 从某项开始成立 $x_n\leq y_n\leq z_n$
且 $\lim\limits_{n\to\infty}x_n=\lim\limits_{n\to\infty}z_n=a$,
则 $\lim\limits_{n\to\infty}y_n=a$

证: $\forall\varepsilon>0$,
由 $\lim\limits_{n\to\infty}x_n=a$, $\exists N_1$,
$\forall n>N_1:|x_n-a|<\varepsilon$,
从而 $a-\varepsilon<x_n$
由 $\lim\limits_{n\to\infty}z_n=a$, $\exists N_2$,
$\forall n>N_2:|z_n-a|<\varepsilon$,
从而 $z_n<a+\varepsilon$

取 $N=\max\{N_0,N_1,N_2\}$,
$\forall n>N$: $a-\varepsilon<x_n\leq y_n\leq z_n<a+\varepsilon$
即 $|y_n-a|<\varepsilon$

------

> 例2-10: 求数列 $\{\sqrt{n+1}-\sqrt{n}\}$ 的极限
>
> 解: $\sqrt{n+1}-\sqrt{n}=\frac{(\sqrt{n+1}-\sqrt{n})(\sqrt{n+1}+\sqrt{n})}{\sqrt{n+1}+\sqrt{n}}=\frac{1}{\sqrt{n+1}+\sqrt{n}}$
> 取 $x_n=0$, $y_n=\sqrt{n+1}-\sqrt{n}$,
> $z_n=\frac{1}{\sqrt{n}}$, 有 $x_n<y_n<z_n$
> 且 $\lim\limits_{n\to\infty}x_n=\lim\limits_{n\to\infty}z_n=0$
> 由夹逼性得 $\lim\limits_{n\to\infty}(\sqrt{n+1}-\sqrt{n})=0$

> 例2-11: 证明
> $\lim\limits_{n\to\infty}(a_1^p+a_2^p+\cdots+a_k^p)^{\frac{1}{p}}=\max\limits_{1\leq i\leq k}|a_i|$,
> 其中 $a_i\geq0$
>
> 证: 不妨设 $a_1=\max\limits_{1\leq i\leq k}|a_i|$
> 有 $a_1\leq(a_1^p+a_2^p+\cdots+a_k^p)^{\frac{1}{p}}\leq a_1\sqrt[p]{k}$
>
> 由 $\lim\limits_{n\to\infty}\sqrt[n]{p}=1$ 知 $\lim\limits_{p\to\infty}a_1\sqrt[p]{k}=a_1$
> 由夹逼性得 $\lim\limits_{p\to\infty}(a_1^p+a_2^p+\cdots+a_k^p)^{\frac{1}{p}}=a_1=\max\limits_{1\leq i\leq k}|a_i|$


## 数列极限的四则运算

定理: 设 $\lim\limits_{n\to\infty}x_n=a$,
$\lim\limits_{n\to\infty}y_n=b$, 则
1. $\lim\limits_{n\to\infty}(\alpha x_n+\beta y_n)=\alpha a+\beta b$ ($\alpha,\beta$ 是常数)
2. $\lim\limits_{n\to\infty}(x_ny_n)=ab$
3. $\lim\limits_{n\to\infty}\frac{x_n}{y_n}=\frac{a}{b}$ ($b\neq0$)

证: 由 $\lim\limits_{n\to\infty}x_n=a$,
$\exists X>0$ 使 $|x_n|\leq X$
$\forall\varepsilon>0$, $\exists N_1$,
$\forall n>N_1:|x_n-a|<\varepsilon$;
由 $\lim\limits_{n\to\infty}y_n=b$, $\exists N_2$,
$\forall n>N_2:|y_n-b|<\varepsilon$
取 $N=\max\{N_1,N_2\}$, $\forall n>N$ 有
$|(\alpha x_n+\beta y_n)-(\alpha a+\beta b)|\leq|\alpha|\cdot|x_n-a|+|\beta|\cdot|y_n-b|<(|\alpha|+|\beta|)\varepsilon$
$|x_ny_n-ab|=|x_n(y_n-b)+b(x_n-a)|<(X+|b|)\varepsilon$
所以 (1)(2) 成立

对 (3), 由保序性的推论 $\exists N_0$,
$\forall n>N_0:|y_n|>\frac{|b|}{2}$
取 $N=\max\{N_0,N_1,N_2\}$,
$\forall n>N$:
$\left|\frac{x_n}{y_n}-\frac{a}{b}\right|=\left|\frac{b(x_n-a)-a(y_n-b)}{y_nb}\right|<\frac{2(|a|+|b|)}{b^2}\varepsilon$
[最后的不等式小于 $\varepsilon$ 乘上一个常数, 不违背数列极限的定义]

------

> 例2-12: 求极限 $\lim\limits_{n\to\infty}\frac{5^{n+1}-(-2)^n}{3\cdot5^n+2\cdot3^n}$
>
> 解: $\lim\limits_{n\to\infty}\frac{5^{n+1}-(-2)^n}{3\cdot5^n+2\cdot3^n}=\lim\limits_{n\to\infty}\frac{5-\left(-\frac{2}{5}\right)^n}{3+2\left(\frac{3}{5}\right)^n}=\frac{5}{3}$

> 例2-13: 证明: 当 $a>0$ 时,
> $\lim\limits_{n\to\infty}\sqrt[n]{a}=1$
>
> 证: 已证 $a>1$ 时成立, $a=1$ 时结论平凡
> 当 $0<a<1$ 时, $\frac{1}{a}>1$, 利用四则运算
> $\lim\limits_{n\to\infty}\sqrt[n]{a}=\lim\limits_{n\to\infty}\frac{1}{\sqrt[n]{\frac{1}{a}}}=1$

> 例2-14: 求极限 $\lim\limits_{n\to\infty}n(\sqrt{n^2+1}-\sqrt{n^2-1})$
>
> 解: $\lim\limits_{n\to\infty}n(\sqrt{n^2+1}-\sqrt{n^2-1})=\lim\limits_{n\to\infty}\frac{2n^2}{\sqrt{n^2+1}+\sqrt{n^2-1}}=\lim\limits_{n\to\infty}\frac{2}{\sqrt{1+\frac{1}{n^2}}+\sqrt{1-\frac{1}{n^2}}}=1$
>
> 这里用到: 若 $x_n\geq0$,
> $\lim\limits_{n\to\infty}x_n=a\geq0$,
> 则 $\lim\limits_{n\to\infty}\sqrt{x_n}=\sqrt{a}$
> [数列极限的四则运算只能推广到有限个数列, 不能推广到无限个数列]

> 例2-15: 设 $a_n>0$,
> 且 $\lim\limits_{n\to\infty}a_n=a$,
> 证明 $\lim\limits_{n\to\infty}\sqrt[n]{a_1a_2\cdots a_n}=a$
>
> 证: 当 $a>0$ 时, 由平均值不等式
> $\frac{a_1+a_2+\cdots+a_n}{n}\geq\sqrt[n]{a_1a_2\cdots a_n}\geq\frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+\cdots+\frac{1}{a_n}}$
>
> 将右端写成 $\frac{1}{\left(\frac{1}{a_1}+\frac{1}{a_2}+\cdots+\frac{1}{a_n}\right)/n}$
> 由 $\lim\limits_{n\to\infty}a_n=a>0$ 知 $\lim\limits_{n\to\infty}\frac{1}{a_n}=\frac{1}{a}$
> 由例2-9 和四则运算, 不等式左右两端的极限都是 $a$
> 由夹逼性得 $\lim\limits_{n\to\infty}\sqrt[n]{a_1a_2\cdots a_n}=a$
>
> 当 $a=0$ 时,
> 由 $\frac{a_1+a_2+\cdots+a_n}{n}\geq\sqrt[n]{a_1a_2\cdots a_n}>0=a$ 同样由夹逼性推出结论


## 无穷大量

定义(无穷大量): 若对于任意给定的 $G>0$, 可以找到正整数 $N$,
使得当 $n>N$ 时成立 $|x_n|>G$
则称数列 $\{x_n\}$ 是无穷大量,
记为 $\lim\limits_{n\to\infty}x_n=\infty$
符号表述: $\forall G>0$, $\exists N$, $\forall n>N:|x_n|>G$

正无穷大量: 若从某一项开始 $x_n$ 都是正的,
记为 $\lim\limits_{n\to\infty}x_n=+\infty$

负无穷大量: 若从某一项开始 $x_n$ 都是负的,
记为 $\lim\limits_{n\to\infty}x_n=-\infty$
[统称为定号无穷大量]

例: $\{n^2\}$ 是正无穷大量, $\{-10^n\}$ 是负无穷大量,
$\{(-2)^n\}$ 是不定号无穷大量

------

> 例2-16: 设 $|q|>1$, 证明 $\{q^n\}$ 是无穷大量
>
> 证: $\forall G>1$,
> 取 $N=\left[\frac{\lg G}{\lg|q|}\right]$,
>
> 于是 $\forall n>N$ 成立
> $|q^n|>|q|^{\frac{\lg G}{\lg|q|}}=G$

> 例2-17: 证明 $\left\{\frac{n^2-1}{n+5}\right\}$ 是正无穷大量
>
> 证: 当 $n>5$ 时, 有 $\frac{n^2-1}{n+5}>\frac{n}{2}$
> $\forall G>0$, 取 $N=\max\{2G,5\}$,
> $\forall n>N$: $\frac{n^2-1}{n+5}>\frac{n}{2}>G$

------

定理: 设 $x_n\neq0$,
则 $\{x_n\}$ 是无穷大量的充分必要条件是 $\left\{\frac{1}{x_n}\right\}$ 是无穷小量

证: 设 $\{x_n\}$ 是无穷大量, $\forall\varepsilon>0$,
取 $G=\frac{1}{\varepsilon}>0$
于是 $\exists N$,
$\forall n>N:|x_n|>G=\frac{1}{\varepsilon}$,
从而 $\left|\frac{1}{x_n}\right|<\varepsilon$

反过来, 设 $\left\{\frac{1}{x_n}\right\}$ 是无穷小量,
$\forall G>0$, 取 $\varepsilon=\frac{1}{G}>0$
则 $\exists N$,
$\forall n>N:\left|\frac{1}{x_n}\right|<\varepsilon=\frac{1}{G}$,
从而 $|x_n|>G$

------

定理: 设 $\{x_n\}$ 是无穷大量,
当 $n>N_0$ 时 $|y_n|\geq\delta>0$ 成立,
则 $\{x_ny_n\}$ 是无穷大量

推论: 设 $\{x_n\}$ 是无穷大量,
$\lim\limits_{n\to\infty}y_n=b\neq0$,
则 $\{x_ny_n\}$ 与 $\left\{\frac{x_n}{y_n}\right\}$ 都是无穷大量

------

以下极限直接求出
$\lim\limits_{n\to\infty}(10^n+\sqrt{n})=+\infty$,
$\lim\limits_{n\to\infty}\left(n-\lg\frac{1}{n}\right)=+\infty$
$\lim\limits_{n\to\infty}\sqrt{n}\arctan n=+\infty$,
$\lim\limits_{n\to\infty}\frac{n}{\sin n}=\infty$


## 待定型

$\infty-\infty$, $0\cdot\infty$,
$\frac{\infty}{\infty}$, $\frac{0}{0}$ 等类型的极限称为待定型
其极限可以是无穷小量, 非零极限, 无穷大量, 也可以没有极限
[如 $\lim\limits_{n\to\infty}n(\sqrt{n+1}-\sqrt{n})$ 是 $0\cdot\infty$ 待定型,
$\lim\limits_{n\to\infty}\frac{a_1+a_2+\cdots+a_n}{n}$ 是 $\frac{\infty}{\infty}$ 待定型]

------

定义(单调数列): 若数列 $\{x_n\}$ 满足 $x_n\leq x_{n+1}$,
$n=1,2,3,\cdots$, 则称 $\{x_n\}$ 为单调增加数列
若进一步满足 $x_n<x_{n+1}$, 则称 $\{x_n\}$ 为严格单调增加数列

类似定义单调减少数列与严格单调减少数列
[数列前面有限项的变化不影响收敛性, 谈单调数列时可将"从某一项开始为单调的数列"统一包括在内]

------

定理(Stolz 定理): 设 $\{y_n\}$ 是严格单调增加的正无穷大量, 且
$\lim\limits_{n\to\infty}\frac{x_n-x_{n-1}}{y_n-y_{n-1}}=a$ ($a$ 可以是有限量,
$+\infty$ 或 $-\infty$)
则 $\lim\limits_{n\to\infty}\frac{x_n}{y_n}=a$

证: 先考虑 $a=0$ 的情况.
由 $\lim\limits_{n\to\infty}\frac{x_n-x_{n-1}}{y_n-y_{n-1}}=0$,
可知 $\forall\varepsilon>0$, $\exists N_1$,
$\forall n>N_1$: $|x_n-x_{n-1}|<\varepsilon(y_n-y_{n-1})$
由于 $\{y_n\}$ 是正无穷大量, 可要求 $y_n>0$, 于是
$|x_n-x_{N_1}|\leq|x_n-x_{n-1}|+|x_{n-1}-x_{n-2}|+\cdots+|x_{N_1+1}-x_{N_1}|<\varepsilon(y_n-y_{N_1})$
不等式两边同除以 $y_n$,
得到 $\left|\frac{x_n}{y_n}-\frac{x_{N_1}}{y_n}\right|\leq\varepsilon\left(1-\frac{y_{N_1}}{y_n}\right)<\varepsilon$
对固定的 $N_1$, 又可取 $N>N_1$,
使得 $\forall n>N:\left|\frac{x_{N_1}}{y_n}\right|<\varepsilon$
从而 $\left|\frac{x_n}{y_n}\right|<\varepsilon+\left|\frac{x_{N_1}}{y_n}\right|<2\varepsilon$

当 $a$ 是非零有限数时, 令 $x_n'=x_n-ay_n$, 于是由
$\lim\limits_{n\to\infty}\frac{x_n'-x_{n-1}'}{y_n-y_{n-1}}=\lim\limits_{n\to\infty}\frac{x_n-x_{n-1}}{y_n-y_{n-1}}-a=0$
得到 $\lim\limits_{n\to\infty}\frac{x_n'}{y_n}=0$,
从而 $\lim\limits_{n\to\infty}\frac{x_n}{y_n}=\lim\limits_{n\to\infty}\frac{x_n'}{y_n}+a=a$

对 $a=+\infty$, 首先 $\exists N$,
$\forall n>N:\frac{x_n-x_{n-1}}{y_n-y_{n-1}}>1$,
即 $x_n-x_{n-1}>y_n-y_{n-1}$
这说明 $\{x_n\}$ 严格单调增加,
且从 $x_n-x_N>y_n-y_N$ 知 $\{x_n\}$ 是正无穷大量
将前面的结论应用到 $\left\{\frac{y_n}{x_n}\right\}$,
得到 $\lim\limits_{n\to\infty}\frac{y_n-y_{n-1}}{x_n-x_{n-1}}=0$,
因而 $\lim\limits_{n\to\infty}\frac{y_n}{x_n}=0$,
即 $\lim\limits_{n\to\infty}\frac{x_n}{y_n}=+\infty$
$a=-\infty$ 的情况证明方法类同

[在例2-9 中令 $x_n=a_1+a_2+\cdots+a_n$, $y_n=n$, 即可直接得到该结论]

------

> 例2-18: 求极限
> $\lim\limits_{n\to\infty}\frac{a_0n^k+a_1n^{k-1}+\cdots+a_{k-1}n+a_k}{b_0n^l+b_1n^{l-1}+\cdots+b_{l-1}n+b_l}$,
> 其中 $k,l$ 为正整数, $a_0\neq0$, $b_0\neq0$
>
> 解: 上式 $=n^{k-l}\frac{a_0+\frac{a_1}{n}+\cdots+\frac{a_{k-1}}{n^{k-1}}+\frac{a_k}{n^k}}{b_0+\frac{b_1}{n}+\cdots+\frac{b_{l-1}}{n^{l-1}}+\frac{b_l}{n^l}}$
>
> 由于 $\lim\limits_{n\to\infty}\frac{a_0+\frac{a_1}{n}+\cdots+\frac{a_k}{n^k}}{b_0+\frac{b_1}{n}+\cdots+\frac{b_l}{n^l}}=\frac{a_0}{b_0}\neq0$,
> 可以得到
> $\lim\limits_{n\to\infty}\frac{a_0n^k+a_1n^{k-1}+\cdots+a_k}{b_0n^l+b_1n^{l-1}+\cdots+b_l}=\begin{cases}0, & k<l\\ \frac{a_0}{b_0}, & k=l\\ \infty, & k>l\end{cases}$

> 例2-19: 求极限 $\lim\limits_{n\to\infty}\frac{1^k+2^k+\cdots+n^k}{n^{k+1}}$ ($k$ 为正整数)
>
> 解: 令 $x_n=1^k+2^k+\cdots+n^k$, $y_n=n^{k+1}$, 由
> $\lim\limits_{n\to\infty}\frac{x_n-x_{n-1}}{y_n-y_{n-1}}=\lim\limits_{n\to\infty}\frac{n^k}{n^{k+1}-(n-1)^{k+1}}=\lim\limits_{n\to\infty}\frac{n^k}{(k+1)n^k-C_{k+1}^2n^{k-1}+\cdots}=\frac{1}{k+1}$
> 得到 $\lim\limits_{n\to\infty}\frac{1^k+2^k+\cdots+n^k}{n^{k+1}}=\frac{1}{k+1}$

> 例2-20: 设 $\lim\limits_{n\to\infty}a_n=a$,
> 求极限 $\lim\limits_{n\to\infty}\frac{a_1+2a_2+\cdots+na_n}{n^2}$
>
> 解: 令 $x_n=a_1+2a_2+\cdots+na_n$, $y_n=n^2$, 由
> $\lim\limits_{n\to\infty}\frac{x_n-x_{n-1}}{y_n-y_{n-1}}=\lim\limits_{n\to\infty}\frac{na_n}{n^2-(n-1)^2}=\lim\limits_{n\to\infty}\frac{na_n}{2n-1}=\frac{a}{2}$
> 得到 $\lim\limits_{n\to\infty}\frac{a_1+2a_2+\cdots+na_n}{n^2}=\frac{a}{2}$


## 单调有界数列收敛定理

定理(单调有界数列收敛定理): 单调有界数列必定收敛

证: 不妨设数列 $\{x_n\}$ 单调增加且有上界
由确界存在定理, 由 $\{x_n\}$ 构成的数集必有上确界 $\beta$, 满足
1. $\forall n\in N^*:x_n\leq\beta$
2. $\forall\varepsilon>0$,
   $\exists x_{n_0}:x_{n_0}>\beta-\varepsilon$

取 $N=n_0$,
$\forall n>N$ 有 $\beta-\varepsilon<x_{n_0}\leq x_n\leq\beta$
因而 $|x_n-\beta|<\varepsilon$,
于是得到 $\lim\limits_{n\to\infty}x_n=\beta$

[单调有界定理不必先知道极限是什么, 用极限定义证明收敛时必须先知道极限]
[用极限运算法则求极限时, 须先判断数列收敛]

------

> 例2-21: 设 $x_1>0$, $x_{n+1}=1+\frac{x_n}{1+x_n}$,
> $n=1,2,3,\cdots$, 证明数列 $\{x_n\}$ 收敛, 并求其极限
>
> 解: 由数学归纳法可得 $1<x_n<2$
> 由 $x_{n+1}=1+\frac{x_n}{1+x_n}$ 可得 $x_{n+1}-x_n=\frac{x_n-x_{n-1}}{(1+x_n)(1+x_{n-1})}$
>
> 这说明对一切 $n\geq2$,
> $x_{n+1}-x_n$ 与 $x_n-x_{n-1}$ 具有相同符号,
> 从而 $\{x_n\}$ 是单调数列, 由定理收敛
>
> 设 $\{x_n\}$ 的极限为 $a$,
> 在等式 $x_{n+1}=1+\frac{x_n}{1+x_n}$ 两边同时求极限,
> 得到方程 $a=1+\frac{a}{1+a}$
> 解得 $a=\frac{1\pm\sqrt5}{2}$, 由 $x_1>1$ 舍去负值,
> 即 $\lim\limits_{n\to\infty}x_n=\frac{1+\sqrt5}{2}$

> 例2-22: 设 $0<x_1<1$, $x_{n+1}=x_n(1-x_n)$,
> $n=1,2,3,\cdots$, 证明数列 $\{x_n\}$ 收敛, 并求其极限
>
> 解: 由数学归纳法可得 $0<x_n<1$
> 由 $x_{n+1}=x_n(1-x_n)$ 可得 $x_{n+1}-x_n=-x_n^2<0$
> 这说明 $\{x_n\}$ 单调减少有下界, 由定理收敛
> 设极限为 $a$, 在 $x_{n+1}=x_n(1-x_n)$ 两边同时求极限,
> 得到方程 $a=a(1-a)$, 解得 $a=0$,
> 即 $\lim\limits_{n\to\infty}x_n=0$
>
> 应用 Stolz 定理还可得到一个有意义的结果
> $\lim\limits_{n\to\infty}(nx_n)=\lim\limits_{n\to\infty}\frac{n}{\frac{1}{x_n}}=\lim\limits_{n\to\infty}\frac{1}{\frac{1}{x_{n+1}}-\frac{1}{x_n}}=\lim\limits_{n\to\infty}\frac{x_{n+1}x_n}{x_n-x_{n+1}}=\lim\limits_{n\to\infty}\frac{x_n^2(1-x_n)}{x_n^2}=1$
> [说明 $0<x_1<1$ 时无穷小量 $\{x_n\}$ 与 $\left\{\frac{1}{n}\right\}$ 变化规律趋于一致,
> 两无穷小量是等价的]

> 例2-23: 设 $x_1=\sqrt2$, $x_{n+1}=\sqrt{3+2x_n}$,
> $n=1,2,3,\cdots$, 证明数列 $\{x_n\}$ 收敛, 并求其极限
>
> 解: 首先有 $0<x_1<3$; 设 $0<x_n<3$,
> 则 $0<x_{n+1}=\sqrt{3+2x_n}<3$, 由数学归纳法知 $0<x_n<3$
> 于是 $x_{n+1}-x_n=\sqrt{3+2x_n}-x_n=\frac{(3-x_n)(1+x_n)}{\sqrt{3+2x_n}+x_n}>0$
> 这说明 $\{x_n\}$ 单调增加且有上界, 由定理收敛
>
> 设极限为 $a$,
> 在 $x_{n+1}=\sqrt{3+2x_n}$ 两边求极限得 $a=\sqrt{3+2a}$,
> 解得 $a=3$, 即 $\lim\limits_{n\to\infty}x_n=3$

> 例2-24: Fibonacci 数列与兔群增长率
> 设一对刚出生的小兔要经过两个季度成长为成熟兔, 每对成熟的兔子每季度产一对小兔, 不考虑死亡
> 设 $a_n$ 是第 $n$ 季度兔对总数, 则 $a_1=1$, $a_2=1$,
> $a_3=2$, $a_4=3$, $a_5=5,\cdots$
> 到第 $n$ 季度能产小兔的兔对数为 $a_{n-1}$,
> 第 $n+1$ 季度兔对总数等于第 $n$ 季度兔对总数的 $a_n$ 加上新产下的小兔对数 $a_{n-1}$
> 数列 $\{a_n\}$ 称为 Fibonacci 数列,
> 具有性质 $a_{n+1}=a_n+a_{n-1}$, $n=2,3,4,\cdots$
> 令 $b_n=\frac{a_{n+1}}{a_n}$,
> 则 $b_n-1$ 表示兔群在第 $n+1$ 季度的增长率, 有 $b_n>0$ 且
> $b_n=\frac{a_{n+1}}{a_n}=\frac{a_n+a_{n-1}}{a_n}=1+\frac{1}{b_{n-1}}$
> 当 $b_n>\frac{\sqrt5+1}{2}$ 时 $b_{n+1}<\frac{\sqrt5+1}{2}$;
> 当 $b_n<\frac{\sqrt5+1}{2}$ 时 $b_{n+1}>\frac{\sqrt5+1}{2}$,
> 故 $\{b_n\}$ 不是单调数列
>
> 但可发现有 $b_{2k-1}\in\left(0,\frac{\sqrt5+1}{2}\right)$,
> $b_{2k}\in\left(\frac{\sqrt5+1}{2},+\infty\right)$,
> $k=1,2,3,\cdots$
> $b_{2k+2}-b_{2k}=1+\frac{1}{1+\frac{1}{b_{2k}}}-b_{2k}=\frac{\left(\frac{\sqrt5+1}{2}-b_{2k}\right)\left(\frac{\sqrt5-1}{2}+b_{2k}\right)}{1+b_{2k}}<0$
> $b_{2k+3}-b_{2k+1}=1+\frac{1}{1+\frac{1}{b_{2k+1}}}-b_{2k+1}=\frac{\left(\frac{\sqrt5+1}{2}-b_{2k+1}\right)\left(\frac{\sqrt5-1}{2}+b_{2k+1}\right)}{1+b_{2k+1}}>0$
>
> 于是 $\{b_{2k}\}$ 是单调减少的有下界数列,
> $\{b_{2k-1}\}$ 是单调增加的有上界数列, 因而都收敛
>
> 记它们的极限分别为 $a$ 与 $b$,
> 显然有 $\frac{\sqrt5+1}{2}\leq a<+\infty$,
> $0<b\leq\frac{\sqrt5+1}{2}$
> 由 $\lim\limits_{k\to\infty}b_{2k+2}=\lim\limits_{k\to\infty}\frac{1+2b_{2k}}{1+b_{2k}}$ 得
> $a=\frac{1+2a}{1+a}$
> 由 $\lim\limits_{k\to\infty}b_{2k+3}=\lim\limits_{k\to\infty}\frac{1+2b_{2k+1}}{1+b_{2k+1}}$ 得
> $b=\frac{1+2b}{1+b}$
> 两方程有相同的解 $a=b=\frac{1\pm\sqrt5}{2}$,
> 于是 $a=b=\frac{1+\sqrt5}{2}$
>
> 结论: 在不考虑兔子死亡的前提下, 经过较长时间,
> 兔群逐季增长率趋于 $\frac{1+\sqrt5}{2}-1\approx0.618$

各季兔群情况

| 季度 | 小兔对数 | 成长兔对数 | 成熟期兔对数 | 兔对总和 |
| --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 | 2 |
| 4 | 1 | 1 | 1 | 3 |
| 5 | 2 | 1 | 2 | 5 |
| 6 | 3 | 2 | 3 | 8 |
| 7 | 5 | 3 | 5 | 13 |


## π 和 e

> 例2-25: 证明数列 $\left\{n\sin\frac{180^\circ}{n}\right\}$ 收敛
>
> 证: 令 $t=\frac{180^\circ}{n(n+1)}$,
> 则当 $n\geq3$ 时 $nt\leq45^\circ$. 于是
> $\tan nt=\frac{\tan(n-1)t+\tan t}{1-\tan(n-1)t\tan t}\geq\tan(n-1)t+\tan t\geq\cdots\geq n\tan t$
> 从而 $\sin(n+1)t=\sin nt\cos t+\cos nt\sin t=\sin nt\cos t\left(1+\frac{\tan t}{\tan nt}\right)\leq\frac{n+1}{n}\sin nt$
>
> 所以当 $n\geq3$ 时 $L_n=n\sin\frac{180^\circ}{n}\leq(n+1)\sin\frac{180^\circ}{n+1}=L_{n+1}$
> 另一方面,
> 单位圆内接正 $n$ 边形的面积 $S_n=n\sin\frac{180^\circ}{n}\cos\frac{180^\circ}{n}<4$
>
> 因此当 $n\geq3$ 时
> $L_n=n\sin\frac{180^\circ}{n}<\frac{4}{\cos\frac{180^\circ}{n}}\leq\frac{4}{\cos60^\circ}=8$
> 数列 $\{L_n\}$ 单调增加且有上界, 因而收敛

将该极限用希腊字母 $\pi$ 来记,
即 $\lim\limits_{n\to\infty}n\sin\frac{180^\circ}{n}=\pi$
有了 $\pi$ 的定义就可以定义角度的弧度制: 单位圆的半周长为 $\pi$, 半个圆周所对圆心角为 $\pi$
在弧度制下,
上式可写成 $\lim\limits_{n\to\infty}\frac{\sin(\pi/n)}{\pi/n}=1$

------

> 例2-26: 证明: 数列 $\left\{\left(1+\frac{1}{n}\right)^n\right\}$ 单调增加,
> $\left\{\left(1+\frac{1}{n}\right)^{n+1}\right\}$ 单调减少,
> 两者收敛于同一极限
>
> 证: 记 $x_n=\left(1+\frac{1}{n}\right)^n$,
> $y_n=\left(1+\frac{1}{n}\right)^{n+1}$,
>
> 利用平均值不等式 $\sqrt[n]{a_1a_2\cdots a_n}\leq\frac{a_1+a_2+\cdots+a_n}{n}$
> 得到 $x_n=\left(1+\frac{1}{n}\right)^n\cdot1\leq\left[\frac{n\left(1+\frac{1}{n}\right)+1}{n+1}\right]^{n+1}=x_{n+1}$
> 和 $\frac{1}{y_n}=\left(\frac{n}{n+1}\right)^{n+1}\cdot1\leq\left[\frac{(n+1)\frac{n}{n+1}+1}{n+2}\right]^{n+2}=\frac{1}{y_{n+1}}$
>
> 由 $2=x_1\leq x_n<y_n\leq y_1=4$,
> 知 $\{x_n\}$ 与 $\{y_n\}$ 都收敛
> 又由 $y_n=x_n\left(1+\frac{1}{n}\right)$, 可知两者具有相同的极限

习惯上用字母 $e$ 表示这一极限
$\lim\limits_{n\to\infty}\left(1+\frac{1}{n}\right)^n=\lim\limits_{n\to\infty}\left(1+\frac{1}{n}\right)^{n+1}=e$
$e=2.718\,281\,828\,459\cdots$ 是一个无理数,
以 $e$ 为底的对数称为自然对数, 记为 $\ln x(=\log_e x)$

------

> 例2-27: 设 $a_n=1+\frac{1}{2^p}+\frac{1}{3^p}+\cdots+\frac{1}{n^p}$ ($p>0$),
> 证明: 当 $p>1$ 时 $\{a_n\}$ 收敛;
> 当 $0<p\leq1$ 时 $\{a_n\}$ 是正无穷大量
>
> 证: $\{a_n\}$ 显然单调增加, 收敛与否取决于其是否有界
> 当 $p>1$ 时, 记 $\frac{1}{2^{p-1}}=r$, 则 $0<r<1$. 由于
> $\frac{1}{2^p}+\frac{1}{3^p}<\frac{1}{2^p}+\frac{1}{2^p}=\frac{1}{2^{p-1}}=r$
> $\frac{1}{4^p}+\frac{1}{5^p}+\frac{1}{6^p}+\frac{1}{7^p}<\frac{1}{4^p}+\frac{1}{4^p}+\frac{1}{4^p}+\frac{1}{4^p}=r^2$
> $\cdots\cdots$
> $\frac{1}{2^{kp}}+\frac{1}{(2^k+1)^p}+\cdots+\frac{1}{(2^{k+1}-1)^p}<\frac{2^k}{2^{kp}}=r^k$
> 可知 $a_n\leq a_{2^{k+1}-1}<1+r+r^2+\cdots+r^k<\frac{1}{1-r}$,
> 这说明当 $p>1$ 时 $\{a_n\}$ 收敛
>
> 当 $p\leq1$ 时, 有
> $\frac{1}{2^p}\geq\frac{1}{2}$
> $\frac{1}{3^p}+\frac{1}{4^p}>\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$
> $\frac{1}{5^p}+\frac{1}{6^p}+\frac{1}{7^p}+\frac{1}{8^p}>\frac{4}{8}=\frac{1}{2}$
> $\cdots\cdots$
> $\frac{1}{(2^k+1)^p}+\frac{1}{(2^k+2)^p}+\cdots+\frac{1}{(2^{k+1})^p}>\frac{2^k}{2^{k+1}}=\frac{1}{2}$
> 因而 $a_{2^k}\geq1+\frac{k}{2}$,
> 由 $\{a_n\}$ 单调增加知 $\{a_n\}$ 是正无穷大量
>
> [特别当 $p=1$ 时,
> $a_n=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}$ 是无穷大量]

> 例2-28: 记 $b_n=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}-\ln n$,
> 证明数列 $\{b_n\}$ 收敛
>
> 证: 由例2-26 知
> $\left(1+\frac{1}{n}\right)^n<e<\left(1+\frac{1}{n}\right)^{n+1}$,
> 由此得到 $\frac{1}{n+1}<\ln\frac{n+1}{n}<\frac{1}{n}$
>
> 于是 $b_{n+1}-b_n=\frac{1}{n+1}-\ln(n+1)+\ln n=\frac{1}{n+1}-\ln\frac{n+1}{n}<0$
> $b_n=1+\frac{1}{2}+\cdots+\frac{1}{n}-\ln n>\ln\frac{2}{1}+\ln\frac{3}{2}+\cdots+\ln\frac{n+1}{n}-\ln n=\ln(n+1)-\ln n>0$
> 这说明数列 $\{b_n\}$ 单调减少有下界, 因而收敛
> $\{b_n\}$ 的极限 $\gamma=0.577\,215\,664\,90\cdots$ 称为 Euler 常数

> 例2-29: 证明
> $\lim\limits_{n\to\infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}\right)=\ln2$
>
> 证: 记 $c_n=\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}$,
> 则由例2-28 显然有 $c_n=b_{2n}-b_n+\ln2$
> 由 $\lim\limits_{n\to\infty}b_n=\gamma$ 易知也有 $\lim\limits_{n\to\infty}b_{2n}=\gamma$,
> 于是得到 $\lim\limits_{n\to\infty}c_n=\ln2$

> 例2-30: 证明
> $\lim\limits_{n\to\infty}\left[1-\frac{1}{2}+\frac{1}{3}-\cdots+(-1)^{n-1}\frac{1}{n}\right]=\ln2$
>
> 证: 记 $d_n=1-\frac{1}{2}+\frac{1}{3}-\cdots+(-1)^{n-1}\frac{1}{n}$,
> 由于
> $b_n=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n-1}+\frac{1}{n}-\ln n\to\gamma$ ($n\to\infty$)
> 和 $b_{2n}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\frac{1}{5}+\frac{1}{6}+\cdots+\frac{1}{2n-1}+\frac{1}{2n}-\ln 2n\to\gamma$ ($n\to\infty$)
>
> 考虑 $b_{2n}-b_n$,
> 用 $b_{2n}$ 中的第 $2k$ 项与 $b_n$ 中的第 $k$ 项对应相减, 得到
> $b_{2n}-b_n=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots+\frac{1}{2n-1}-\frac{1}{2n}-\ln 2=d_{2n}-\ln 2\to0$ ($n\to\infty$)
> 由 $d_{2n+1}=d_{2n}+\frac{1}{2n+1}$ 及 $\lim\limits_{n\to\infty}\frac{1}{2n+1}=0$,
> 即可得到 $\lim\limits_{n\to\infty}d_n=\ln2$


## 闭区间套定理

定义(闭区间套): 如果一列闭区间 $\{[a_n,b_n]\}$ 满足
1. $[a_{n+1},b_{n+1}]\subseteq[a_n,b_n]$, $n=1,2,3,\cdots$
2. $\lim\limits_{n\to\infty}(b_n-a_n)=0$
则称这列闭区间形成一个闭区间套

------

定理(闭区间套定理): 如果 $\{[a_n,b_n]\}$ 形成一个闭区间套,
则存在唯一的实数 $\xi$ 属于所有的闭区间 $[a_n,b_n]$,
且 $\xi=\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n$

证: 由条件 (1) 可得
$a_1\leq\cdots\leq a_{n-1}\leq a_n<b_n\leq b_{n-1}\leq\cdots\leq b_1$
数列 $\{a_n\}$ 单调增加有上界 $b_1$,
$\{b_n\}$ 单调减少有下界 $a_1$, 由单调有界定理都收敛

设 $\lim\limits_{n\to\infty}a_n=\xi$, 则
$\lim\limits_{n\to\infty}b_n=\lim\limits_{n\to\infty}[(b_n-a_n)+a_n]=\lim\limits_{n\to\infty}(b_n-a_n)+\lim\limits_{n\to\infty}a_n=\xi$
由于 $\xi$ 是 $\{a_n\}$ 的上确界, 也是 $\{b_n\}$ 的下确界,
于是有 $a_n\leq\xi\leq b_n$, $n=1,2,3,\cdots$

若另有实数 $\xi'$ 属于所有闭区间 $[a_n,b_n]$,
也有 $a_n\leq\xi'\leq b_n$, $n=1,2,3,\cdots$
令 $n\to\infty$,
由极限的夹逼性得到 $\xi'=\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n=\xi$

[若将条件中的闭区间套改为开区间套, 则数列 $\{a_n\}$,
$\{b_n\}$ 仍收敛于同一个极限 $\xi$,
但 $\xi$ 可能不属于任何一个开区间 $(a_n,b_n)$]

------

定理: 实数集 $R$ 是不可列的

证: 反证法. 假设实数集 $R$ 可列,
即可找到一种排列的规则使 $R=\{x_1,x_2,\cdots,x_n,\cdots\}$
先取闭区间 $[a_1,b_1]$ 使 $x_1\in[a_1,b_1]$, 这总是可以做到的
将 $[a_1,b_1]$ 三等分,
则在 $\left[a_1,\frac{2a_1+b_1}{3}\right]$,
$\left[\frac{2a_1+b_1}{3},\frac{a_1+2b_1}{3}\right]$,
$\left[\frac{a_1+2b_1}{3},b_1\right]$ 中至少有一个不含有 $x_2$,
记为 $[a_2,b_2]$

再将 $[a_2,b_2]$ 三等分, 同样在三个小区间中至少有一个不含有 $x_3$, 记为 $[a_3,b_3]$
这样的步骤可一直做下去, 于是得到一个闭区间套 $\{[a_n,b_n]\}$,
满足 $x_n\notin[a_n,b_n]$, $n=1,2,3,\cdots$

由闭区间套定理, 存在唯一实数 $\xi$ 属于所有的闭区间 $[a_n,b_n]$,
换言之 $\xi\neq x_n(n=1,2,3,\cdots)$,
这与 $R=\{x_1,x_2,\cdots\}$ 矛盾


## 子列

定义(子列): 设 $\{x_n\}$ 是一个数列,
而 $n_1<n_2<\cdots<n_k<n_{k+1}<\cdots$ 是一列严格单调增加的正整数
则 $x_{n_1},x_{n_2},\cdots,x_{n_k},\cdots$ 也形成一个数列,
称为 $\{x_n\}$ 的子列, 记为 $\{x_{n_k}\}$
下标 $n_k$ 表示子列中的第 $k$ 项恰好是原数列中的第 $n_k$ 项

例: 取偶数列可表示为 $\{x_{2k}\}$; 取 $n_k=2^k$,
则 $\{x_{2^k}\}$ 是由原数列第 $2,4,8,16,\cdots$ 项构成的数列
由下标严格单调增加, 可知 $n_k\geq k$, $k\in N^*$,
和 $n_j\geq n_k$, $j\geq k$

------

定理: 若数列 $\{x_n\}$ 收敛于 $a$, 则它的任何子列 $\{x_{n_k}\}$ 也收敛于 $a$, 即
$\lim\limits_{n\to\infty}x_n=a\implies\lim\limits_{k\to\infty}x_{n_k}=a$

证: 由 $\lim\limits_{n\to\infty}x_n=a$,
$\forall\varepsilon>0$, $\exists N$,
$\forall n>N:|x_n-a|<\varepsilon$
取 $K=N$, 当 $k>K$ 时 $n_k\geq k>N$,
因而成立 $|x_{n_k}-a|<\varepsilon$

------

推论:
若存在数列 $\{x_n\}$ 的两个子列 $\{x_{n_k}^{(1)}\}$ 与 $\{x_{n_k}^{(2)}\}$ 分别收敛于不同的极限,
则 $\{x_n\}$ 必定发散

------

> 例2-31: 数列 $\left\{\sin\frac{n\pi}{4}\right\}$ 发散
>
> 证: 取 $n_k^{(1)}=4k$, $n_k^{(2)}=8k+2$,
> 则子列 $\{x_{n_k}^{(1)}\}$ 收敛于 $0$,
> 子列 $\{x_{n_k}^{(2)}\}$ 收敛于 $1$
> 由上述推论知 $\{x_n\}$ 发散


## Bolzano-Weierstrass 定理

定理(Bolzano-Weierstrass 定理): 有界数列必有收敛子列

证: 设数列 $\{x_n\}$ 有界,
于是存在实数 $a_1,b_1$ 使 $a_1\leq x_n\leq b_1$,
$n=1,2,3,\cdots$

将闭区间 $[a_1,b_1]$ 等分为两个小区间 $\left[a_1,\frac{a_1+b_1}{2}\right]$ 与
$\left[\frac{a_1+b_1}{2},b_1\right]$
其中至少有一个含有数列 $\{x_n\}$ 中的无穷多项, 把它记为 $[a_2,b_2]$
再将闭区间 $[a_2,b_2]$ 等分为两个小区间,
同样取一个含有 $\{x_n\}$ 中无穷多项的记为 $[a_3,b_3]$
这样的步骤一直做下去, 得到一个闭区间套 $\{[a_k,b_k]\}$,
其中每一个闭区间 $[a_k,b_k]$ 都含有 $\{x_n\}$ 中的无穷多项
根据闭区间套定理,
存在实数 $\xi$ 使 $\xi=\lim\limits_{k\to\infty}a_k=\lim\limits_{k\to\infty}b_k$

在 $[a_1,b_1]$ 中选取 $\{x_n\}$ 中某一项记为 $x_{n_1}$;
在 $[a_2,b_2]$ 中含有 $\{x_n\}$ 中无穷多项,
选取位于 $x_{n_1}$ 后的某一项记为 $x_{n_2}$, $n_2>n_1$
继续这样选取, 得到 $\{x_n\}$ 的一个子列 $\{x_{n_k}\}$,
满足 $a_k\leq x_{n_k}\leq b_k$, $k=1,2,3,\cdots$
由 $\lim\limits_{k\to\infty}a_k=\lim\limits_{k\to\infty}b_k=\xi$ 和极限的夹逼性得到
$\lim\limits_{k\to\infty}x_{n_k}=\xi$

------

定理: 若 $\{x_n\}$ 是一个无界数列, 则存在子列 $\{x_{n_k}\}$,
使得 $\lim\limits_{k\to\infty}x_{n_k}=\infty$

证: 由 $\{x_n\}$ 无界, 对任意 $M>0$,
$\{x_n\}$ 中存在无穷多个 $x_n$ 满足 $|x_n|>M$

先取 $M_1=1$, 存在 $x_{n_1}$ 使 $|x_{n_1}|>1$;
取 $M_2=2$, 在 $x_{n_1}$ 后可取 $x_{n_2}$, $n_2>n_1$,
使 $|x_{n_2}|>2$
继续取 $M_k=k$, 同理可取 $x_{n_k}$, $n_k>n_{k-1}$,
使 $|x_{n_k}|>k$,
这样得到 $\{x_n\}$ 的一个子列 $\{x_{n_k}\}$ 满足 $|x_{n_k}|>k$
由定义 $\lim\limits_{k\to\infty}x_{n_k}=\infty$


## Cauchy 收敛原理

定义(基本数列):
若数列 $\{x_n\}$ 具有以下特性: 对于任意给定的 $\varepsilon>0$,
存在正整数 $N$, 使得当 $n,m>N$ 时成立 $|x_n-x_m|<\varepsilon$
则称数列 $\{x_n\}$ 是一个基本数列

------

> 例2-32: 设 $x_n=1+\frac{1}{2^2}+\frac{1}{3^2}+\cdots+\frac{1}{n^2}$,
> 则 $\{x_n\}$ 是一个基本数列
>
> 证: 对任意正整数 $n$ 与 $m$, 不妨设 $m>n$, 则
> $x_m-x_n=\frac{1}{(n+1)^2}+\frac{1}{(n+2)^2}+\cdots+\frac{1}{m^2}$
> $<\frac{1}{n(n+1)}+\frac{1}{(n+1)(n+2)}+\cdots+\frac{1}{(m-1)m}$
> $=\left(\frac{1}{n}-\frac{1}{n+1}\right)+\left(\frac{1}{n+1}-\frac{1}{n+2}\right)+\cdots+\left(\frac{1}{m-1}-\frac{1}{m}\right)=\frac{1}{n}-\frac{1}{m}<\frac{1}{n}$
> 对任意给定的 $\varepsilon>0$,
>
> 取 $N=\left[\frac{1}{\varepsilon}\right]$,
> 当 $m>n>N$ 时成立 $|x_m-x_n|<\varepsilon$

> 例2-33: 设 $x_n=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}$,
> 则 $\{x_n\}$ 不是基本数列
>
> 证: 对任意正整数 $n$,
> 有 $x_{2n}-x_n=\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}>n\cdot\frac{1}{2n}=\frac{1}{2}$
> 取 $\varepsilon_0=\frac{1}{2}$, 无论 $N$ 多大,
> 总存在正整数 $n>N$, $m=2n>N$,
> 使得 $|x_m-x_n|=|x_{2n}-x_n|\geq\varepsilon_0$

------

定理(Cauchy 收敛原理): 数列 $\{x_n\}$ 收敛的充分必要条件是 $\{x_n\}$ 是基本数列

证: 必要性: 设 $\{x_n\}$ 收敛于 $a$,
按定义 $\forall\varepsilon>0$, $\exists N$,
$\forall n,m>N$: $|x_n-a|<\frac{\varepsilon}{2}$,
$|x_m-a|<\frac{\varepsilon}{2}$
于是 $|x_n-x_m|\leq|x_n-a|+|x_m-a|<\varepsilon$

充分性: 先证明基本数列必定有界. 取 $\varepsilon_0=1$,
因为 $\{x_n\}$ 是基本数列, 所以 $\exists N_0$,
$\forall n>N_0:|x_n-x_{N_0+1}|<1$
令 $M=\max\{|x_1|,|x_2|,\cdots,|x_{N_0}|,|x_{N_0+1}|+1\}$,
则对一切 $n$ 成立 $|x_n|\leq M$

由 Bolzano-Weierstrass 定理,
在 $\{x_n\}$ 中必有收敛子列 $\lim\limits_{k\to\infty}x_{n_k}=\xi$
因为 $\{x_n\}$ 是基本数列, 所以 $\forall\varepsilon>0$,
$\exists N$,
$\forall n,m>N:|x_n-x_m|<\frac{\varepsilon}{2}$
在上式中取 $x_m=x_{n_k}$, 其中 $k$ 充分大, 满足 $n_k>N$,
并且令 $k\to\infty$,
于是得到 $|x_n-\xi|\leq\frac{\varepsilon}{2}<\varepsilon$

[例2-32 中 $\{x_n\}$ 收敛, 例2-33 中 $\{x_n\}$ 发散,
与例2-27 中得到的结论一致]
[完备性: 由实数构成的基本数列必存在实数极限, 有理数集不具有完备性,
如 $\left\{\left(1+\frac{1}{n}\right)^n\right\}$ 是由有理数构成的基本数列,
其极限 $e$ 不是有理数]

------

> 例2-34: 设数列 $\{x_n\}$ 满足压缩性条件 $|x_{n+1}-x_n|\leq k|x_n-x_{n-1}|$,
> $0<k<1$, $n=2,3,\cdots$, 则 $\{x_n\}$ 收敛
>
> 证: 只要证明 $\{x_n\}$ 是基本数列. 首先对一切 $n$ 有
> $|x_{n+1}-x_n|\leq k|x_n-x_{n-1}|\leq k^2|x_{n-1}-x_{n-2}|\leq\cdots\leq k^{n-1}|x_2-x_1|$
>
> 设 $m>n$, 则
> $|x_m-x_n|\leq|x_m-x_{m-1}|+|x_{m-1}-x_{m-2}|+\cdots+|x_{n+1}-x_n|$
> $\leq k^{m-2}|x_2-x_1|+k^{m-3}|x_2-x_1|+\cdots+k^{n-1}|x_2-x_1|<\frac{k^{n-1}}{1-k}|x_2-x_1|\to0$ ($n\to\infty$)
> 因此 $\{x_n\}$ 是基本数列, 从而收敛


## 实数系的基本定理

确界存在定理
$\downarrow$
单调有界数列收敛定理
$\downarrow$
闭区间套定理
$\downarrow$
Bolzano-Weierstrass 定理
$\downarrow$
Cauchy 收敛原理

------

实数系的连续性包含了完备性

定理: 实数系的完备性等价于实数系的连续性

证: 分两步证明完备性包含连续性: Cauchy 收敛原理 $\implies$ 闭区间套定理 $\implies$ 确界存在定理

先证 Cauchy 收敛原理 $\implies$ 闭区间套定理
设 $\{[a_n,b_n]\}$ 是一列闭区间, 满足条件
1. $[a_{n+1},b_{n+1}]\subseteq[a_n,b_n]$, $n=1,2,3,\cdots$
2. $\lim\limits_{n\to\infty}(b_n-a_n)=0$
设 $m>n$,
则 $0\leq a_m-a_n<b_n-a_n\to0\ (n\to\infty)$,
所以数列 $\{a_n\}$ 是一基本数列,
从而 $\lim\limits_{n\to\infty}a_n=\xi$
并由此得到 $\lim\limits_{n\to\infty}b_n=\lim\limits_{n\to\infty}(b_n-a_n)+\lim\limits_{n\to\infty}a_n=\xi$
由于 $\{a_n\}$ 单调增加, $\{b_n\}$ 单调减少,
可知 $\xi$ 属于所有闭区间 $[a_n,b_n]$, 闭区间套定理得证

再证 闭区间套定理 $\implies$ 确界存在定理

设 $S$ 是非空有上界的实数集合,
又设 $\tilde T$ 是由 $S$ 的所有上界组成的集合,
证 $\tilde T$ 有最小数, 即 $S$ 有上确界

取 $a_1\notin\tilde T$, $b_1\in\tilde T$,
显然 $a_1<b_1$, 按下述规则依次构造一列闭区间
$[a_2,b_2]=\begin{cases}\left[a_1,\frac{a_1+b_1}{2}\right], & \text{若}\frac{a_1+b_1}{2}\in\tilde T\\ \left[\frac{a_1+b_1}{2},b_1\right], & \text{若}\frac{a_1+b_1}{2}\notin\tilde T\end{cases}$
$[a_3,b_3]=\begin{cases}\left[a_2,\frac{a_2+b_2}{2}\right], & \text{若}\frac{a_2+b_2}{2}\in\tilde T\\ \left[\frac{a_2+b_2}{2},b_2\right], & \text{若}\frac{a_2+b_2}{2}\notin\tilde T\end{cases}$
$\cdots\cdots$
由此得到一个闭区间套 $\{[a_n,b_n]\}$,
满足 $a_n\notin\tilde T$, $b_n\in\tilde T$,
$n=1,2,3,\cdots$
由闭区间套定理, 存在唯一的实数 $\xi$ 属于所有闭区间 $[a_n,b_n]$,
且 $\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n=\xi$

现只需说明 $\xi$ 是集合 $\tilde T$ 的最小数, 也就是集合 $S$ 的上确界
若 $\xi\notin\tilde T$, 即 $\xi$ 不是集合 $S$ 的上界,
则存在 $x\in S$ 使得 $\xi<x$
由 $\lim\limits_{n\to\infty}b_n=\xi$
可知当 $n$ 充分大时 $b_n<x$, 与 $b_n\in\tilde T$ 矛盾,
所以 $\xi\in\tilde T$

若存在 $\eta\in\tilde T$ 使得 $\eta<\xi$,
则由 $\lim\limits_{n\to\infty}a_n=\xi$
可知当 $n$ 充分大时 $\eta<a_n$
于是存在 $y\in S$ 使得 $\eta<y<a_n$,
与 $\eta\in\tilde T$ 矛盾,
所以 $\xi$ 是集合 $\tilde T$ 的最小数
确界存在定理得证
[以上五个定理是等价的, 其中任何一个出发都可推出其他的定理, 每一个都可称为实数系的基本定理]

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
