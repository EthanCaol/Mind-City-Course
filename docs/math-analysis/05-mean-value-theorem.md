


## 微分中值定理

微分中值定理: 联系函数与其导数的一组定理, 是微分学中最重要的结论之一
它把函数在一个区间上的增量与导数在某点的值联系起来
本章以微分中值定理为核心, 介绍微分学中与它联系的几个基本定理


## 函数极值与 Fermat 引理

极大值: 设函数 $f(x)$ 在 $(a,b)$ 上有定义, $x_0\in(a,b)$
若存在 $x_0$ 的某个邻域 $O(x_0,\delta)\subset(a,b)$,
使得
$f(x)\leq f(x_0),\quad x\in O(x_0,\delta)$
则称 $x_0$ 是 $f(x)$ 的一个极大值点, $f(x_0)$ 称为极大值

极小值: 将上述不等式换成 $f(x)\geq f(x_0)$, 得极小值点与极小值
[不需要区分极大与极小时, 统称极值点与极值]

从定义可以看出
1. 极大与极小只指 $x_0$ 附近一个局部范围内函数值的大小关系, 是局部性质

2. 一个区间内, $f(x)$ 的一个极小值完全可能大于它的某些极大值

3. 一个区间内极值点可以有无数个, 如在 $(0,1)$ 上考虑函数
$f(x)=\sin\frac{1}{x}$
   $x=\frac{2}{(2n+1)\pi}\ (n=0,1,2,\cdots)$ 都是极值点,
   $n$ 为偶数时是极大值点, $n$ 为奇数时是极小值点

4. 极值点的定义不牵涉函数的其他性质, 如连续, 可微等
   如在 $(0,1)$ 上定义的 Riemann 函数
   $R(x)$
   $=\begin{cases}\frac{1}{p}, & x=\frac{q}{p}\ (p,q\text{为互素正整数})\\ 0, & x\text{为}(0,1)\text{上的无理数}\end{cases}$
   $(0,1)$ 中每个有理点都是它的极大值点, 每个无理点都是它的极小值点

------

Fermat 引理: 设 $x_0$ 是 $f(x)$ 的一个极值点, 且
$f(x)$ 在 $x_0$ 处导数存在, 则
$f'(x_0)=0$

证明: 不妨设 $x_0$ 是 $f(x)$ 的极大值点
由极大值点的定义, 在 $x_0$ 的某个邻域 $O(x_0,\delta)$ 上
$f(x)$ 有定义, 且 $f(x)\leq f(x_0)$

当 $x<x_0$ 时,
$\frac{f(x)-f(x_0)}{x-x_0}\geq0$; 当
$x>x_0$ 时, $\frac{f(x)-f(x_0)}{x-x_0}\leq0$

因为 $f(x)$ 在 $x_0$ 可导, 所以
$f'_-(x_0)$
$=\lim\limits_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}\geq0,\quad f'_+(x_0)$
$=\lim\limits_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}\leq0$

而 $f'_-(x_0)=f'_+(x_0)=f'(x_0)$, 因此
$f'(x_0)=0$
$x_0$ 为极小值点的情形同理可证

Fermat 引理的几何意义: 若曲线 $y=f(x)$ 在其极值点处可导,
或在该点存在切线, 则该切线必平行于 $x$ 轴
当 $f(x)$ 可导时, 条件 $f'(x_0)=0$ 只是
$x_0$ 为极值点的必要条件而非充分条件, 如函数 $f(x)=x^3$ 在
$x_0=0$ 处


## Rolle 定理

Rolle 定理: 设函数 $f(x)$ 在闭区间 $[a,b]$ 上连续, 在开区间
$(a,b)$ 上可导, 且 $f(a)=f(b)$, 则至少存在一点
$\xi\in(a,b)$, 使
$f'(\xi)=0$

证明: 由闭区间上连续函数的性质, 存在 $\xi,\eta\in[a,b]$, 满足
$f(\xi)=M$ 和 $f(\eta)=m$
其中 $M$ 和 $m$ 分别是 $f(x)$ 在 $[a,b]$ 上的最大值和最小值,
分两种情况

1. $M=m$: 此时 $f(x)$ 在 $[a,b]$ 上恒为常数, 结论显然成立

2. $M>m$: 此时 $M$ 和 $m$ 中至少有一个与 $f(a)$(亦即
$f(b)$)不相同
   不妨设 $M=f(\xi)>f(a)=f(b)$, 因此 $\xi\in(a,b)$
   显然是极大值点
   由 Fermat 引理, $f'(\xi)=0$

图5-1: Rolle 定理的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206300.png =400x)

Rolle 定理的几何意义: 满足定理条件的函数一定在某一点存在一条与 $x$ 轴平行,
亦即与曲线两个端点的连线平行的切线
定理的条件是充分的, 但三个条件中的任意一个不满足, 都可能导致结论不成立, 如以下三个函数
1. $f_1(x)=\begin{cases}x, & x\in[0,1)\\ 0, & x=1\end{cases}$ 不满足闭区间
$[0,1]$ 上连续的条件

2. $f_2(x)=|1-2x|,\ x\in[0,1]$ 不满足开区间
$(0,1)$ 上可导的条件

3. $f_3(x)=x,\ x\in[0,1]$ 不满足 $f_3(a)=f_3(b)$

这三个函数都满足其他两个条件, 但在 $(0,1)$ 中都不存在水平切线
Rolle 定理常被用来讨论函数及其导函数在某范围中的零点问题

------

> 例5-1: 设
> $p_n(x)=\frac{1}{2^nn!}\frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n\ (n=0,1,2,\cdots)$ 为
> $n$ 次 Legendre 多项式
> 证明 $p_n(x)$ 在 $(-1,1)$ 上恰有 $n$ 个不同的根
>
> 证明: 由高阶导数的 Leibniz 公式, 函数
> $q_{2n-m}(x)\equiv\frac{\mathrm{d}^m}{\mathrm{d}x^m}(x^2-1)^n\ (m=0,1,2,\cdots,n-1)$
> 都含有 $(x^2-1)$ 因子, 即当 $m<n$ 时
> $q_{2n-m}(x)$ 都有实根 $-1$ 和 $1$
>
> 1. $m=0$ 时, $q_{2n}(x)=(x^2-1)^n$, 因此 $-1$ 和
> $1$ 是它仅有的两个相异根
>    由 Rolle 定理, $q_{2n-1}(x)=q'_{2n}(x)$ 在
> $(-1,1)$ 中必有一个根, 记为 $x_{11}$
>
> 2. 这样 $q_{2n-1}(x)$ 在 $[-1,1]$ 上就至少有
> $-1,x_{11},1$ 三个相异根
>
>    再由 Rolle 定理, $q_{2n-2}(x)=q'_{2n-1}(x)$ 在
> $(-1,x_{11})$ 和 $(x_{11},1)$ 中至少各有一个根, 记为
> $x_{21},x_{22}$
>
>    则 $q_{2n-2}(x)$ 在 $[-1,1]$ 上就至少有
> $-1,x_{21},x_{22},1$ 四个相异根
>
> 3. 反复使用 Rolle 定理, 运用数学归纳法可证 $q_{2n-m}(x)$ 在
> $[-1,1]$ 上至少有 $m+2$ 个相异根
> $-1,x_{m1},x_{m2},\cdots,x_{mm},1\ (m=0,1,2,\cdots,n-1)$
>
> 4. 令 $m=n-1$, 即 $q_{n+1}(x)$ 在 $[-1,1]$ 上至少有
> $n+1$ 个相异根, 再用一次 Rolle 定理, 便知
> $q_n(x)=q'_{n+1}(x)$ 在 $(-1,1)$ 中至少有 $n$ 个相异根
>
> 由于 $q_n(x)$ 是 $n$ 次多项式, 它在 $(-1,1)$ 中至多只有
> $n$ 个根, 因此恰有 $n$ 个根
> $p_n(x)$ 与 $q_n(x)$ 只相差一个系数, 所以对
> $p_n(x)$ 结论也成立
[Legendre 多项式是数学物理中一个重要的特殊函数]


## Lagrange 中值定理

在 Rolle 定理的三个条件中, 前两个条件对讨论 $f(x)$ 在
$(a,b)$ 中某些点处的切线而言是必不可少的
保留这两个条件, 将第三个条件 $f(a)=f(b)$ 去掉, 得到更一般的结论
Lagrange 中值定理: 设函数 $f(x)$ 在闭区间 $[a,b]$ 上连续,
在开区间 $(a,b)$ 上可导, 则至少存在一点 $\xi\in(a,b)$, 使
$f'(\xi)=\frac{f(b)-f(a)}{b-a}$

证明: 作辅助函数
$\varphi(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a),\quad x\in[a,b]$

由于 $f(x)$ 在 $[a,b]$ 上连续, 在 $(a,b)$ 上可导, 因此
$\varphi(x)$ 也在 $[a,b]$ 上连续, 在 $(a,b)$ 上可导, 并且
$\varphi(a)=\varphi(b)=0$

于是由 Rolle 定理, 至少存在一点 $\xi\in(a,b)$, 使
$\varphi'(\xi)=0$
对 $\varphi(x)$ 求导并令 $\varphi'(\xi)=0$, 整理后便得
$f'(\xi)=\frac{f(b)-f(a)}{b-a}$

图5-2: Lagrange 中值定理的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206301.png =400x)

上式称为 Lagrange 公式
由于 $\xi\in(a,b)$, 因而总可以找到某个 $\theta\in(0,1)$,
使 $\xi=a+\theta(b-a)$, 于是 Lagrange 公式也可写成
$f(b)-f(a)=f'(a+\theta(b-a))(b-a),\quad\theta\in(0,1)$

若记 $a$ 为 $x$, $b-a$ 为 $\Delta x$, 则上式又可表示为
$f(x+\Delta x)-f(x)=f'(x+\theta\Delta x)\Delta x,\quad\theta\in(0,1)$

最后一种形式
$\Delta y=f'(x+\theta\Delta x)\Delta x$ 给出了自变量, 因变量的差分与函数的导数值的精确关系
[与 Rolle 定理相仿, Lagrange 中值定理的任何一个条件不满足时,
定理结论就有可能不成立]


## 用 Lagrange 中值定理讨论函数性质

由 Lagrange 中值定理可以推出一些重要结果
定理: 若 $f(x)$ 在 $(a,b)$ 上可导且 $f'(x)\equiv0$, 则
$f(x)$ 在 $(a,b)$ 上恒为常数

证明: 设 $x_1$ 和 $x_2\ (x_1<x_2)$ 是区间
$(a,b)$ 中任意两点

在 $[x_1,x_2]$ 上应用 Lagrange 中值定理, 即知存在
$\xi\in(x_1,x_2)\subset(a,b)$, 使
$f(x_2)-f(x_1)=f'(\xi)(x_2-x_1)$

由条件 $f'(\xi)=0$, 便有 $f(x_1)=f(x_2)$
由 $x_1$ 和 $x_2$ 的任意性, 就得到 $f(x)=C,\ x\in(a,b)$

推论: 若 $f(x)$ 和 $g(x)$ 都在 $(a,b)$ 可导, 且
$f'(x)=g'(x)$, 则 $f(x)$ 和 $g(x)$ 在
$(a,b)$ 上至多相差一个常数, 即
$f(x)=g(x)+C$

定理(一阶导数与单调性的关系): 设函数 $f(x)$ 在区间 $I$ 上可导, 则
$f(x)$ 在 $I$ 上单调增加的充分必要条件是: 对任意 $x\in I$ 有
$f'(x)\geq0$
特别地, 若对任意 $x\in I$ 有 $f'(x)>0$, 则 $f(x)$ 在
$I$ 上严格单调增加

证明 充分性: 设 $x_1$ 和 $x_2\ (x_1<x_2)$ 是区间
$I$ 中任意两点

在 $[x_1,x_2]$ 上应用 Lagrange 中值定理, 即知存在
$\xi\in(x_1,x_2)$, 使
$f(x_2)-f(x_1)=f'(\xi)(x_2-x_1)$

由于 $x_2-x_1>0$, 因此 $f'(x_2)-f(x_1)$ 与
$f'(\xi)$ 同号

所以当 $f'(\xi)\geq0$ 或 $f'(\xi)>0$ 时, 相应地有
$f(x_2)-f(x_1)\geq0$ 或 $f(x_2)-f(x_1)>0$
由 $x_1$ 和 $x_2$ 在 $I$ 中的任意性, 即知 $f$ 在
$I$ 单调增加或严格单调增加

必要性: 设 $x$ 是区间 $I$ 中任意一点
由于 $f(x)$ 在 $I$ 单调增加, 所以对于任意
$x'\in I\ (x'\neq x)$ 成立
$\frac{f(x')-f(x)}{x'-x}\geq0$

令 $x'\to x$, 即得到 $f'(x)\geq0\ (x\in I)$

[若将后半部分的条件减弱为"在 $I$ 中除了有限个点外都有 $f'(x)>0$", 结论"
$f(x)$ 在 $I$ 上严格单调增加"仍然成立, 因此"$f'(x)>0$
"只是充分条件而非必要条件]

------

定义(下凸函数): 设函数 $f(x)$ 在区间 $I$ 上定义, 若对
$I$ 中的任意两点 $x_1$ 和 $x_2$, 和任意
$\lambda\in(0,1)$, 都有
$f(\lambda x_1+(1-\lambda)x_2)\leq\lambda f(x_1)+(1-\lambda)f(x_2)$
则称 $f(x)$ 是 $I$ 上的下凸函数

不等号严格成立时, 称 $f(x)$ 在 $I$ 上是严格下凸函数
类似地可以给出上凸函数和严格上凸函数的定义

图5-3: 下凸函数的定义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206302.png =400x)

定理(二阶导数与凸性的关系): 设函数 $f(x)$ 在区间 $I$ 上二阶可导, 则
$f(x)$ 在区间 $I$ 上是下凸函数的充分必要条件是: 对任意 $x\in I$ 有
$f''(x)\geq0$
特别地, 若对任意 $x\in I$ 有 $f''(x)>0$, 则 $f(x)$ 在
$I$ 上是严格下凸函数

证明 必要性: 因为 $f(x)$ 在 $I$ 上是下凸函数, 由定义可推出, 对于任意
$x\in I$ 和 $\Delta x>0$, 若 $x+\Delta x$ 与
$x-\Delta x$ 都属于 $I$, 则有(在定义中取
$\lambda=\frac{1}{2}$)
$\frac{f(x+\Delta x)+f(x-\Delta x)}{2}\geq f\left(\frac{1}{2}(x+\Delta x)+\frac{1}{2}(x-\Delta x)\right)$
$=f(x)$

所以 $f(x+\Delta x)-f(x)\geq f(x)-f(x-\Delta x)$

对于任意 $x_1,x_2\in I$, 不妨设 $x_1<x_2$, 令
$\Delta x_n=\frac{x_2-x_1}{n}$, 反复使用上式, 就得到

$\begin{aligned}
f(x_2)-f(x_2-\Delta x_n)&\geq f(x_2-\Delta x_n)-f(x_2-2\Delta x_n)\\
&\geq f(x_2-2\Delta x_n)-f(x_2-3\Delta x_n)\geq\cdots\\
&\geq f(x_2-(n-1)\Delta x_n)-f(x_2-n\Delta x_n)\\
&=f(x_1+\Delta x_n)-f(x_1)
\end{aligned}$

因此有
$\frac{f(x_2-\Delta x_n)-f(x_2)}{-\Delta x_n}\geq\frac{f(x_1+\Delta x_n)-f(x_1)}{\Delta x_n}$

由于 $f(x)$ 在 $x_1$ 和 $x_2$ 可导, 令 $n\to\infty$
即 $\Delta x_n\to0$, 便得到
$f'(x_2)\geq f'(x_1)$
即 $f'(x)$ 在 $I$ 上单调增加, 即
$f''(x)\geq0,\ x\in I$

充分性: 若 $f''(x)\geq0$, 则 $f'(x)$ 在 $I$ 上单调增加

对 $I$ 上任意两点 $x_1,x_2$(不妨设 $x_1<x_2$)及
$\lambda\in(0,1)$, 取
$x_0=\lambda x_1+(1-\lambda)x_2$, 那么
$x_1<x_0<x_2$, 且
$x_1-x_0=(1-\lambda)(x_1-x_2),\quad x_2-x_0=\lambda(x_2-x_1)$

在 $[x_1,x_0]$ 和
$[x_0,x_2]$ 上分别应用 Lagrange 中值定理, 则存在
$\eta_1\in(x_1,x_0)$ 和 $\eta_2\in(x_0,x_2)$,
使得
$f(x_1)=f(x_0)+f'(\eta_1)(x_1-x_0),\quad f(x_2)=f(x_0)+f'(\eta_2)(x_2-x_0)$

因此利用 $f'(x)$ 在 $I$ 上的单调增加性得
$f(x_1)\geq f(x_0)+f'(x_0)(x_1-x_0)=f(x_0)+(1-\lambda)f'(x_0)(x_1-x_2)$
$f(x_2)\geq f(x_0)+f'(x_0)(x_2-x_0)=f(x_0)+\lambda f'(x_0)(x_2-x_1)$
分别用 $\lambda$ 和 $1-\lambda$ 乘以上两式并相加得
$\lambda f(x_1)+(1-\lambda)f(x_2)\geq f(x_0)=f(\lambda x_1+(1-\lambda)x_2)$
由定义, $f(x)$ 在 $I$ 上是下凸函数

[类似地可以得到 $f''(x)\leq0$(或 $f''(x)<0$)与
$f(x)$ 在 $I$ 上上凸(或严格上凸)之间的关系]

------

拐点: 曲线上凸与下凸的分界点

定理(拐点): 设 $f(x)$ 在区间 $I$ 上连续,
$(x_0-\delta,x_0+\delta)\subset I$
1. 若 $f''(x)$ 在 $(x_0-\delta,x_0)$ 与
$(x_0,x_0+\delta)$ 上的符号相反, 则点
$(x_0,f(x_0))$ 是曲线 $y=f(x)$ 的拐点
   若符号相同, 则点 $(x_0,f(x_0))$ 不是曲线 $y=f(x)$ 的拐点

2. 设 $f(x)$ 在
$(x_0-\delta,x_0+\delta)$ 上二阶可导, 若点
$(x_0,f(x_0))$ 是曲线 $y=f(x)$ 的拐点, 则
$f''(x_0)=0$

证明: 结论(1)是显然的, 现证结论(2)

由于点 $(x_0,f(x_0))$ 是曲线 $y=f(x)$ 的拐点, 不妨设
$y=f(x)$ 在 $(x_0-\delta,x_0)$ 上是下凸的, 在
$(x_0,x_0+\delta)$ 上是上凸的

由 $f(x)$ 二阶可导的假设与前述定理, 可知在
$(x_0-\delta,x_0)$ 上 $f''(x)\geq0$, 在
$(x_0,x_0+\delta)$ 上 $f''(x)\leq0$

换言之, $f'(x)$ 在 $(x_0-\delta,x_0)$ 上单调增加, 而在
$(x_0,x_0+\delta)$ 上单调减少, 即 $x_0$ 是
$f'(x)$ 的极大值点

由 $f'(x_0)$ 的存在性与 Fermat 引理, 得到 $f''(x_0)=0$

[结论(2)给出的是二阶可导函数曲线的拐点所满足的必要条件, 而非充分条件, 例如曲线
$y=x^4$ 上的 $(0,0)$ 点满足 $f''(0)=0$, 但它不是拐点]
[使 $f''(x)$ 不存在的点 $(x_0,f(x_0))$ 也可能是拐点, 如
$y=x^{\frac{1}{3}}$ 的 $(0,0)$ 点,
因此通过二阶导数来确定拐点时, 既要考虑满足 $f''(x)=0$ 的点, 也要考虑
$f''(x)$ 不存在的点]

------

> 例5-2: 求曲线 $y=\sqrt[3]{x^2}(x^2-4x)$ 的拐点
> 解: $y=\sqrt[3]{x^2}(x^2-4x)$ 的定义域是
> $(-\infty,+\infty)$, 经计算得到
> $y''=\frac{40}{9\sqrt[3]{x}}(x-1)$
>
> 由拐点定理, 只需考虑满足 $y''=0$ 与使 $y''$ 不存在的点, 即
> $x=1$ 与 $x=0$
>
> 由于在 $x=1$ 的左右邻域与 $x=0$ 的左右邻域, $y''$ 都具有相反的符号
> 可知 $(1,-3)$ 与 $(0,0)$ 都是曲线
> $y=\sqrt[3]{x^2}(x^2-4x)$ 的拐点

------

定理(Jensen 不等式): 若 $f(x)$ 为区间 $I$ 上的下凸(上凸)函数,
则对于任意 $x_i\in I$ 和满足
$\sum\limits_{i=1}^n\lambda_i=1$ 的
$\lambda_i>0\ (i=1,2,\cdots,n)$, 成立
$f\left(\sum\limits_{i=1}^n\lambda_ix_i\right)\leq\sum\limits_{i=1}^n\lambda_if(x_i)\quad\left(f\left(\sum\limits_{i=1}^n\lambda_ix_i\right)\geq\sum\limits_{i=1}^n\lambda_if(x_i)\right)$

特别地, 取
$\lambda_i=\frac{1}{n}\ (i=1,2,\cdots,n)$, 就有
$f\left(\frac{1}{n}\sum\limits_{i=1}^nx_i\right)\leq\frac{1}{n}\sum\limits_{i=1}^nf(x_i)\quad\left(f\left(\frac{1}{n}\sum\limits_{i=1}^nx_i\right)\geq\frac{1}{n}\sum\limits_{i=1}^nf(x_i)\right)$

------

> 例5-3: 证明不等式 $|\arctan a-\arctan b|\leq|a-b|$
> 证明: 显然, $f(x)=\arctan x$ 在任意区间
> $[a,b]$ 上满足 Lagrange 中值定理条件
> 所以存在 $\xi\in(a,b)$, 满足
> $|\arctan a-\arctan b|=|f'(\xi)|\cdot|a-b|=\left|\frac{1}{1+\xi^2}\right|\cdot|a-b|\leq|a-b|$

> 例5-4: 证明恒等式
> $\arctan\frac{1+x}{1-x}-\arctan x=\begin{cases}\frac{\pi}{4}, & x<1\\ \frac{3\pi}{4}, & x>1\end{cases}$
>
> 证明: 令
> $f(x)=\arctan\frac{1+x}{1-x}-\arctan x$, 则当
> $x\neq1$ 时, 有
>
> $f'(x)$
> $=\frac{1}{1+\left(\frac{1+x}{1-x}\right)^2}\cdot\left(\frac{1+x}{1-x}\right)'-\frac{1}{1+x^2}$
> $=\frac{1}{1+\left(\frac{1+x}{1-x}\right)^2}\cdot\frac{2}{(1-x)^2}-\frac{1}{1+x^2}$
> $=0$
>
> 由"导数为零的函数恒为常数", 知在任何一个不含 $x=1$ 的区间,
> $\arctan\frac{1+x}{1-x}-\arctan x\equiv C$
> 当 $x<1$ 时, 令 $x=0$, 即得到常数 $C=\frac{\pi}{4}$
> 当 $x>1$ 时, 令 $x\to+\infty$, 即得到常数
> $C=-\frac{3\pi}{4}$

> 例5-5: 判别 $e^\pi$ 与 $\pi^e$ 的大小关系
> 解: 考虑更一般的情形, 设 $a$ 和 $b$ 是两个不同的正实数, 在什么条件下成立
> $a^b>b^a$
>
> 两边取对数后再整理, 即知上式等价于
> $\frac{\ln a}{a}>\frac{\ln b}{b}$
> 所以判别 $a^b$ 与 $b^a$ 的大小关系可以通过确定函数
> $\frac{\ln x}{x}$ 的单调情况来得到
>
> 记 $f(x)=\frac{\ln x}{x}$, 则
> $f'(x)=\frac{1-\ln x}{x^2}\begin{cases}<0, & x>e\\ >0, & 0<x<e\end{cases}$
> 由"一阶导数与单调性", $f(x)$ 在 $[e,+\infty)$ 严格单调减少
> 因此 $\frac{\ln e}{e}>\frac{\ln\pi}{\pi}$,
> 即可判别出 $e^\pi>\pi^e$

> 例5-6: 证明不等式 $\sin x>x-\frac{x^3}{6}\ (x>0)$
> 证明: 令 $f(x)=\sin x-x+\frac{x^3}{6}$, 则当
> $x>0$ 时, 有
>
> $f''(x)=[f'(x)]'=x-\sin x>0$
> 所以 $f'(x)$ 在 $x\geq0$ 严格单调增加, 即当 $x\geq0$ 时, 有
> $f'(x)=\cos x-1+\frac{x^2}{2}>f'(0)=0$
>
> 由此可知 $f(x)$ 在 $[0,+\infty)$ 也是严格单调增加的, 这样当
> $x>0$ 时, 便成立
> $f(x)=\sin x-x+\frac{x^3}{6}>f(0)=0$

> 例5-7: 证明不等式
> $a\ln a+b\ln b\geq(a+b)[\ln(a+b)-\ln2]\quad(a,b>0)$
> 证明: 令 $f(x)=x\ln x$, 则
> $f'(x)=\ln x+1,\quad f''(x)=\frac{1}{x}>0\quad(x>0)$
>
> 由"二阶导数与凸性的关系", $f(x)$ 在
> $(0,+\infty)$ 上是严格下凸的, 因而对任意 $a,b>0$, 都成立
> $\frac{f(a)+f(b)}{2}\geq f\left(\frac{a+b}{2}\right)$
> 即
> $\frac{a\ln a+b\ln b}{2}\geq\frac{a+b}{2}\ln\frac{a+b}{2}$

> 例5-8: 设 $a,b\geq0$, $p,q$ 为满足
> $\frac{1}{p}+\frac{1}{q}=1$ 的正数
> 证明 $ab\leq\frac{1}{p}a^p+\frac{1}{q}b^q$
>
> 证明: 当 $a,b$ 其中之一为 $0$ 时, 上式显然成立
> 现证 $a,b>0$ 的情形
>
> 考虑函数 $f(x)=\ln x\ (x>0)$, 由于在 $(0,+\infty)$ 上
> $f''(x)=-\frac{1}{x^2}<0$, 所以 $f(x)$ 在
> $(0,+\infty)$ 上是严格上凸函数
>
> 于是由定义得
> $\frac{1}{p}f(a^p)+\frac{1}{q}f(b^q)\leq f\left(\frac{1}{p}a^p+\frac{1}{q}b^q\right)$,
> 即
> $\ln(ab)=\frac{1}{p}\ln a^p+\frac{1}{q}\ln b^q\leq\ln\left(\frac{1}{p}a^p+\frac{1}{q}b^q\right)$
>
> 于是利用 $f(x)=\ln x$ 在 $(0,+\infty)$ 上的单调增加性即得
> $ab\leq\frac{1}{p}a^p+\frac{1}{q}b^q\quad(a,b>0)$
[利用 $\ln x$ 在 $(0,+\infty)$ 上的严格上凸性,
由 Jensen 不等式还可得到, 对于任意正数
$x_1,x_2,\cdots,x_n$ 成立
$\frac{\ln x_1+\ln x_2+\cdots+\ln x_n}{n}\leq\ln\left(\frac{x_1+x_2+\cdots+x_n}{n}\right)$,
由此得到
$\sqrt[n]{x_1x_2\cdots x_n}\leq\frac{x_1+x_2+\cdots+x_n}{n}$,
即算术-几何平均不等式]


## Cauchy 中值定理

Cauchy 中值定理: 设 $f(x)$ 和 $g(x)$ 都在闭区间
$[a,b]$ 上连续, 在开区间 $(a,b)$ 上可导, 且对于任意
$x\in(a,b)$, $g'(x)\neq0$, 则至少存在一点
$\xi\in(a,b)$, 使
$\frac{f'(\xi)}{g'(\xi)}=\frac{f(b)-f(a)}{g(b)-g(a)}$

[当 $g(x)=x$ 时, 上式即为 Lagrange 公式,
所以 Lagrange 中值定理是 Cauchy 中值定理的特殊情况]

证明: 设 $g(a)=\alpha$, $g(b)=\beta$

由闭区间上连续函数的性质, 以及 $g(x)$ 在 $[a,b]$ 上连续, 在
$(a,b)$ 上可导, 且导数恒不为零, 不难用反证法证明 $g(x)$ 在
$[a,b]$ 上严格单调, 不妨设 $g(x)$ 严格单调增加

由反函数存在定理和反函数导数存在定理, 在 $[\alpha,\beta]$ 上存在
$g(x)$ 的反函数 $g^{-1}(y)$, $g^{-1}(y)$ 在
$[\alpha,\beta]$ 上可导, 其导数
$[g^{-1}(y)]'=\frac{1}{g'(x)}$
并且 $g^{-1}(y)$ 在 $[\alpha,\beta]$ 上也是严格单调增加的

考虑 $[\alpha,\beta]$ 上的复合函数
$F(y)=f(g^{-1}(y))$, 由定理条件和以上讨论, 即知 $F(y)$ 在
$[\alpha,\beta]$ 上满足 Lagrange 中值定理条件

于是存在 $\eta\in(\alpha,\beta)$, 使得
$F'(\eta)$
$=\frac{F(\beta)-F(\alpha)}{\beta-\alpha}$
$=\frac{f(g^{-1}(\beta))-f(g^{-1}(\alpha))}{g(b)-g(a)}$
$=\frac{f(b)-f(a)}{g(b)-g(a)}$

由 $g(x)$ 和 $g^{-1}(y)$ 的关系, 在 $(a,b)$ 中存在一点
$\xi$, 满足 $g(\xi)=\eta$, 于是

$F'(\eta)$
$=[f(g^{-1}(y))]'\big|_{y=\eta}$
$=f'(g^{-1}(y))\cdot[g^{-1}(y)]'\big|_{y=\eta}$
$=f'(x)\cdot\left.\frac{1}{g'(x)}\right|_{x=g^{-1}(\eta)=\xi}$
$=\frac{f'(\xi)}{g'(\xi)}$
代入上式就得到了定理结论

图5-4: Cauchy 中值定理的参数表示

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206303.png =400x)

若将 $f(t)$ 和 $g(t)$ 看成 $xy$ 平面上某条曲线
$y=F(x)$ 的参数方程, 即 $y=F(x)$ 可以表示为
$\begin{cases}x=g(t),\\ y=f(t),\end{cases}\quad t\in[a,b]$
则 Cauchy 中值定理也可以看成是 Lagrange 中值定理的参数表达形式

------

> 例5-9: 设 $f(x)$ 在 $[1,+\infty)$ 上连续, 在
> $(1,+\infty)$ 上可导
> 已知函数 $e^{-x^2}f'(x)$ 在 $(1,+\infty)$ 上有界,
> 证明函数 $xe^{-x^2}f(x)$ 在 $(1,+\infty)$ 上也有界
>
> 证明: 设
> $|e^{-x^2}f'(x)|\leq M,\ x\in(1,+\infty)$
>
> 首先对于函数 $e^{-x^2}f(x),\ x\in(1,+\infty)$,
> 应用 Cauchy 中值定理, 可以证明它是有界的
> $\left|\frac{f(x)}{e^{x^2}}\right|\leq\left|\frac{f(x)-f(1)}{e^{x^2}}\right|+\left|\frac{f(1)}{e^{x^2}}\right|\leq\left|\frac{f(x)-f(1)}{e^{x^2}-e}\right|+\frac{|f(1)|}{e}$
> $=\left|\frac{f'(\xi)}{2\xi e^{\xi^2}}\right|+\frac{|f(1)|}{e}\leq\frac{|f'(\xi)|}{2e^{\xi^2}\cdot e}+\frac{|f(1)|}{e}\leq\frac{M}{2}+\frac{|f(1)|}{e}$
> 其中 $\xi\in(1,x)$
>
> 进一步, 对于函数 $xe^{-x^2}f(x),\ x\in(1,+\infty)$,
> 也有
> $\left|\frac{xf(x)}{e^{x^2}}\right|\leq\left|\frac{xf(x)-f(1)}{e^{x^2}}\right|+\left|\frac{f(1)}{e^{x^2}}\right|$
> $=\left|\frac{xf(x)-1\cdot f(1)}{e^{x^2}-e}\right|+\frac{|f(1)|}{e}\leq\left|\frac{\xi f'(\xi)+f(\xi)}{2\xi e^{\xi^2}}\right|+\frac{|f(1)|}{e}\leq\frac{3M}{4}+\frac{3|f(1)|}{2e}$


## 待定型极限和 L'Hospital 法则

待定型: 计算分式函数的极限时, 分子分母都趋于零或都趋于无穷大的极限类型
1. $\frac{0}{0}$ 型待定型, 简称 $\frac{0}{0}$ 型
2. $\frac{\infty}{\infty}$ 型待定型, 简称
$\frac{\infty}{\infty}$ 型

例:
$\lim\limits_{x\to\infty}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0}{b_mx^m+b_{m-1}x^{m-1}+\cdots+b_1x+b_0}=\begin{cases}\frac{a_n}{b_m}, & n=m\\ 0, & n<m\\ \infty, & n>m\end{cases}$ 就是一个分子分母都趋于无穷大的例子

待定型极限除此以外, 还有 $0\cdot\infty$ 型,
$\infty\pm\infty$ 型, $\infty^0$ 型,
$1^\infty$ 型, $0^0$ 型等
后面几种类型都可以化成前两种类型进行计算

------

L'Hospital 法则: 设函数 $f(x)$ 和 $g(x)$ 在
$(a,a+d]$ 上可导($d$ 是某个正常数), 且 $g'(x)\neq0$

若此时有
$\lim\limits_{x\to a+}f(x)=\lim\limits_{x\to a+}g(x)=0$
或
$\lim\limits_{x\to a+}g(x)=\infty$

且
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 存在(可以是有限数或
$\infty$), 则成立
$\lim\limits_{x\to a+}\frac{f(x)}{g(x)}=\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$

证明: 这里仅对
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}=A$ 为有限数时来证明,
当 $A$ 为无穷大时的证明过程是类似的

先证明
$\lim\limits_{x\to a+}f(x)=\lim\limits_{x\to a+}g(x)=0$ 的情况
由于函数在 $x=a$ 处的值与 $x\to a+$ 时的极限无关, 因此可以补充定义
$f(a)=g(a)=0$
使得 $f(x)$ 和 $g(x)$ 在 $[a,a+d]$ 上连续

这样, 经补充定义后的函数 $f(x)$ 和 $g(x)$ 在
$[a,a+d]$ 上满足 Cauchy 中值定理的条件, 因而对于任意
$x\in(a,a+d)$, 存在 $\xi\in(a,x)$ 满足
$\frac{f(x)}{g(x)}=\frac{f(x)-f(a)}{g(x)-g(a)}=\frac{f'(\xi)}{g'(\xi)}$

当 $x\to a+$ 时显然有 $\xi\to a+$, 由于
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 存在,
两端令 $x\to a+$, 即有
$\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$
$=\lim\limits_{\xi\to a+}\frac{f'(\xi)}{g'(\xi)}$
$=\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$

下面证明 $\lim\limits_{x\to a+}g(x)=\infty$ 时的情况
记 $x_0$ 是 $(a,a+d)$ 中任意一个固定点, 则当
$x\neq x_0$ 时, $\frac{f(x)}{g(x)}$ 可以改写为

$\begin{aligned}
\frac{f(x)}{g(x)}&=\frac{f(x)-f(x_0)}{g(x)}+\frac{f(x_0)}{g(x)}\\
&=\frac{g(x)-g(x_0)}{g(x)}\cdot\frac{f(x)-f(x_0)}{g(x)-g(x_0)}+\frac{f(x_0)}{g(x)}\\
&=\left[1-\frac{g(x_0)}{g(x)}\right]\frac{f(x)-f(x_0)}{g(x)-g(x_0)}+\frac{f(x_0)}{g(x)}
\end{aligned}$

于是
$\left|\frac{f(x)}{g(x)}-A\right|$
$=\left|\left[1-\frac{g(x_0)}{g(x)}\right]\frac{f(x)-f(x_0)}{g(x)-g(x_0)}-A\right|\leq\left|1-\frac{g(x_0)}{g(x)}\right|\cdot\left|\frac{f(x)-f(x_0)}{g(x)-g(x_0)}-A\right|+\left|\frac{f(x_0)-Ag(x_0)}{g(x)}\right|$

因为
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}=A$,
所以对于任意 $\varepsilon>0$, 存在
$\rho>0\ (\rho<d)$, 当 $0<x-a<\rho$ 时,
$\left|\frac{f'(x)}{g'(x)}-A\right|<\varepsilon$

取 $x_0=a+\rho$, 由 Cauchy 中值定理, 对于任意
$x\in(a,x_0)$, 存在
$\xi\in(x,x_0)\subset(a,a+\rho)$ 满足
$\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\xi)}{g'(\xi)}$

于是得到
$\left|\frac{f(x)-f(x_0)}{g(x)-g(x_0)}-A\right|=\left|\frac{f'(\xi)}{g'(\xi)}-A\right|<\varepsilon$

又因为 $\lim\limits_{x\to a+}g(x)=\infty$,
所以可以找到正数 $\delta<\rho$, 当 $0<x-a<\delta$ 时, 成立
$\left|\frac{g(x_0)}{g(x)}\right|<2,\quad\left|\frac{f(x_0)-Ag(x_0)}{g(x)}\right|<\varepsilon$

综上所述, 即知对于任意 $\varepsilon>0$, 存在 $\delta>0$,
当 $0<x-a<\delta$ 时,
$\left|\frac{f(x)}{g(x)}-A\right|\leq\left|1-\frac{g(x_0)}{g(x)}\right|\cdot\left|\frac{f(x)-f(x_0)}{g(x)-g(x_0)}-A\right|+\left|\frac{f(x_0)-Ag(x_0)}{g(x)}\right|<2\varepsilon+\varepsilon=3\varepsilon$
由定义即得
$\lim\limits_{x\to a+}\frac{f(x)}{g(x)}=A=\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$

从定理后半部分的证明过程可以知道, 当 $x\to a+$ 时
$g(x)\to\infty$, 那么此时对 $f(x)$ 的变化趋势事实上没有任何要求
也就是说, 这时无论 $f(x)$ 有无极限, 有界无界, 只要
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 存在,
L'Hospital 法则都是有效的

所以尽管习惯上称它为 $\frac{\infty}{\infty}$ 型,
但实际上它的使用范围可以扩展为 $\frac{*}{\infty}$ 型极限,
$*$ 代表任意变化类型

以上结论在 $x\to a\pm$, $x\to a$ 或 $x\to\infty$(包括
$+\infty$ 和 $-\infty$)时也是成立的

------

> 例5-10: 求
> $\lim\limits_{x\to0}\frac{1-\cos 2x}{x^2}$
>
> 解: 这是 $\frac{0}{0}$ 型
> 因为
> $\frac{(1-\cos 2x)'}{(x^2)'}=\frac{2\sin 2x\cos x}{x}\to2\ (x\to0)$,
> 由 L'Hospital 法则, 就可以得到
> $\lim\limits_{x\to0}\frac{1-\cos 2x}{x^2}=2$
>
> 一般可以写成如下格式
> $\lim\limits_{x\to0}\frac{1-\cos 2x}{x^2}$
> $=\lim\limits_{x\to0}\frac{(1-\cos 2x)'}{(x^2)'}$
> $=\lim\limits_{x\to0}\frac{2\sin 2x\cos x}{x}$
> $=2\lim\limits_{x\to0}\frac{\sin x}{x}\cdot\lim\limits_{x\to0}\cos x=2$

> 例5-11: 求
> $\lim\limits_{x\to\infty}\frac{\frac{\pi}{2}-\arctan x}{\sin\frac{1}{x}}$
>
> 解: 由 L'Hospital 法则得
> $\lim\limits_{x\to\infty}\frac{\frac{\pi}{2}-\arctan x}{\sin\frac{1}{x}}$
> $=\lim\limits_{x\to\infty}\frac{-\frac{1}{1+x^2}}{\cos\frac{1}{x}\left(-\frac{1}{x^2}\right)}$
> $=\lim\limits_{x\to\infty}\frac{1}{1+x^2}\cdot\lim\limits_{x\to\infty}\frac{x^2}{\cos\frac{1}{x}}$
> $=1$

> 例5-12: 求
> $\lim\limits_{x\to0}\frac{x-\tan x}{x^3}$
>
> 解: 这是 $\frac{0}{0}$ 型, 由 L'Hospital 法则得
> $\lim\limits_{x\to0}\frac{x-\tan x}{x^3}=\lim\limits_{x\to0}\frac{1-\sec^2x}{3x^2}$
> (仍是 $\frac{0}{0}$ 型, 再用 L'Hospital 法则)
> $=\lim\limits_{x\to0}\frac{-2\sec^2x\tan x}{6x}$
> $=\lim\limits_{x\to0}\left(-\frac{1}{3}\cdot\frac{\sin x}{x}\cdot\frac{1}{\cos^3x}\right)$
> $=-\frac{1}{3}$

> 例5-13: 求
> $\lim\limits_{x\to+\infty}\frac{x^a}{e^{bx}}\ (a>0,b>0)$
>
> 解: 这是 $\frac{\infty}{\infty}$ 型
> 设 $[a]'=n$(记号 $[x]'$ 表示不小于 $x$ 的最小整数),
> 反复使用 L'Hospital 法则 $n$ 次, 即有
>
> $\lim\limits_{x\to+\infty}\frac{x^a}{e^{bx}}$
> $=\lim\limits_{x\to+\infty}\frac{a\cdot x^{a-1}}{b\cdot e^{bx}}$
> $=\lim\limits_{x\to+\infty}\frac{a(a-1)\cdot x^{a-2}}{b^2\cdot e^{bx}}$
> $=\cdots=\lim\limits_{x\to+\infty}\frac{a(a-1)(a-2)\cdots(a-n+1)}{b^n\cdot e^{bx}}$
> $=0$
>
> 这说明当 $x\to+\infty$ 的时候, 指数函数
> $a^x\ (a>1)$ 与任何次数的幂函数 $x^\alpha$ 相比,
> 都是更高阶的无穷大量
> 同样可以导出, $\log_a x\ (a>1)$ 与任何次数的幂函数
> $x^\alpha\ (\alpha>0)$ 相比, 都是更低阶的无穷大量


## 可化为 $\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型的极限

前面已经指出, $0\cdot\infty$ 型,
$\infty\pm\infty$ 型, $\infty^0$ 型,
$1^\infty$ 型, $0^0$ 型等类型的极限都可以化成
$\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型
1. $0\cdot\infty$ 型可化成
$\frac{1}{\infty}\cdot\infty$ 型, 即
$\frac{\infty}{\infty}$ 型, 或
$0\cdot\frac{1}{0}$ 型, 即 $\frac{0}{0}$ 型

------

> 例5-14: 求 $\lim\limits_{x\to0+}x\ln x$
> 解: 这是 $0\cdot\infty$ 型, 将其转化为
> $\frac{\infty}{\infty}$ 型
> $\lim\limits_{x\to0+}x\ln x=\lim\limits_{x\to0+}\frac{\ln x}{\frac{1}{x}}$
> 再由 L'Hospital 法则得
>
> $\lim\limits_{x\to0+}x\ln x=\lim\limits_{x\to0+}\frac{\frac{1}{x}}{-\frac{1}{x^2}}$
> $=\lim\limits_{x\to0+}(-x)$
> $=0$
2. $\infty-\infty$ 型可化成
$\frac{1}{0}-\frac{1}{0}$ 型, 再通分变成
$\frac{0-0}{0}$ 型, 即 $\frac{0}{0}$ 型

------

> 例5-15: 求
> $\lim\limits_{x\to0}\left(\cot x-\frac{1}{x}\right)$
> 解: 这是 $\infty-\infty$ 型, 先对它通分
>
> $\lim\limits_{x\to0}\left(\cot x-\frac{1}{x}\right)$
> $=\lim\limits_{x\to0}\left(\frac{\cos x}{\sin x}-\frac{1}{x}\right)$
> $=\lim\limits_{x\to0}\frac{x\cos x-\sin x}{x\sin x}$
> 现在它已被转变成 $\frac{0}{0}$ 型了
>
> 由 L'Hospital 法则得
> $\lim\limits_{x\to0}\left(\cot x-\frac{1}{x}\right)$
> $=\lim\limits_{x\to0}\frac{(x\cos x-\sin x)'}{(x\sin x)'}$
>
> $=\lim\limits_{x\to0}\frac{\cos x-x\sin x-\cos x}{\sin x+x\cos x}$
> $=\lim\limits_{x\to0}\frac{-x\sin x}{\sin x+x\cos x}$
> $=\lim\limits_{x\to0}\frac{-\sin x}{\frac{\sin x}{x}+\cos x}$
> $=0$
3. $\infty^0$ 型, $1^\infty$ 型, $0^0$ 型极限
$\lim\limits_{x\to a}f(x)^{g(x)}$ 可以通过对数恒等式统一化成
$\lim\limits_{x\to a}f(x)^{g(x)}$
$=\lim\limits_{x\to a}e^{g(x)\ln f(x)}$
$=e^{\lim\limits_{x\to a}g(x)\ln f(x)}$

这里的 $\lim\limits_{x\to a}g(x)\ln f(x)$ 已成为
$0\cdot\infty$ 型

------

> 例5-16: 求 $\lim\limits_{x\to0+}x^x$
> 解: 这是 $0^0$ 型, 将其改写为
> $\lim\limits_{x\to0+}x^x=\lim\limits_{x\to0+}e^{x\ln x}=e^{\lim\limits_{x\to0+}x\ln x}$
> 由例5-14知 $\lim\limits_{x\to0+}x\ln x=0$, 于是
> $\lim\limits_{x\to0+}x^x=e^{\lim\limits_{x\to0+}x\ln x}=e^0=1$

> 例5-17: 求
> $\lim\limits_{x\to0+}\ln\left(\frac{1}{x}\right)^x$
> 解: 这是 $\infty^0$ 型, 将其改写为
> $\lim\limits_{x\to0+}\ln\left(\frac{1}{x}\right)^x=\lim\limits_{x\to0+}e^{x\ln\ln\frac{1}{x}}$
> $=e^{\lim\limits_{x\to0+}x\ln\ln\frac{1}{x}}$
>
> 由 L'Hospital 法则得
> $\lim\limits_{x\to0+}x\ln\ln\frac{1}{x}$
> $=\lim\limits_{x\to0+}\frac{\ln\ln\frac{1}{x}}{\frac{1}{x}}$
> $=\lim\limits_{x\to0+}\frac{\frac{1}{\ln\frac{1}{x}}\cdot\frac{1}{\frac{1}{x}}\cdot\left(-\frac{1}{x^2}\right)}{-\frac{1}{x^2}}$
> $=\lim\limits_{x\to0+}\frac{x}{\ln\frac{1}{x}}$
> $=0$
>
> 于是
> $\lim\limits_{x\to0+}\ln\left(\frac{1}{x}\right)^x=e^{\lim\limits_{x\to0+}x\ln\ln\frac{1}{x}}=e^0=1$

> 例5-18: 求
> $\lim\limits_{x\to\frac{\pi}{2}}(\sin x)^{\tan x}$
> 解: 这是 $1^\infty$ 型, 将其改写为
> $\lim\limits_{x\to\frac{\pi}{2}}(\sin x)^{\tan x}$
> $=\lim\limits_{x\to\frac{\pi}{2}}e^{\tan x\ln\sin x}$
> $=e^{\lim\limits_{x\to\frac{\pi}{2}}\tan x\ln\sin x}$
>
> 由 L'Hospital 法则得
> $\lim\limits_{x\to\frac{\pi}{2}}\tan x\ln\sin x=\lim\limits_{x\to\frac{\pi}{2}}\frac{(\ln\sin x)'}{(\cot x)'}$
> $=\lim\limits_{x\to\frac{\pi}{2}}\frac{\frac{\cos x}{\sin x}}{-\csc^2x}$
> $=0$
>
> 于是
> $\lim\limits_{x\to\frac{\pi}{2}}(\sin x)^{\tan x}=e^{\lim\limits_{x\to\frac{\pi}{2}}\tan x\ln\sin x}=e^0=1$
使用 L'Hospital 法则时要注意两个问题
1. 当
$\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$ 不是
$\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型时,
不能使用 L'Hospital 法则, 否则将会造成错误

------

> 例5-19: 求
> $\lim\limits_{x\to\frac{\pi}{2}}\frac{1+\sin x}{1-\cos x}$
>
> 解: 这不是 $\frac{0}{0}$ 型, 也不是
> $\frac{\infty}{\infty}$ 型, 它的极限为
> $\lim\limits_{x\to\frac{\pi}{2}}\frac{1+\sin x}{1-\cos x}$
> $=\frac{1+\sin\frac{\pi}{2}}{1-\cos\frac{\pi}{2}}$
> $=2$
>
> 若不问情况地贸然使用 L'Hospital 法则, 则
> $\lim\limits_{x\to\frac{\pi}{2}}\frac{1+\sin x}{1-\cos x}$
> $=\lim\limits_{x\to\frac{\pi}{2}}\frac{\cos x}{\sin x}$
> $=0$
> 就会得出不正确的结果
> 因此每次使用 L'Hospital 法则之前都必须对极限的类型加以检验
2. L'Hospital 法则只告诉我们, 对于 $\frac{0}{0}$ 型或
$\frac{\infty}{\infty}$ 型, 当
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 存在时,
它的值等于 $\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$

那么这是否意味着, 当
$\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 不存在时,
$\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$ 也不存在呢

------

> 例5-20: 求
> $\lim\limits_{x\to\infty}\frac{x+\cos x}{x}$
>
> 解: 这是 $\frac{\infty}{\infty}$ 型
> 但我们不能根据当 $x\to\infty$ 时
> $\frac{(x+\cos x)'}{x'}=1-\sin x$ 的极限不存在,
> 就错误地得出
> $\lim\limits_{x\to\infty}\frac{x+\cos x}{x}$ 也不存在的结论
>
> 事实上显然有
> $\lim\limits_{x\to\infty}\frac{x+\cos x}{x}=1$
>
> 因此,
> $\lim\limits_{x\to a+}\frac{f'(x)}{g'(x)}$ 不存在并不表示
> $\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$ 本身存在或不存在,
> 它仅仅意味着此时不能使用 L'Hospital 法则, 而应改用其他方法来讨论
> $\lim\limits_{x\to a+}\frac{f(x)}{g(x)}$


## 带 Peano 余项的 Taylor 公式

多项式: 一类比较简单的函数, 理论上可以用多项式近似地代替某些复杂的函数
如果函数 $f(x)$ 在 $x_0$ 处可微, 那么在 $x_0$ 附近就有
$f(x)=f(x_0)+f'(x_0)(x-x_0)+o(x-x_0)$

这意味着当在 $x=x_0$ 附近用一次多项式
$f(x_0)+f'(x_0)(x-x_0)$ 近似代替 $f(x)$ 时, 其精度对于
$x-x_0$ 而言只达到一阶, 即误差为 $(x-x_0)$ 的高阶无穷小量

为了提高精确度, 必须考虑用更高次数的多项式作逼近
事实上, 当 $f(x)$ 在 $x_0$ 处 $n$ 阶可导时, 有如下更精确的估计

------

带 Peano 余项的 Taylor 公式: 设函数 $f(x)$ 在 $x_0$ 处有
$n$ 阶导数, 则存在 $x_0$ 的一个邻域, 对于该邻域中的任一点 $x$, 成立
$f(x)$
$=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+r_n(x)$
其中余项 $r_n(x)$ 满足
$r_n(x)=o((x-x_0)^n)$

上述公式的前 $n+1$ 项组成的多项式
$p_n(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n$
称为 $f(x)$ 的 $n$ 次 Taylor 多项式, 余项
$r_n(x)=o((x-x_0)^n)$ 称为 Peano 余项

证明: 考虑
$r_n(x)=f(x)-\sum\limits_{k=0}^n\frac{1}{k!}f^{(k)}(x_0)(x-x_0)^k$,
只要证明 $r_n(x)=o((x-x_0)^n)$

显然
$r_n(x_0)=r'_n(x_0)=\cdots=r_n^{(n-1)}(x_0)=0$

反复应用 L'Hospital 法则, 可得
$\lim\limits_{x\to x_0}\frac{r_n(x)}{(x-x_0)^n}$
$=\lim\limits_{x\to x_0}\frac{r'_n(x)}{n(x-x_0)^{n-1}}$
$=\lim\limits_{x\to x_0}\frac{r''_n(x)}{n(n-1)x^{n-2}}$
$=\cdots=\lim\limits_{x\to x_0}\frac{r_n^{(n-1)}(x)}{n(n-1)\cdots2\cdot(x-x_0)}$

$=\frac{1}{n!}\lim\limits_{x\to x_0}\left[\frac{f^{(n-1)}(x)-f^{(n-1)}(x_0)}{x-x_0}-f^{(n)}(x_0)\right]$
$=\frac{1}{n!}[f^{(n)}(x_0)-f^{(n)}(x_0)]$
$=0$
因此 $r_n(x)=o((x-x_0)^n)$


## 带 Lagrange 余项的 Taylor 公式

带 Lagrange 余项的 Taylor 公式: 设 $f(x)$ 在
$[a,b]$ 上有 $n$ 阶连续导数, 且在 $(a,b)$ 上有 $n+1$ 阶导数
设 $x_0\in[a,b]$ 为一定点, 则对于任意 $x\in[a,b]$, 成立
$f(x)$
$=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+r_n(x)$

其中余项 $r_n(x)$ 满足
$r_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1},\quad\xi\text{在}x\text{和}x_0\text{之间}$
上述公式的余项称为 Lagrange 余项

证明: 考虑辅助函数
$G(t)=f(t)-\sum\limits_{k=0}^n\frac{1}{k!}f^{(k)}(t)(x-t)^k$ 和
$H(t)=(x-t)^{n+1}$

那么定理的结论(即需要证明的)就是
$G(x_0)=\frac{f^{(n+1)}(\xi)}{(n+1)!}H(x_0)$
不妨设 $x_0<x$(当 $x<x_0$ 时证明类似)

则 $G(t)$ 和 $H(t)$ 在 $[x_0,x]$ 上连续, 在
$(x_0,x)$ 上可导, 且
$G'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n,\quad H'(t)=-(n+1)(x-t)^n$
显然 $H'(t)$ 在 $(x_0,x)$ 上不等于零

因为 $G(x)=H(x)=0$, 由 Cauchy 中值定理可得
$\frac{G(x_0)}{H(x_0)}$
$=\frac{G(x)-G(x_0)}{H(x)-H(x_0)}$
$=\frac{G'(\xi)}{H'(\xi)}$
$=\frac{f^{(n+1)}(\xi)}{(n+1)!},\quad\xi\in(x_0,x)$

因此
$G(x_0)=\frac{f^{(n+1)}(\xi)}{(n+1)!}H(x_0)$

特别地, 当 $n=0$ 时, 上式成为
$f(x)=f(x_0)+f'(\xi)(x-x_0),\quad\xi\text{在}x\text{和}x_0\text{之间}$
这恰为 Lagrange 中值定理的结果,
所以带 Lagrange 余项的 Taylor 公式可以看成是 Lagrange 中值定理的推广

当 $x\to x_0$ 时,
带 Lagrange 余项的 Taylor 公式蕴涵了带 Peano 余项的 Taylor 公式,
即前者的结论强于后者, 但采用带 Peano 余项的 Taylor 公式时, 对
$f(x)$ 的要求也比采用带 Lagrange 余项的 Taylor 公式时稍弱一些

在实际使用时, 经常将 Taylor 公式写成(带 Lagrange 余项)
$f(x+\Delta x)$
$=f(x)+f'(x)\Delta x+\frac{f''(x)}{2!}\Delta x^2+\cdots+\frac{f^{(n)}(x)}{n!}\Delta x^n+\frac{f^{(n+1)}(x+\theta\Delta x)}{(n+1)!}\Delta x^{n+1}\quad(\theta\in(0,1))$

或是(带 Peano 余项)
$f(x+\Delta x)$
$=f(x)+f'(x)\Delta x+\frac{f''(x)}{2!}\Delta x^2+\cdots+\frac{f^{(n)}(x)}{n!}\Delta x^n+o(\Delta x^n)$
的形式


## 插值多项式和余项

插值多项式: 要求多项式与原函数在某些指定的点上有相同的函数值乃至若干阶导数值
为原来的函数的插值多项式

定义: 设函数 $f(x)$ 在 $[a,b]$ 上的 $m+1$ 个互异节点
$x_0,x_1,\cdots,x_m$ 上的函数值和若干阶导数值
$f^{(j)}(x_i)\ (i=0,1,2,\cdots,m,\ j=0,1,\cdots,n_i-1)$ 是已知的,
这里
$\sum\limits_{i=0}^m n_i=n+1$

若存在一个 $n$ 次多项式 $p_n(x)$, 满足如下的插值条件
$p_n^{(j)}(x_i)=f^{(j)}(x_i)\quad(i=0,1,2,\cdots,m,\ j=0,1,\cdots,n_i-1)$
则称 $p_n(x)$ 是 $f(x)$ 在 $[a,b]$ 上关于插值节点
$x_0,x_1,\cdots,x_m$ 的 $n$ 次插值多项式, 而

$r_n(x)=f(x)-p_n(x)$
称为插值余项

例如在 $x_0,x_1,x_2,x_3$ 4 个点处(即 $m=3$), 已知
$f(x)$ 的函数值和若干阶导数值如下表
| | $x_0$ | $x_1$ | $x_2$ | $x_3$ | $m_j$ |
| --- | --- | --- | --- | --- | --- |
| $j=0$ | $f(x_0)$ | $f(x_1)$ | $f(x_2)$ | $f(x_3)$ | 4 |
| $j=1$ | $f'(x_0)$ | — | $f'(x_2)$ | $f'(x_3)$ | 3 |
| $j=2$ | $f''(x_0)$ | — | $f''(x_2)$ | $f''(x_3)$ | 3 |
| $j=3$ | — | — | $f'''(x_2)$ | — | 1 |
| $n_i$ | 3 | 1 | 4 | 3 | $n+1=11$ |
这里 $n_i$ 表示在点 $x_i$ 处所知道的值的个数, 而 $m_j$ 表示已知
$j$ 阶导数值的点的个数(为叙述问题方便, 当
$\max\limits_i n_i\leq j\leq n+1$ 时, 认为
$m_j=0$)

显然
$\sum\limits_{i=0}^m n_i=\sum\limits_{j=0}^3 m_j=n+1$

如果能找到一个 10 次多项式 $p_{10}(x)$,
在这 4 个点处相应的 11 个值与上表相同, 那么按定义它就是
$f(x)$ 的 10 次插值多项式

[定义没有要求知道 $f(x)$ 的表达式, 在处理实际问题时这一点具有特别重要的意义]

------

引理: 设函数 $g(x)$ 在 $[a,b]$ 上连续, 在 $(a,b)$ 上可导,
在 $[a,b]$ 上的 $l_0$ 个不同的点上有 $g(x)=0$, 同时在其中的
$l_1$ 个点上有 $g'(x)=0$, 则 $g'(x)$ 在
$[a,b]$ 内至少有 $l_0+l_1-1$ 个不同的零点

插值多项式的余项估计: 设 $f(x)$ 在 $[a,b]$ 上具有 $n$ 阶连续导数,
在 $(a,b)$ 上有 $n+1$ 阶导数
且 $f(x)$ 在 $[a,b]$ 上的 $m+1$ 个互异点
$x_0,x_1,\cdots,x_m$ 上的函数值和若干阶导数值
$f^{(j)}(x_i)$ 是已知的, 则对于任意 $x\in[a,b]$,
上述插值问题有余项估计

$r_n(x)=f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod\limits_{i=0}^m(x-x_i)^{n_i}$
这里 $\xi$ 是介于
$x_{\min}=\min(x_0,x_1,\cdots,x_m,x)$ 和
$x_{\max}=\max(x_0,x_1,\cdots,x_m,x)$ 之间的一个数(一般依赖于
$x$)

证明: 设 $x$ 是 $[a,b]$ 中任一给定值, 当 $x$ 恰为某个插值节点时,
余项估计式两端均为 $0$, 结论已经成立

设 $x$ 不等于 $x_i\ (i=0,1,2,\cdots,m)$, 记
$n+1$ 次多项式
$\omega_{n+1}(t)=\prod\limits_{i=0}^m(t-x_i)^{n_i}$

作辅助函数
$\varphi(t)=f(t)-p_n(t)-\frac{\omega_{n+1}(t)}{\omega_{n+1}(x)}(f(x)-p_n(x))$

则 $\varphi(t)$ 在任意 $x_i$ 处的 $j$ 阶导数值
$(j=0,1,\cdots,n_i-1)$ 为
$\varphi^{(j)}(x_i)$
$=f^{(j)}(x_i)-p_n^{(j)}(x_i)-\frac{\omega_{n+1}^{(j)}(x_i)}{\omega_{n+1}(x)}(f(x)-p_n(x))$
$=0$

此外还有
$\varphi(x)=f(x)-p_n(x)-\frac{\omega_{n+1}(x)}{\omega_{n+1}(x)}(f(x)-p_n(x))=0$
所以, 使 $\varphi(t)=0$ 的点至少为 $m_0+1$ 个, 而使得
$\varphi^{(j)}(t)=0$ 的点的个数至少为
$m_j\ (j=1,\cdots,n+1)$

由引理, 在区间 $[x_{\min},x_{\max}]$ 内,
$\varphi'(t)$ 至少有 $m_0+m_1$ 个互异的零点;
$\varphi''(t)$ 至少有 $m_0+m_1+m_2-1$ 个互异的零点

用数学归纳法容易证明, 当 $j\leq n+1$ 时, 在区间
$[x_{\min},x_{\max}]\subset[a,b]$ 内,
$\varphi^{(j)}(t)$ 至少有
$\sum\limits_{i=0}^j m_i-j+1$ 个互异的零点

当 $j=n+1$ 时,
$\sum\limits_{i=0}^{n+1}m_i-(n+1)+1=\sum\limits_{i=0}^{n+1}m_i-n=(n+1)-n=1$
所以, 至少应有 1 个点 $\xi\in(x_{\min},x_{\max})$, 使得
$\varphi^{(n+1)}(\xi)=0$

因为 $p_n(t)$ 是 $n$ 次多项式, 所以
$p_n^{(n+1)}(t)=0$, 而 $\omega_{n+1}(t)$ 是
$n+1$ 次的首一多项式(最高项系数为 1 的多项式), 因此
$\omega_{n+1}^{(n+1)}(t)=(n+1)!$, 于是便得到

$0=\varphi^{(n+1)}(\xi)=f^{(n+1)}(\xi)-\frac{(n+1)!}{\omega_{n+1}(x)}(f(x)-p_n(x))$
亦即
$r_n(x)=f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod\limits_{i=0}^m(x-x_i)^{n_i}$

插值多项式的存在唯一性: 满足上述插值条件的插值多项式存在且唯一

证明: 插值多项式的存在性可利用构造法证明

设 $p_n(x)$ 和 $q_n(x)$ 都是 $f(x)$ 的满足插值条件的
$n$ 次多项式, 考虑 $p_n(x)-q_n(x)$

由插值条件, $x_i$ 是它的 $n_i$ 重根, 将 $n_i$ 重根视为
$n_i$ 个根, 则它共有
$\sum\limits_{i=0}^m n_i=n+1$ 个根
但 $p_n(x)-q_n(x)$ 是不超过 $n$ 次的多项式, 由代数基本定理,
$p_n(x)-q_n(x)$ 只能恒为零, 即 $p_n(x)\equiv q_n(x)$


## Lagrange 插值多项式和 Taylor 公式

常用的插值多项式有多种类型, 这里只介绍最重要的两种
1. $n_0=n_1=\cdots=n_m=1$, 即 $m=n$
   这时 $n+1$ 个插值条件均为函数值而不包括导数值, 即 $p_n(x)$ 满足
   $p_n(x_i)=f(x_i),\quad i=0,1,2,\cdots,n$

   由插值余项估计, 它的插值余项为
   $r_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod\limits_{i=0}^n(x-x_i),\quad\xi\in(x_{\min},x_{\max})$

   用基函数法来具体构造: 如果能找到一组 $n$ 次多项式
   $q_k(x),\ k=0,1,2,\cdots,n$, 满足
   $q_k(x_i)=\delta_{ik}$

   这里
   $\delta_{ik}=\begin{cases}0, & i\neq k\\ 1, & i=k\end{cases}$ 称为 Kronecker 记号

   则
   $p_n(x)=\sum\limits_{i=0}^n f(x_i)q_i(x)$ 就是满足条件的插值多项式,
   函数 $\{q_i(x)\}_{i=0}^n$ 称为基函数

   基函数可取为
   $q_k(x)$
   $=\frac{\omega_{n+1}(x)}{(x-x_k)\omega'_{n+1}(x_k)}$
   $=\prod\limits_{\substack{i=0\\ i\neq k}}^n\frac{x-x_i}{x_k-x_i},\quad k=0,1,2,\cdots,n$

   于是得到 $f(x)$ 的 $n$ 次插值多项式
   $p_n(x)$
   $=\sum\limits_{i=0}^n\left[f(x_i)\prod\limits_{\substack{j=0\\ j\neq i}}^n\frac{x-x_j}{x_i-x_j}\right]$
   这称为 Lagrange 插值多项式

------

> 例5-21: 用 $f(x)=\sqrt{x}$ 的二次 Lagrange 插值多项式计算
> $\sqrt{1.15}$ 的近似值
> 解: 取 $x_0=1$, $x_1=1.21$, $x_2=1.44$ 为插值节点,
> 则函数 $f(x)=\sqrt{x}$ 相应的函数值为 $f(x_0)=1$,
> $f(x_1)=1.1$, $f(x_2)=1.2$
>
> 由 Lagrange 插值公式
> $f(x)\approx p_2(x)$
> $=1\cdot\frac{(x-1.21)(x-1.44)}{(1-1.21)(1-1.44)}+1.1\cdot\frac{(x-1)(x-1.44)}{(1.21-1)(1.21-1.44)}+1.2\cdot\frac{(x-1)(x-1.21)}{(1.44-1)(1.44-1.21)}$
> $\approx-0.094\,108\,789\,x^2+0.684\,170\,901\,x+0.409\,937\,888$
>
> 将 $x=1.15$ 代入, 便得到 $\sqrt{1.15}$ 的近似值
> $\sqrt{1.15}\approx p_2(1.15)=1.072\,275\,51$
>
> 它与准确值
> $\sqrt{1.15}=1.072\,380\,53\cdots$ 差的绝对值(称为绝对误差)约为
> $1.0\times10^{-4}$
>
> 而由插值余项估计公式, 其误差约为
> $|r_2(1.15)|$
> $=\left|\frac{1}{6}\cdot\frac{(1.15-1)(1.15-1.21)(1.15-1.44)}{\xi^{5/2}}\right|\leq2.77\times10^{-4}$
> 可见其与理论结果非常吻合
2. $n_0=n+1$, $m=0$
   这时插值节点只剩下一个 $x_0$, 而
   $n+1$ 个插值条件成了这一点上的函数值与各阶导数值, 即 $p_n(x)$ 满足
   $p_n^{(j)}(x_0)=f^{(j)}(x_0),\quad j=0,1,2,\cdots,n$

   考虑 $k$ 次多项式
   $q_k(x)=\frac{(x-x_0)^k}{k!},\quad k=0,1,2,\cdots,n$

   则显然有 $q_k^{(j)}(x_0)=\delta_{jk}$,
   于是它们构成了一组基函数, 作
   $p_n(x)=\sum\limits_{k=0}^n f^{(k)}(x_0)q_k(x)$

   易知 $p_n(x)$ 就是满足条件的插值多项式
   将上述表达式代入 $f(x)=p_n(x)+r_n(x)$,
   并利用插值多项式的余项估计结果, 便得到了带 Lagrange 余项的 Taylor 公式

------

> 例5-22: 用 $f(x)=\sqrt{x}$ 在
> $x=1$ 处的二次 Taylor 多项式计算 $\sqrt{1.15}$ 的近似值,
> 并将结果与例5-21相比较
>
> 解: 由于 $f(x)=\sqrt{x}$,
> $f'(x)=\frac{1}{2\sqrt{x}}$,
> $f''(x)=-\frac{1}{4x\sqrt{x}}$
> 所以 $f(1)=1$, $f'(1)=\frac{1}{2}$,
> $f''(1)=-\frac{1}{4}$
>
> 代入 Taylor 公式并取 $n=2$, 则得到
> $\sqrt{x}\approx p_2(x)$
> $=1+\frac{1}{2}(x-1)-\frac{1}{8}(x-1)^2$
> $=-\frac{1}{8}x^2+\frac{3}{4}x+\frac{3}{8}$
>
> 于是可算出
> $\sqrt{1.15}\approx p_2(1.15)=1.072\,187\,5$
>
> 它与准确值 $\sqrt{1.15}=1.072\,380\,53\cdots$ 相比,
> 绝对误差约为 $1.9\times10^{-4}$, 而此时的余项估计为
> $|r_2(1.15)|=\left|\frac{1}{6}\cdot\frac{0.15^3}{\xi^{5/2}}\right|\leq2.1\times10^{-4}$
> 与理论结果也吻合得很好
对 $n$ 次 Lagrange 插值多项式和 Taylor 多项式的性质做一简单比较
- 对函数的某些形态进行理论分析(尤其是在某个定点的附近)时,
Taylor 公式大有武用之地

- 但从近似计算角度来说, Taylor 多项式的效果往往是局部的, 一般仅对
$x_0$ 附近的 $x$ 有较高的精度, 计算效果随着 $x$ 远离 $x_0$ 急剧变坏

- Lagrange 插值多项式计算时, 对
$x$ 的要求一般比 Taylor 多项式要"宽"些
- 例如 $\sqrt{1.5}$:
用 Lagrange 插值多项式算得的近似值约为 1.224 450,
用 Taylor 多项式算得的近似值约为 1.242 187 5, 而精确值是
$\sqrt{1.5}=1.224\,744\cdots$

[除了一些非常简单的函数之外, 求 $f(x)$ 的高阶导数是繁重的工作,
而 Lagrange 插值多项式的紧凑形式
$p_n(x)=\sum\limits_{i=0}^n\left[f(x_i)\prod\limits_{\substack{j=0\\ j\neq i}}^n\frac{x-x_j}{x_i-x_j}\right]$ 无需求任意阶导数,
计算量极大]


## 函数在 x=0 处的 Taylor 公式

Maclaurin 公式: 函数 $f(x)$ 在 $x=0$ 处的 Taylor 公式
$f(x)=f(0)+f'(0)x+\frac{f''(0)}{2!}x^2+\cdots+\frac{f^{(n)}(0)}{n!}x^n+r_n(x)$
其中 $r_n(x)$ 有 Peano 余项与 Lagrange 余项两种表示形式, 即
$r_n(x)=o(x^n)$, 或
$r_n(x)=\frac{f^{(n+1)}(\theta x)}{(n+1)!}x^{n+1},\ \theta\in(0,1)$

------

> 例5-23: 求 $f(x)=e^x$ 在 $x=0$ 处的 Taylor 公式
> 解: 对函数 $f(x)=e^x$ 有
> $f(x)=f'(x)=f''(x)=\cdots=f^{(n)}(x)=e^x$
> 于是 $f(0)=f'(0)=f''(0)=\cdots=f^{(n)}(0)=1$
>
> 因此得到 $e^x$ 在 $x=0$ 处的 Taylor 公式
> $e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots+\frac{x^n}{n!}+r_n(x)$
> 它的余项为 $r_n(x)=o(x^n)$, 或
> $r_n(x)=\frac{e^{\theta x}}{(n+1)!}x^{n+1},\ \theta\in(0,1)$

> 例5-24: 求 $f(x)=\sin x$ 和 $f(x)=\cos x$ 在
> $x=0$ 处的 Taylor 公式
>
> 解: 先考虑 $f(x)=\sin x$
> 由于对 $k=0,1,2,\cdots$, 有
> $f^{(k)}(x)=\sin\left(x+\frac{k}{2}\pi\right)$
> 于是
> $f^{(k)}(0)=\begin{cases}0, & k=2n\\ (-1)^n, & k=2n+1\end{cases}$
>
> 因此 $\sin x$ 在 $x=0$ 处的 Taylor 公式为
> $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots+(-1)^n\frac{x^{2n+1}}{(2n+1)!}+r_{2n+2}(x)$
> 相应的余项为 $r_{2n+2}(x)=o(x^{2n+2})$, 或
> $r_{2n+2}(x)=\frac{x^{2n+3}}{(2n+3)!}\sin\left(\theta x+\frac{2n+3}{2}\pi\right),\ \theta\in(0,1)$
>
> 同理可以求出 $\cos x$ 在 $x=0$ 处的 Taylor 公式为
> $\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots+(-1)^n\frac{x^{2n}}{(2n)!}+r_{2n+1}(x)$
> 相应的余项为 $r_{2n+1}(x)=o(x^{2n+1})$, 或
> $r_{2n+1}(x)=\frac{x^{2n+2}}{(2n+2)!}\cos\left(\theta x+\frac{2n+2}{2}\pi\right),\ \theta\in(0,1)$

> 例5-25: 求 $f(x)=(1+x)^\alpha$($\alpha$ 为任意实数)在
> $x=0$ 处的 Taylor 公式
>
> 解: 因为 $f(0)=(1+x)^\alpha\big|_{x=0}=1$,
> $f'(0)=\alpha(1+x)^{\alpha-1}\big|_{x=0}=\alpha$
> $f''(0)=\alpha(\alpha-1)(1+x)^{\alpha-2}\big|_{x=0}=\alpha(\alpha-1)$
> 对任意正整数 $k$, 一般地有
> $f^{(k)}(0)=\alpha(\alpha-1)\cdots(\alpha-k+1)$
>
> 记
> $\binom{\alpha}{k}=\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$,
> 并规定 $\binom{\alpha}{0}=1$
>
> 当 $\alpha$ 为正整数 $n$ 时,
> $\binom{n}{j}=C_n^j,\ 1\leq j\leq n$,
> 因而它是组合数的推广, 由此得到
> $(1+x)^\alpha=\binom{\alpha}{0}+\binom{\alpha}{1}x+\binom{\alpha}{2}x^2+\binom{\alpha}{3}x^3+\cdots+\binom{\alpha}{n}x^n+r_n(x)$
> 它的余项为 $r_n(x)=o(x^n)$, 或
> $r_n(x)=\binom{\alpha}{n+1}(1+\theta x)^{\alpha-n-1}\cdot x^{n+1},\ \theta\in(0,1)$
>
> 下面是几种最常见的情况
> (a) 当 $\alpha$ 为正整数 $n$ 时, 上式即成为
> $(1+x)^n=\sum\limits_{k=0}^n\binom{n}{k}x^k=\sum\limits_{k=0}^nC_n^kx^k$
> 这是熟知的二项式展开定理, 此时的余项为零
>
> (b) 当 $\alpha=-1$ 时, 易知
> $\binom{-1}{k}=(-1)^k$, 因此
> $\frac{1}{1+x}=1-x+x^2-x^3+\cdots+(-1)^nx^n+r_n(x)$
> 余项为 $r_n(x)=o(x^n)$, 或
> $r_n(x)=(-1)^{n+1}\frac{x^{n+1}}{(1+\theta x)^{n+2}},\ \theta\in(0,1)$
>
> (c) 当 $\alpha=\frac{1}{2}$ 时, 对 $k\geq1$, 有
> $\binom{\frac{1}{2}}{k}$
> $=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\cdots\left(\frac{1}{2}-k+1\right)}{k!}$
> $=\frac{(1-2)(1-4)\cdots(1-2(k-1))}{2^kk!}$
> $=\begin{cases}\frac{1}{2}, & k=1\\ (-1)^{k-1}\frac{(2k-3)!!}{(2k)!!}, & k>1\end{cases}$
>
> 其中记号 $k!!$ 为
> $k!!=\begin{cases}k(k-2)(k-4)\cdots4\cdot2, & k=2n\\ k(k-2)(k-4)\cdots5\cdot3\cdot1, & k=2n+1\end{cases}$
> 因此
> $\sqrt{1+x}=1+\frac{1}{2}x-\frac{1}{2\cdot4}x^2+\frac{1\cdot3}{2\cdot4\cdot6}x^3-\cdots+(-1)^{n-1}\frac{(2n-3)!!}{(2n)!!}x^n+r_n(x)$
> 余项为 $r_n(x)=o(x^n)$, 或
> $r_n(x)=(-1)^n\frac{(2n-1)!!}{(2n+2)!!}\cdot\frac{x^{n+1}}{(1+\theta x)^{n+\frac{1}{2}}},\ \theta\in(0,1)$
>
> (d) 当 $\alpha=-\frac{1}{2}$ 时, 对 $k\geq1$, 有
> $\binom{-\frac{1}{2}}{k}$
> $=\frac{\left(-\frac{1}{2}\right)\left(-\frac{1}{2}-1\right)\cdots\left(-\frac{1}{2}-k+1\right)}{k!}$
> $=\frac{(-1)(-2)(-4)\cdots(-1-2(k-1))}{2^kk!}$
> $=(-1)^k\frac{(2k-1)!!}{(2k)!!}$
>
> 因此
> $\frac{1}{\sqrt{1+x}}=1-\frac{1}{2}x+\frac{1\cdot3}{2\cdot4}x^2-\frac{1\cdot3\cdot5}{2\cdot4\cdot6}x^3+\cdots+(-1)^n\frac{(2n-1)!!}{(2n)!!}x^n+r_n(x)$
> 余项为 $r_n(x)=o(x^n)$, 或
> $r_n(x)=(-1)^{n+1}\frac{(2n+1)!!}{(2n+2)!!}\cdot\frac{x^{n+1}}{(1+\theta x)^{n+\frac{3}{2}}},\ \theta\in(0,1)$
例5-23, 例5-24, 例5-25 的一般形式是最低限度需要熟记的 Taylor 公式
从这些公式出发, 利用换元, 四则运算, 待定系数, 求导数以及以后要学的求积分等方法,
可以较方便地得到几乎所有常用的初等函数的 Taylor 公式

------

定理: 设 $f(x)$ 在 $x_0$ 的某个邻域有 $n+2$ 阶导数存在, 则它的
$n+1$ 次 Taylor 多项式的导数恰为 $f'(x)$ 的
$n$ 次 Taylor 多项式

------

> 例5-26: 求 $f(x)=2^x$ 在 $x=0$ 处的 Taylor 公式
> 解: 将 $2^x$ 写成 $e^{(\ln 2)x}$, 令
> $u=(\ln 2)x$ 并对 $e^u$ 使用例5-23 的 Taylor 公式,
> 代回变量即得
> $2^x=1+(\ln 2)x+\frac{(\ln 2)^2x^2}{2!}+\frac{(\ln 2)^3x^3}{3!}+\cdots+\frac{(\ln 2)^nx^n}{n!}+o(x^n)$

> 例5-27: 求 $f(x)=\sqrt[3]{2-\cos x}$ 在
> $x=0$ 处的 Taylor 公式(展开至 4 次)
> 解: 令 $u=1-\cos x$, 则当 $x\to0$ 时 $u\to0$, 于是
>
> $\sqrt[3]{2-\cos x}$
> $=\sqrt[3]{1+(1-\cos x)}$
> $=\sqrt[3]{1+u}$
> $=1+\frac{u}{3}-\frac{u^2}{9}+o(u^2)$
> $=1+\frac{1-\cos x}{3}-\frac{(1-\cos x)^2}{9}+o((1-\cos x)^2)$
>
> 由于
> $1-\cos x=\frac{x^2}{2}-\frac{x^4}{24}+o(x^4)$,
> 代入上式得到展开式
> $\sqrt[3]{2-\cos x}=1+\frac{x^2}{6}-\frac{x^4}{24}+o(x^4)$

> 例5-28: 求 $f(x)=\ln(1+x)$ 在 $x=0$ 处的 Taylor 公式
> 解: 由于 $[\ln(1+x)]'=\frac{1}{1+x}$, 设
> $\ln(1+x)$ 的 Taylor 公式为
> $\ln(1+x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n+o(x^n)$
>
> 则由定理知
> $[\ln(1+x)]'=a_1+2a_2x+3a_3x^2+\cdots+na_nx^{n-1}+o(x^{n-1})$
> 由于 $[\ln(1+x)]'=\frac{1}{1+x}$,
> 而由例5-25 的 (b) 知 $\frac{1}{1+x}$ 的 Taylor 公式为
> $\frac{1}{1+x}=1-x+x^2-x^3+\cdots+(-1)^{n-1}x^{n-1}+o(x^{n-1})$
>
> 比较两式, 便得到
> $a_j=\frac{(-1)^{j-1}}{j},\quad j=1,2,\cdots,n$
> 同时可以明显看出 $a_0=\ln 1=0$
> 因此可得
> $\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots+(-1)^{n-1}\frac{x^n}{n}+o(x^n)$

> 例5-29: 求 $f(x)=\arctan x$ 在 $x=0$ 处的 Taylor 公式
> 解: 由例5-25 的 (b), 函数 $\frac{1}{1+x^2}$ 在
> $x=0$ 的 Taylor 公式为
> $\frac{1}{1+x^2}=1-x^2+x^4-x^6+\cdots+(-1)^nx^{2n}+o(x^{2n+1})$
>
> 因为 $(\arctan x)'=\frac{1}{1+x^2}$,
> 按例5-28 同样的方法, 易知
> $\arctan x=x-\frac{x^3}{3}+\frac{x^5}{5}-\cdots+(-1)^n\frac{x^{2n+1}}{2n+1}+o(x^{2n+2})$
函数 $f(x)$ 在 $x=x_0$ 处的 Taylor 公式可以通过对它先在
$x=0$ 处的 Taylor 公式作适当的变换后直接得到, 而不需要再按定义去计算

------

> 例5-30: 求 $f(x)=\sqrt{x}$ 在 $x=1$ 处的 Taylor 公式
> 解: 将 $\sqrt{x}$ 改写成 $\sqrt{1+(x-1)}$,
> 用例5-25 的 (c) 的结论, 即有
> $\sqrt{x}$
> $=\sqrt{1+(x-1)}$
> $=1+\frac{1}{2}(x-1)-\frac{1}{2\cdot4}(x-1)^2+\frac{1\cdot3}{2\cdot4\cdot6}(x-1)^3-\cdots+(-1)^{n-1}\frac{(2n-3)!!}{(2n)!!}(x-1)^n+o((x-1)^n)$


## Taylor 公式的应用

1. 近似计算

------

> 例5-31: 用 $e^x$ 的 10 次 Taylor 多项式求 $e$ 的近似值,
> 并估计误差
> 解: 在 $e^x$ 的 Taylor 公式中取 $x=1$, $n=10$, 则可算得
> $e\approx1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{10!}=2.718\,281\,801\cdots$
> 由于 $e$ 的精确值为 $e=2.718\,281\,828\cdots$,
> 可以看出这样算得的结果是比较准确的
>
> 关于计算的误差, 有如下的估计
> $|d|=\left|\frac{e^{\theta x}}{11!}x^{11}\right|\bigg|_{x=1}<\frac{3}{11!}\approx6.8\times10^{-8}$
必须注意, Taylor 公式只是一种局部性质, 因此在用它进行近似计算时,
$x$ 不能远离 $x_0$, 否则效果会比较差

如在 $\ln(1+x)$ 的 Taylor 公式中令 $x=1$,
取它的前 10 项计算 $\ln 2$ 的近似值, 得到
$\ln 2\approx1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-\frac{1}{8}+\frac{1}{9}-\frac{1}{10}$
$=0.645\,634\,92\cdots$
而 $\ln 2=0.693\,147\,18\cdots$, 误差相当大

如果改用其他形式的 Taylor 公式, 如
$\ln\frac{1+x}{1-x}$
$=\ln(1+x)-\ln(1-x)$
$=\left[x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots-\frac{x^{2n}}{2n}\right]-\left[-x-\frac{x^2}{2}-\frac{x^3}{3}-\cdots-\frac{x^{2n}}{2n}\right]+o(x^{2n})$
$=2\left[x+\frac{x^3}{3}+\frac{x^5}{5}+\cdots+\frac{x^{2n-1}}{2n-1}\right]+o(x^{2n})$

令 $x=\frac{1}{3}$, 只取前两项便有
$\ln 2\approx2\left[\frac{1}{3}+\frac{1}{3}\left(\frac{1}{3}\right)^3\right]=0.691\,35\cdots$
取前四项则可达到
$\ln 2\approx2\left[\frac{1}{3}+\frac{1}{3}\left(\frac{1}{3}\right)^3+\frac{1}{5}\left(\frac{1}{3}\right)^5+\frac{1}{7}\left(\frac{1}{3}\right)^7\right]=0.693\,134\,75\cdots$

2. 求极限
对于待定型的极限问题, 一般可以采用 L'Hospital 法则来求
但是对于一些求导比较繁琐, 特别是要多次使用 L'Hospital 法则的情况,
Taylor 公式往往是比 L'Hospital 法则更为有效的求极限工具

------

> 例5-32: 求
> $\lim\limits_{x\to0}\frac{\cos x-e^{-\frac{x^2}{2}}}{x^4}$
> 解: 这是 $\frac{0}{0}$ 待定型的极限问题
> 如果用 L'Hospital 法则, 则分子分母需要求导 4 次
>
> $\lim\limits_{x\to0}\frac{\cos x-e^{-\frac{x^2}{2}}}{x^4}=\lim\limits_{x\to0}\frac{-\sin x+xe^{-\frac{x^2}{2}}}{4x^3}$
> (仍为 $\frac{0}{0}$ 型)
> $=\lim\limits_{x\to0}\frac{-\cos x+e^{-\frac{x^2}{2}}-x^2e^{-\frac{x^2}{2}}}{12x^2}$
> (仍为 $\frac{0}{0}$ 型)
>
> $=\lim\limits_{x\to0}\frac{\sin x-3xe^{-\frac{x^2}{2}}+x^3e^{-\frac{x^2}{2}}}{24x}$
> (仍为 $\frac{0}{0}$ 型)
> $=\lim\limits_{x\to0}\frac{\cos x-3e^{-\frac{x^2}{2}}+6x^2e^{-\frac{x^2}{2}}-x^4e^{-\frac{x^2}{2}}}{24}$
> $=-\frac{1}{12}$
>
> 但若采用 Taylor 公式, 则
> $\lim\limits_{x\to0}\frac{\cos x-e^{-\frac{x^2}{2}}}{x^4}$
> $=\lim\limits_{x\to0}\frac{\left[1-\frac{x^2}{2!}+\frac{x^4}{4!}+o(x^4)\right]-\left[1+\left(-\frac{x^2}{2}\right)+\frac{1}{2!}\left(\frac{x^2}{2}\right)^2+o(x^4)\right]}{x^4}$
> $=\lim\limits_{x\to0}\frac{-\frac{1}{12}x^4+o(x^4)}{x^4}$
> $=-\frac{1}{12}$
> 计算过程就简洁得多了

> 例5-33: 求
> $\lim\limits_{x\to0}\frac{\ln(1+\sin^2x)-6(\sqrt[3]{2-\cos x}-1)}{x^4}$
> 解: 这也是 $\frac{0}{0}$ 待定型的极限问题
> 由例5-27 和例5-28, 有
>
> $\sqrt[3]{2-\cos x}-1$
> $=\frac{x^2}{6}-\frac{x^4}{24}+o(x^4),\quad\ln(1+\sin^2x)$
> $=\sin^2x-\frac{\sin^4x}{2}+o(\sin^4x)$
>
> 用
> $\sin^2x=\left[x-\frac{x^3}{6}+o(x^3)\right]^2$ 代入,
> 即有
> $\ln(1+\sin^2x)=x^2-\frac{5x^4}{6}+o(x^4)$
>
> 于是
> $\lim\limits_{x\to0}\frac{\ln(1+\sin^2x)-6(\sqrt[3]{2-\cos x}-1)}{x^4}$
> $=\lim\limits_{x\to0}\frac{\left[x^2-\frac{5}{6}x^4+o(x^4)\right]-6\left[\frac{1}{6}x^2-\frac{1}{24}x^4+o(x^4)\right]}{x^4}$
> $=\frac{7}{12}$
3. 证明不等式

------

> 例5-34: 设 $\alpha>1$, 证明当 $x>-1$ 时成立
> $(1+x)^\alpha\geq1+\alpha x$, 且等号仅当 $x=0$ 时成立
>
> 证明: $f(x)=(1+x)^\alpha$ 在
> $(-1,+\infty)$ 上二阶可导, 且有
> $f(0)=1$, $f'(x)=\alpha(1+x)^{\alpha-1}$,
> $f'(0)=\alpha$,
> $f''(x)=\alpha(\alpha-1)(1+x)^{\alpha-2}$
>
> 于是, 对 $f(x)$ 应用在
> $x=0$ 处的带 Lagrange 余项的 Taylor 公式, 得到
> $(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}{2}(1+\theta x)^{\alpha-2}x^2,\quad x>-1$
>
> 注意到上式中最后一项是非负的, 且仅当 $x=0$ 时为零, 所以
> $(1+x)^\alpha\geq1+\alpha x,\ x>-1$, 且等号仅当
> $x=0$ 时成立

> 例5-35: 设 $f(x)$ 在 $[0,1]$ 上具有二阶导数, 且
> $[0,1]$ 上成立 $|f(x)|\leq A$, $|f''(x)|\leq B$,
> 证明
> $|f'(x)|\leq2A+\frac{1}{2}B,\quad x\in[0,1]$
>
> 证明: 对于任意 $c\in[0,1]$, $f(x)$ 在
> $x=c$ 处的带 Lagrange 余项的 Taylor 公式为
> $f(x)=f(c)+f'(c)(x-c)+\frac{1}{2}f''(\xi)(x-c)^2,\quad x\in[0,1]$
>
> 其中 $\xi$ 在 $c$ 与 $x$ 之间, 因此 $\xi\in[0,1]$,
> 特别地有
> $f(0)=f(c)+f'(c)(0-c)+\frac{1}{2}f''(\xi_1)(0-c)^2$
> $f(1)=f(c)+f'(c)(1-c)+\frac{1}{2}f''(\xi_2)(1-c)^2$
> 其中 $\xi_1,\xi_2\in[0,1]$
>
> 将以上两式相减得
> $f'(c)=f(1)-f(0)-\frac{1}{2}[f''(\xi_2)(1-c)^2-f''(\xi_1)c^2]$
> 于是由已知条件得
> $|f'(c)|\leq|f(1)|+|f(0)|+\frac{1}{2}[|f''(\xi_2)|(1-c)^2+|f''(\xi_1)|c^2]\leq2A+\frac{B}{2}[(1-c)^2+c^2]$
>
> 注意到在 $[0,1]$ 上成立 $(1-x)^2+x^2\leq1$, 因此
> $|f'(c)|\leq2A+\frac{1}{2}B$
> 由 $c$ 在 $[0,1]$ 上的任意性, 即得结论
4. 求曲线的渐近线方程
渐近线: 若曲线 $y=f(x)$ 上的点 $(x,f(x))$ 到直线
$y=ax+b$ 的距离在 $x\to+\infty$ 或
$x\to-\infty$ 时趋于零, 则称直线 $y=ax+b$ 是曲线
$y=f(x)$ 的一条渐近线

- 当 $a=0$ 时称为水平渐近线
- 否则称为斜渐近线

显然, 直线 $y=ax+b$ 是曲线 $y=f(x)$ 的渐近线的充分必要条件为
$\lim\limits_{x\to+\infty}[f(x)-(ax+b)]=0$ 或
$\lim\limits_{x\to-\infty}[f(x)-(ax+b)]=0$

如果 $y=ax+b$ 是曲线 $y=f(x)$ 的渐近线, 则
$\lim\limits_{x\to+\infty}\frac{f(x)-(ax+b)}{x}=0$
或
$\lim\limits_{x\to-\infty}\frac{f(x)-(ax+b)}{x}=0$

因此首先有
$a=\lim\limits_{x\to+\infty}\frac{f(x)}{x}$ 或
$a=\lim\limits_{x\to-\infty}\frac{f(x)}{x}$

其次, 再由
$\lim\limits_{x\to+\infty}[f(x)-(ax+b)]=0$ 或
$\lim\limits_{x\to-\infty}[f(x)-(ax+b)]=0$ 可得
$b=\lim\limits_{x\to+\infty}[f(x)-ax]$ 或
$b=\lim\limits_{x\to-\infty}[f(x)-ax]$

反之, 如果由以上两式确定了 $a$ 和 $b$, 那么 $y=ax+b$ 就是曲线
$y=f(x)$ 的一条渐近线

垂直渐近线: 当 $x\to a+$ 或 $x\to a-$ 时, $f(x)$ 趋于
$+\infty$ 或 $-\infty$, 即
$\lim\limits_{x\to a+}f(x)=\pm\infty$ 或
$\lim\limits_{x\to a-}f(x)=\pm\infty$
则称直线 $x=a$ 是曲线 $y=f(x)$ 的一条垂直渐近线

------

> 例5-36: 求曲线 $y=\frac{(x-1)^2}{3(x+1)}$ 的渐近线方程
> 解: 由于
> $a=\lim\limits_{x\to\infty}\frac{y}{x}=\lim\limits_{x\to\infty}\frac{(x-1)^2}{3x(x+1)}=\frac{1}{3}$
>
> $b=\lim\limits_{x\to\infty}\left[\frac{(x-1)^2}{3(x+1)}-ax\right]$
> $=\lim\limits_{x\to\infty}\left[\frac{(x-1)^2}{3(x+1)}-\frac{1}{3}x\right]$
> $=\frac{1}{3}\lim\limits_{x\to\infty}\frac{-3x+1}{x+1}$
> $=-1$
>
> 因此 $y=\frac{x}{3}-1$ 为曲线
> $y=\frac{(x-1)^2}{3(x+1)}$ 的斜渐近线
> 又由于
> $\lim\limits_{x\to-1+}\frac{(x-1)^2}{3(x+1)}=+\infty,\quad\lim\limits_{x\to-1-}\frac{(x-1)^2}{3(x+1)}=-\infty$
> 可知 $x=-1$ 是曲线
> $y=\frac{(x-1)^2}{3(x+1)}$ 的垂直渐近线

> 例5-37: 求曲线 $y=\sqrt[3]{x^3-x^2+x+1}$ 的渐近线方程
> 解: 设 $y=\sqrt[3]{x^3-x^2+x+1}$ 的渐近线方程为
>
> $y=ax+b$, 则由定义
> $a=\lim\limits_{x\to\infty}\frac{y}{x}$
> $=\lim\limits_{x\to\infty}\frac{\sqrt[3]{x^3-x^2+x+1}}{x}$
> $=\lim\limits_{x\to\infty}\sqrt[3]{1-\frac{1}{x}+\frac{1}{x^2}+\frac{1}{x^3}}$
> $=1$
>
> $b=\lim\limits_{x\to\infty}(\sqrt[3]{x^3-x^2+x+1}-x)$
> $=\lim\limits_{x\to\infty}x\left(\sqrt[3]{1-\frac{1}{x}+\frac{1}{x^2}+\frac{1}{x^3}}-1\right)$
> $=\lim\limits_{x\to\infty}x\left[\left(1-\frac{1}{3}\cdot\frac{x^2+x+1}{x^3}+o\left(\frac{1}{x}\right)\right)-1\right]$
> $=\lim\limits_{x\to\infty}\left[-\frac{1}{3}+o(1)\right]$
> $=-\frac{1}{3}$
>
> 因此 $y=\sqrt[3]{x^3-x^2+x+1}$ 的渐近线方程为
> $y=x-\frac{1}{3}$
[例5-36 和例5-37 的图形见 §5 的图5-8 和图5-9]

------

> 例5-38: 求曲线
> $y=x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)$ 的渐近线方程
> 解: 设
> $y=x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)$ 的渐近线方程为
>
> $y=ax+b$, 则由定义
> $a=\lim\limits_{x\to\infty}\frac{y}{x}$
> $=\lim\limits_{x\to\infty}x^2\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)$
> $=\lim\limits_{x\to\infty}x^2\left[\left(1+\frac{1}{x}+\frac{1}{2x^2}+o\left(\frac{1}{x^2}\right)\right)+\left(1-\frac{1}{x}+\frac{1}{2x^2}+o\left(\frac{1}{x^2}\right)\right)-2\right]$
> $=1$
>
> $b=\lim\limits_{x\to\infty}\left[x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)-x\right]$
> $=\lim\limits_{x\to\infty}x\left[\left(1+\frac{1}{x}+\frac{1}{2x^2}+\frac{1}{6x^3}+o\left(\frac{1}{x^3}\right)\right)+\left(1-\frac{1}{x}+\frac{1}{2x^2}-\frac{1}{6x^3}+o\left(\frac{1}{x^3}\right)\right)-2\right]-x=\lim\limits_{x\to\infty}[x+o(1)-x]$
> $=0$
>
> 因此 $y=x$ 为曲线
> $y=x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)$ 的斜渐近线
> 又由于
> $\lim\limits_{x\to0+}x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)=\lim\limits_{x\to0+}x^3e^{\frac{1}{x}}=+\infty,\quad\lim\limits_{x\to0-}x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)=\lim\limits_{x\to0-}x^3e^{-\frac{1}{x}}=-\infty$
> 可知 $x=0$ 是曲线
> $y=x^3\left(e^{\frac{1}{x}}+e^{-\frac{1}{x}}-2\right)$ 的垂直渐近线
5. 外推
外推: 通过将精度较低的近似值进行适当组合, 产生精度较高的近似值的方法

若对于某个值 $a$, 按参数 $h$ 算出的近似值 $a_1(h)$ 可以展开成
$a_1(h)=a+c_1h+c_2h^2+c_3h^3+\cdots$(这里先不管
$c_i$ 的具体形式)

那么按参数 $\frac{h}{2}$ 算出的近似值
$a_1\left(\frac{h}{2}\right)$ 就是
$a_1\left(\frac{h}{2}\right)=a+\frac{1}{2}c_1h+\frac{1}{4}c_2h^2+\frac{1}{8}c_3h^3+\cdots$

$a_1(h)$ 和 $a_1\left(\frac{h}{2}\right)$ 与准确值
$a$ 的误差都是 $O(h)$ 阶的

现在, 将后一式乘上 2 减去前一式, 便得到
$a_2(h)=\frac{2a_1\left(\frac{h}{2}\right)-a_1(h)}{2-1}=a+d_2h^2+d_3h^3+\cdots$

也就是说, 对两个 $O(h)$ 阶的近似值化了少量几步四则运算进行组合之后,
却得到了具有 $O(h^2)$ 阶的近似值 $a_2(h)$, 这样的过程就称为外推

若进行了一次外推之后精度仍未达到要求, 则可以从 $a_2(h)$ 出发再次外推
$a_3(h)=\frac{4a_2\left(\frac{h}{2}\right)-a_2(h)}{4-1}=a+e_3h^3+e_4h^4+\cdots$

得到 $O(h^3)$ 阶的近似值 $a_3(h)$, 这样的过程可以进行
$k-1$ 步, 直到
$a_k(h)=\frac{2^{k-1}a_{k-1}\left(\frac{h}{2}\right)-a_{k-1}(h)}{2^{k-1}-1}=a+O(h^k)$
满足预先给定的精度
外推方法能以较小的代价获得高精度的结果, 因此是一种非常重要的近似计算技术

------

> 例5-39: 单位圆的内接正 $n$ 边形的面积可以表示为
> $S(h)=\frac{1}{2h}\sin(2h\pi)$, 这里
> $h=\frac{1}{n}$
> 按 Taylor 公式
> $S(h)=\frac{1}{2h}\left[2h\pi-\frac{(2h\pi)^3}{3!}+\frac{(2h\pi)^5}{5!}-\cdots\right]=\pi+c_2h^2+c_4h^4+c_6h^6+\cdots$
>
> 因此, 其内接正 $2n$ 边形的面积可以表示为
> $S\left(\frac{h}{2}\right)$
> $=\frac{1}{h}\left[h\pi-\frac{(h\pi)^3}{3!}+\frac{(h\pi)^5}{5!}-\cdots\right]$
> $=\pi+\frac{1}{4}c_2h^2+\frac{1}{16}c_4h^4+\frac{1}{64}c_6h^6+\cdots$
> 用它们作为 $\pi$ 的近似值, 误差都是 $O(h^2)$ 量级的
>
> 现在将这两个近似值的程度不够理想的近似值按以下方式组合
> $\tilde{S}(h)$
> $=\frac{4S\left(\frac{h}{2}\right)-S(h)}{4-1}$
> $=S\left(\frac{h}{2}\right)+\frac{S\left(\frac{h}{2}\right)-S(h)}{3}$
>
> 那么通过简单的计算就可以知道
> $\tilde{S}(h)=\pi+d_4h^4+d_6h^6+\cdots$
> $h^2$ 项被消掉了, 也就是说, 用 $\tilde{S}(h)$ 近似表示
> $\pi$, 其精度可以大大提高
>
> 我国三国时的著名数学家刘徽曾对半径为 10 的圆算出
> $100\cdot S\left(\frac{1}{96}\right)$
> $=313\frac{584}{625},\quad100\cdot S\left(\frac{1}{192}\right)$
> $=314\frac{64}{625}$
>
> 接着他"以一百九十三觚之幂以率消息", "当取此分寸之三十六", 用现在的话来说, 即以
> $\frac{36}{625}$ 加到
> $100\cdot S\left(\frac{1}{192}\right)$ 上去,
> 便得到了当时最精确的圆周率
> $\pi\approx\frac{1}{100}\left(314+\frac{64}{625}+\frac{36}{625}\right)=3.1416$
>
> 后人发现, 他用的增量 $\frac{36}{625}$ 与
> $\tilde{S}(h)$ 表达式中对
> $S\left(\frac{h}{2}\right)$ 的修正量
>
> $\frac{S\left(\frac{h}{2}\right)-S(h)}{3}$
> $=\frac{314\frac{64}{625}-313\frac{584}{625}}{3}$
> $=\frac{35}{625}$
> 相当接近, 因此有理由认为, 他在当时已经掌握了某种与外推方法类似的计算技术

> 例5-40: 证明 $e$ 是无理数
> 证明: 用反证法, 假设 $e$ 是有理数, 那么显而易见, 一定存在充分大的自然数
> $m$, 使得 $(m!)e$ 是正整数
>
> 在 $e^x$ 的 Taylor 公式
> $e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots+\frac{x^n}{n!}+\frac{e^{\theta x}}{(n+1)!}x^{n+1},\quad\theta\in(0,1)$
> 中, 将 $n$ 取为 $m$, 并令 $x=1$
> 由于 $e^x$ 在整个实数范围都满足带 Lagrange 余项的 Taylor 公式,
> 即有
> $e=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{m!}+\frac{e^\theta}{(m+1)!},\quad\theta\in(0,1)$
>
> 两边同乘上 $m!$, 便得到
> $(m!)e=(m!)\left[1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{m!}\right]+\frac{(m!)e^\theta}{(m+1)!}$
> 即
> $(m!)\left\{e-\left[1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{m!}\right]\right\}=\frac{e^\theta}{m+1}$
>
> 按假设, 等式的左端是正整数
> 但由于 $e^x$ 是单调增加函数, 而 $\theta\in(0,1)$, 因此
> $1<e^\theta<3$
> 代入上式的右端, 就得到估计式
> $\frac{1}{m+1}<\frac{e^\theta}{m+1}<\frac{3}{m+1}$
>
> 于是, 对于任意正整数 $m\geq2$, 都有
> $\frac{e^\theta}{m+1}\in(0,1)$, 也就是说,
> 上述等式的右端绝不可能是正整数, 这样就导出了矛盾
> 所以假设 $e$ 是有理数不成立, 即 $e$ 是无理数


## 极值问题

驻点: 使 $f'(x)=0$ 的点
$f(x)$ 的全部极值点必在使 $f'(x)=0$ 和使 $f'(x)$ 不存在的点之中
因此可以求出 $f(x)$ 的驻点(即使 $f'(x)=0$ 的点)与使
$f'(x)$ 不存在的点, 再进行判别

极值点判定定理: 设函数 $f(x)$ 在 $x_0$ 点的某一邻域中有定义, 且
$f(x)$ 在 $x_0$ 点连续
1. 设存在 $\delta>0$, 使得 $f(x)$ 在
$(x_0-\delta,x_0)$ 与 $(x_0,x_0+\delta)$ 上可导

   1.1 若在 $(x_0-\delta,x_0)$ 上有 $f'(x)\geq0$, 在
   $(x_0,x_0+\delta)$ 上有 $f'(x)\leq0$, 则 $x_0$ 是
   $f(x)$ 的极大值点

   1.2 若在 $(x_0-\delta,x_0)$ 上有 $f'(x)\leq0$, 在
   $(x_0,x_0+\delta)$ 上有 $f'(x)\geq0$, 则 $x_0$ 是
   $f(x)$ 的极小值点

   1.3 若 $f'(x)$ 在 $(x_0-\delta,x_0)$ 与
   $(x_0,x_0+\delta)$ 上同号, 则 $x_0$ 不是 $f(x)$ 的极值点

2. 设 $f'(x_0)=0$, 且 $f(x)$ 在 $x_0$ 点二阶可导
   2.1 若 $f''(x_0)<0$, 则 $x_0$ 是 $f(x)$ 的极大值点

   2.2 若 $f''(x_0)>0$, 则 $x_0$ 是 $f(x)$ 的极小值点
   2.3 若 $f''(x_0)=0$, 则 $x_0$ 可能是 $f(x)$ 的极值点,
   也可能不是 $f(x)$ 的极值点

证明: (1) 的结论显然, 只证 (2)

因为 $f'(x_0)=0$, 由 Taylor 公式
$f(x)$
$=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+o((x-x_0)^2)$
$=f(x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+o((x-x_0)^2)$

得到
$\frac{f(x)-f(x_0)}{(x-x_0)^2}=\frac{1}{2}f''(x_0)+\frac{o((x-x_0)^2)}{(x-x_0)^2}$

因为当 $x\to x_0$ 时上式右侧第二项趋于 0, 所以当
$f''(x_0)<0$ 时, 由极限的性质可知在 $x_0$ 点附近成立
$\frac{f(x)-f(x_0)}{(x-x_0)^2}<0$
所以 $f(x)<f(x_0)$, 从而 $f(x)$ 在 $x_0$ 取极大值,
同样可讨论 $f''(x_0)>0$ 的情况
[关于 (2) 中 2.3, 可分别考察函数 $y=x^4$, $y=-x^4$ 和
$y=x^3$: $x=0$ 是 $y=x^4$ 的极小值点, 是
$y=-x^4$ 的极大值点, 而不是 $y=x^3$ 的极值点, 但都满足
$y'(0)=0$ 和 $y''(0)=0$]

------

> 例5-41: 求函数 $f(x)=\sqrt[3]{(2x-x^2)^2}$ 的极值
> 解: 函数 $f(x)$ 的定义域为 $(-\infty,+\infty)$, 由
> $f'(x)=\frac{4}{3}(2x-x^2)^{-\frac{1}{3}}(1-x)$
> 可知 $f(x)$ 的驻点为 $x=1$, 使得 $f'(x)$ 不存在的点为
> $x=0$ 和 $x=2$
>
> 1. 当 $-\infty<x<0$ 时, $f'(x)<0$
> 2. 当 $0<x<1$ 时, $f'(x)>0$
> 3. 当 $1<x<2$ 时, $f'(x)<0$
> 4. 当 $2<x<+\infty$ 时, $f'(x)>0$
>
> 由极值点判定定理 1 的结论知 $f(0)=0$ 是极小值, $f(1)=1$ 是极大值,
> $f(2)=0$ 是极小值

> 例5-42: 求函数 $f(x)=(x^2-1)^3+1$ 的极值
> 解: 函数 $f(x)$ 的定义域为 $(-\infty,+\infty)$, 计算得
> $f'(x)=6x(x^2-1)^2,\quad f''(x)=6(x^2-1)(5x^2-1)$
> 显然 $f(x)$ 的驻点为 $x=0$, $x=1$ 和 $x=-1$
>
> 由于 $f''(0)=6>0$, 所以由极值点判定定理 2 的结论知
> $f(0)=0$ 是极小值
>
> 由于 $f'(\pm1)=0$, 不能用极值点判定定理 2 的结论, 但由于
> $f'(x)$ 在 $x=1$ 与 $x=-1$ 的左, 右侧保持同号,
> 由极值点判定定理 1 的结论, 知 $f(1)$ 和 $f(-1)$ 都不是函数
> $f(x)$ 的极值


## 最值问题

最值: 函数的最大值与最小值的统称

最大值点(或最小值点): 使函数取到最大值(或最小值)的点, 也称为最值点

函数的极大值与极小值反映的是函数的一种局部性质,
而函数的最大值与最小值反映的是函数在某一范围内的一种整体性质
对于定义于闭区间 $[a,b]$ 上的函数 $f(x)$ 来说, 区间的两个端点
$a$ 与 $b$ 也有可能成为它的最值点
因此只要按照极值问题中所述的方法, 找出所有驻点与使 $f'(x)$ 不存在的点,
再加上区间的端点, 从中找出使函数取最大值或最小值的点就可以了

------

> 例5-43: 求函数 $f(x)=\sqrt[3]{(2x-x^2)^2}$ 在区间
> $[-1,4]$ 上的最大值与最小值
>
> 解: 由例5-41, 已知函数 $f(x)$ 在区间 $[-1,4]$ 上的极大值点为
> $x=1$, 极大值为 $f(1)=1$, 极小值点为 $x=0$ 与 $x=2$,
> 两个极小值都为 0
>
> 为了求最大值与最小值, 还须加上函数在区间端点的值
> $f(-1)=\sqrt[3]{9}$ 与 $f(4)=4$
> 对这些值进行比较, 就得到函数 $f(x)$ 在区间 $[-1,4]$ 上的最大值点为
> $x=4$, 最大值为 $f(4)=4$, 最小值点为 $x=0$ 与 $x=2$,
> 最小值为 0

> 例5-44: 用铝合金制造容积固定的圆柱形罐头, 罐身(侧面和底部)用整块材料拉制而成,
> 顶盖是另装上去的, 设顶盖的厚度是罐身厚度的三倍,
> 问如何确定它的底面半径和高才能使得用料最省
>
> 解: 设罐身的厚度为 $\delta$, 则顶盖的厚度是 $3\delta$
> 记罐头的容积为 $V$, 底面半径为 $r$, 则高为
> $h=\frac{V}{\pi r^2}$, 于是罐身的用料为
> $U_1(r)=\delta(\pi r^2+2\pi rh)=\delta\left(\pi r^2+\frac{2V}{r}\right)$
> 顶盖的用料为 $U_2(r)=3\delta\pi r^2$
>
> 因此问题化为求函数
> $U(r)=U_1(r)+U_2(r)=\delta\left(4\pi r^2+\frac{2V}{r}\right),\quad r\in(0,+\infty)$
> 的最小值
>
> 对 $U(r)$ 求导,
> $U'(r)=2\delta\left(4\pi r-\frac{V}{r^2}\right)$
> 因此 $U'(r)$ 只有唯一的零点
> $r_0=\sqrt[3]{\frac{V}{4\pi}}$
>
> 由于
> $U''(r)=4\delta\left(2\pi+\frac{2V}{r^3}\right)>0,\quad r\in(0,+\infty)$
> 所以 $r_0$ 是 $U(r)$ 的极小值点
>
> 这时, 相应的高为
> $h_0=\frac{V}{\pi r_0^2}=\frac{4\pi r_0^3}{\pi r_0^2}=4r_0$
> 也就是说, 当罐头的高为底面直径的 2 倍时用料最省
[用同样的方法可以推出, 若圆柱形的有盖容器是用厚薄相同的材料制成的,
那么当它的底面直径和高相等的时候用料最省]

------

> 例5-45: 设一辆汽车在平原上的行驶速度为 $v_1$, 在草原上的行驶速度为
> $v_2$, 现要求它以最短的时间从平原上的 $A$ 点到达草原上的 $B$ 点,
> 问应该怎么走
> 解: 显然, 在同一种地形上, 汽车应沿直线行进, 所以它从 $A$ 到
> $B$ 的运动轨迹应是由两条直线段组成的折线
>
> 设汽车的行驶路径中, 平原段与草原段的水平距离分别为 $x$ 与 $l-x$,
> 垂直落差分别为 $h_1$ 与 $h_2$, 那么它的整个行驶时间应为
> $T(x)=\frac{\sqrt{h_1^2+x^2}}{v_1}+\frac{\sqrt{h_2^2+(l-x)^2}}{v_2}$
> 由
> $T'(x)=\frac{x}{v_1\sqrt{h_1^2+x^2}}-\frac{l-x}{v_2\sqrt{h_2^2+(l-x)^2}}$
> 可知 $T'(0)<0$, $T'(l)>0$
>
> 由于
> $T''(x)=\frac{h_1^2}{v_1(h_1^2+x^2)^{\frac{3}{2}}}+\frac{h_2^2}{v_2(h_2^2+(l-x)^2)^{\frac{3}{2}}}>0$
> 可知存在唯一的 $x_0\in(0,l)$, 使得 $T'(x_0)=0$
>
> 因此 $x_0$ 是 $T(x)$ 的唯一的极小值点, 也就是它的最小值点, 这时得到关系式
> $\frac{x_0}{v_1\sqrt{h_1^2+x_0^2}}=\frac{l-x_0}{v_2\sqrt{h_2^2+(l-x_0)^2}}$
>
> 由于光线在传播过程中所花的时间总是最短的, 即光线总是走"捷径"的,
> 所以光线的传播问题在本质上与本题是相同的
> 将本题中汽车的行驶换成光线的传播, 将平原和草原换成光线传播过程中的两种不同的介质,
> 这样就得到了光学中著名的折射定律
> $\frac{\sin\theta_1}{v_1}=\frac{\sin\theta_2}{v_2}$
最值问题在社会科学的许多方面, 尤其是经济活动分析中得到了广泛的应用

------

> 例5-46: 对产品从生产到销售的过程进行经济核算时, 至少要涉及三个方面的问题:
> 成本, 收益和利润
>
> 1. 设产量为 $Q$, 则总成本 $C(Q)$ 一般可以表示成两部分的和
>    $C(Q)=f+v(Q)\cdot Q$
>    这里 $f>0$ 为固定成本(如厂房和设备的折旧, 工作人员的工资, 财产保险费等),
> 一般可以认为与产量的大小无关
>
>    而 $v(Q)\cdot Q$ 称为可变成本(如原材料, 能源等),
> $v(Q)$ 是一个正值函数, 表示在总共生产 $Q$ 件产品的情况下,
> 每生产一件的可变成本, 最简单的情形是 $v(Q)=v=\text{常数}$
>    $C(Q)$ 的导数 $C'(Q)$ 称为边际成本, 其经济学意义是在总共生产
> $Q$ 件产品的情况下, 生产第 $Q$ 件产品的成本
>
> 2. 总收益 $E(Q)=p(Q)\cdot Q$, 即是指把
> $Q$ 件产品销售出去后得到的收入, 这里 $p(Q)$ 称为价格函数, 表示在总共生产
> $Q$ 件产品的情况下, 每件产品的销售价格
>    一般来说, 生产量越大, 每件产品的价格就越便宜, 因此 $p(Q)$ 是
> $Q$ 的单调减少函数
>    $E(Q)$ 的导数 $E'(Q)$ 相应地称为边际收益
>
> 3. 总收益减去总成本便是总利润, 将利润函数记为 $P(Q)$, 则
> $P(Q)=E(Q)-C(Q)$
>
>    当 $E(Q)$ 和 $C(Q)$ 二阶可导时, 由极值点判定定理,
> 就可以得到经济学中的"最大利润原理": 当且仅当边际成本与边际收益相等,
> 并且边际成本的变化率大于边际收益的变化率时, 可取得最大利润
>    这里的第一个条件即为 $P'(Q)=E'(Q)-C'(Q)=0$
>    而第二个条件可表示为 $P''(Q)=E''(Q)-C''(Q)<0$
>
> 例如, 某产品的价格
> $p(Q)=a-bQ\left(a,b>0,Q<\frac{a}{b}\right)$,
> 成本 $C(Q)=f+vQ$, 于是利润
> $P(Q)=E(Q)-C(Q)=-bQ^2+(a-v)Q-f$
>
> 要使得整个生产经营不亏本, 显然在定价时须保证 $a-v>0$
> 容易算出, 当产量 $Q_0=\frac{a-v}{2b}$ 时有
> $P'(Q_0)=0$ 和 $P''(Q_0)<0$, 这时所获取的利润为最大


## 数学建模

数学建模: 用数学技术去解决实际问题时, 首先将所考虑的现实问题通过"去芜存菁,
去伪存真"的深入分析和研究, 用数学工具将它归结为一个相应的数学问题的过程
所得到的数学问题称为数学模型

------

> 例5-47: Malthus 人口模型
> 设 $p(t)$ 是某地区的人口数量函数, 由定义, 该地区在单位时间中的人口增长率,
> 即人口增长速率应为人口数量函数的导数 $p'(t)$
>
> 显然, 某一时刻的人口数量越多, 在单位时间中的人口增长数也就越多
> 通过对当时的资料分析, Malthus 假定这两者成比例关系, 设比例系数为
> $\lambda$(可以由已有的资料定出),
> 于是他在 1798 年提出了人类历史上的第一个人口模型
> $\begin{cases}p'(t)=\lambda p(t),\\ p(t_0)=p_0\end{cases}$
>
> 这里, 像
> $p'(t)=\lambda p(t)$ 这种含有未知函数的导数(或微分)的方程称为微分方程,
> 而 $p(t_0)=p_0$ 称为微分方程的初值条件, 代表在某个给定的
> $t_0$ 时刻的实际人口数
>
> 将 $p'(t)=\lambda p(t)$ 写成微分形式
> $\frac{\mathrm{d}p}{p}=\lambda\,\mathrm{d}t$
> 把它看成是由某个隐函数 $f(p)=g(t)$ 两边求微分的结果,
> 由一阶微分的形式不变性和基本初等函数的微分表, 即得
>
> $f(p)=\ln p+C,\quad g(t)=\lambda t+C$
> $C$ 是任意给定的常数, 于是 $\ln p=\lambda t+C$, 也就是
> $p=C_1e^{\lambda t}$, 其中 $C_1=e^C$
>
> 令 $t=t_0$ 并利用初值条件 $p(t_0)=p_0$, 可以定出
> $C_1=p_0e^{-\lambda t_0}$
> 最终得到人口数量函数 $p(t)=p_0e^{\lambda(t-t_0)}$
> 以上求未知函数 $p(t)$ 的过程称为解微分方程, 其结果
> $p(t)=p_0e^{\lambda(t-t_0)}$ 称为该微分方程的满足初值条件的解

> 例5-48: 在供水, 化工生产等过程中, 都有一个对液体进行过滤, 除去渣滓的问题
> 现以过滤式净水器的使用为例, 来建立相应的数学模型
> 要对液体进行过滤, 首先要设置一个由过滤物质组成的过滤层(称为滤芯)
> 在过滤的过程中, 水中的杂质沉积在过滤层上, 也成为过滤层的一部分
>
> 假设杂质在水中的含量和进水的压力都是常数, 那么杂质沉积的厚度与累积的总滤出流量
> $Q(t)$ 成正比
> 同时, 流速的减少与杂质沉积的厚度也成正比
>
> 若设初始时刻的流速为 $q_0$, 由导数的意义即知 $t$ 时刻的流速应当是
> $Q'(t)$, 从而流速的减少量为 $q_0-Q'(t)$
> 由上所述, 它应与总滤出流量 $Q(t)$ 成正比, 这样, 就得到了它的数学模型为
> $\begin{cases}Q'(t)=q_0-\lambda Q(t),\\ Q(0)=0\end{cases}$
>
> 作代换 $Q_1(t)=q_0-\lambda Q(t)$, 便有
> $\begin{cases}Q_1'(t)=-\lambda Q_1(t),\\ Q_1(0)=q_0\end{cases}$
>
> 这是关于 $Q_1(t)$ 的微分方程, 它与例5-47 所得的微分方程的形式完全相同
> 采用与例5-47 类似的方法, 可以求出
> $Q_1(t)=q_0e^{-\lambda t}$
> 即得到累积的总滤出流量为
> $Q(t)=\frac{1}{\lambda}(q_0-Q_1(t))=\frac{q_0}{\lambda}(1-e^{-\lambda t})$
>
> 因为
> $\lim\limits_{t\to\infty}Q(t)=\frac{q_0}{\lambda}$ 及
> $\lim\limits_{t\to\infty}Q'(t)=0$
>
> 所以我们可以知道, 在定压的过滤过程中, 并不是想滤多少就可以不受限制地滤多少,
> 其流出的总量是有上限 $\frac{q_0}{\lambda}$ 的
> 在流量接近这个上限的时候, 其流速将趋近于零, 也就是说, 此时杂质已沉积得过厚,
> 需要清洗或更换滤芯了


## 函数作图

函数作图的一般过程可分为以下几个步骤
1. 考察函数 $f(x)$ 的定义域及其在定义域内的连续性, 找出函数的不连续点,
并以这些点作为分点, 将定义域分成若干个区间, 使函数在每个区间上连续

2. 计算 $f'(x)$, 找出 $f(x)$ 的驻点与导数不存在的点, 从而求出
$f(x)$ 的极值点与极值, 并以这些点为分点, 对区间进行再划分,
使函数在每个区间上保持单调

3. 计算 $f''(x)$, 找出所有使 $f''(x)=0$ 的点与使
$f''(x)$ 不存在的点, 从而求出 $f(x)$ 的拐点, 并以这些点为分点,
继续对区间进行再划分, 使函数在每个区间上保持固定的凸性

4. 对上述三个步骤所得到的结果列出表格,
在表格中标出函数在每个分点上的函数值(如果有定义的话), 以及函数在每个区间上的单调性与凸性

5. 求出曲线 $y=f(x)$ 的渐近线, 包括水平渐近线, 垂直渐近线和斜渐近线
通过上述步骤, 我们就可以在平面坐标系上标出函数曲线的一些特殊点, 如极值点与拐点等,
再根据曲线的凸性与渐近线的位置, 就可作出函数 $y=f(x)$ 的图像

在作图之前, 应该先考察函数的几何性质如奇偶性, 周期性等, 如
$f(x)$ 是奇函数或偶函数, 那么只要画出一半图形, 而另一半可通过对称画出;
对于周期函数, 只要画出一个周期的图形就可以了

------

> 例5-49: 作出函数
> $y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ 的图像
> 解: 因为
> $f(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ 是定义于整个实数域上的偶函数,
> 我们只要考察 $x\geq0$ 就可以了
>
> 求
> $f(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ 的一阶导数和二阶导数,
> 有
> $f'(x)=-\frac{1}{\sqrt{2\pi}}xe^{-\frac{x^2}{2}}$ 和
> $f''(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}(x^2-1)$
>
> $f(x)$ 的可能极值点为 $f'(x)$ 的零点 $x=0$, 可能的拐点的横坐标为
> $f''(x)$ 的零点 $x=1$
> 经检验, $f'(x)$ 在 $x=0$ 的右侧和左侧的符号分别为负和正, 所以
> $x=0$ 是 $f(x)$ 的极大值点; $f''(x)$ 在
> $x=1$ 的右侧和左侧的符号分别为正和负, 所以 $(1,f(1))$ 是曲线
> $y=f(x)$ 的拐点
>
> 根据上述结果即可列出下面的表格
| $x$ | $0$ | $(0,1)$ | $1$ | $(1,+\infty)$ |
| --- | --- | --- | --- | --- |
| $f'(x)$ | $0$ | $-$ | $-$ | $-$ |
| $f''(x)$ | $-$ | $-$ | $0$ | $+$ |
| $f(x)$ | 极大值 $\frac{1}{\sqrt{2\pi}}$ | $\searrow$ | 拐点 $\left(1,\frac{1}{\sqrt{2\pi e}}\right)$ | $\searrow$ |
> 当 $x\to\infty$ 时,
> $y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}\to0$,
> 因此 $y=0$ 即 $x$ 轴是 $y=f(x)$ 的水平渐近线, 容易看出, 曲线
> $y=f(x)$ 不再有其他的渐近线
>
> 根据这些信息, 便不难作出函数 $y=f(x)$ 在右半平面的图像, 然后利用对称性,
> 就可以作出函数的整个图像了

图5-5: 函数

$y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ 的图像

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206304.png =500x)

[以后学习概率论时会知道,
$y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ 是一个非常重要的函数]

------

> 例5-50: 作出函数 $y=\frac{(x-1)^2}{3(x+1)}$ 的图像
> 解: 由于函数 $f(x)=\frac{(x-1)^2}{3(x+1)}$ 的定义域为
> $(-\infty,-1)\cup(-1,+\infty)$,
> 可知函数的图像包含两条曲线, 它们被直线 $x=-1$ 左右分开
>
> 先对 $f(x)$ 求导
> $f'(x)=\frac{(2x-2)(x+1)-(x-1)^2}{3(x+1)^2}=\frac{(x+3)(x-1)}{3(x+1)^2}$
> $f'(x)$ 有零点 $x=1$ 和 $x=-3$
> 由于 $f'(x)$ 在 $x=-3$ 的右侧和左侧的符号分别为负和正, 而在
> $x=1$ 的右侧和左侧的符号分别为正和负, 所以 $x=-3$ 是
> $f(x)$ 的极大值点, $x=1$ 是 $f(x)$ 的极小值点
>
> 再求 $f(x)$ 的二阶导数 $f''(x)=\frac{8}{3(x+1)^3}$
> 因为 $f''(x)$ 在定义域中没有零点, 所以曲线上没有拐点
> 根据上述结果即可列出下面的表格
| $x$ | $(-\infty,-3)$ | $-3$ | $(-3,-1)$ | $-1$ | $(-1,1)$ | $1$ | $(1,+\infty)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f'(x)$ | $+$ | $0$ | $-$ | 无定义 | $-$ | $0$ | $+$ |
| $f''(x)$ | $-$ | $-$ | $-$ | 无定义 | $+$ | $+$ | $+$ |
| $f(x)$ | $\nearrow$ | 极大值 $\frac{8}{3}$ | $\searrow$ | 无定义 | $\searrow$ | 极小值 $0$ | $\nearrow$ |
> 由例5-36, $y=\frac{(x-1)^2}{3(x+1)}$ 的斜渐近线方程为
> $y=\frac{x}{3}-1$
>
> 又因为
> $\lim\limits_{x\to-1+}\frac{(x-1)^2}{3(x+1)}=+\infty,\quad\lim\limits_{x\to-1-}\frac{(x-1)^2}{3(x+1)}=-\infty$
> 所以 $x=-1$ 是它的垂直渐近线, 且根据上面两个极限值, 可以知道曲线在
> $x=-1$ 的左右两侧以怎样的方式趋近于渐近线
>
> 根据这些信息, 再求出若干个特殊点上 $f(x)$ 的函数值, 就不难作出函数
> $y=f(x)$ 的图形了

图5-6: 函数 $y=\frac{(x-1)^2}{3(x+1)}$ 的图像

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206305.png =500x)

> 例5-51: 作出函数 $y=\sqrt[3]{x^3-x^2+x+1}$ 的图像
> 解: 函数
> $f(x)=\sqrt[3]{x^3-x^2+x+1}=\sqrt[3]{(x-1)^2\cdot(x+1)}$ 的定义域为
> $(-\infty,+\infty)$
>
> 先对 $f(x)$ 求导
> $f'(x)$
> $=\frac{1}{3}\cdot\frac{2(x+1)+(x-1)}{\sqrt[3]{x-1}\cdot\sqrt[3]{(x+1)^2}}$
> $=\frac{x+\frac{1}{3}}{\sqrt[3]{x-1}\cdot\sqrt[3]{(x+1)^2}}$
>
> $f'(x)$ 有零点 $x=-\frac{1}{3}$, 并且在 $x=\pm1$ 处
> $f'(x)$ 不存在
> 经检验 $f'(x)$ 在这些点左右两侧的符号, 即可知道
> $x=-1$ 不是函数的极值点, $x=-\frac{1}{3}$ 是函数的极大值点,
> $x=1$ 是函数的极小值点
>
> 再对 $f(x)$ 求二阶导数
> $f''(x)=\frac{-8}{9\cdot\sqrt[3]{(x-1)^4}\cdot\sqrt[3]{(x+1)^5}}$
> 即知 $f(x)$ 的二阶导数没有零点, 但在 $x=\pm1$ 处
> $f''(x)$ 不存在
>
> 由于 $f''(x)$ 在 $x=-1$ 的两侧符号相反, 而在
> $x=1$ 的两侧符号相同, 所以 $(-1,0)$ 是曲线的拐点, 而
> $(1,0)$ 不是曲线的拐点
> 根据上述结果即可列出下面的表格
| $x$ | $(-\infty,-1)$ | $-1$ | $\left(-1,-\frac{1}{3}\right)$ | $-\frac{1}{3}$ | $\left(-\frac{1}{3},1\right)$ | $1$ | $(1,\infty)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f'(x)$ | $+$ | 不存在 | $+$ | $0$ | $-$ | 不存在 | $+$ |
| $f''(x)$ | $+$ | 不存在 | $-$ | $-$ | $-$ | 不存在 | $-$ |
| $f(x)$ | $\nearrow$ | 拐点 $(-1,0)$ | $\nearrow$ | 极大值 $\frac{2}{3}\sqrt[3]{4}$ | $\searrow$ | 极小值 $0$ | $\nearrow$ |
> 由例5-37, $y=\sqrt[3]{x^3-x^2+x+1}$ 的渐近线方程为
> $y=x-\frac{1}{3}$
> 根据这些信息, 再求出若干个特殊点上 $f(x)$ 的函数值, 就不难作出函数
> $y=f(x)$ 的图形了

图5-7: 函数 $y=\sqrt[3]{x^3-x^2+x+1}$ 的图像

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206306.png =500x)


## 解析方法和数值方法

求方程 $f(x)=0$ 的解(或根), 就是要寻找一个数 $x^*$, 使得满足
$f(x^*)=0$

解析方法(公式法): 将方程的解表达为方程的系数的函数形式
只要把待求解的方程的系数代入表达式, 就可以求出方程的解
在不考虑运算中的四舍五入所产生的误差时, 解析方法所得到的解是精确的, 称为解析解或精确解
[由于真正运算时不可能不产生误差, 因此从求解实际问题来说, 不存在真正的精确方法]

例如一元二次方程 $ax^2+bx+c=0\ (a\neq0)$ 的两个解为
$x_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
除了简单的三角方程, 对数方程和指数方程等情况之外,
能精确求解的方程与实际问题需要求解的方程相比, 只能说是九牛之一毛

数值方法: 一种近似求解的方法, 设法构造一个可实际计算的过程
通过这个过程产生方程的精确解的一系列近似值,
在一定条件下这些近似值理论上将收敛于方程的精确解, 称为数值解或近似解


## 二分法

二分法: 最简单的数值求解方法,
计算过程与用闭区间套定理证明闭区间上连续函数的零点存在定理的过程差不多

设 $f(x)$ 在 $[a,b]$ 中连续, 且成立 $f(a)\cdot f(b)<0$
那么在 $[a,b]$ 至少存在着 $f(x)$ 的一个解 $x^*$
假定 $f(x)$ 在 $[a,b]$ 中只有这个解, 希望求出它的近似值
$\bar{x}$, 满足 $|\bar{x}-x^*|\leq\varepsilon_0$
这里 $\varepsilon_0$ 是预先给定的精度要求, 如 $10^{-8}$,
$10^{-10}$ 等

计算步骤如下
1. 记 $[a_1,b_1]=[a,b]$, 取 $x_1$ 为
$[a_1,b_1]$ 的中点, 即 $x_1=\frac{a_1+b_1}{2}$

2. 计算 $f(x_1)$: 若 $f(x_1)=0$, 则 $x_1$ 即为方程的解
$x^*$, 取 $\bar{x}=x_1$, 计算结束

3. 否则, 按如下规则得到区间 $[a_2,b_2]$
   3.1 若 $f(x_1)\cdot f(b_1)<0$, 此时 $f(x)$ 的解在
   $[x_1,b_1]$ 中, 取 $a_2=x_1,b_2=b_1$

   3.2 若 $f(x_1)\cdot f(b_1)>0$, 此时 $f(x)$ 的解在
   $[a_1,x_1]$ 中, 取 $a_2=a_1,b_2=x_1$
   易知 $x^*\in[a_2,b_2]$, 且 $[a_2,b_2]$ 的长度是
   $[a_1,b_1]$ 的一半

4. 取 $x_2$ 为 $[a_2,b_2]$ 的中点
5. 类似地, 若 $x_2$ 是方程的解 $x^*$, 计算结束; 否则可以得到
$[a_3,b_3]$
6. 重复上述过程

假设执行过程中没有发生 $x_k$ 恰好等于 $x^*$ 的情况, 由于对任何 $k$ 都有
$b_k-a_k=\frac{b-a}{2^{k-1}}$

因此 $[a_k,b_k]$ 的中点 $x_k$ 与精确解 $x^*$ 的距离不会超过
$[a_k,b_k]$ 长度的一半, 即
$|x_k-x^*|\leq\frac{b_k-a_k}{2}=\frac{b-a}{2^k}$

所以, 当
$k=\left[\log_2\frac{b-a}{\varepsilon_0}\right]$ 时,
必有
$|x_k-x^*|\leq\frac{b-a}{2^k}\leq\varepsilon_0$
于是 $\bar{x}=x_k$ 便是符合精度要求的近似解


## Newton 迭代法

迭代法: 将方程 $f(x)=0$ 化为等价形式 $x=F(x)$, 其中
$F(x)$ 称为迭代函数

取一个适当的初始值 $x_0$, 按
$x_{k+1}=F(x_k)\ (k=0,1,2,\cdots)$ 产生序列
$\{x_k\}$, 这个过程称为迭代
在理论上成立 $x_k\to x^*\ (k\to\infty)$,
因此只要在迭代过程中选取某个合适的 $x_k$ 作为 $\bar{x}$,
就得到原方程的近似解

实际计算时, 采用比较相邻两次的迭代值是否满足
$|x_{k+1}-x_k|\leq\varepsilon_0$ 来决定迭代是否进行下去

Newton 迭代法(简称 Newton 法): 取迭代函数
$F(x)=x-\frac{f(x)}{f'(x)}$, 得到迭代公式
$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)},\quad k=0,1,2,\cdots$

牛顿法的几何意义: 曲线 $y=f(x)$ 在 $x=x_k$ 处的切线方程为
$y=f'(x_k)(x-x_k)+f(x_k)$
它与 $x$ 轴的交点的横坐标为
$x=x_k-\frac{f(x_k)}{f'(x_k)}=x_{k+1}$
因此 Newton 法实质上是通过一系列的切线与 $x$ 轴的交点的横坐标, 来逼近曲线与
$x$ 轴的交点的横坐标, 所以 Newton 迭代法也叫 Newton 切线法

Newton 迭代法收敛定理: 设 $f(x)$ 在 $[a,b]$ 中有二阶连续导数,
且满足条件
1. $f(a)\cdot f(b)<0$

2. $f'(x)$ 在 $(a,b)$ 保号

3. $f''(x)$ 在 $(a,b)$ 保号

取 $x_0$ 是 $a$ 和 $b$ 中满足
$f(x_0)\cdot f''(x_0)>0$ 的那一个点, 则以
$x_0$ 为初值的 Newton 迭代过程
$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)},\quad k=0,1,2,\cdots$
产生的序列 $\{x_k\}$ 单调收敛于方程 $f(x)=0$ 在
$[a,b]$ 中的唯一解

图5-8: Newton 切线法

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206307.png =400x)

[条件 1 保证了 $f(x)$ 在 $(a,b)$ 有解; 条件 2 表明
$f(x)$ 在 $[a,b]$ 严格单调, 因此 $f(x)$ 在
$(a,b)$ 中的解是唯一的; 而条件 3 表示 $f(x)$ 在
$[a,b]$ 中保持固定的凸性, 这保证了每一个 $x_k$ 都在同一方向上比
$x_k$ 更靠近 $x^*$, 因此 $\{x_k\}$ 是一个单调有界数列,
它必有极限, 这个极限当然就是 $x^*$]

------

> 例5-52: 解方程 $\ln x=\sin x$
> 解: 记 $f(x)=\ln x-\sin x$, 考虑区间
> $\left[\frac{\pi}{2},e\right]$, 则有
> $f\left(\frac{\pi}{2}\right)=\ln\frac{\pi}{2}-\sin\frac{\pi}{2}<0,\quad f(e)=\ln e-\sin e>0$
>
> 而
> $f'(x)=\frac{1}{x}-\cos x>0,\quad x\in\left[\frac{\pi}{2},e\right]$
> $f''(x)=\sin x-\frac{1}{x^2}>\sin e-\frac{4}{\pi^2}>0,\quad x\in\left[\frac{\pi}{2},e\right]$
> 所以符合 Newton 迭代法收敛定理的全部条件
> 因为 $f(e)f''(e)>0$, 所以初值取为 $x_0=e$, 计算结果如下
| $k$ | $x_k$ | $|x_k-x^*|$ |
| --- | --- | --- |
| $1$ | 2.257 815 620 636 622 89 | $3.87\times10^{-2}$ |
| $2$ | 2.219 512 490 173 004 78 | $4.05\times10^{-4}$ |
| $3$ | 2.219 107 195 173 873 23 | $4.63\times10^{-8}$ |
| $4$ | 2.219 107 148 913 746 83 | $8.88\times10^{-16}$ |
> 最后, 取
> $\bar{x}=x_4=2.219\,107\,148\,913\,746\,83$ 作为
> $x^*$ 的近似值
从计算结果可以发现, 每迭代一次, 误差中的指数大致增加了一倍, 这是当 $x_k$ 与
$x^*$ 很接近时, Newton 法的一个重要性质

由 Taylor 公式容易导出
$x^*-x_{k+1}=\frac{f''(\xi)}{f'(x_k)}\cdot\frac{(x^*-x_k)^2}{2}$
这里 $\xi$ 在 $x_k$ 与 $x^*$ 之间, 因此

$\lim\limits_{k\to\infty}\frac{|x^*-x_{k+1}|}{|x^*-x_k|^2}$
$=\frac{1}{2}\left|\frac{f''(x^*)}{f'(x^*)}\right|$
$=C$

所以 Newton 法是一个二次收敛(也叫平方收敛)的迭代方法, 或者说,
Newton 迭代法的收敛速度是二次的

------

> 例5-53: 用 Newton 法求 $\sqrt{A}$, $A>0$ 是一个给定的数
> 解: 显然, 求 $\sqrt{A}$ 等价于求方程 $f(x)=x^2-A=0$ 的解
> $x^*\ (x^*\in R^*)$
>
> 计算机首先自动寻找一个正整数 $n$, 使得 $(n-1)^2<A<n^2$
> 然后取 $x_0=n$, 用 Newton 迭代
> $x_{k+1}=x_k-\frac{x_k^2-A}{2x_k}=\frac{1}{2}\left(x_k+\frac{A}{x_k}\right)\quad(k=0,1,2,\cdots)$
>
> 得到序列 $\{x_k\}$, 可以验证, 在区间
> $[n-1,n]$ 上 Newton 迭代法收敛定理的条件全部满足, 因此
> $x_k\to x^*=\sqrt{A}$
> 以下是 $x_0=3$ 为初值求 $\sqrt{7}$ 的计算结果
| $k$ | $x_k$ | $|x_k-\sqrt{7}|$ |
| --- | --- | --- |
| $1$ | 2.666 666 666 666 666 52 | $2.09\times10^{-2}$ |
| $2$ | 2.654 833 333 333 333 48 | $8.20\times10^{-4}$ |
| $3$ | 2.645 751 312 335 958 17 | $1.27\times10^{-6}$ |
| $4$ | 2.645 751 311 064 590 72 | $<10^{-13}$ |
在计算机上做除法和求 $n$ 次方根 $\sqrt[n]{A}$ 的思路是类似的,
都是先将其转化为方程求解问题, 再用 Newton 法迭代出近似解

------

使用数值方法求解方程时有几点说明
1. Newton 迭代法收敛定理的条件是充分的而不是必要的

   但是条件不满足时迭代确实有可能不收敛, 图中 (a) 为
   $f'(x)\neq0$ 没被破坏, $f(x)$ 在 $[a,b]$ 中有一个极值点;
   (b) 为 $f'(x)\neq0$ 没被破坏, $[a,b]$ 中有
   $y=f(x)$ 的一个拐点
   从中可以看到, 这时迭代序列在两个固定点处无休止地来回跳动, 迭代过程以失败而告终

2. Newton 迭代法是求解函数方程最基本和最重要的方法之一,
它可以推广到由若干个方程构成的方程组的求解上去
   实际求解方程中往往是首选的方法, 但由于迭代函数比较简单, 除了导数特殊复杂的情况之外,
   每做一步迭代所化的运算量是比较小的, 当初值选得好时收敛速度相当快

3. 与 Newton 法相比, 二分法最突出的优点是对求解函数 $f(x)$ 的要求较低
   只要连续就行了, 因此有些性质较差的函数只能用二分法而不能用 Newton 法来求解
   另外, 它每做一步迭代所化的计算量也较小(只需要计算函数值),
   并且可以根据精度的要求事先确定执行的步数
   但它的主要缺点是收敛速度不快

4. 当函数 $f(x)$ 的导函数不太容易计算时, 可以用
$\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}$ 近似代替
$f'(x_k)$, 这时的迭代公式成为
   $\begin{cases}\text{取初值}x_0,x_1,\\ x_{k+1}=x_k-f(x_k)\frac{x_k-x_{k-1}}{f(x_k)-f(x_{k-1})},\quad k=1,2,\cdots.\end{cases}$

   它的几何意义是用过 $(x_{k-1},f(x_{k-1}))$ 和
   $(x_k,f(x_k))$ 的割线代替过 $(x_k,f(x_k))$ 的切线,
   将这条割线与 $x$ 轴的交点的横坐标作为新的近似值 $x_{k+1}$
   因此这个方法也叫割线法或弦截法

   割线法满足
   $\lim\limits_{k\to\infty}\frac{|x^*-x_{k+1}|}{|x^*-x_k|^p}=C$,
   其中 $p=\frac{1+\sqrt{5}}{2}\approx1.618$

   因此收敛速度稍慢于 Newton 法, 但由于它每做一步迭代只需要计算一次函数值,
   运算量小, 且又避免了导数运算, 因而也是一种很常用的数值求解方法
   [在求解由多个方程联立的方程组时更是如此]

图5-9: 割线法(弦截法)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194206308.png =400x)

<script src="/assets/katex/katex.min.js"></script>
<script src="/assets/katex/auto-render.min.js"></script>
<script>renderMathInElement(document.querySelector('.md-content'));</script>
