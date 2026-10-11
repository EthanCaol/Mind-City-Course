


## 定积分的概念和可积条件

定积分的概念来自两类问题

1. 曲边梯形的面积: 设 $f(x)\geq0$ 在 $[a,b]$ 上连续,
   由曲线 $y=f(x)$, 两条直线 $x=a$, $x=b$ 与 $x$ 轴围成的图形
2. 变速直线运动的路程: 设质点以速度 $v(t)$ 作直线运动,
求时间段 $[T_1,T_2]$ 内走过的路程

两类问题都归结为对区间作划分, 在小区间上取近似, 再对和式取极限

------


> 例7-1: 求由抛物线 $y=x^2$, 直线 $x=0$,
> $x=1$ 与 $x$ 轴围成的曲边三角形的面积 $S$
> 用步长 $h=\frac{1}{n}$ 将 $[0,1]$ 分成 $n$ 个等长的小区间,
> 分点为 $x_i=ih\ (i=0,1,2,\cdots,n)$
>
> 先在每个小区间 $[x_{i-1},x_i]$ 上, 构造以 $h$ 为底,
> 以 $f(x_{i-1})=x_{i-1}^2$ 为高的小矩形,
> 面积和为
> $S_n'=\sum_{i=1}^n h\cdot x_{i-1}^2=\frac{1}{n}\sum_{i=1}^n\left(\frac{i-1}{n}\right)^2$
> $=\frac{1}{n^3}\sum_{i=1}^n(i-1)^2$
>
> 再在每个小区间 $[x_{i-1},x_i]$ 上, 构造以 $h$ 为底,
> 以 $f(x_i)=x_i^2$ 为高的小矩形, 面积和为
> $S_n''=\sum_{i=1}^n h\cdot x_i^2=\frac{1}{n}\sum_{i=1}^n\left(\frac{i}{n}\right)^2$
> $=\frac{1}{n^3}\sum_{i=1}^n i^2$
>
> 设曲边三角形的面积为 $S$, 则有 $S_n'\leq S\leq S_n''$
> 由 $\sum_{i=1}^n(i-1)^2=\frac{n(n-1)(2n-1)}{6}$,
> $\sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}{6}$
>
> 得
> $\lim\limits_{n\to\infty}S_n'=\lim\limits_{n\to\infty}\frac{n(n-1)(2n-1)}{6n^3}=\frac{1}{3}$,
> $\lim\limits_{n\to\infty}S_n''=\frac{1}{3}$
> 由夹逼定理, $S=\frac{1}{3}$
>
> 在每个小区间 $[x_{i-1},x_i]$ 上任取 $\xi_i\in[x_{i-1},x_i]$,
> 以 $f(\xi_i)=\xi_i^2$ 为高作小矩形
> 面积和 $\frac{1}{n}\sum_{i=1}^n\xi_i^2$ 仍满足 $S_n'\leq\frac{1}{n}\sum_{i=1}^n\xi_i^2\leq S_n''$,
> 于是 $\lim\limits_{n\to\infty}\frac{1}{n}\sum_{i=1}^n\xi_i^2=\frac{1}{3}$

图7-1: 抛物线 $y=x^2$ 下曲边三角形的矩形逼近

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005500.png =600x)

一般地, 在 $[a,b]$ 中取一系列的分点作成划分
$P:\ a=x_0<x_1<x_2<\cdots<x_n=b$
记小区间 $[x_{i-1},x_i]$ 的长度为 $\Delta x_i=x_i-x_{i-1}$
在每个小区间上任取一点 $\xi_i$, 用底为 $\Delta x_i$,
高为 $f(\xi_i)$ 的矩形面积近似代替小的曲边梯形面积
这些矩形面积之和 $\sum_{i=1}^n f(\xi_i)\Delta x_i$ 是曲边梯形面积的近似值

令 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}$,
当 $\lambda\to0$ 时, 若极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$ 存在,
则该极限是曲边梯形面积的精确值
这个极限与对 $[a,b]$ 所作的划分 $P$ 和对 $\xi_i$ 的取法无关

图7-2: 曲边梯形的分割

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005501.png =500x)


## 定积分的定义

设 $f(x)$ 是定义在 $[a,b]$ 上的函数
若要求对任意划分 $P$ 和任意 $\xi_i\in[x_{i-1},x_i]$,
极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$ 都存在,
则 $f(x)$ 必是 $[a,b]$ 上的有界函数
所以在定义函数的定积分时, 首先要求函数是有界的

------


定义7.1.1: 设 $f(x)$ 是定义在 $[a,b]$ 上的有界函数
在 $[a,b]$ 上任意取分点 $\{x_i\}_{i=0}^n$ 作成划分 $P:\ a=x_0<x_1<\cdots<x_n=b$
并任取 $\xi_i\in[x_{i-1},x_i]$, 记小区间 $[x_{i-1},x_i]$ 的长度为 $\Delta x_i=x_i-x_{i-1}$,
并令 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}$

若当 $\lambda\to0$ 时, 极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i$ 存在
且极限值与划分 $P$ 无关, 又与对 $\xi_i$ 的取法无关
则称 $f(x)$ 在 $[a,b]$ 上 Riemann 可积

和式 $S_n=\sum_{i=1}^n f(\xi_i)\Delta x_i$ 称为 Riemann 和
其极限值 $I$ 称为 $f(x)$ 在 $[a,b]$ 上的定积分,
记为 $I=\int_a^b f(x)dx$
$a$ 与 $b$ 分别称为积分的下限和上限

规定: $a>b$ 时 $\int_a^b f(x)dx=-\int_b^a f(x)dx$,
由此得到 $\int_a^a f(x)dx=0$

定义7.1.1 也可以用 ε-δ 语言表述
有定数 $I$, 对任意给定的 $\epsilon>0$,
存在 $\delta>0$,
使得对任意一种划分 $P$ 和任意 $\xi_i\in[x_{i-1},x_i]$,
只要 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$,
便有
$\left|\sum_{i=1}^n f(\xi_i)\Delta x_i-I\right|<\epsilon$

[不发生混淆时, Riemann 可积简称为可积]
[可积要求 Riemann 和的极限值与划分 $P$ 及 $\xi_i$ 的取法无关]

------


> 例7-2: 讨论 Dirichlet 函数
> $D(x)=\begin{cases}1, & x\text{为有理数}\\0, & x\text{为无理数}\end{cases}$
> 在 $[0,1]$ 上的可积性
>
> 有理数与无理数在实数域上稠密, 任意划分的每个小区间 $[x_{i-1},x_i]$ 中既有有理数又有无理数
> 当 $\xi_i$ 全取有理数时 $\lim\limits_{\lambda\to0}\sum_{i=1}^n D(\xi_i)\Delta x_i$
> $=\lim\limits_{\lambda\to0}\sum_{i=1}^n 1\cdot\Delta x_i=1$
>
> 当 $\xi_i$ 全取无理数时 $\lim\limits_{\lambda\to0}\sum_{i=1}^n D(\xi_i)\Delta x_i$
> $=\lim\limits_{\lambda\to0}\sum_{i=1}^n 0\cdot\Delta x_i=0$
> 两个和式的极限都存在但极限值不相同, 所以 Dirichlet 函数在 Riemann 意义下不可积


## Darboux 和

记 $f(x)$ 在 $[a,b]$ 上的上确界与下确界分别为 $M$ 和 $m$,
则有 $m\leq f(x)\leq M$
记 $f(x)$ 在 $[x_{i-1},x_i]$ 上的上确界与下确界分别为 $M_i$ 和 $m_i$,
即
$M_i=\sup\{f(x)\mid x\in[x_{i-1},x_i]\}$,
$m_i=\inf\{f(x)\mid x\in[x_{i-1},x_i]\}$
它们与对 $[a,b]$ 所作的划分 $P$ 有关

Darboux 大和: $S(P)=\sum_{i=1}^n M_i\Delta x_i$
Darboux 小和: $\underline{S}(P)=\sum_{i=1}^n m_i\Delta x_i$
两者统称为 Darboux 和, 显然有 $\underline{S}(P)\leq\sum_{i=1}^n f(\xi_i)\Delta x_i\leq S(P)$

[当 $\lambda\to0$ 时, 大和(顶边为实线的矩形面积之和)与小和(顶边为虚线的矩形面积之和)的极限若存在且相等,
则 $f(x)$ 可积, 反之亦然]

图7-3: Darboux 大和与小和

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005502.png =500x)

------


引理7.1.1: 若在原有划分中加入分点形成新的划分, 则大和不增,
小和不减

证明: 设 $S(P)$ 和 $\underline{S}(P)$ 是对应于某一划分 $P$ 的 Darboux 大和与小和,
设相应的分点为 $\{x_i\}_{i=0}^n$

不失一般性, 证明对这种划分再增加一个新分点后所得到新划分 $P'$ 的 Darboux 大和 $S(P')$ 与 Darboux 小和 $\underline{S}(P')$
成立 $\underline{S}(P')\geq\underline{S}(P)$,
$S(P')\leq S(P)$

设增加的新分点 $x'\in(x_{i-1},x_i)$,
记 $f(x)$ 在 $[x_{i-1},x']$ 和 $[x',x_i]$ 上的上确界分别为 $M_i'$ 和 $M_i''$,
则显然有 $M_i'\leq M_i$, $M_i''\leq M_i$
于是 $M_i'(x'-x_{i-1})+M_i''(x_i-x_{i-1})\leq M_i(x_i-x_{i-1})$
而此时 $S(P')$ 与 $S(P)$ 中的其他项都没有变化,
因此 $S(P')\leq S(P)$

同理可证 $\underline{S}(P)\leq\underline{S}(P')$

------


记 $\bar{S}$ 是一切可能的划分所得到的 Darboux 大和的集合,
而 $\underline{S}$ 是一切可能的划分所得到的 Darboux 小和的集合

------


引理7.1.2: 对任意 $S(P_1)\in\bar{S}$ 和 $\underline{S}(P_2)\in\underline{S}$,
恒有 $m(b-a)\leq\underline{S}(P_2)\leq S(P_1)\leq M(b-a)$

证明: 任意一种划分都可以看成是由 $n=1$ 的划分 $a=x_0<x_1=b$ 中插入若干分点所产生的新划分
因此由引理7.1.1 即知上式中前后两个不等式成立

下面证明中间的不等式
若 $S(P_1)$ 与 $\underline{S}(P_2)$ 是同一种划分的 Darboux 大和与 Darboux 小和,
则不等式已经成立

若它们是相应于不同划分的 Darboux 大和与 Darboux 小和,
则将这两种划分的分点合并在一起形成一种新的划分 $\tilde{P}$
设相应于新划分 $\tilde{P}$ 的 Darboux 大和与 Darboux 小和分别为 $S(\tilde{P})$ 和 $\underline{S}(\tilde{P})$
则由引理7.1.1, $\underline{S}(P_2)\leq\underline{S}(\tilde{P})\leq S(\tilde{P})\leq S(P_1)$

------


由引理7.1.2, $\bar{S}$ 和 $\underline{S}$ 都是有界集合,
因此分别有下确界和上确界
记 $\bar{S}$ 的下确界为 $L=\inf\{S(P)\mid S(P)\in\bar{S}\}$
记 $\underline{S}$ 的上确界为 $l=\sup\{\underline{S}(P)\mid\underline{S}(P)\in\underline{S}\}$
则对任意 $S(P_1)\in\bar{S}$ 和 $\underline{S}(P_2)\in\underline{S}$,
有 $\underline{S}(P_2)\leq l\leq L\leq S(P_1)$

------


引理7.1.3 (Darboux 定理): 对任意在 $[a,b]$ 上有界函数 $f(x)$,
恒有
$\lim\limits_{\lambda\to0}S(P)=L$,
$\lim\limits_{\lambda\to0}\underline{S}(P)=l$

证明: 只就大和的情况加以证明
对任意给定的 $\epsilon>0$, 因为 $L$ 是 $\bar{S}$ 的下确界,
所以存在着一个 $S(P')\in\bar{S}$ 满足 $0\leq S(P')-L<\frac{\epsilon}{2}$
设对应 $S(P')$ 的划分为 $P':\ a=x_0'<x_1'<x_2'<\cdots<x_p'=b$
取 $\delta=\min\left\{\Delta x_1',\Delta x_2',\cdots,\Delta x_p',\frac{\epsilon}{2(p-1)(M-m)}\right\}$

对任意一个满足 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$ 的划分 $P:\ a$
$=x_0<x_1<x_2<\cdots<x_n=b$
记与其相应的大和为 $S(P)$, 在 $\{x_i\}_{i=0}^n$ 中插入 $\{x_j'\}_{j=0}^p$ 形成新的划分 $P^*$,
并将这一新划分的大和记作 $S(P^*)$, 则由引理7.1.1 知 $S(P^*)-S(P)\leq0$

将对应于划分 $P$ 的区间 $[x_{i-1},x_i]$ 分成两类
1. $[x_{i-1},x_i]$ 中不含有新插入的分点,
此时 $S(P)$ 和 $S(P^*)$ 中的相应项同为 $M_i\Delta x_i$
2. $[x_{i-1},x_i]$ 中含有新插入的分点,
由于两种划分的端点 $a$,
   $b$ 重合, 这样的区间至多只有 $p-1$ 个

因为对任意 $i,j$ 有 $\Delta x_i\leq\delta\leq\Delta x_j'$,
所以在 $[x_{i-1},x_i]$ 中只有一个新插入的分点 $x_j'$
利用前面的记号, 这时 $S(P)$ 和 $S(P^*)$ 中的相应项之差为
$M_i(x_i-x_{i-1})-[M_i'(x_j'-x_{i-1})+M_i''(x_i-x_j')]\leq(M-m)(x_i-x_{i-1})<(M-m)\delta$

于是 $0\leq S(P)-S(P^*)\leq(p-1)(M-m)\delta\leq\frac{\epsilon}{2}$
综合上面的结论, 即有
$0\leq S(P)-L=[S(P)-S(P^*)]+[S(P^*)-S(P')]+[S(P')-L]<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$

小和的情况类似

[证明中 $M'$ 与 $M''$ 分别是 $f(x)$ 在 $[x_{i-1},x']$ 和 $[x',x_i]$ 上的上确界]


## Riemann 可积的充分必要条件

定理7.1.1: 有界函数 $f(x)$ 在 $[a,b]$ 可积的充分必要条件是,
对任意划分 $P$, 当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$ 时,
Darboux 大和与 Darboux 小和的极限相等, 即成立
$\lim\limits_{\lambda\to0}S(P)=L=l=\lim\limits_{\lambda\to0}\underline{S}(P)$

证明: 先证必要性
设 $f(x)$ 可积且积分值为 $I$, 则由定义, 对任意的 $\epsilon>0$,
存在 $\delta>0$, 使得对任意划分 $P:\ a=x_0<x_1<\cdots<x_n=b$ 和任意 $\xi_i\in[x_{i-1},x_i]$,
只要 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$,
便有
$\left|\sum_{i=1}^n f(\xi_i)\Delta x_i-I\right|<\frac{\epsilon}{2}$

特别地, 取 $\xi_i$ 是 $[x_{i-1},x_i]$ 中满足 $0\leq M_i-f(\xi_i)<\frac{\epsilon}{2(b-a)}$ 的点
由于 $M_i$ 是 $f(x)$ 在 $[x_{i-1},x_i]$ 上的上确界,
因此这样的 $\xi_i$ 一定可以取到

于是 $\left|S(P)-\sum_{i=1}^n f(\xi_i)\Delta x_i\right|=\sum_{i=1}^n[M_i-f(\xi_i)]\Delta x_i$
$<\frac{\epsilon}{2(b-a)}\cdot(b-a)$
$=\frac{\epsilon}{2}$

所以 $|S(P)-I|\leq\left|S(P)-\sum_{i=1}^n f(\xi_i)\Delta x_i\right|+\left|\sum_{i=1}^n f(\xi_i)\Delta x_i-I\right|$
$<\frac{\epsilon}{2}+\frac{\epsilon}{2}$
$=\epsilon$

即 $\lim\limits_{\lambda\to0}S(P)=I$; 同理可证 $\lim\limits_{\lambda\to0}\underline{S}(P)=I$
于是 $\lim\limits_{\lambda\to0}S(P)=\lim\limits_{\lambda\to0}\underline{S}(P)$

再证充分性
按 Darboux 和的定义, 对任意一种划分 $P$, 其 Darboux 大和与小和总满足 $\underline{S}(P)$
$\leq\sum_{i=1}^n f(\xi_i)\Delta x_i\leq S(P)$

若 $\lim\limits_{\lambda\to0}S(P)=\lim\limits_{\lambda\to0}\underline{S}(P)=I$,
那么两边取极限, 即有 $\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i=I$

------


若记 $\omega_i=M_i-m_i$ 为 $f(x)$ 在 $[x_{i-1},x_i]$ 上的振幅,
则定理7.1.1 也可以等价地表述为

------


定理7.1.2: 有界函数 $f(x)$ 在 $[a,b]$ 可积的充分必要条件是,
对任意划分, 当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$ 时
$\lim\limits_{\lambda\to0}\sum_{i=1}^n\omega_i\Delta x_i=0$

定理7.1.2 的几何意义是当划分无限细分时(即 $\lambda\to0$),
图7-4 中的阴影部分的面积之和趋于零

图7-4: 振幅之和的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005503.png =500x)

------


推论1: 闭区间上的连续函数必定可积

证明: 设 $f(x)$ 在 $[a,b]$ 上连续, 则它在 $[a,b]$ 上一致连续
也就是说, 对任意 $\epsilon>0$, 存在 $\delta>0$,
对任意 $x',x''\in[a,b]$, 只要 $|x'-x''|<\delta$ 就有 $|f(x')-f(x'')|<\frac{\epsilon}{b-a}$

因此对任意划分 $P$, 只要 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$,
便有
$\omega_i=\max\limits_{x\in[x_{i-1},x_i]}f(x)-\min\limits_{x\in[x_{i-1},x_i]}f(x)$
$<\frac{\epsilon}{b-a}\quad(i$
$=1,2,\cdots,n)$

于是 $\sum_{i=1}^n\omega_i\Delta x_i<\frac{\epsilon}{b-a}\sum_{i=1}^n\Delta x_i=\epsilon$
由定理7.1.2, $f(x)$ 在 $[a,b]$ 可积

------


推论2: 闭区间上的单调函数必定可积

证明: 设 $f(x)$ 在 $[a,b]$ 上单调, 不妨设为单调增加,
则在任意小区间 $[x_{i-1},x_i]$ 上 $f(x)$ 的振幅为 $\omega_i=f(x_i)-f(x_{i-1})$

于是, 对任意给定的 $\epsilon>0$, 取 $\delta=\frac{\epsilon}{f(b)-f(a)}>0$,
当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$ 时
$\sum_{i=1}^n\omega_i\Delta x_i=\sum_{i=1}^n[f(x_i)-f(x_{i-1})]\Delta x_i$
$<\frac{\epsilon}{f(b)-f(a)}\sum_{i=1}^n[f(x_i)-f(x_{i-1})]$
$=\frac{\epsilon}{f(b)-f(a)}\cdot[f(b)-f(a)]=\epsilon$
由定理7.1.2, $f(x)$ 在 $[a,b]$ 可积

------


对于实际应用来说, 定理7.1.2 对于判别函数不可积更为方便
如例7-2 所述的 $[0,1]$ 上的 Dirichlet 函数,
不管如何作划分,
它在每个小区间 $[x_{i-1},x_i]$ 上的振幅恒有 $\omega_i=1$

于是 $\lim\limits_{\lambda\to0}\sum_{i=1}^n\omega_i\Delta x_i$
$=\lim\limits_{\lambda\to0}\sum_{i=1}^n\Delta x_i$
$=1$
所以 Dirichlet 函数不是 Riemann 可积的

要通过"对任意划分都有 $\sum_{i=1}^n\omega_i\Delta x_i\to0\ (\lambda\to0)$"来证明函数可积,
一般说来是很困难的, 下面给出一个更易于判断的条件

回顾 Darboux 定理的证明过程可以知道, 它实际上证明了: 对任意给定的 $\epsilon>0$,
只要有一个划分 $P'$, 使得
$0\leq S(P')-L<\frac{\epsilon}{2}$ (或 $0\leq l-\underline{S}(P')<\frac{\epsilon}{2}$)

那么就一定存在某个 $\delta>0$, 对满足 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}<\delta$ 的任意一种划分 $P$,
必有
$0\leq S(P)-L<\epsilon$ (或 $0\leq l-\underline{S}(P)<\epsilon$)

------


定理7.1.3: 有界函数 $f(x)$ 在 $[a,b]$ 可积的充分必要条件是,
对任意给定的 $\epsilon>0$, 存在着一种划分,
使得相应的振幅满足
$\sum_{i=1}^n\omega_i\Delta x_i<\epsilon$

证明留给读者

------


推论3: 闭区间上只有有限个不连续点的有界函数必定可积

证明: 设 $f(x)$ 在 $[a,b]$ 上的不连续点共有 $k$ 个,
记为 $a\leq p_1'<p_2'<\cdots<p_k'\leq b$,
设相邻两点之间的最小距离为 $d$, 不妨设 $p_1'$ 和 $p_k'$ 在 $[a,b]$ 的内部

对任意给定的 $\epsilon>0$, 取 $\delta=\min\left\{\frac{p_1'-a}{2},\frac{b-p_k'}{2},\frac{d}{3},\frac{\epsilon}{4k(M-m)}\right\}$
$>0$

先以 $p_j'$ 的 $\delta$ 领域的两个端点 $p_j'-\delta$,
$p_j'+\delta$ 为分点, 将 $[a,b]$ 分成 $2k+1$ 个子区间
于是 $f(x)$ 在子区间 $D^{(1)}=[a,p_1'-\delta]$,
$D^{(j)}=[p_{j-1}'+\delta,p_j'-\delta]\ (j=2,\cdots,k)$,
$D^{(k+1)}=[p_k'+\delta,b]$ 上连续

由推论1, $f(x)$ 在这些子区间上可积, 所以在每个 $D^{(j)}$ 上分别存在分点 $x_0^{(j)}<x_1^{(j)}<\cdots<x_{l_j}^{(j)}\ (j$
$=1,\cdots,k+1)$,
使得
$\sum_{i=1}^{l_j}\omega_i^{(j)}\Delta x_i^{(j)}<\frac{\epsilon}{2(k+1)}$

将所有分点合为一组, 看成 $[a,b]$ 的一个划分, 记 $\omega_j'$ 为 $f(x)$ 在 $[p_j'-\delta,p_j'+\delta]$ 上的振幅,
即有
$\sum_{i=1}^n\omega_i\Delta x_i=\sum_{j=1}^{k+1}\sum_{i=1}^{l_j}\omega_i^{(j)}\Delta x_i^{(j)}+\sum_{j=1}^k\omega_j'[(p_j'+\delta)-(p_j'-\delta)]$
$<(k+1)\cdot\frac{\epsilon}{2(k+1)}+\frac{2\epsilon}{4k(M-m)}\cdot k(M-m)$
$=\epsilon$
由定理7.1.3, $f(x)$ 在 $[a,b]$ 可积

[当 $p_j'$ 为 $[a,b]$ 的端点时可类似证明]
[若一个函数虽然振幅的最大值 $\max\{\omega_i\}$ 并不随 $\lambda\to0$
而趋于零,
但可使振幅不趋于零的小区间的长度之和任意小, 这个函数仍然是 Riemann 可积的]

------


> 例7-3: 证明 Riemann 函数
> $R(x)=\begin{cases}\frac{1}{p}, & x=\frac{q}{p}\ (p\in N^*,q\in Z-\{0\},p,q\text{互质})\\1, & x=0\\0, & x\text{为无理数}\end{cases}$
> 在 $[0,1]$ 上可积
>
> 由 Riemann 函数的性质, 对任意给定的 $0<\epsilon<2$,
> 在 $[0,1]$ 上使得 $R(x)\geq\frac{\epsilon}{2}$ 的点至多只有有限个,
> 不妨设为 $k$ 个, 记为 $0=p_1'<p_2'<\cdots<p_k'=1$
>
> 作 $[0,1]$ 的划分 $0=x_0<x_1<x_2<\cdots<x_{2k-1}=1$,
> 使得满足
>
> $p_1'\in[x_0,x_1)$, $x_1-x_0<\frac{\epsilon}{2k}$
> $p_2'\in(x_2,x_3)$, $x_3-x_2<\frac{\epsilon}{2k}$
> $\cdots$
> $p_{k-1}'\in(x_{2k-4},x_{2k-3})$,
> $x_{2k-3}-x_{2k-4}<\frac{\epsilon}{2k}$
>
> $p_k'\in(x_{2k-2},x_{2k-1}]$,
> $x_{2k-1}-x_{2k-2}<\frac{\epsilon}{2k}$
>
> 由于 $\sum_{i=1}^{2k-1}\omega_i\Delta x_i=\sum_{j=0}^{k-1}\omega_{2j+1}\Delta x_{2j+1}+\sum_{j=1}^{k-1}\omega_{2j}\Delta x_{2j}$
> 而在右边的第一个和式中, 有 $\Delta x_{2j+1}<\frac{\epsilon}{2k}$
> 且 $\omega_{2j+1}\leq1$; 在第二个和式中,
>
> 有 $\omega_{2j}\leq\frac{\epsilon}{2}$
> 且 $\sum_{j=1}^{k-1}\Delta x_{2j}<1$
> 因此得到 $\sum_{i=1}^n\omega_i\Delta x_i<k\cdot\frac{\epsilon}{2k}+\frac{\epsilon}{2}=\epsilon$
> 由定理7.1.3, Riemann 函数可积

图7-5: $k=3$ 时 Riemann 函数的振幅估计

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005504.png =350x)


## 定积分的基本性质

本节利用定积分的定义及其存在的充分必要条件, 给出定积分的基本性质

------


性质1 (线性性): 设 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
$k_1$ 和 $k_2$ 是常数, 则函数 $k_1f(x)+k_2g(x)$ 在 $[a,b]$ 上也可积,
且有
$\int_a^b[k_1f(x)+k_2g(x)]dx=k_1\int_a^b f(x)dx+k_2\int_a^b g(x)dx$

证明: 对 $[a,b]$ 的任意划分 $a=x_0<x_1<x_2<\cdots<x_n=b$ 和任意 $\xi_i\in[x_{i-1},x_i]$,
成立等式
$\sum_{i=1}^n[k_1f(\xi_i)+k_2g(\xi_i)]\Delta x_i=k_1\sum_{i=1}^n f(\xi_i)\Delta x_i+k_2\sum_{i=1}^n g(\xi_i)\Delta x_i$

两边令 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$,
由于 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
因此有
$\lim\limits_{\lambda\to0}\sum_{i=1}^n[k_1f(\xi_i)+k_2g(\xi_i)]\Delta x_i$
$=k_1\int_a^b f(x)dx+k_2\int_a^b g(x)dx$
由定义, $k_1f(x)+k_2g(x)$ 在 $[a,b]$ 上可积且积分式成立

推论: 若 $f(x)$ 在 $[a,b]$ 上可积, 而 $g(x)$ 只在有限个点上与 $f(x)$ 的取值不相同,
则 $g(x)$ 在 $[a,b]$ 上也可积, 并且有 $\int_a^b f(x)dx=\int_a^b g(x)dx$
[在有限个点上改变一个可积函数的函数值, 并不影响其可积性和积分值]

------


性质2 (乘积可积性): 设 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
则 $f(x)\cdot g(x)$ 在 $[a,b]$ 上也可积

证明: 由于 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
所以它们在 $[a,b]$ 上有界, 因此存在常数 $M$,
满足 $|f(x)|\leq M$ 和 $|g(x)|\leq M$,
$x\in[a,b]$

对 $[a,b]$ 的任意划分 $a=x_0<x_1<x_2<\cdots<x_n=b$
设 $\hat{x}$ 和 $\tilde{x}$ 是 $[x_{i-1},x_i]$ 中的任意两点,
则有
$|f(\hat{x})g(\hat{x})-f(\tilde{x})g(\tilde{x})|\leq M[|f(\hat{x})-f(\tilde{x})|+|g(\hat{x})-g(\tilde{x})|]$

记 $f(x)\cdot g(x)$ 在小区间 $[x_{i-1},x_i]$ 上的振幅为 $\omega_i$,
$f(x)$ 和 $g(x)$ 在小区间 $[x_{i-1},x_i]$ 上的振幅分别为 $\omega_i'$ 和 $\omega_i''$,
则上式意味着 $\omega_i\leq M(\omega_i'+\omega_i'')$
因此 $0\leq\sum_{i=1}^n\omega_i\Delta x_i\leq M\left(\sum_{i=1}^n\omega_i'\Delta x_i+\sum_{i=1}^n\omega_i''\Delta x_i\right)$

由于 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 可积,
因而当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$ 时,
上面不等式的右端趋于零
由极限的夹逼性, 得到 $\lim\limits_{\lambda\to0}\sum_{i=1}^n\omega_i\Delta x_i=0$
根据 Riemann 可积的充分必要条件, 即知 $f(x)\cdot g(x)$ 在 $[a,b]$ 可积

[一般说来 $\int_a^b f(x)g(x)dx\neq\left(\int_a^b f(x)dx\right)\cdot\left(\int_a^b g(x)dx\right)$]

------


性质3 (保序性): 设 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
且在 $[a,b]$ 上恒有 $f(x)\geq g(x)$, 则成立
$\int_a^b f(x)dx\geq\int_a^b g(x)dx$

证明: 只要证明对 $[a,b]$ 上的非负函数 $f(x)$
成立 $\int_a^b f(x)dx\geq0$

由于在 $[a,b]$ 上 $f(x)\geq0$, 因此对 $[a,b]$ 的任意划分和任意 $\xi_i\in[x_{i-1},x_i]$,
有 $\sum_{i=1}^n f(\xi_i)\Delta x_i\geq0$
令 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$,
即得到 $\int_a^b f(x)dx=\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i\geq0$

------


性质4 (绝对可积性): 设 $f(x)$ 在 $[a,b]$ 上可积,
则 $|f(x)|$ 在 $[a,b]$ 上也可积, 且成立
$\left|\int_a^b f(x)dx\right|\leq\int_a^b|f(x)|dx$

证明: 由于对任意两点 $\hat{x}$ 和 $\tilde{x}$,
都有 $||f(\hat{x})|-|f(\tilde{x})||\leq|f(\hat{x})-f(\tilde{x})|$,
仿照性质2 的证明即可证得 $|f(x)|$ 在 $[a,b]$ 上可积

又因为对任意 $x\in[a,b]$, 成立 $-|f(x)|\leq f(x)\leq|f(x)|$
由性质3 得到 $-\int_a^b|f(x)|dx\leq\int_a^b f(x)dx\leq\int_a^b|f(x)|dx$
即 $\left|\int_a^b f(x)dx\right|\leq\int_a^b|f(x)|dx$

[性质4 的逆命题不成立, 即由 $|f(x)|$ 在 $[a,b]$ 上可积推不出 $f(x)$ 在 $[a,b]$ 上可积]
例: $f(x)=\begin{cases}1, & x\text{为有理数}\\-1, & x\text{为无理数}\end{cases}$,
$x\in[0,1]$
$f(x)$ 在任意小区间上的振幅恒为 $2$, 所以不可积,
但 $|f(x)|=1$,
$x\in[0,1]$ 在 $[0,1]$ 上显然可积

------


性质5 (区间可加性): 设 $f(x)$ 在 $[a,b]$ 上可积,
则对任意点 $c\in[a,b]$, $f(x)$ 在 $[a,c]$ 和 $[c,b]$ 上都可积
反过来, 若 $f(x)$ 在 $[a,c]$ 和 $[c,b]$ 上都可积,
则 $f(x)$ 在 $[a,b]$ 上可积
此时成立 $\int_a^b f(x)dx=\int_a^c f(x)dx+\int_c^b f(x)dx$

证明: 先假定 $f(x)$ 在 $[a,b]$ 上可积,
设 $c$ 是 $[a,b]$ 中任意给定的一点
由定理7.1.3, 对任意给定的 $\epsilon>0$,
存在 $[a,b]$ 的一个划分 $a=x_0<x_1<\cdots<x_n=b$,
使得满足 $\sum_{i=1}^n\omega_i\Delta x_i<\epsilon$
我们总可以假定 $c$ 是其中的一个分点 $x_i$, 否则只要在原有划分中插入分点 $c$ 作成新的划分,
由 Darboux 和的性质(引理7.1.1), 上面的不等式仍然成立

将 $a=x_0<x_1<x_2<\cdots<x_i=c$ 和 $c=x_i<x_{i+1}<x_{i+2}<\cdots<x_n=b$ 分别看成是对 $[a,c]$ 和 $[c,b]$ 作的划分,
则显然有
$\sum_{i=1}^{n_1}\omega_i\Delta x_i<\epsilon$ 和 $\sum_{i=1}^{n_2}\omega_i\Delta x_i<\epsilon$
由定理7.1.3, $f(x)$ 在 $[a,c]$ 和 $[c,b]$ 上都是可积的

反过来, 若 $f(x)$ 在 $[a,c]$ 和 $[c,b]$ 上都可积,
则对任意给定的 $\epsilon>0$, 分别存在 $[a,c]$ 和 $[c,b]$ 的划分
$a=x_0'<x_1'<x_2'<\cdots<x_{n_1}'=c$ 和 $c=x_0''<x_1''<x_2''<\cdots<x_{n_2}''=b$
使得 $\sum_{i=1}^{n_1}\omega_i'\Delta x_i'<\frac{\epsilon}{2}$ 和 $\sum_{i=1}^{n_2}\omega_i''\Delta x_i''$
$<\frac{\epsilon}{2}$

将这两组分点合起来作为 $[a,b]$ 的一组分点 $\{x_i\}_{i=0}^n$,
这里 $n=n_1+n_2$, 于是得到 $\sum_{i=1}^n\omega_i\Delta x_i=\sum_{i=1}^{n_1}\omega_i'\Delta x_i'+\sum_{i=1}^{n_2}\omega_i''\Delta x_i''$
$<\epsilon$
因此 $f(x)$ 在 $[a,b]$ 上可积

在 $\int_a^c f(x)dx$, $\int_c^b f(x)dx$ 和 $\int_a^b f(x)dx$ 都存在时,
利用定积分的定义, 容易证明 $\int_a^b f(x)dx=\int_a^c f(x)dx+\int_c^b f(x)dx$

[当 $c$ 是 $[a,b]$ 之外的一点时, 只要函数 $f(x)$ 的可积性依然保持,
定积分的区间可加性依然成立]

------


性质6 (积分第一中值定理): 设 $f(x)$ 和 $g(x)$ 都在 $[a,b]$ 上可积,
$g(x)$ 在 $[a,b]$ 上不变号, 则存在 $\eta\in[m,M]$,
使得
$\int_a^b f(x)g(x)dx=\eta\int_a^b g(x)dx$
这里 $M$ 和 $m$ 分别表示 $f(x)$ 在 $[a,b]$ 的上确界和下确界
特别地, 若 $f(x)$ 在 $[a,b]$ 上连续, 则存在 $\xi\in[a,b]$,
使得 $\int_a^b f(x)g(x)dx=f(\xi)\int_a^b g(x)dx$

证明: 因为 $g(x)$ 在 $[a,b]$ 上不变号,
不妨设 $g(x)\geq0$,
$x\in[a,b]$
于是有 $mg(x)\leq f(x)g(x)\leq Mg(x)$

由性质3, 得到 $m\int_a^b g(x)dx\leq\int_a^b f(x)g(x)dx\leq M\int_a^b g(x)dx$
由于 $\int_a^b f(x)g(x)dx$ 和 $\int_a^b g(x)dx$ 都是常数,
因而必有某个 $\eta\in[m,M]$, 使得 $\int_a^b f(x)g(x)dx=\eta\int_a^b g(x)dx$

若 $f(x)$ 在 $[a,b]$ 上连续, 则由闭区间上连续函数的中间值定理,
此时必存在某个 $\xi\in[a,b]$, 使得 $f(\xi)=\eta$,
因此 $\int_a^b f(x)g(x)dx=f(\xi)\int_a^b g(x)dx$

[当 $f(x)$ 在 $[a,b]$ 上连续, 而 $g(x)\equiv1$ 时,
积分第一中值定理化为 $\int_a^b f(x)dx=f(\xi)(b-a)$]

图7-6: 积分第一中值定理的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005505.png =350x)

[当 $f(x)\geq0$ 时, 上式左边表示由曲线 $f(x)$,
直线 $x=a$, $x=b$ 以及 $x$ 轴围成的曲边梯形的面积,
它一定等于以 $[a,b]$ 为底, 某个 $f(\xi)$ 为高的矩形面积]

------


> 例7-4: 设 $f(x)$ 在 $[a,b]$ 上连续,
> 且 $f(x)>0$,
> 证明 $\frac{1}{b-a}\int_a^b\ln f(x)dx\leq\ln\left(\frac{1}{b-a}\int_a^b f(x)dx\right)$
>
> 将区间 $[a,b]$ 等分, 并设 $x_i=a+\frac{i}{n}(b-a)$
> 利用 $\ln x$ 在 $(0,+\infty)$ 上的上凸性, 由 Jensen 不等式得 $\sum_{i=1}^n\frac{1}{n}\ln f(x_i)$
> $\leq\ln\left(\sum_{i=1}^n\frac{1}{n}f(x_i)\right)$
> 即 $\frac{1}{b-a}\sum_{i=1}^n\ln f(x_i)\Delta x_i\leq\ln\left(\frac{1}{b-a}\sum_{i=1}^n f(x_i)\Delta x_i\right)$
>
> 由假设条件知 $f(x)$ 和 $\ln f(x)$ 在 $[a,b]$ 上连续,
> 因此可积
>
> 在上式中令 $n\to\infty$, 则由定积分的定义及 $\ln x$ 的连续性得 $\frac{1}{b-a}\int_a^b\ln f(x)dx$
> $\leq\ln\left(\frac{1}{b-a}\int_a^b f(x)dx\right)$

> 例7-5 (Hölder 不等式): 设 $f(x),g(x)$ 在 $[a,b]$ 上连续,
> $p,q$ 为满足 $\frac{1}{p}+\frac{1}{q}=1$ 的正数,
> 证明
> $\int_a^b|f(x)g(x)|dx\leq\left(\int_a^b|f(x)|^p dx\right)^{\frac{1}{p}}\left(\int_a^b|g(x)|^q dx\right)^{\frac{1}{q}}$
>
> 当 $f(x)\equiv0$ 或 $g(x)\equiv0$ 时,
> 上式显然成立,
> 否则令
> $\varphi(x)=\frac{|f(x)|}{\left(\int_a^b|f(x)|^p dx\right)^{\frac{1}{p}}}$,
> $\psi(x)=\frac{|g(x)|}{\left(\int_a^b|g(x)|^q dx\right)^{\frac{1}{q}}}$,
> $x\in[a,b]$
>
> 由 Young 不等式 $\varphi(x)\psi(x)\leq\frac{1}{p}\varphi(x)^p+\frac{1}{q}\psi(x)^q$
> 得
> $\frac{|f(x)g(x)|}{\left(\int_a^b|f(x)|^p dx\right)^{\frac{1}{p}}\left(\int_a^b|g(x)|^q dx\right)^{\frac{1}{q}}}$
> $\leq\frac{|f(x)|^p}{p\int_a^b|f(x)|^p dx}+\frac{|g(x)|^q}{q\int_a^b|g(x)|^q dx}$
>
> 对上式两边在 $[a,b]$ 上求积分, 利用定积分的性质得
> $\frac{1}{\left(\int_a^b|f(x)|^p dx\right)^{\frac{1}{p}}\left(\int_a^b|g(x)|^q dx\right)^{\frac{1}{q}}}\int_a^b|f(x)g(x)|dx$
> $\leq\frac{1}{p}+\frac{1}{q}$
> $=1$
>
> 在不等式两边同乘以 $\left(\int_a^b|f(x)|^p dx\right)^{\frac{1}{p}}\left(\int_a^b|g(x)|^q dx\right)^{\frac{1}{q}}$,
> 即得

> 例7-6: 设函数 $f(x)$ 在 $[a,b]$ 上二阶可导,
> $f\left(\frac{a+b}{2}\right)=0$
> 记 $M=\sup\limits_{a\leq x\leq b}|f''(x)|$,
> 证明 $\left|\int_a^b f(x)dx\right|\leq\frac{M(b-a)^3}{24}$
>
> $f(x)$ 在 $x=\frac{a+b}{2}$ 处的带 Lagrange 余项的 Taylor 公式为
> $f(x)=f\left(\frac{a+b}{2}\right)+f'\left(\frac{a+b}{2}\right)\left(x-\frac{a+b}{2}\right)+\frac{1}{2}f''(\xi)\left(x-\frac{a+b}{2}\right)^2$
> $=f'\left(\frac{a+b}{2}\right)\left(x-\frac{a+b}{2}\right)+\frac{1}{2}f''(\xi)\left(x-\frac{a+b}{2}\right)^2$,
> $x\in[a,b]$
> 其中 $a\leq\xi\leq b$
>
> 对等式两边求积分, 利用 $\int_a^b\left(x-\frac{a+b}{2}\right)dx=0$,
> 得到
> $\int_a^b f(x)dx=\frac{1}{2}\int_a^b f''(\xi)\left(x-\frac{a+b}{2}\right)^2 dx$
>
> 于是 $\left|\int_a^b f(x)dx\right|\leq\frac{1}{2}\int_a^b\left|f''(\xi)\left(x-\frac{a+b}{2}\right)^2\right|dx$
> $\leq\frac{M}{2}\int_a^b\left(x-\frac{a+b}{2}\right)^2 dx$
> $=\frac{M(b-a)^3}{24}$


## 从实例看微分与积分的联系

以速度 $v(t)$ 作变速运动的物体, 在时间段 $[T_1,T_2]$ 内走过的路程 $S$ 可表示为定积分 $S$
$=\lim\limits_{\lambda\to0}\sum_{i=1}^n v(\xi_i)\Delta t_i$
$=\int_{T_1}^{T_2}v(t)dt$

若设物体在时间段 $[0,t]$ 内走过的路程为 $S(t)$,
则 $S=S(T_2)-S(T_1)$,
因此 $\int_{T_1}^{T_2}v(t)dt=S(T_2)-S(T_1)$

注意到 $v(t)=S'(t)$, 即 $S(t)$ 是 $v(t)$ 的一个原函数
于是 $v(t)$ 在区间 $[T_1,T_2]$ 上的积分值可以用它的一个原函数在区间的两个端点处的函数值之差来表示

再看一个几何实例
直角三角形的两条直角边分别平行于两坐标轴, 斜率为 $k(k=\tan\theta)$ 时,
高为 $h=k(b-a)$
将斜边换成曲线 $y=f(x)$, 求 $f(x)$ 在区间 $[a,b]$ 上的积分,
得到曲边直角三角形

若将 $f(x)$ 在 $x=a$ 处的导数 $f'(a)$ 近似地视作"斜边"的斜率,
则它近似地有 $h\approx f'(a)\cdot(b-a)$,
这个结果是很粗糙的

为提高精确度, 对区间 $[a,b]$ 作划分 $a=x_0<x_1<x_2<\cdots<x_n=b$
在每个小区间 $[x_{i-1},x_i]$ 上构造小曲边直角三角形,
将 $f'(x_{i-1})$ 近似地视作"斜边"的斜率,
则小曲边直角三角形的"高"近似地等于 $h_i=f'(x_{i-1})\cdot\Delta x_i$
将所有 $h_i$ 加起来得 $\sum_{i=1}^n h_i=\sum_{i=1}^n f'(x_{i-1})\Delta x_i$

令小区间的最大长度 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$,
就得到曲边直角三角形的"高"为 $h=\lim\limits_{\lambda\to0}\sum_{i=1}^n f'(x_{i-1})\Delta x_i$
由定积分的定义, 这个极限值就是 $\int_a^b f'(x)dx$

由于曲边直角三角形的"高"实际上就是 $f(x)$ 在 $[a,b]$ 的两个端点处的函数值之差 $f(b)-f(a)$,
于是得到 $\int_a^b f'(x)dx=f(b)-f(a)$

图7-7: 曲边直角三角形及其分割

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005506.png =600x)


## 微积分基本定理: Newton-Leibniz 公式

设 $f$ 在区间 $[a,b]$ 上可积, 由积分区间可加性,
对任意 $x\in[a,b]$,
$\int_a^x f(t)dt$ 存在
当 $x$ 在 $[a,b]$ 中变化时, $\int_a^x f(t)dt$ 的值也随之变化,
它是定义在 $[a,b]$ 上的函数

------


定理7.3.1: 设 $f(x)$ 在 $[a,b]$ 上可积,
作函数 $F(x)=\int_a^x f(t)dt$,
$x\in[a,b]$, 则
(1) $F(x)$ 是 $[a,b]$ 上的连续函数
(2) 若 $f(x)$ 在 $[a,b]$ 上连续, 则 $F(x)$ 在 $[a,b]$ 上可微,
且有 $F'(x)=f(x)$

证明: 由定义条件, 知 $F(x)$ 在整个 $[a,b]$ 上有定义,
由定积分的区间可加性
$F(x+\Delta x)-F(x)=\int_a^{x+\Delta x}f(t)dt-\int_a^x f(t)dt=\int_x^{x+\Delta x}f(t)dt$
记 $m,M$ 分别为 $f(x)$ 在 $[a,b]$ 上的下确界和上确界,
由定积分第一中值定理, 即得到
$F(x+\Delta x)-F(x)=\begin{cases}\eta\cdot\Delta x, & \eta\in[m,M],\quad f(x)\text{在}[a,b]\text{上可积}\\f(\xi)\cdot\Delta x, & \xi\text{在}x\text{与}x+\Delta x\text{之间},\quad f(x)\text{在}[a,b]\text{上连续}\end{cases}$

不管在哪一种情况下, 当 $\Delta x\to0$ 时都有 $F(x+\Delta x)-F(x)\to0$,
即 $F(x)$ 在 $[a,b]$ 上连续

若 $f(x)$ 在 $[a,b]$ 连续, 当 $\Delta x\to0$ 时有 $\xi\to x$,
因而 $f(\xi)\to f(x)$, 于是 $F'(x)=\lim\limits_{\Delta x\to0}\frac{F(x+\Delta x)-F(x)}{\Delta x}$
$=\lim\limits_{\Delta x\to0}f(\xi)=f(x)$

[定理7.3.1 说明: 当 $f(x)$ 在 $[a,b]$ 上连续时,
$\int_a^x f(t)dt$ 正是 $f(x)$ 在 $[a,b]$ 上的一个原函数,
即任何连续函数必存在原函数]
[结论(2)给出了对积分上限求导的法则: $\left(\int_a^x f(t)dt\right)'=f(x)$]

------


> 例7-7: 计算 $F(x)=\int_0^{x^2}\sin\sqrt{t}dt$ 的导数
> 记 $u=x^2$, 则 $F(x)=G(u)=\int_0^u\sin\sqrt{t}dt$,
> 由复合函数求导法则
> $F'(x)=\frac{d}{du}G(u)\cdot u'(x)=\left.\left(\frac{d}{du}\int_0^u\sin\sqrt{t}dt\right)\right|_{u=x^2}\cdot2x$
> $=2x\sin x$

> 例7-8: 求极限 $\lim\limits_{x\to0}\frac{\int_0^{x^2}\sin\sqrt{t}dt}{x^3}$
> 由于 $\int_0^0 f(x)dx=0$, 因此这个极限是 $\frac{0}{0}$ 待定型
> 由 L'Hospital 法则和上题结论
> $\lim\limits_{x\to0}\frac{\int_0^{x^2}\sin\sqrt{t}dt}{x^3}$
> $=\lim\limits_{x\to0}\frac{\left(\int_0^{x^2}\sin\sqrt{t}dt\right)'}{(x^3)'}$
> $=\lim\limits_{x\to0}\frac{2x\sin x}{3x^2}=\frac{2}{3}$

------


定理7.3.2 (微积分基本定理): 设 $f(x)$ 在 $[a,b]$ 上连续,
$F(x)$ 是 $f(x)$ 在 $[a,b]$ 上的一个原函数,
则成立
$\int_a^b f(x)dx=F(b)-F(a)$

证明: 设 $F(x)$ 是 $f(x)$ 在 $[a,b]$ 上的任一个原函数,
由定理7.3.1, $\int_a^x f(t)dt$ 也是 $f(x)$ 在 $[a,b]$ 上的一个原函数,
因而两者至多相差一个常数, 记
$\int_a^x f(t)dt=F(x)+C$

令 $x=a$, 即得到 $C=-F(a)$, 所以 $\int_a^x f(t)dt=F(x)-F(a)$
再令 $x=b$, 由于定积分中的自变量用什么记号与积分值无关,
便可得 $\int_a^b f(x)dx=\int_a^b f(t)dt=F(b)-F(a)$

定理的结论称为 Newton-Leibniz 公式, 其中 $F(b)-F(a)$ 一般记为 $F(x)\big|_a^b$
[Newton-Leibniz 公式将"求曲线的切线斜率"和"求曲线所围面积"这两件看上去风马牛不相及的事统一起来,
揭示了微分与积分的联系]

------


> 例7-9: 计算 $\int_0^1 x^2dx$
> 因为 $\int x^2dx=\frac{1}{3}x^3+C$,
> 取 $F(x)=\frac{1}{3}x^3$,
> 由 Newton-Leibniz 公式
> $\int_0^1 x^2dx=\frac{1}{3}x^3\bigg|_0^1=\frac{1}{3}-0=\frac{1}{3}$
> 这正是 §1 中用无限求和的方法求出的曲边三角形的面积

> 例7-10: 求 $\int_0^\pi\sin xdx$
> 因为 $-\cos x$ 是 $\sin x$ 的一个原函数,
> 所以 $\int_0^\pi\sin xdx=(-\cos x)\big|_0^\pi=-\cos\pi+\cos0=2$
> $y=\sin x$ 的一拱的面积为整数 $2$

> 例7-11: 计算 $\lim\limits_{n\to\infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}\right)$
> 将和式改写为 $\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}$
> $=\frac{1}{n}\left(\frac{1}{1+\frac{1}{n}}+\frac{1}{1+\frac{2}{n}}+\cdots+\frac{1}{1+\frac{n}{n}}\right)$
>
> 这相当于在 $[0,1]$ 中对函数 $f(x)=\frac{1}{1+x}$ 作 $\Delta x_i=\frac{1}{n}$ 的等距分割后,
> 在小区间 $[x_{i-1},x_i]$ 上将 $\xi_i$ 取为 $x_i$ 的 Riemann 和 $\sum_{i=1}^n f(\xi_i)\cdot\Delta x_i$
>
> 于是 $\lim\limits_{n\to\infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}\right)$
> $=\int_0^1\frac{1}{1+x}dx=\ln(1+x)\bigg|_0^1=\ln2$


## 定积分的分部积分法和换元积分法

将 $\int f(x)dx$ 理解为 $f(x)$ 的任意一个给定的原函数,
则 Newton-Leibniz 公式可以形式上表达为
$\int_a^b f(x)dx=\left(\int f(x)dx\right)\bigg|_a^b$
因此, 由不定积分的运算法则可直接推出定积分的相应的运算法则

------


定理7.3.3 (分部积分): 设 $u(x),v(x)$ 在区间 $[a,b]$ 上有连续导数,
则
$\int_a^b u(x)v'(x)dx=[u(x)v(x)]\bigg|_a^b-\int_a^b v(x)u'(x)dx$
上式也能写成下列形式 $\int_a^b u(x)dv(x)=[u(x)v(x)]\bigg|_a^b-\int_a^b v(x)du(x)$

------


> 例7-12: 求由曲线 $y=\sin x$ $(0\leq x\leq\pi)$ 和 $x$ 轴围成的面积
> 由定积分的几何意义, 应用分部积分公式
> $S=\int_0^\pi x\sin xdx=(-x\cos x)\bigg|_0^\pi+\int_0^\pi\cos xdx=\pi\sin x\bigg|_0^\pi=\pi$

------


定义7.3.1: 设 $g_n(x)$ 是定义在 $[a,b]$ 上的一列函数 $(n=0,1,2,\cdots)$
若对任意的 $m,n$ 有 $g_m(x)g_n(x)$ 在 $[a,b]$ 上可积,
且有
$\int_a^b g_m(x)g_n(x)dx=\begin{cases}0, & m\neq n\\c_n^2>0, & m=n\end{cases}$
则称 $\{g_n(x)\}$ 是 $[a,b]$ 上的正交函数列
特别地, 当 $g_n(x)$ 是 $n$ 次多项式时, 称 $\{g_n(x)\}$ 是 $[a,b]$ 上的正交多项式列

$n$ 次 Legendre 多项式为 $p_n(x)=\frac{1}{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n$ $(n=0,1,2,\cdots)$
它在 $(-1,1)$ 上恰有 $n$ 个不同的根

------


> 例7-13: 证明 $\{p_n(x)\}$ 是 $[-1,1]$ 上的正交多项式列,
> 即 $\int_{-1}^1 p_m(x)p_n(x)dx=\begin{cases}0, & m\neq n\\\frac{2}{2n+1}, & m=n\end{cases}$
>
> 设 $n\geq m$, 记 $I_{mn}=m!n!2^{m+n}\int_{-1}^1 p_m(x)p_n(x)dx$
> $=\int_{-1}^1\frac{d^m}{dx^m}(x^2-1)^m\cdot\frac{d^n}{dx^n}(x^2-1)^ndx$
> 将 $\frac{d^m}{dx^m}(x^2-1)^n$ 看成 $u(x)$,
> 将 $\frac{d^n}{dx^n}(x^2-1)^n$ 看成 $v'(x)$,
> 利用分部积分法
>
> $I_{mn}=\frac{d^m}{dx^m}(x^2-1)^n\cdot\frac{d^{n-1}}{dx^{n-1}}(x^2-1)^n\bigg|_{-1}^1-\int_{-1}^1\frac{d^{m+1}}{dx^{m+1}}(x^2-1)^n\cdot\frac{d^{n-1}}{dx^{n-1}}(x^2-1)^ndx$
> 由 $\frac{d^{n-1}}{dx^{n-1}}(x^2-1)^n(k=1,2,\cdots,n-1)$ 中都含有 $(x^2-1)$ 因子,
> 因此 $\frac{d^{n-1}}{dx^{n-1}}(x^2-1)^n\bigg|_{x=\pm1}=0$
> 所以 $I_{mn}=-\int_{-1}^1\frac{d^{m+1}}{dx^{m+1}}(x^2-1)^n\cdot\frac{d^{n-1}}{dx^{n-1}}(x^2-1)^ndx$
>
> 反复执行上述过程, 最后得到 $I_{mn}=(-1)^n\int_{-1}^1\left[\frac{d^{m+n}}{dx^{m+n}}(x^2-1)^n\right]\cdot(x^2-1)^ndx$
> 1. 若 $n>m$, 则有 $\frac{d^{m+n}}{dx^{m+n}}(x^2-1)^n\equiv0$,
> 因此 $\int_{-1}^1 p_m(x)p_n(x)dx=0$
>
> 2. 若 $n=m$, 则有 $\frac{d^{2n}}{dx^{2n}}(x^2-1)^n=(2n)!$,
> 再次利用分部积分法
> $I_{nn}=(2n)!\int_{-1}^1(1-x)^n(1+x)^ndx=\frac{(2n)!}{n+1}\int_{-1}^1(1-x)^{n-1}(1+x)^{n+1}dx$
> $=\cdots=\frac{(n!)^22^{2n+1}}{2n+1}$
> 于是便有 $\int_{-1}^1 p_n^2(x)dx=\frac{I_{nn}}{(n!)^22^{2n}}=\frac{2}{2n+1}$

> 例7-14: 求 $I_n=\int_0^{\frac{\pi}{2}}\sin^n xdx$
> 显然 $I_0=\int_0^{\frac{\pi}{2}}\sin^0xdx=\frac{\pi}{2}$,
> $I_1=\int_0^{\frac{\pi}{2}}\sin xdx=1$
>
> 而对于 $n\geq2$
> $I_n=\int_0^{\frac{\pi}{2}}\sin^nxdx=\int_0^{\frac{\pi}{2}}\sin^{n-1}x\cdot\sin xdx$
> $=-\sin^{n-1}x\cos x\bigg|_0^{\frac{\pi}{2}}+(n-1)\int_0^{\frac{\pi}{2}}\sin^{n-2}x\cdot\cos^2xdx$
> $=(n-1)\int_0^{\frac{\pi}{2}}\sin^{n-2}x\cdot(1-\sin^2x)dx=(n-1)(I_{n-2}-I_n)$
>
> 于是得到递推关系 $I_n=\frac{n-1}{n}I_{n-2}$,
> 即
> $\int_0^{\frac{\pi}{2}}\sin^nxdx=\begin{cases}\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdots\frac{1}{2}\cdot\frac{\pi}{2}=\frac{(n-1)!!}{n!!}\cdot\frac{\pi}{2}, & n\text{为偶数}\\\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdots\frac{2}{3}=\frac{(n-1)!!}{n!!}, & n\text{为奇数}\end{cases}$

------


定理7.3.4 (换元积分): 设 $f(x)$ 在区间 $[a,b]$ 上连续,
$x=\varphi(t)$ 在区间 $[\alpha,\beta]$(或 $[\beta,\alpha]$) 上有连续导数
其值域包含于 $[a,b]$, 且满足 $\varphi(\alpha)=a$ 和 $\varphi(\beta)=b$,
则
$\int_a^b f(x)dx=\int_\alpha^\beta f(\varphi(t))\varphi'(t)dt$

证明: 因为 $f(x)$ 连续, 所以必有原函数
设 $F(x)$ 为 $f(x)$ 的某个原函数, 由复合函数求导法则,
可知 $F(\varphi(t))$ 是 $f(\varphi(t))\varphi'(t)$ 的一个原函数

按 Newton-Leibniz 公式, 则有 $\int_\alpha^\beta f(\varphi(t))\varphi'(t)dt$
$=F(\varphi(\beta))-F(\varphi(\alpha))$
$=F(b)-F(a)=\int_a^b f(x)dx$

[换元后的定积分 $\int_\alpha^\beta f(\varphi(t))\varphi'(t)dt$ 的上下限 $\alpha$ 和 $\beta$ 必须与原来定积分的上下限 $a$ 和 $b$ 相对应,
而不必考虑 $\alpha$ 与 $\beta$ 之间谁大谁小]

------


> 例7-15: 求 $\int_1^2\frac{dx}{x(1+x^4)}$
> 令 $x=\varphi(t)=\frac{1}{t}$,
>
> 于是 $dx=-\frac{1}{t^2}dt$(也可以对等式 $x^4=t$ 的两边求对数后微分,
> 得到 $\frac{dx}{x}=\frac{dt}{4t}$)
>
> 因为 $\varphi(1)=1$, $\varphi(16)=2$,
> 所以积分区间由 $x\in[1,2]$ 变为 $t\in[1,16]$
>
> 应用换元积分公式 $\int_1^2\frac{dx}{x(1+x^4)}=\int_1^{16}\frac{dt}{4t(1+t)}$
> $=\left(\frac{1}{4}\ln\frac{t}{1+t}\right)\bigg|_1^{16}$
> $=\frac{1}{4}\ln\frac{32}{17}$

> 例7-16: 求 $\int_0^{\frac{\pi}{2}}\sin^3x\cos^4xdx$
> 对积分作如下的变形 $\int_0^{\frac{\pi}{2}}\sin^3x\cos^4xdx=-\int_0^{\frac{\pi}{2}}(1-\cos^2x)\cos^4xd(\cos x)$
>
> 令 $\cos x=t$, 因为当 $x=0$ 时 $t=1$,
> 当 $x=\frac{\pi}{2}$ 时 $t=0$,
> 于是
>
> $\int_0^{\frac{\pi}{2}}\sin^3x\cos^4xdx=-\int_1^0(1-t^2)t^4dt=\int_0^1(t^4-t^6)dt=\frac{2}{35}$
> [换元后的积分上下限必须对应, 不能将积分化简成 $-\int_0^1(1-t^2)t^4dt$]
>
> 本例还可以用例7-14 中得到的递推公式求积分值: $\int_0^{\frac{\pi}{2}}\sin^3x\cos^4xdx$
> $=\int_0^{\frac{\pi}{2}}\sin x(1-\sin^2x)^2dx$
> $=\frac{2}{3}-\frac{4}{5}+\frac{2}{7}=\frac{2}{35}$
>
> 归纳: 对于形如 $\int_0^{\frac{\pi}{2}}\sin^mx\cos^nxdx$ 的积分,
> 当 $m$ 与 $n$ 中有一个是奇数时, 都可以用本例中的换元积分法求出积分值
> 当 $m$ 与 $n$ 都是偶数时, 一般只能通过三角函数的恒等变形(如半角公式等),
> 将三角函数的幂指数降低到 $1$ 后加以解决
>
> 当 $\alpha=0$, $\beta=\frac{\pi}{2}$(或积分可化成 $\int_0^{\frac{\pi}{2}}\sin^mx\cos^nxdx$ 的形式)时,
> 只要 $m$ 与 $n$ 中有一个是偶数, 就可以用例7-14 中得到的递推公式求出积分值

> 例7-17: 求半径为 $r$ 的圆的面积
> 设圆的方程为 $x^2+y^2=r^2$, 利用对称性, 只求它在第一象限部分的面积
> 在第一象限, 它的方程是 $y=\sqrt{r^2-x^2}$,
> 因此相应的面积应为 $\int_0^r\sqrt{r^2-x^2}dx$
>
> 令 $x=r\sin t$, 于是 $dx=r\cos tdt$,
> 积分区间由 $x\in[0,r]$ 变为 $t\in\left[0,\frac{\pi}{2}\right]$,
> 于是
>
> $\int_0^r\sqrt{r^2-x^2}dx=r^2\int_0^{\frac{\pi}{2}}\cos^2tdt$
> $=\frac{r^2}{2}\left(t+\frac{\sin2t}{2}\right)\bigg|_0^{\frac{\pi}{2}}$
> $=\frac{\pi r^2}{4}$
> 因此, 整个圆的面积为 $S=\pi r^2$

[对定积分作变量代换 $x=\varphi(t)$ 时, 并不要求 $\varphi(t)$ 是一个单调的一一对应的函数,
通过换元, 求出关于新变量 $t$ 的定积分后, 就可直接求出定积分的值]
[上述例中若作变换 $x=\varphi(t)=r\cos t$, 虽然 $x=\varphi(t)$ 把 $t\in\left[0,\frac{\pi}{2}\right]$ 变为 $x\in[0,r]$,
但由于 $\varphi\left(\frac{\pi}{2}\right)=0$,
$\varphi(0)=r$, 因此要将积分化成 $\int_{\frac{\pi}{2}}^0\sqrt{r^2-x^2}dx$
$=-r^2\int_{\frac{\pi}{2}}^0\sin^2tdt$]

图7-8: 圆在第一象限的部分

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005507.png =300x)

[定理7.3.4 要求 $x=\varphi(t)$ 的值域包含在区间 $[a,b]$ 中]
[事实上, 即使 $\varphi(t)$ 的值域超出了区间 $[a,b]$,
只要 $\varphi(t)$ 的值域包含在被积函数 $f(x)$ 的连续范围内,
并在区间端点有 $\varphi(\alpha)=a$ 和 $\varphi(\beta)=b$,
定理的证明照样能通过]

> 例7-18: 计算 $\int_{\ln2}^1\frac{dx}{\sqrt{e^x-1}}$
> 作变换 $\sqrt{e^x-1}=u$, 则 $x=\ln(1+u^2)$,
> 当 $x$ 从 $\ln2$ 变到 $1$ 时, $u$ 从 $1$ 变到 $\sqrt{e-1}$
> 且 $dx=\frac{2u}{1+u^2}du$, 于是 $\int_{\ln2}^1\frac{dx}{\sqrt{e^x-1}}$
> $=\int_1^{\sqrt{e-1}}\frac{2u}{u(1+u^2)}du$
> $=2\arctan u\bigg|_1^{\sqrt{e-1}}=2\arctan\sqrt{e-1}-\frac{\pi}{2}$

> 例7-19: 设 $f(x)=\begin{cases}\sin\frac{x}{2}, & x\geq0\\\arctan x, & x<0\end{cases}$,
> 计算 $I=\int_0^{x+1}f(x-1)dx$
> 作变换 $x-1=u$ 得 $I=\int_0^{x+1}f(x-1)dx=\int_{-1}^0 f(u)du+\int_0^x f(u)du$
> $=\int_{-1}^0 u\arctan udu+\int_0^x\sin\frac{u}{2}du$
>
> 由 $\int_{-1}^0 u\arctan udu=\frac{1}{2}\int_{-1}^0\arctan ud(u^2)$
> $=\frac{1}{2}u^2\arctan u\bigg|_{-1}^0-\frac{1}{2}\int_{-1}^0\frac{u^2}{1+u^2}du$
> $=\frac{\pi}{8}-\frac{1}{2}\int_{-1}^0\left(1-\frac{1}{1+u^2}\right)du$
> $=\frac{\pi}{8}-\frac{1}{2}(u-\arctan u)\bigg|_{-1}^0$
> $=\frac{\pi}{4}-\frac{1}{2}$
>
> 与 $\int_0^x\sin\frac{u}{2}du=-2\cos\frac{u}{2}\bigg|_0^x=2$,
> 得到 $I=\frac{\pi}{4}+\frac{3}{2}$

> 例7-20: 计算 $I=\int_0^1\frac{\ln(1+x)}{1+x^2}dx$
> 作变换 $x=\tan t$, 则 $dx=\sec^2tdt$,
> 于是
>
> $I=\int_0^{\frac{\pi}{4}}\ln(1+\tan t)dt=\int_0^{\frac{\pi}{4}}\ln\frac{\sin t+\cos t}{\cos t}dt$
> $=\int_0^{\frac{\pi}{4}}\ln\frac{\sqrt{2}\cos\left(\frac{\pi}{4}-t\right)}{\cos t}dt$
> $=\int_0^{\frac{\pi}{4}}\ln\sqrt{2}dt+\int_0^{\frac{\pi}{4}}\ln\cos\left(\frac{\pi}{4}-t\right)dt-\int_0^{\frac{\pi}{4}}\ln\cos tdt$
>
> 对上式第二个积分作变量变换 $u=\frac{\pi}{4}-t$
> 得 $\int_0^{\frac{\pi}{4}}\ln\cos\left(\frac{\pi}{4}-t\right)dt$
> $=\int_{\frac{\pi}{4}}^0\ln\cos u(-du)=\int_0^{\frac{\pi}{4}}\ln\cos udu$
>
> 因此 $I=\int_0^{\frac{\pi}{4}}\ln\sqrt{2}dt+\int_0^{\frac{\pi}{4}}\ln\cos udu-\int_0^{\frac{\pi}{4}}\ln\cos tdt$
> $=\int_0^{\frac{\pi}{4}}\ln\sqrt{2}dt=\frac{\pi}{8}\ln2$

> 例7-21: 计算 $\int_0^{\frac{\pi}{2}}\frac{\sin^2x}{\sin x+\cos x}dx$
> 作变量代换 $x=\frac{\pi}{2}-t$, 得到 $\int_0^{\frac{\pi}{2}}\frac{\sin^2x}{\sin x+\cos x}dx$
> $=\int_0^{\frac{\pi}{2}}\frac{\cos^2t}{\sin t+\cos t}dt$
>
> 因此 $\int_0^{\frac{\pi}{2}}\frac{\sin^2x}{\sin x+\cos x}dx$
> $=\frac{1}{2}\left(\int_0^{\frac{\pi}{2}}\frac{\sin^2x}{\sin x+\cos x}dx+\int_0^{\frac{\pi}{2}}\frac{\cos^2x}{\sin x+\cos x}dx\right)$
> $=\frac{1}{2}\int_0^{\frac{\pi}{2}}\frac{1}{\sin x+\cos x}dx$
>
> $=\frac{1}{\sqrt{2}}\int_0^{\frac{\pi}{2}}\frac{1}{\sin\left(x+\frac{\pi}{4}\right)}dx$
> $=\frac{1}{2\sqrt{2}}\ln(1+\sqrt{2})$

> 例7-22: 计算 $\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx$
> 先看一个不正确的解法: 由 $\left[\arctan\frac{x(x-2)}{x-1}\right]'=\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}$,
> 于是由 Newton-Leibniz 公式得到
> $\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx=\arctan\frac{x(x-2)}{x-1}\bigg|_0^2=0$
>
> 但这个结果是不可能的, 因为被积函数在 $[0,2]$ 连续且恒大于零,
> 所以必有 $\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx>0$,
> Newton-Leibniz 公式显然"失灵"了
>
> 问题出在微积分基本定理的条件是"$F(x)$ 是 $f(x)$ 在 $[a,b]$ 上的一个原函数",
> 而在这个例子中, 由于 $\arctan\frac{x(x-2)}{x-1}$ 在 $[0,2]$ 中有不连续点 $x=1$,
> 因此它绝不可能是 $\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}$ 在 $[0,2]$ 上的原函数
>
> 在任何一个不含 $x=1$ 的区间上, $\arctan\frac{x(x-2)}{x-1}$ 确实是 $f(x)$ 的原函数,
> 而 $x=1$ 是它的第一类不连续点, 因此作函数
> $F(x)=\begin{cases}\arctan\frac{x(x-2)}{x-1}, & x\in[0,1)\\\frac{\pi}{2}, & x=1\end{cases}$
>
> 可以验证 $F(x)$ 是 $f(x)$ 在 $[0,1]$ 上的原函数
> 同样地, 函数
> $F(x)=\begin{cases}\arctan\frac{x(x-2)}{x-1}, & x\in(1,2]\\\frac{\pi}{2}, & x=1\end{cases}$
> 是 $f(x)$ 在 $[1,2]$ 上的原函数
>
> 正确的方法是利用积分的区间可加性, 分别在区间 $[0,1]$ 和 $[1,2]$ 上应用 Newton-Leibniz 公式,
> 即
>
> $\int_0^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx=\int_0^1\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx+\int_1^2\frac{(x-1)^2+1}{(x-1)^2+x^2(x-2)^2}dx$
> $=F(x)\bigg|_0^1+F(x)\bigg|_1^2=\left[\frac{\pi}{2}-0\right]+\left[0-\left(-\frac{\pi}{2}\right)\right]$
> $=\pi$
> [用 Newton-Leibniz 公式时必须把条件弄清楚]

------


定理7.3.5: 设 $f(x)$ 在对称区间 $[-a,a]$ 上可积
(1) 若 $f(x)$ 是偶函数, 则成立 $\int_{-a}^a f(x)dx=2\int_0^a f(x)dx$
(2) 若 $f(x)$ 是奇函数, 则成立 $\int_{-a}^a f(x)dx=0$

证明: 由 $\int_{-a}^a f(x)dx=\int_{-a}^0 f(x)dx+\int_0^a f(x)dx$
对积分 $\int_{-a}^0 f(x)dx$ 作变量代换 $x=-t$,
得
$\int_{-a}^0 f(x)dx=-\int_a^0 f(-t)dt=\begin{cases}\int_0^a f(x)dx, & f(x)\text{为偶函数}\\-\int_0^a f(x)dx, & f(x)\text{为奇函数}\end{cases}$

从而得到所需结论

------


定理7.3.6: 设 $f(x)$ 是以 $T$ 为周期的可积函数,
则对任意 $a$,
$\int_a^{a+T}f(x)dx=\int_0^T f(x)dx$

------


> 例7-23: 证明函数列 $\{1,\sin x,\cos x,\sin2x,\cos2x,\cdots,\sin nx,\cos nx,\cdots\}$ 是任意一个长度为 $2\pi$ 的区间上的正交函数列
> 考虑区间 $[-\pi,\pi]$ 上的积分
> 将 $1$ 记为 $\cos0x$, 则对任何 $m=1,2,\cdots$ 和 $n=0,1,2,\cdots$,
>
> 由于 $\sin mx\cos nx$ 是奇函数, 所以 $\int_{-\pi}^\pi\sin mx\cos nxdx=0$
> 对任何 $m=1,2,\cdots$ 和 $n=1,2,\cdots$,
>
> 由于 $\sin mx\sin nx$ 是偶函数
> $\int_{-\pi}^\pi\sin mx\sin nxdx=2\int_0^\pi\sin mx\sin nxdx=\int_0^\pi[\cos(m-n)x-\cos(m+n)x]dx=\begin{cases}0, & m\neq n\\\pi, & m=n\end{cases}$
>
> 同理可证, 对任何 $m=0,1,2,\cdots$ 和 $n=0,1,2,\cdots$,
> 有
>
> $\int_{-\pi}^\pi\cos mx\cos nxdx=\begin{cases}0, & m\neq n\\\pi, & m=n\neq0\\2\pi, & m=n=0\end{cases}$
> 由定义7.3.1, 这组函数确是 $[-\pi,\pi]$ 上的正交函数列
> 又由于 $2\pi$ 是这些函数的公共周期, 由定理7.3.6,
> 即知这组函数是任意一个长度为 $2\pi$ 的区间上的正交函数列


## 求平面图形的面积

考虑由连续曲线 $y=f(x)$, 直线 $x=a$, $x=b$ 和 $y=0$(即 $x$ 轴)所围区域的面积
当 $f(x)>0$ 时, 面积为 $\int_a^b f(x)dx$
当 $f(x)<0$ 时, 面积为 $\int_a^b[-f(x)]dx$

当 $f(x)$ 在区间 $[a,b]$ 上不保持定号时,
所求的面积应为
$S=\int_a^b|f(x)|dx$
进一步得到夹在连续曲线 $y=f(x)$ 和 $y=g(x)$ 之间,
左右分别由直线 $x=a$, $x=b$ 界定的那部分区域的面积为
$S=\int_a^b|f(x)-g(x)|dx$

若 $y=f(x)$ 用参数形式 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$ 表达,
$x(t)$ 在 $[T_1,T_2]$ 上具有连续导数,
且 $x'(t)\neq0$,
则由换元法可证所求的面积可表示成
$S=\int_{T_1}^{T_2}|y(t)x'(t)|dt$

------


下面导出极坐标下的求面积公式
设曲线的极坐标方程 $r=r(\theta)$ 是区间 $[\alpha,\beta]$ 上的连续函数 $(\beta-\alpha\leq2\pi)$,
求由 $\theta=\alpha$, $\theta=\beta$ 与 $r=r(\theta)$ 围成的图形的面积 $S$

在 $[\alpha,\beta]$ 中取一系列的分点 $\theta_i$,
满足 $\alpha=\theta_0<\theta_1<\theta_2<\cdots<\theta_n=\beta$,
记 $\Delta\theta_i=\theta_i-\theta_{i-1}$
在每个 $[\theta_{i-1},\theta_i]$ 上任取一点 $\xi_i$,
用半径为 $r(\xi_i)$, 圆心角为 $\Delta\theta_i$ 的小扇形的面积 $\frac{1}{2}r^2(\xi_i)\Delta\theta_i$ 近似代替相应的小曲边扇形的面积,
那么
$S\approx\frac{1}{2}\sum_{i=1}^n r^2(\xi_i)\Delta\theta_i$

因为 $r=r(\theta)$ 在 $[\alpha,\beta]$ 中连续,
所以 $\frac{1}{2}r^2(\theta)$ 在 $[\alpha,\beta]$ 上可积
令小扇形的圆心角的最大值 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta\theta_i\}\to0$,
即有
$S=\frac{1}{2}\lim\limits_{\lambda\to0}\sum_{i=1}^n r^2(\xi_i)\Delta\theta_i$
$=\frac{1}{2}\int_\alpha^\beta r^2(\theta)d\theta$

图7-9: 极坐标下小曲边扇形的分割

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005508.png =400x)

------


> 例7-24: 计算由曲线 $y=x^2$ 和 $y=\sqrt{x}$ 所围区域的面积
> 求出曲线 $y=x^2$ 和 $y=\sqrt{x}$ 的交点坐标为 $(0,0)$ 和 $(1,1)$,
> 而在 $x\in[0,1]$ 中 $\sqrt{x}\geq x^2$,
> 因此
> $S=\int_0^1(\sqrt{x}-x^2)dx=\left(\frac{2}{3}x^{\frac{3}{2}}-\frac{1}{3}x^3\right)\bigg|_0^1$
> $=\frac{1}{3}$

图7-10: 曲线 $y=x^2$ 与 $y=\sqrt{x}$ 所围的区域

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005509.png =350x)

> 例7-25: 设 $(x,y)$ 是等轴双曲线 $x^2-y^2=1$ 上的任意一点,
> 求由双曲线与连接点 $(x,y)$ 和原点的线段, 连接点 $(x,-y)$ 和原点的线段所围成的曲边三角形的面积 $t$
>
> 不妨设 $x>0$, 利用对称性, 可求出位于第一象限的那部分面积再乘以 $2$;
> 而对那部分面积,
> 可以先求出由双曲线, $x$ 轴及过点 $(x,y)$ 并与 $y$ 轴平行的直线所围区域的面积,
> 再用大三角形的面积 $\frac{xy}{2}$ 减去它
>
> $t=2\left(\frac{xy}{2}-\int_1^x\sqrt{u^2-1}du\right)=xy-\left(x\sqrt{x^2-1}-\ln\left|x+\sqrt{x^2-1}\right|\right)$
> $=xy-x\sqrt{x^2-1}+\ln(x+\sqrt{x^2-1})=\ln(x+y)$
>
> 由此得到 $x+y=e^t$, 由于 $x^2-y^2=1$,
> 两式相除便有 $x-y=e^{-t}$,
> 于是解得
> $\begin{cases}x=\frac{e^t+e^{-t}}{2}=\text{ch}\,t,\\y=\frac{e^t-e^{-t}}{2}=\text{sh}\,t\end{cases}$
>
> [三角函数又称圆函数, 因为在单位圆上取点 $(x,y)$ 和 $(x,-y)$ 时,
> 由圆弧与连接点 $(x,y)$ 和原点的线段, 连接点 $(x,-y)$ 和原点的线段所围成的扇形面积为 $t$ 时有 $x=\cos t$,
> $y=\sin t$]
>
> [两相比较, 把 $y=\text{sh}\,x$, $y=\text{ch}\,x$ 统称为双曲函数,
> 并分别冠以双曲正弦和双曲余弦的名称]

图7-11: 等轴双曲线上的曲边三角形

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005510.png =400x)

> 例7-26: 求椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 的面积
> 利用对称性, 只求第一象限的那一块面积, 将椭圆写成参数方程形式 $\begin{cases}x=a\cos t,\\y=b\sin t\end{cases}$
> 则当 $x$ 从 $0$ 变到 $a$ 时, $t$ 从 $\frac{\pi}{2}$ 变到 $0$,
> 所以
>
> $\frac{S}{4}=ab\int_{\frac{\pi}{2}}^0\sin t(\cos t)'dt=ab\int_0^{\frac{\pi}{2}}\sin^2tdt$
> $=\frac{\pi}{4}ab$
> 即 $S=\pi ab$

> 例7-27: 求旋轮线(摆线)
> $\begin{cases}x=a(t-\sin t),\\y=a(1-\cos t),\end{cases}t\in[0,2\pi]$
> 与 $x$ 轴所围区域的面积
> 图7-12 为摆线的一拱
> $S=a^2\int_0^{2\pi}(1-\cos t)^2dt=a^2\int_0^{2\pi}\left(1-2\cos t+\frac{1+\cos2t}{2}\right)dt$
> $=3\pi a^2$

图7-12: 摆线的一拱

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005511.png =500x)

> 例7-28: 求双曲螺线 $r\theta=a$ 当 $\theta$ 从 $\frac{\pi}{4}$ 变到 $2\pi+\frac{\pi}{4}$ 时,
> 极径 $r$ 扫过的面积
> 直接用极坐标下的求面积公式
> $S=\frac{a^2}{2}\int_{\frac{\pi}{4}}^{\frac{9\pi}{4}}\frac{1}{\theta^2}d\theta$
> $=\frac{a^2}{2}\left(-\frac{1}{\theta}\right)\bigg|_{\frac{\pi}{4}}^{\frac{9\pi}{4}}$
> $=\frac{16a^2}{9\pi}$

图7-13: 双曲螺线 $\theta r=a$

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005512.png =350x)

> 例7-29: 求三叶玫瑰线 $r=a\sin3\theta$,
> $\theta\in[0,\pi]$ 所围区域的面积
> 由对称性, 只求半叶"玫瑰"的面积, 这时 $\theta$ 的变化范围是 $\left[0,\frac{\pi}{6}\right]$
> $S=6\cdot\frac{a^2}{2}\int_0^{\frac{\pi}{6}}\sin^23\theta d\theta$
> $=a^2\int_0^{\frac{\pi}{2}}\sin^2\varphi d\varphi$
> $=\frac{\pi a^2}{4}$

图7-14: 三叶玫瑰线 $r=a\sin3\theta$

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005513.png =350x)


## 求曲线的弧长

设平面曲线的参数方程为 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$
对区间 $[T_1,T_2]$ 作如下划分 $T_1=t_0<t_1<t_2<\cdots<t_n=T_2$
得到这条曲线上顺次排列的 $n+1$ 个点 $P_0,P_1,\cdots,P_n$,
$P_i=(x(t_i),y(t_i))$
用 $\overline{P_{i-1}P_i}$ 表示联结 $P_{i-1}$ 和 $P_i$ 的直线段的长度,
那么相应的折线的长度可以表示为 $\sum_{i=1}^n\overline{P_{i-1}P_i}$

若当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta t_i\}\to0$ 时,
极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^n\overline{P_{i-1}P_i}$ 存在,
且极限值与区间 $[T_1,T_2]$ 的划分无关, 则称这条曲线是可求长的,
并将此极限值
$l=\lim\limits_{\lambda\to0}\sum_{i=1}^n\overline{P_{i-1}P_i}$
称为该条曲线的弧长

按定义得到的和式 $\sum_{i=1}^n\overline{P_{i-1}P_i}$ 并非是 Riemann 和 $\sum_{i=1}^n f(\xi_i)\Delta t_i$ 的形式
为了能够用定积分来求弧长, 首先必须将它化成 Riemann 和的形式

显然 $\overline{P_{i-1}P_i}=\sqrt{[x(t_i)-x(t_{i-1})]^2+[y(t_i)-y(t_{i-1})]^2}$
若 $x(t)$ 和 $y(t)$ 在 $[T_1,T_2]$ 中连续,
在 $(T_1,T_2)$ 中可导, 则由 Lagrange 中值定理,
存在 $\eta_i$ 和 $\sigma_i$ 属于 $[t_{i-1},t_i]$,
满足
$x(t_i)-x(t_{i-1})=x'(\eta_i)\Delta t_i$,
$y(t_i)-y(t_{i-1})=y'(\sigma_i)\Delta t_i$

于是
$\sum_{i=1}^n\overline{P_{i-1}P_i}=\sum_{i=1}^n\sqrt{[x'(\eta_i)]^2+[y'(\sigma_i)]^2}\cdot\Delta t_i$
由于 $\eta_i$ 和 $\sigma_i$ 一般不会相同, 上式还不是 Riemann 和 $\sum_{i=1}^n\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\cdot\Delta t_i$,
$\xi_i\in[t_{i-1},t_i]$ 的形式, 但两者已相当接近了

------


定义7.4.1: 若 $x'(t)$ 和 $y'(t)$ 在 $[T_1,T_2]$ 上连续,
且 $[x'(t)]^2+[y'(t)]^2\neq0$, 则由参数方程
$\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$
确定的曲线称为光滑曲线
[光滑曲线上的切线是连续变动的]

------


定理7.4.1 (弧长公式): 若由参数方程 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$ 确定的曲线是光滑曲线,
则它是可求长的, 其弧长为
$l=\int_{T_1}^{T_2}\sqrt{[x'(t)]^2+[y'(t)]^2}dt$

证明: 对区间 $[T_1,T_2]$ 的任意划分, 有
$\left|\sum_{i=1}^n\overline{P_{i-1}P_i}-\sum_{i=1}^n\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\Delta t_i\right|$
$=\left|\sum_{i=1}^n\sqrt{[x'(\eta_i)]^2+[y'(\sigma_i)]^2}\Delta t_i-\sum_{i=1}^n\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\Delta t_i\right|$
$\leq\sum_{i=1}^n\left|\sqrt{[x'(\eta_i)]^2+[y'(\sigma_i)]^2}-\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\right|\Delta t_i$

由三角不等式 $|\sqrt{x_1^2+x_2^2}-\sqrt{y_1^2+y_2^2}|\leq\sqrt{(x_1-y_1)^2+(x_2-y_2)^2}$
$\leq|x_1-y_1|+|x_2-y_2|$,
得到
$\left|\sum_{i=1}^n\overline{P_{i-1}P_i}-\sum_{i=1}^n\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\Delta t_i\right|$
$\leq\sum_{i=1}^n|x'(\eta_i)-x'(\xi_i)|\Delta t_i+\sum_{i=1}^n|y'(\sigma_i)-y'(\xi_i)|\Delta t_i$
$\leq\sum_{i=1}^n\bar{\omega}_i\Delta t_i+\sum_{i=1}^n\tilde{\omega}_i\Delta t_i$
其中 $\bar{\omega}_i$ 和 $\tilde{\omega}_i$ 分别是 $x'(t)$ 和 $y'(t)$ 在 $[t_{i-1},t_i]$ 中的振幅

因为 $x'(t)$ 和 $y'(t)$ 在 $[T_1,T_2]$ 上可积,
由定积分存在的充分必要条件, 当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta t_i\}\to0$ 时,
有 $\sum_{i=1}^n\bar{\omega}_i\Delta t_i\to0$ 及 $\sum_{i=1}^n\tilde{\omega}_i\Delta t_i\to0$

于是 $l=\lim\limits_{\lambda\to0}\sum_{i=1}^n\overline{P_{i-1}P_i}$
$=\lim\limits_{\lambda\to0}\sum_{i=1}^n\sqrt{[x'(\xi_i)]^2+[y'(\xi_i)]^2}\Delta t_i$
$=\int_{T_1}^{T_2}\sqrt{[x'(t)]^2+[y'(t)]^2}dt$

将 $dl=\sqrt{[x'(t)]^2+[y'(t)]^2}dt$ 称为弧长的微分

当曲线采用直角坐标系下的显式方程 $y=f(x)$, $x\in[a,b]$ 时,
容易得到相应的弧长公式
$l=\int_a^b\sqrt{1+[f'(x)]^2}dx$

当曲线采用极坐标方程 $r=r(\theta)$, $\theta\in[\alpha,\beta]$ 时,
由于 $x=r(\theta)\cos\theta$, $y=r(\theta)\sin\theta$,
因此
$x'(\theta)=r'(\theta)\cos\theta-r(\theta)\sin\theta$,
$y'(\theta)=r'(\theta)\sin\theta+r(\theta)\cos\theta$
所以 $[x'(\theta)]^2+[y'(\theta)]^2=[r(\theta)]^2+[r'(\theta)]^2$,
于是
$l=\int_\alpha^\beta\sqrt{[r(\theta)]^2+[r'(\theta)]^2}d\theta$

图7-15: 曲线的折线逼近

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005514.png =500x)

------


> 例7-30: 求半径为 $a$ 的圆的周长
> 解法一: 采用直角坐标系下的显式方程 $y=\sqrt{a^2-x^2}$,
> 只求第一象限部分
>
> $l=4\int_0^a\sqrt{1+[f'(x)]^2}dx=4a\int_0^a\frac{dx}{\sqrt{a^2-x^2}}$
> $=4a\cdot\arcsin\frac{x}{a}\bigg|_0^a$
> $=2\pi a$
>
> 解法二: 采用直角坐标系下的参数方程 $\begin{cases}x=a\cos t,\\y=a\sin t,\end{cases}$ 同样只求第一象限部分
> $l=4a\int_0^{\frac{\pi}{2}}\sqrt{\cos^2t+\sin^2t}dt=2\pi a$
>
> 解法三: 采用极坐标方程 $r=a$, $\theta\in[0,2\pi]$,
> 这时 $r'=0$, 因此
> $l=\int_0^{2\pi}\sqrt{[r(\theta)]^2+[r'(\theta)]^2}d\theta=a\int_0^{2\pi}d\theta=2\pi a$
> [采用不同的方程形式求曲线的弧长, 难易程度会有所不同]

> 例7-31: 求摆线一拱的弧长
> $l=a\int_0^{2\pi}\sqrt{(1-\cos t)^2+\sin^2t}dt=\sqrt{2}a\int_0^{2\pi}\sqrt{1-\cos t}dt$
> $=2a\int_0^{2\pi}\sin\frac{t}{2}dt=8a$

用同样的方法, 可将定理7.4.1 的结论推广到求空间曲线的弧长,
设 $x'(t),y'(t),z'(t)$ 在 $[T_1,T_2]$ 上连续,
且 $[x'(t)]^2+[y'(t)]^2+[z'(t)]^2\neq0$,
由参数方程 $\begin{cases}x=x(t),\\y=y(t),\\z=z(t),\end{cases}t\in[T_1,T_2]$ 确定的曲线的弧长为
$l=\int_{T_1}^{T_2}\sqrt{[x'(t)]^2+[y'(t)]^2+[z'(t)]^2}dt$

> 例7-32: 求圆锥螺线 $\begin{cases}x=at\cos t,\\y=-at\sin t,\\z=bt\end{cases}$ 第一圈的长度
> $l=\int_0^{2\pi}\sqrt{a^2[\cos t-t\sin t]^2+a^2[-\sin t-t\cos t]^2+b^2}dt$
>
> $=\int_0^{2\pi}\sqrt{a^2t^2+a^2+b^2}dt=\frac{a}{2}\left(t\sqrt{t^2+s^2}+s^2\ln\left|t+\sqrt{t^2+s^2}\right|\right)\bigg|_0^{2\pi}$
> $=a\left(\pi\sqrt{4\pi^2+s^2}+\frac{s^2}{2}\ln\frac{2\pi+\sqrt{4\pi^2+s^2}}{s}\right)$
>
> 其中 $\frac{b^2}{a^2}+1=s^2$
> 当 $b=0$ 时, 圆锥螺线退化为平面上的 Archimedes 螺线,
>
> 此时 $s^2=1$, 因此
> $l=\frac{a}{2}\left[2\pi\sqrt{4\pi^2+1}+\ln\left(2\pi+\sqrt{4\pi^2+1}\right)\right]$
> 这正是 Archimedes 螺线 $r=a\theta$ 第一圈的长度

图7-16: 圆锥螺线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005515.png =400x)


## 求某些特殊的几何体的体积

设三维空间中的一个几何体夹在平面 $x=a$ 和 $x=b$ 之间,
若对于任意 $x\in[a,b]$,
过 $x$ 点且与 $x$ 轴垂直的平面与该几何体相截, 截面的面积 $A(x)$ 是已知的,
且 $A(x)$ 又是 $[a,b]$ 上的连续函数, 则可以用定积分计算出它的体积

对区间 $[a,b]$ 作划分 $a=x_0<x_1<x_2<\cdots<x_n=b$,
记小区间 $[x_{i-1},x_i]$ 的长度为 $\Delta x_i=x_i-x_{i-1}$
在每个小区间上取一点 $\xi_i$, 用底面积为 $A(\xi_i)$,
高为 $\Delta x_i$ 的柱体体积近似代替夹在平面 $x=x_{i-1}$ 和 $x=x_i$ 之间的那块小几何体的体积,
那么这些柱体体积之和 $\sum_{i=1}^n A(\xi_i)\Delta x_i$ 就是整个几何体体积的近似

由于 $A(x)$ 在 $[a,b]$ 上连续, 当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta x_i\}\to0$ 时,
即知
$V=\lim\limits_{\lambda\to0}\sum_{i=1}^n A(\xi_i)\Delta x_i=\int_a^b A(x)dx$
就是所要求的几何体的体积

[祖暅原理: "夫叠綦成立积, 缘幂势既同, 则积不容异". 一个几何体("立积")是由一系列很薄的小片("基")叠成的;
若两个几何体相应的小片的截面积("幂势")都相同,
则它们的体积("积")必然相等]
[意大利数学家 Cavalieri 在 1635 年得到了同样的结论,
但比祖暅迟了一千多年]

图7-17: 截面面积已知的几何体

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005516.png =350x)

------


> 例7-33: 已知一个直圆柱体的底面半径为 $a$, 平面 $P_1$ 过其底面圆周上的一点,
> 且与其底面所在的平面 $P_2$ 成夹角 $\theta$,
> 求圆柱体被 $P_1$ 与 $P_2$ 所截得的那部分的体积
>
> 建立坐标系, 将平面 $P_2$ 取成 $xy$ 平面, 并使得圆柱体底面的圆心与原点重合,
> 同时让 $P_1$ 与圆柱体底面圆周的交点落在 $y$ 轴上
>
> 对于任意 $y\in[-a,a]$, 过 $y$ 点且与 $y$ 轴垂直的平面与该几何体的截面是一个竖立的矩形,
> 它的底为 $2\sqrt{a^2-y^2}$, 高为 $(y+a)\tan\theta$,
> 于是
>
> $A(y)=2\sqrt{a^2-y^2}(y+a)\cdot\tan\theta$
> 因此, 所求的体积为 $V=2\tan\theta\left(\int_{-a}^a y\sqrt{a^2-y^2}dy+a\int_{-a}^a\sqrt{a^2-y^2}dy\right)$
>
> 容易看出, 括号内的第一项是一个奇函数在对称区间上的积分,
> 其值为 $0$,
>
> 第二项中的积分恰为上半圆的面积, 即得到
> $V=\pi a^3\tan\theta$
>
> [对几何体作截面的方式与计算是否简便关系很大, 在实际计算时要根据具体情况仔细分析,
> 找到最简便的方案]

图7-18: 圆柱体被平面 $P_1$ 所截

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005517.png =350x)

旋转体是公式 $V=\int_a^b A(x)dx$ 的一个很重要的用途
设函数 $f(x)$ 在 $[a,b]$ 上连续, 对于由 $0\leq y\leq|f(x)|$ 与 $a\leq x\leq b$ 所界定的那块平面图形绕 $x$ 轴旋转一周得到的旋转体
若用过 $x$ 点且与 $x$ 轴垂直的平面去截, 得到的截面显然是一个半径为 $|f(x)|$ 的圆,
因此它的面积为 $A(x)=\pi[f(x)]^2$

所以该旋转体的体积计算公式为 $V=\pi\int_a^b[f(x)]^2dx$

设曲线的参数方程为 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$
假设在 $[T_1,T_2]$ 上, $x'(t)$ 和 $y(t)$ 连续,
且 $x'(t)\neq0$, 对上式作变量代换, 即得到相应的旋转体的体积公式
$V=\pi\int_{T_1}^{T_2}y^2(t)|x'(t)|dt$

图7-19: 旋转体

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005518.png =350x)

> 例7-34: 求半径为 $a$ 的球的体积
> 即求上半圆周 $y=\sqrt{a^2-x^2}$ 与 $x$ 轴围成的那个半圆绕 $x$ 轴旋转一周所得的旋转体的体积
> $V=\pi\int_{-a}^a(a^2-x^2)dx=\pi\left(a^2x-\frac{x^3}{3}\right)\bigg|_{-a}^a=\frac{4}{3}\pi a^3$

> 例7-35: 求旋轮线一拱与 $x$ 轴围成的图形绕 $x$ 轴旋转一周所得的旋转体的体积
> 将旋轮线的参数方程代入求旋转体体积的公式
> $V=\pi\int_{T_1}^{T_2}y^2(t)|x'(t)|dt=\pi a^3\int_0^{2\pi}(1-\cos t)^3dt=5\pi^2a^3$

极坐标下由 $0\leq r\leq r(\theta)(\theta\in[\alpha,\beta]\subset[0,\pi])$ 所表示的区域绕极轴旋转一周所得的旋转体的体积为
$V=\frac{2}{3}\pi\int_\alpha^\beta r^3(\theta)\sin\theta d\theta$


## 求旋转曲面的面积

确定平面上的一段光滑曲线, 且在 $[T_1,T_2]$ 上 $y(t)\geq0$,
它绕 $x$ 轴旋转一周得到一个旋转曲面

对区间 $[T_1,T_2]$ 作划分 $T_1=t_0<t_1<t_2<\cdots<t_n=T_2$
由此得到曲线上顺次排列的 $n+1$ 个点 $P_0,P_1,\cdots,P_n$,
$P_i=(x(t_i),y(t_i))$
记 $\Delta S_i$ 是联结 $P_{i-1}$ 和 $P_i$ 的直线段绕 $x$ 轴旋转一周得到的圆台侧面的面积,
则
$\Delta S_i=\pi[y(t_{i-1})+y(t_i)]\cdot\overline{P_{i-1}P_i}$

若当 $\lambda=\max\limits_{1\leq i\leq n}\{\Delta t_i\}\to0$ 时,
极限 $\lim\limits_{\lambda\to0}\sum_{i=1}^n\Delta S_i=\pi\lim\limits_{\lambda\to0}\sum_{i=1}^n[y(t_{i-1})+y(t_i)]\cdot\overline{P_{i-1}P_i}$ 存在,
且极限值与区间 $[T_1,T_2]$ 的划分无关, 则称极限值
$S=\lim\limits_{\lambda\to0}\sum_{i=1}^n\Delta S_i=\pi\lim\limits_{\lambda\to0}\sum_{i=1}^n[y(t_{i-1})+y(t_i)]\cdot\overline{P_{i-1}P_i}$
为该段曲线绕 $x$ 轴旋转一周所得到的旋转曲面的面积

与求曲线长度时的讨论一样, 可以得到
$S=2\pi\int_{T_1}^{T_2}y(t)\sqrt{[x'(t)]^2+[y'(t)]^2}dt$
利用弧长的微分公式, 也可以将上式写成 $S=2\pi\int_{T_1}^{T_2}y(t)dl$

图7-20: 旋转曲面

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005519.png =350x)

------


> 例7-36: 求半径为 $a$ 的球的表面积
> 即求半径为 $a$ 的圆的上半部分 $y=\sqrt{a^2-x^2}$ 绕 $x$ 轴旋转一周所得的旋转曲面的面积
> $S=2\pi\int_{-a}^a f(x)\sqrt{1+[f'(x)]^2}dx=2\pi a\int_{-a}^a\frac{\sqrt{a^2-x^2}}{\sqrt{a^2-x^2}}dx$
> $=4\pi a^2$

> 例7-37: 求旋轮线一拱绕 $x$ 轴旋转一周所得旋转曲面的面积
> 将旋轮线的参数方程代入求旋转曲面面积的公式
> $S=2\pi a^2\int_0^{2\pi}(1-\cos t)\sqrt{(1-\cos t)^2+\sin^2t}dt$
> $=2\sqrt{2}\pi a^2\int_0^{2\pi}(1-\cos t)\sqrt{1-\cos t}dt$
> $=16\pi a^2\int_0^{2\pi}\sin^3\frac{t}{2}d\left(\frac{t}{2}\right)=\frac{64}{3}\pi a^2$

------


将本节得到的计算公式列成下面的简表, 在使用这些公式的时候务必注意它们的使用范围和条件,
尤其是采用参数方程时积分上下限的取法

| | 直角坐标显式方程 $y=f(x),x\in[a,b]$ | 直角坐标参数方程 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$ | 极坐标方程 $r=r(\theta),\theta\in[\alpha,\beta]$ |
|---|---|---|---|
| 平面图形面积 | $\int_a^b f(x)dx$ | $\int_{T_1}^{T_2}\lvert y(t)x'(t)\rvert dt$ | $\frac{1}{2}\int_\alpha^\beta r^2(\theta)d\theta$ |
| 弧长的微分 | $dl=\sqrt{1+[f'(x)]^2}dx$ | $dl=\sqrt{[x'(t)]^2+[y'(t)]^2}dt$ | $dl=\sqrt{r^2(\theta)+[r'(\theta)]^2}d\theta$ |
| 曲线弧长 | $\int_a^b\sqrt{1+[f'(x)]^2}dx$ | $\int_{T_1}^{T_2}\sqrt{[x'(t)]^2+[y'(t)]^2}dt$ | $\int_\alpha^\beta\sqrt{r^2(\theta)+[r'(\theta)]^2}d\theta$ |
| 旋转体体积 | $\pi\int_a^b[f(x)]^2dx$ | $\pi\int_{T_1}^{T_2}y^2(t)\lvert x'(t)\rvert dt$ | $\frac{2}{3}\pi\int_\alpha^\beta r^3(\theta)\sin\theta d\theta$ |
| 旋转曲面面积 | $2\pi\int_a^b\lvert f(x)\rvert\sqrt{1+[f'(x)]^2}dx$ | $2\pi\int_{T_1}^{T_2}\lvert y(t)\rvert\sqrt{[x'(t)]^2+[y'(t)]^2}dt$ | $2\pi\int_\alpha^\beta r(\theta)\sin\theta\sqrt{r^2(\theta)+[r'(\theta)]^2}d\theta$ |


## 曲线的曲率

在铁路设计时, 在拐弯处不能让弯曲程度太大, 否则火车在运行时就会出现危险
考察图7-21 所示的两条光滑曲线 $C$ 和 $C'$ 上的曲线段 $\overset{\frown}{AB}$ 和 $\overset{\frown}{A'B'}$,
它们的弧长分别记为 $\Delta s$ 与 $\Delta s'$
当动点从 $A$ 点沿曲线段 $\overset{\frown}{AB}$ 运动到 $B$ 点时,
$A$ 点的切线 $\tau_A$ 也随着转动到 $B$ 点的切线 $\tau_B$
记这两条切线之间的夹角为 $\Delta\varphi$(它等于 $\tau_B$ 和 $x$ 轴的交角与 $\tau_A$ 和 $x$ 轴的交角之差); 同样地,
记曲线段 $\overset{\frown}{A'B'}$ 的两个端点 $A',B'$ 处的切线 $\tau_{A'}$ 和 $\tau_{B'}$ 的夹角为 $\Delta\varphi'$

当弧的长度相同时, 则切线间的夹角愈大, 曲线的弯曲程度就愈大;
而当切线间的夹角相同时,
则弧的长度愈小, 同样曲线的弯曲程度就愈大

也就是说, 如果 $\Delta s'=\Delta s$,
而 $\Delta\varphi'>\Delta\varphi$,
那么可以认为 $\overset{\frown}{A'B'}$ 的弯曲程度比 $\overset{\frown}{AB}$ 的弯曲程度大; 反之,
如果 $\Delta\varphi'=\Delta\varphi$,
而 $\Delta s'<\Delta s$,
那么同样可以认为 $\overset{\frown}{A'B'}$ 的弯曲程度比 $\overset{\frown}{AB}$ 的弯曲程度大

图7-21: 曲率定义的几何背景

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005520.png =600x)

定义: 称 $K=\left|\frac{\Delta\varphi}{\Delta s}\right|$ 为曲线段 $\overset{\frown}{AB}$ 的平均曲率,
它刻画了曲线段 $\overset{\frown}{AB}$ 的平均弯曲程度

平均曲率只描写了曲线 $C$ 在这一段的"平均弯曲程度",
$B$ 越接近于 $A$,
即 $\Delta s$ 越小, $\overset{\frown}{AB}$ 弧的平均曲率就越能精确刻画曲线 $C$ 在 $A$ 处的弯曲程度,
因此定义
$K=\lim\limits_{\Delta s\to0}\left|\frac{\Delta\varphi}{\Delta s}\right|$
$=\left|\frac{d\varphi}{ds}\right|$
为曲线 $C$ 在 $A$ 点的曲率
[这里取绝对值是为了使曲率不为负数]

设曲线 $C$ 在点 $A$ 处的曲率 $K\neq0$,
若过 $A$ 点作一个半径为 $\frac{1}{K}$ 的圆,
使它在 $A$ 点处与曲线 $C$ 有相同的切线, 并在 $A$ 点附近与该曲线位于切线的同侧,
则把这个圆称为曲线 $C$ 在点 $A$ 处的曲率圆或密切圆
曲率圆的半径 $R=\frac{1}{K}$ 和圆心 $A_0$ 分别称为曲线 $C$ 在点 $A$ 处的曲率半径和曲率中心
[由曲率圆的定义可以知道, 曲线 $C$ 在点 $A$ 处与曲率圆既有相同的切线,
又有相同的曲率和凸性]

图7-22: 曲率圆

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005521.png =400x)

设光滑曲线由参数方程 $\begin{cases}x=x(t),\\y=y(t),\end{cases}\alpha\leq t\leq\beta$ 确定,
且 $x(t),y(t)$ 有二阶导数

对于每个 $t\in[\alpha,\beta]$, 曲线在对应点的切线斜率为
$\frac{dy}{dx}=\frac{y'(t)}{x'(t)}=\tan\varphi$
其中 $\varphi$ 是该切线与 $x$ 轴的夹角, 由 $\varphi=\arctan\frac{y'(t)}{x'(t)}$,
即可得到
$\frac{d\varphi}{dt}=\frac{x'(t)y''(t)-x''(t)y'(t)}{x'^2(t)+y'^2(t)}$

另外, 由弧长的微分公式知 $\frac{ds}{dt}=\sqrt{x'^2(t)+y'^2(t)}$,
于是
$K=\left|\frac{d\varphi}{ds}\right|=\left|\frac{\frac{d\varphi}{dt}}{\frac{ds}{dt}}\right|$
$=\frac{|x'(t)y''(t)-x''(t)y'(t)|}{(x'^2(t)+y'^2(t))^{\frac{3}{2}}}$
这就是曲率的计算公式

特别地, 如果曲线由 $y=y(x)$ 表示, 且 $y(x)$
有二阶导数,
那么相应的计算公式为
$K=\frac{|y''|}{(1+y'^2)^{\frac{3}{2}}}$
[直线上曲率处处为 $0$]

------


> 例7-38: 求椭圆 $x=a\cos t, y=b\sin t\ (0\leq t\leq2\pi)$ 上曲率最大和最小的点 $(0<b\leq a)$
> 由于 $x'=-a\sin t, x''=-a\cos t, y'=b\cos t, y''=-b\sin t$
>
> 因此 $K=\frac{|x'y''-x''y'|}{(x'^2+y'^2)^{\frac{3}{2}}}=\frac{|ab\sin^2t+ab\cos^2t|}{(a^2\sin^2t+b^2\cos^2t)^{\frac{3}{2}}}$
> $=\frac{ab}{[(a^2-b^2)\sin^2t+b^2]^{\frac{3}{2}}}$
>
> 因此当 $a>b>0$ 时, 椭圆上在 $t=0,\pi$ 对应的点,
> 即长轴的两个端点, 曲率最大; 在 $t=\frac{\pi}{2},\frac{3\pi}{2}$ 对应的点,
> 即短轴的两个端点, 曲率最小
>
> 当 $a=b=R$ 时(这时椭圆成为半径为 $R$ 的圆),
> $K=1/R$,
> 即圆上各点处的曲率相同, 其值为圆半径的倒数, 而曲率半径正好是 $R$

> 例7-39: 求悬链线 $y=\frac{a}{2}\left(e^{\frac{x}{a}}+e^{-\frac{x}{a}}\right)$ 的曲率 $(a>0)$
> 易知 $y'=\frac{1}{2}\left(e^{\frac{x}{a}}-e^{-\frac{x}{a}}\right)$,
>
> $y''=\frac{1}{2a}\left(e^{\frac{x}{a}}+e^{-\frac{x}{a}}\right)=\frac{y}{a^2}$
> 由于 $y>0$ 及 $\sqrt{1+y'^2}=\sqrt{1+\frac{1}{4}\left(e^{\frac{x}{a}}-e^{-\frac{x}{a}}\right)^2}$
> $=\frac{y}{a}$,
> 所以
>
> $K=\frac{|y''|}{(1+y'^2)^{\frac{3}{2}}}=\left|\frac{y}{a^2}\right|\bigg/\left(\frac{y}{a}\right)^3$
> $=\frac{a}{y^2}=\frac{4}{a\left(e^{\frac{x}{a}}+e^{-\frac{x}{a}}\right)^2}$


## 附录 常用几何曲线图示

图7-23: 常用几何曲线图示 (1) Archimedes 螺线,
(2) 对数螺线,
(3) 双曲螺线, (4) 圆的渐开线, (5) 摆线, (6) 星形线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005522.png =600x)

图7-24: 常用几何曲线图示 (7) 三叶玫瑰线 $r=a\cos3\theta$,
(8) 三叶玫瑰线 $r=a\sin3\theta$, (9) 四叶玫瑰线 $r=a\cos2\theta$,
(10) 四叶玫瑰线 $r=a\sin2\theta$, (11) 双纽线,
(12) 心脏线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005523.png =700x)

图7-25: 常用几何曲线图示 (13) Descartes 叶形线,
(14) 蔓叶线, (15) 箕舌线, (16) 斜抛物线,
(17) 悬链线,
(18) 概率曲线 $y=e^{-x^2}$

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005524.png =700x)


## 微元法

求曲边梯形面积 $S$ 的步骤是: 对区间 $[a,b]$ 作划分 $a=x_0<x_1<\cdots<x_n=b$,
然后在小区间 $[x_{i-1},x_i]$ 中任取 $\xi_i$,
记 $\Delta x_i=x_i-x_{i-1}$, 得到小曲边梯形面积的近似值 $\Delta S_i\approx f(\xi_i)\Delta x_i$,
最后将所有小曲边梯形面积的近似值相加, 再取极限, 就得到
$S=\lim\limits_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i=\int_a^b f(x)dx$

换一个角度: 将分点 $x_{i-1}$ 和 $x_i$ 分别记为 $x$ 和 $x+dx$,
将区间 $[x,x+dx]$ 上的小曲边梯形的面积记为 $\Delta S$,
并取 $\xi_i=x$, 则 $\Delta S\approx f(x)\Delta x$

令 $\Delta x\to0$, 这相当于对自变量作微分,
这样 $\Delta x$ 变成 $dx$,
$\Delta S$ 变成 $dS$, 于是上面的近似等式就变为微分形式下的严格等式 $dS=f(x)dx$
把对小曲边梯形面积的近似值进行相加, 再取极限的过程视作对微分形式 $dS=f(x)dx$ 在区间 $[a,b]$ 上求定积分,
就得到
$S=\int_a^b f(x)dx$

解决实际问题时, 可以按照步骤
自变量分划 $\to[x,x+dx]\to$ 科学规律 $\to\Delta S\approx f(x)\Delta x\to$ 微分 $\to dS$
$=f(x)dx\to$ 直接积分 $\to S=\int_a^b f(x)dx$
来直接求解

一开始就将小区间形式地取为 $[x,x+dx]$($dx$ 称为 $x$ 的微元),
然后根据实际问题得出微分形式 $dS=f(x)dx$($dS$ 称为 $S$ 的微元),
再在区间 $[a,b]$ 上求积分: 也就是
$dx\longrightarrow dS=f(x)dx\longrightarrow S=\int_a^b f(x)dx$

在 $dS=f(x)dx$ 中, 微元 $dx$ 的作用有两重性
1. 首先, $dx$ 被当作一个相对静止的有限量,
这时根据所考虑的具体问题建立的 $dS$ 与 $dx$ 的关系式是近似成立的
2. 然后, 再将 $dx$ 看成无穷小量, 这时关系式 $dS=f(x)dx$ 严格成立,
   便可对其进行积分

这种处理问题和解决问题的方法称为微元法, 微元法略去了 $\Delta x\to0$ 的极限过程以及在运算过程中可能出现的高阶无穷小量,
使用起来非常方便


## 由静态分布求总量

设一根长度为 $l$ 的线段上分布着某种物理量, 将其平放在 $x$ 轴的正半轴上,
使它的一头与原点重合

若它在 $x$ 处的密度(称为线密度)可由某个连续的分布函数 $\rho(x)$ 表示($x\in[0,l]$),
由微元法, 它在 $[x,x+dx]$ 上的物理量 $dQ$ 为 $dQ=\rho(x)dx$
对等式两边在 $[0,l]$ 上积分, 就得到由分布函数求总量的公式
$Q=\int_0^l\rho(x)dx$

------


> 例7-40: 一根金属棒, 其密度分布为 $\rho(x)=2x^2+3x+6\ (\text{kg/m})$,
> 求这根金属棒的质量 $m$
> $m=\int_0^6(2x^2+3x+6)dx=\left(\frac{2}{3}x^3+\frac{3}{2}x^2+6x\right)\bigg|_0^6=234\ (\text{kg})$
>
> 这个问题可以作以下的推广: 假定物理量分布在一个平面区域上,
> $x$ 的变化范围为区间 $[a,b]$
>
> 如果过 $x(a\leq x\leq b)$ 点并且垂直于 $x$ 轴的直线与该平面区域之交上的物理量的密度可以用 $f(x)$ 表示,
> 或者说该平面区域在横坐标位于 $[x,x+dx]$ 中的部分上的物理量可以表示为 $f(x)dx$,
> 那么由类似的讨论, 就可以得到这个区域上的总物理量为 $Q=\int_a^b f(x)dx$

> 例7-41: 求圆心在水下 $10\ \text{m}$,
> 半径为 $1\ \text{m}$ 的竖直放置的圆形铁片所受到的水压力
>
> 由物理定律, 浸在液体中的物体在深度为 $h$ 的地方所受到的压强为 $p=h\cdot\rho g$,
> 这里 $\rho$ 是液体的密度, $g$ 是重力加速度
>
> 以铁片的圆心为原点, 沿铅垂线方向向下为 $x$ 轴的正向建立坐标系,
> 于是铁片在深度为 $10+x$ 处 $(-1\leq x\leq1)$ 受到的压强为 $(10+x)g$
>
> 在圆铁片上截取与水面平行, 以微元 $dx$ 为宽度的一条带域,
> 则带域的面积 $dS=2\sqrt{1-x^2}dx$
>
> 所以带域上所受到的压力为 $dF=2g\sqrt{1-x^2}\cdot(10+x)dx$
> 于是铁片所受到的水压力为 $F=2g\int_{-1}^1\sqrt{1-x^2}\cdot(10+x)dx=10\pi g\ (\text{N})$

图7-26: 圆形铁片所受水压力

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005525.png =300x)

[这个结论还可以推广到立体区域去]
[§4 求三维空间夹在平面 $x=a$ 和 $x=b$ 之间的几何体体积公式 $V=\int_a^b A(x)dx$ 也可看成是应用本方法的一个特例,
其中物理量的密度函数 $A(x)$ 是截面的面积]

假定物理量是分布在一条平面曲线 $\begin{cases}x=x(t),\\y=y(t),\end{cases}t\in[T_1,T_2]$ 上,
分布函数(即物理量的密度)为 $f(t)$, 在 $(x(t),y(t))$ 处截取一段长度为 $dl$ 的弧,
那么在这段弧上的物理量 $dQ$ 为 $dQ=f(t)dl$

利用弧长的微分公式, $dQ=f(t)dl=f(t)\sqrt{x'^2(t)+y'^2(t)}dt$
关于 $t$ 在 $[T_1,T_2]$ 上积分, 就得到 $Q=\int_{T_1}^{T_2}f(t)dl$
$=\int_{T_1}^{T_2}f(t)\sqrt{x'^2(t)+y'^2(t)}dt$
[这个结论可以推广到空间曲线的情况]

> 例7-42: 若上半个金属环 $x^2+y^2=R^2\ (y\geq0)$ 上的任何一点处的电荷线密度等于该点到 $y$ 轴的距离的平方,
> 求环上的总电量
> 将金属环的方程写成参数形式 $\begin{cases}x=R\cos t,\\y=R\sin t,\end{cases}t\in[0,\pi]$
>
> 于是 $dl=\sqrt{x'^2(t)+y'^2(t)}dt=Rdt$
> 分布函数 $f(t)=[x(t)]^2=R^2\cos^2t$,
> 因此 $dQ=f(t)dl=R^3\cos^2tdt$
> 所以环上的总电量为 $Q=R^3\int_0^\pi\cos^2tdt=\frac{R^3\pi}{2}$

图7-27: 半圆环上的电荷分布

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005526.png =300x)


## 求动态效应

除了静态的物理量之外, 还有一类物理量是通过运动而产生的,
或者是另一个物理量持续作用的效果
例如"位移"是速度作用了一段时间的结果, "功"是力作用了一段距离的结果
在 §1 中已知, 以速度 $v(t)$ 作变速运动的物体在 $[T_1,T_2]$ 走过的路程为 $S=\int_{T_1}^{T_2}v(t)dt$
这可以用微元法来理解: 在小区间 $[t,t+dt]$ 上速度可近似地看作是 $v(t)$,
因此走过的一小段路程为 $dS=v(t)dt$, 两边求积分,
就得到了前面的结果

------


> 例7-43: 一个内半径为 $R$ 的圆柱形汽缸, 点火后于时刻 $t_0$ 到 $t_1$ 将活塞从 $x=a$ 处推至 $x=b$ 处($t_0$ 与 $t_1$ 非常接近),
> 求它在这段时间中的平均功率
>
> 由于 $t_0$ 与 $t_1$ 非常接近, 可以认为在这段时间内汽缸中的温度没有变化,
> 由物理学的等温律, 汽缸中气体的压强 $p$ 与体积 $V$ 成反比,
> 即 $p=\frac{C}{V}$
>
> $C$ 是点火瞬间汽缸中气体的压强 $p_0$ 与体积 $aS$ 的乘积($S$ 为活塞的截面积 $\pi R^2$),
> 所以当活塞在 $x$ 处时, 作用在活塞上的压力为 $F=p\cdot S=\frac{C}{V}S=\frac{C}{Sx}S=\frac{C}{x}$
>
> 利用微元法, 活塞移动 $dx$ 距离所做的功可表示为 $dW=Fdx=\frac{C}{x}dx$
> 于是, 所求的平均功率为 $N=\frac{W}{T}=\frac{C}{t_1-t_0}\int_a^b\frac{dx}{x}$
> $=\frac{ap_0S}{t_1-t_0}\ln\frac{b}{a}$

图7-28: 圆柱形汽缸

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005527.png =400x)


## 简单数学模型和求解

用数学技术去解决实际问题, 首先必须建立数学模型
由于最重要的数学建模工具是微分, 而微分与积分互为逆运算,
所以积分便理所当然地成为求解数学模型的有力手段
将微分与积分结合起来, 就可以为许多实际问题建立起相应的数学关系

例如 Malthus 人口模型 $\begin{cases}p'(t)=\lambda p(t),\\p(t_0)=p_0,\end{cases}$
在学习了积分以后, 可以直接对微分等式 $\frac{dp}{p}=\lambda dt$ 的两边在 $[t_0,t]$ 上求积分,
这时 $p$ 的变化范围相应地为 $[p_0,p]$, 即 $\int_{p_0}^p\frac{dp}{p}=\lambda\int_{t_0}^t dt$
于是 $\ln\frac{p}{p_0}=\lambda(t-t_0)$,
即 $p=p_0e^{\lambda(t-t_0)}$

------


> 例7-44 (跟踪问题模型): 设 $A$ 在初始时刻从坐标原点沿 $y$ 轴正向前进,
> 与此同时 $B$ 于 $[a,0]$ 处开始保持距离 $a$ 对 $A$ 进行跟踪(即 $B$ 的前进方向始终对着 $A$ 的位置,
> 并与 $A$ 始终保持距离 $a$), 求 $B$ 的运动轨迹
>
> 设 $B$ 的运动轨迹为 $y=y(x)$, 按跟踪的要求和导数的几何意义,
> 容易得到数学模型 $\begin{cases}y'=-\frac{\sqrt{a^2-x^2}}{x},\\y(a)=0\end{cases}$
>
> 两边求定积分 $\int_0^y dy=-\int_a^x\frac{\sqrt{a^2-x^2}}{x}dx$
> 即得到 $B$ 的运动轨迹方程为 $y=a\ln\frac{a+\sqrt{a^2-x^2}}{x}-\sqrt{a^2-x^2}$
>
> [这也可以看成是一个重物 $B$ 被 $A$ 用一根长度为 $a$ 的绳子拖着走时留下的轨迹,
> 所以该曲线又称为曳线]

图7-29: 跟踪问题的轨迹

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005528.png =350x)

> 例7-45 (火箭飞行的运动规律): 火箭是靠将燃料变成气体向后喷射,
> 即甩去一部分质量来得到前进的动力的
> 设在时刻 $t$ 火箭的总质量为 $M(t)$, 速度为 $v(t)$,
> 从而其动量为 $M(t)v(t)$
>
> 在从 $t$ 到 $t+dt$ 时间段中, 有部分燃料以相对于火箭体的常速度 $u$ 被反向喷射出去($u$ 是由火箭的推进器的结构和性能决定的,
> 与火箭本身的飞行速度无关)
>
> 在时刻 $t+dt$ 火箭质量为 $M(t+dt)$, 速度为 $v(t+dt)$,
> 相应地, 喷射掉的燃料质量为 $M(t)-M(t+dt)$,
> 而其速度为 $v(t+dt)-u$,
>
> 且此时系统的动量等于火箭剩余部分的动量与燃料的动量之和
> 因此在时间段 $[t,t+dt]$ 中, 系统动量的改变量为
>
> $M(t+dt)v(t+dt)+[M(t)-M(t+dt)]\cdot[v(t+dt)-u]-M(t)v(t)=M(t)[v(t+dt)-v(t)]+[M(t+dt)-M(t)]u$
> $=M(t)v'(t)dt+uM'(t)dt$
>
> 再由冲量定律, 动量的改变量等于力与作用时间的乘积, 即冲量 $Fdt$,
> 这样就得到火箭运动的微分方程为
>
> $M\frac{dv}{dt}=F-u\frac{dM}{dt}$
> 这里 $F$ 是作用于火箭系统的外力, $M\frac{dv}{dt}$ 称为火箭的反推力
> 特别地, 当火箭在地球表面垂直向上发射时, $F=-Mg$, 方程成为
>
> $\begin{cases}\frac{dv}{dt}=-g-u\frac{1}{M}\frac{dM}{dt},\\v(0)=0, M(0)=M_0,\end{cases}$
> 两边在 $[0,t]$ 上积分, $\int_0^t v'(t)dt=-\int_0^t gdt-u\int_0^t\frac{M'(t)}{M(t)}dt$
> 就得到 $v(t)=u\ln\frac{M_0}{M(t)}-gt$

图7-30: 火箭的运动

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005529.png =250x)

> 例7-46 (Logistic 人口模型): Malthus 人口模型的解 $p=p_0e^{\lambda(t-t_0)}$ 中当 $t\to\infty$ 时有 $p(t)\to\infty$,
> 这显然是荒谬的
>
> 因为人口的数量增加到一定程度后, 自然资源和环境条件就会对人口的继续增长起限制作用,
> 并且限制的力度随人口的增加而越来越强
> 也就是说, 在任何一个给定的环境和资源条件下, 人口的增长不可能是无限的,
> 它必定有一个上界 $p_{\max}$
>
> 因此, 荷兰生物学家 Verhulst 认为, 人口的增长速率应随着 $p(t)$ 接近 $p_{\max}$
> 而越来越小,
> 他提出了一个修正的人口模型
> $\begin{cases}p'(t)=\lambda\left[1-\frac{p(t)}{p_{\max}}\right]p(t),\\p(t_0)=p_0\end{cases}$
>
> 将含有 $p$ 的项全部集中到左边, 两边在 $[t_0,t]$ 上积分,
> $\int_{p_0}^p\frac{dp}{p_{\max}\cdot p-p^2}=\frac{\lambda}{p_{\max}}\int_{t_0}^t dt$
>
> 利用有理函数的积分公式, 即可解出 $p=\frac{p_{\max}}{1+\left(\frac{p_{\max}}{p_0}-1\right)e^{-\lambda(t-t_0)}}$
> 当 $t\to\infty$ 时有 $p(t)\to p_{\max}$
> [美国和法国都曾用这个模型预测过人口, 结果是令人满意的]


## 从 Kepler 行星运动定律到万有引力定律

用 Kepler 的行星运动三大定律, Newton 第二运动定律再加上微积分来导出万有引力定律
对任意一个确定的行星, 由 Kepler 第一定律, 以太阳(即椭圆的一个焦点)为极点, 椭圆的长轴为极轴建立极坐标,
则行星的轨道方程为
$r=\frac{p}{1-e\cos\theta}$
这里 $p=\frac{b^2}{a}$ 是焦参数, $e=\sqrt{1-\frac{b^2}{a^2}}$ 是离心率,
$a$ 和 $b$ 分别是椭圆的半长轴和半短轴
设时刻 $t$ 行星与太阳的距离为 $r=r(t)$, 它们的连线与极轴的夹角为 $\theta=\theta(t)$,
则行星的坐标可以用向量记号表示成 $\boldsymbol{r}=(r\cos\theta,r\sin\theta)$

记 $dA$ 是极径转过角度 $d\theta$ 所扫过的那块椭圆的面积,
由极坐标下的面积公式 $dA=\frac{1}{2}r^2d\theta$
由 Kepler 第二定律, 单位时间中扫过的面积 $\frac{dA}{dt}=\frac{1}{2}r^2\omega=$ 常数
这里 $\omega=\frac{d\theta}{dt}$ 表示行星运动的角速度

记行星绕太阳运行一周的时间为 $T$, 则经过 $T$ 时间极径所扫过的面积恰为整个椭圆的面积 $\pi ab$,
即
$\pi ab=\int_0^T\frac{dA}{dt}dt=\frac{1}{2}r^2\omega T$
因此常数 $r^2\omega=\frac{2\pi ab}{T}$
两边对 $t$ 求导后得到 $(r^2\omega)'=2r\dot{r}\omega+r^2\dot{\omega}=0$,
即 $2\dot{r}\omega+r\dot{\omega}=0$

这里行星沿极径方向的速度和加速度分别为 $\frac{dr}{dt}=\dot{r}$ 和 $\frac{d^2r}{dt^2}=\ddot{r}$
[用字母上面加点表示对 $t$ 的导数是 Newton 的记号]

行星在 $x$ 方向和 $y$ 方向上的加速度分量分别为
$\frac{d^2(r\cos\theta)}{dt^2}=\ddot{r}\cos\theta-2\dot{r}\omega\sin\theta-r[\dot{\omega}\sin\theta+\omega^2\cos\theta]$
$=(\ddot{r}-r\omega^2)\cos\theta-(2\dot{r}\omega+r\dot{\omega})\sin\theta$
$=(\ddot{r}-r\omega^2)\cos\theta$
$\frac{d^2(r\sin\theta)}{dt^2}=\ddot{r}\sin\theta+2\dot{r}\omega\cos\theta+r[\dot{\omega}\cos\theta-\omega^2\sin\theta]$
$=(2\dot{r}\omega+r\dot{\omega})\cos\theta+(\ddot{r}-r\omega^2)\sin\theta$
$=(\ddot{r}-r\omega^2)\sin\theta$

记 $\boldsymbol{e}_r=\frac{\boldsymbol{r}}{r}=(\cos\theta,\sin\theta)$ 是 $\boldsymbol{r}$ 方向上的单位向量,
于是得到加速度向量 $\boldsymbol{a}=(\ddot{r}-r\omega^2)\boldsymbol{e}_r$
即行星在任一点的加速度的方向恰与它的极径同向, 加速度的值为 $\ddot{r}-r\omega^2$

图7-31: 行星的椭圆轨道

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005530.png =500x)

为了求出 $\ddot{r}-r\omega^2$, 将椭圆方程 $p=r(1-e\cos\theta)$ 两边求二阶导数,
注意到 $p$ 是焦参数即常数
$0=\ddot{r}(1-e\cos\theta)+2\dot{r}e\sin\theta\,\omega+re(\dot{\omega}\sin\theta+\omega^2\cos\theta)$

由 $2\dot{r}\omega+r\dot{\omega}=0$ 消去上式的第二, 四项,
即得 $\ddot{r}(1-e\cos\theta)=-re\omega^2\cos\theta$

于是 $\ddot{r}-r\omega^2=-\frac{r^2\omega^2}{p}=-\frac{4\pi^2a^3}{T^2r^2}$
由 $\frac{1}{p}=\frac{1}{b^2/a}=\frac{a}{b^2}$,
$\frac{1}{r^2}=\frac{1}{p^2}(1-e\cos\theta)^2$ 及 $r^2\omega=\frac{2\pi ab}{T}$ 亦可得到同一结果

最后, 由 Newton 第二运动定律和 Kepler 第三定律即 $\frac{a^3}{T^2}=$ 常数,
便有
$F=ma=m(\ddot{r}-r\omega^2)\boldsymbol{e}_r=\left(\frac{4\pi^2}{M}\cdot\frac{a^3}{T^2}\right)\cdot\frac{Mm}{r^2}\boldsymbol{e}_r$
$=-G\frac{Mm}{r^2}\boldsymbol{e}_r$
这里 $M$ 是太阳的质量, $G=\frac{4\pi^2}{M}\frac{a^3}{T^2}=6.67\times10^{-11}\ (\text{N}\cdot\text{m}^2/\text{kg}^2)$ 称为引力常量

[导出万有引力定律是人类历史上最成功的数学模型之一, 它的结论为以后一系列的观测和实验数据所证实(其中最为人津津乐道的是发现海王星),
它的适用范围从天体运动一直延展到微观世界, 令人信服地定量地解释了许多既有的物理现象,
并成为探索未知世界的有力工具]


## 数值积分

尽管 Newton-Leibniz 公式给出了求定积分的一条捷径,
但对于解决实际问题来说,
它是远远不够的

能够用初等函数表示不定积分的只占很小一部分, 也就是说, 对绝大部分在理论上可积的函数,
并不能用 Newton-Leibniz 公式求得其定积分之值

另外, 实际问题中许多函数是通过测量, 试验等方法给出了在若干个离散点上的函数值,
求这些函数在某个区间上的积分值只能借助数值方法
数值积分是其中最重要的一种

从数值计算的观点来看, 若能在 $[a,b]$ 上找到一个具有足够精度的替代 $f(x)$ 的可积函数 $p(x)$,
而 $p(x)$ 的原函数可以用初等函数 $P(x)$ 表示,
那么便可用 $p(x)$ 的积分值近似地代替 $f(x)$ 的积分值,
即
$\int_a^b f(x)dx\approx\int_a^b p(x)dx=P(x)\bigg|_a^b$

此外, 从定积分的几何意义知道, 将积分区间分得越细, 小块近似面积之和与总面积就越是接近
因此, 用简单函数替代被积函数, 并将积分区间细化是数值积分的主要思想


## Newton-Cotes 求积公式

这是一个取等距节点的数值积分公式
将积分区间 $[a,b]$ 以步长 $h=\frac{b-a}{n}$ 分成 $n$ 等份,
以分点 $x_i=a+ih\ (i=0,1,2,\cdots,n)$ 为节点作 $f(x)$ 的 Lagrange 插值多项式
$f(x)\approx p_n(x)=\sum_{i=0}^n\left[\prod_{\substack{j=0\\j\neq i}}^n\frac{x-x_j}{x_i-x_j}\right]f(x_i)$

对等式两边在 $[a,b]$ 上积分, 便有 $\int_a^b f(x)dx\approx\int_a^b p_n(x)dx=(b-a)\sum_{i=0}^n C_i^{(n)}f(x_i)$
这里 $C_i^{(n)}=\frac{1}{b-a}\int_a^b\prod_{\substack{j=0\\j\neq i}}^n\frac{x-x_j}{x_i-x_j}dx$
$=\frac{1}{n}\frac{(-1)^{n-i}}{i!(n-i)!}\int_0^n\prod_{\substack{j=0\\j\neq i}}^n(t-j)dt$(令 $x$
$=a+th$)

这就是 n 步 Newton-Cotes 求积公式, 计算时需取 $n+1$ 个节点,
相应的 $C_i^{(n)}$ 称为 Cotes 系数, 它与积分区间和被积函数无关,
可通过求多项式的积分事先算好

Cotes 系数具有如下性质
1. 对称性: $C_i^{(n)}=C_{n-i}^{(n)}$,
$i=0,1,2,\cdots,n$
2. 规范性: 由于 Newton-Cotes 公式对 $f(x)\equiv1$ 是精确成立的,
   因此 $\sum_{i=0}^n C_i^{(n)}=1$

Newton-Cotes 公式将求定积分问题近似地转化为一个求和问题,
下面是几个常用的情况

(1) 梯形公式
当 $n=1$ 时, 由 Cotes 系数的性质, 即知 $C_0^{(1)}=C_1^{(1)}=\frac{1}{2}$,
因此
$\int_a^b f(x)dx\approx\frac{b-a}{2}[f(a)+f(b)]$
它的几何意义是用以 $(a,0)$, $(a,f(a))$,
$(b,f(b))$ 和 $(b,0)$ 为顶点的直角梯形的面积近似代替由 $y=f(x)$,
$x=a$, $x=b$ 和 $x$ 轴所围成的曲边梯形的面积,
所以称为梯形公式

图7-32: 梯形公式的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005531.png =400x)

(2) Simpson 公式
当 $n=2$ 时, $C_0^{(2)}=\frac{1}{4}\int_0^2(t-1)(t-2)dt=\frac{1}{6}=C_2^{(2)}$,
$C_1^{(2)}=1-C_0^{(2)}-C_2^{(2)}=\frac{4}{6}$,
因此得到 Simpson 公式
$\int_a^b f(x)dx\approx\frac{b-a}{6}\left[f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right]$

它的几何意义是用过点 $(a,f(a))$, $\left(\frac{a+b}{2},f\left(\frac{a+b}{2}\right)\right)$ 和 $(b,f(b))$ 的抛物线 $y$
$=p_2(x)$ 与 $x=a$,
$x=b$ 和 $x$ 轴所围成的曲边梯形的面积, 近似代替由 $y=f(x)$,
$x=a$, $x=b$ 和 $x$ 轴所围成的曲边梯形的面积,
所以 Simpson 公式也称为抛物线公式

图7-33: Simpson 公式的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011194005532.png =400x)

(3) Cotes 公式
当 $n=4$ 时
$C_0^{(4)}=\frac{1}{96}\int_0^4(t-1)(t-2)(t-3)(t-4)dt=\frac{7}{90}=C_4^{(4)}$
$C_1^{(4)}=\frac{1}{24}\int_0^4 t(t-2)(t-3)(t-4)dt=\frac{32}{90}=C_3^{(4)}$
$C_2^{(4)}=1-2(C_0^{(4)}-C_1^{(4)})=\frac{12}{90}$

于是得到 Cotes 公式
$\int_a^b f(x)dx\approx\frac{b-a}{90}[7f(x_0)+f(x_4)+32(f(x_1)+f(x_3))+12f(x_2)]$
这里 $x_i=\frac{(4-i)a+ib}{4}$,
$i=0,1,2,3,4$

------


> 例7-47: 分别用以上三个公式求 $\int_{-1}^1 e^xdx$ 的近似值
> 梯形公式: $I_1=e^1+e^{-1}=3.08616127\cdots$
>
> Simpson 公式: $I_2=\frac{1}{3}(e^1+4e^0+e^{-1})=2.362053757\cdots$
> Cotes 公式: $I_4=\frac{1}{45}[7(e^1+e^{-1})+32(e^{\frac{1}{2}}+e^{-\frac{1}{2}})+12e^0]$
> $=2.350470904\cdots$
>
> 面积的精确值为 $I=\int_{-1}^1 e^xdx=e-\frac{1}{e}=2.350402387\cdots$
> 所以, Cotes 公式的精度最高, 但它要计算 $5$ 个函数值,
> 而梯形公式只要计算两个就够了

------


定理7.6.1 (Newton-Cotes 公式误差估计): 设 $f^{(n+1)}(x)$ 在 $[a,b]$ 连续,
则用 Newton-Cotes 公式计算 $\int_a^b f(x)dx$ 的误差 $R_n(f)$ 满足估计式
$|R_n(f)|\leq\frac{M_nh^{n+2}}{(n+1)!}\int_0^n\left|\prod_{j=0}^n(t-j)\right|dt$
这里 $M_n=\max\limits_{a\leq x\leq b}|f^{(n+1)}(x)|$

证明: $R_n(f)=\int_a^b f(x)dx-(b-a)\sum_{i=0}^n C_i^{(n)}f(x_i)=\int_a^b f(x)dx-\int_a^b p_n(x)dx$
$=\int_a^b[f(x)-p_n(x)]dx$

由 Lagrange 插值多项式余项定理, $R_n(f)=\int_a^b\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_i)dx$,
$\xi\in(x_{\min},x_{\max})$

于是
$|R_n(f)|\leq\int_a^b\left|\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_i)\right|dx$
$\leq\frac{M_n}{(n+1)!}\int_a^b\left|\prod_{i=0}^n(x-x_i)\right|dx$
$\leq\frac{M_nh^{n+2}}{(n+1)!}\int_0^n\left|\prod_{i=0}^n(t-i)\right|dt$

------


定义7.6.1: 若一个数值求积公式在被积函数是任意不高于 $n$ 次的多项式时都精确成立,
而存在着一个 $n+1$ 次多项式使公式不能精确成立, 则称该求积公式具有 n 次代数精度
[从某种意义上说, 代数精度的次数越高越好]

------


推论1: n 步 Newton-Cotes 求积公式的代数精度至少为 $n$

------


推论2: $n=2k$ 步的 Newton-Cotes 求积公式的代数精度至少为 $2k+1$

证明(推论2): 只要证明 $n=2k$ 步的 Newton-Cotes 求积公式对 $f(x)=x^{2k+1}$ 精确成立就可以了
此时 $f^{(2k+1)}(x)=(2k+1)!$, 由定理7.6.1 证明的中间过程得到
$\frac{R_{2k}(f)}{h^{2k+2}}=\int_0^{2k}\prod_{j=0}^{2k}(t-j)dt=\int_{-k}^{k}\prod_{j=-k}^{k}(u+j)du$
$=(-1)^{2k+1}\int_{-k}^{k}\prod_{j=-k}^{k}(u-j)du=-\int_{-k}^{k}\prod_{j=-k}^{k}(u+j)du$
$=-\frac{R_{2k}(f)}{h^{2k+2}}$

所以 $R_{2k}(f)=0$

[实际上可以验证, 当 $n$ 分别为奇数和偶数时, n 步 Newton-Cotes 求积公式的代数精度恰为 $n$ 和 $n+1$]
[特别地, 当 $n=2$ 时, Simpson 公式具有三次代数精度,
这就是一般不采用 $3$ 步 Newton-Cotes 公式的缘故]


## 复化求积公式

要提高数值积分的精度, 不能采用一味提高 Newton-Cotes 公式的步数的办法
理论上已经证明, $n$ 较大时, Newton-Cotes 公式的计算过程中将产生不稳定,
因此实际使用时, 几乎不会有人将 $n$ 取得大于 $4$

一条思路是先将积分区间分成若干等份, 再在每一个小区间上使用低步数的 Newton-Cotes 公式,
最后将各小区间上的积分近似值加起来

(1) 复化梯形公式
将 $[a,b]$ 以步长 $h=\frac{b-a}{m}$ 作 $m$ 等分 $x_i=a+ih\ (i=0,1,2,\cdots,m-1,m)$,
在每一个小区间 $[x_{i-1},x_i]$ 使用梯形公式
$\int_a^b f(x)dx=\sum_{i=1}^m\int_{x_{i-1}}^{x_i}f(x)dx\approx\frac{h}{2}\sum_{i=1}^m[f(x_{i-1})+f(x_i)]$

记 $T_m^{(1)}=\frac{h}{2}\left[f(a)+f(b)+2\sum_{i=1}^{m-1}f(x_i)\right]$,
则 $T_m^{(1)}$ 称为将区间 $m$ 等分的复化梯形公式
[复化梯形公式与 $\int_a^b f(x)dx$ 的误差为 $O((b-a)h^2)$,
与对整个区间直接使用梯形公式时的误差 $O((b-a)^3)$ 相比,
精度大大提高了]

(2) 复化 Simpson 公式和复化 Cotes 公式
记 $x_{i-\frac{1}{2}}$ 为区间 $[x_{i-1},x_i]$ 的中点,
可以完全类似地得到复化 Simpson 公式
$T_m^{(2)}=S_m=\frac{h}{6}\sum_{i=1}^m\left[f(x_{i-1})+4f\left(x_{i-\frac{1}{2}}\right)+f(x_i)\right]$
$=\frac{h}{6}\left[f(a)+f(b)+2\sum_{i=1}^{m-1}f(x_i)+4\sum_{i=1}^m f\left(x_{i-\frac{1}{2}}\right)\right]$

复化 Simpson 公式与复化梯形公式之间存在着如下关系
$T_m^{(2)}=\frac{4T_{2m}^{(1)}-T_m^{(1)}}{4-1}$
将它与第五章 §4 的外推公式相比较, 就知道复化 Simpson 公式实质上是对复化梯形公式做了一次外推的结果

但复化 Simpson 公式的误差为 $O((b-a)h^4)$,
远远好于 $T_m^{(1)}$ 和 $T_{2m}^{(1)}$,
这一现象符合两个低精度的近似值进行适当外推后, 可产生一个精度高得多的近似值

(3) Romberg 方法
将上面的外推的思想推广到一般的 $T_m^{(k)}$, 记 $T_m^{(k+1)}=\frac{4^kT_{2m}^{(k)}-T_m^{(k)}}{4^k-1}$,
就成数值积分的 Romberg 方法

它的具体过程为: 先取适当的初始值 $m$, 再按顺序逐次计算,
向下的箭头表示区间再细化一半,
向右的箭头表示外推

$T_m^{(1)}\ \to\ T_m^{(2)}\ \to\ T_m^{(3)}\ \to\ T_m^{(4)}$
$\downarrow$
$T_{2m}^{(1)}\ \to\ T_{2m}^{(2)}\ \to\ T_{2m}^{(3)}$
$\downarrow$
$T_{4m}^{(1)}\ \to\ T_{4m}^{(2)}$
$\downarrow$
$T_{8m}^{(1)}$

具体执行时一般从 $m=1$, $k=1$ 开始, 逐个计算 $T_m^{(k)}$
若对某个 $k$ 有 $|T_{2m}^{(k)}-T_m^{(k)}|$ 小于预先设定的精度要求时,
就将 $T_{2m}^{(k)}$ 作为积分的近似值, 计算结束
否则将小区间长度缩小二分之一, 重新由复化梯形公式开始, 一直到算出 $T_m^{(k+1)}$,
再作上述的比较

这种根据预置的精度要求, 由计算机在计算过程中自动将区间划分到最合适程度的算法称为自适应算法

------


> 例7-48: 用 Romberg 方法计算 $\int_{-1}^1 e^xdx$ 的近似值
> 计算结果见下表

表: Romberg 方法计算 $\int_{-1}^1 e^xdx$

| $m$ | $T_m^{(1)}$ | $T_m^{(2)}$ | $T_m^{(3)}$ | $T_m^{(4)}$ |
|---|---|---|---|---|
| 1 | 3.086 161 270 |  |  |  |
| 2 | 2.543 080 635 | 2.362 053 757 |  |  |
| 4 | 2.399 166 283 | 2.351 194 823 | 2.350 470 904 |  |
| 8 | 2.362 631 334 | 2.350 453 017 | 2.350 403 568 | 2.350 402 494 |

[读者可自行与积分的精确值以及例7-47 比较]


## Gauss 型求积公式

Newton-Cotes 公式是采用 $f(x)$ 在 $[a,b]$ 中等距的 $n+1$ 个点处的函数值求积分的近似公式
能否通过适当地选取求积公式中的节点 $a=x_0<x_1<\cdots<x_n=b$ 和系数 $a_i^{(n)}$,
来达到尽可能高的计算精度

------


定义7.6.2: 设使用 $[a,b]$ 上 $n+1$ 个节点 $\{x_i\}_{i=0}^n$ 的近似求积公式 $\int_a^b f(x)dx\approx\sum_{i=0}^n a_i^{(n)}f(x_i)$
对于 $2n+1$ 次的任意多项式 $p_{2n+1}(x)$, 都有 $\int_a^b p_{2n+1}(x)dx\equiv\sum_{i=0}^n a_i^{(n)}p_{2n+1}(x_i)$
则称该求积公式为 $[a,b]$ 上的 Gauss 型求积公式

[对任意给定的 $n+1$ 个节点, 特殊地构造 $2n+2$ 次多项式 $f(x)=\prod_{i=0}^n(x-x_i)^2$ 代入上式,
左边恒大于零而右式恒等于零, 这说明不存在使用 $n+1$ 个节点,
而对于任意 $2n+2$ 次多项式都精确成立的近似求积分公式,
从这个意义上讲, Gauss 型求积公式是精度最高的数值求积公式]

Gauss 型求积公式有很多种类型, 下面介绍最常用的一类
先设 $[a,b]$ 为 $[-1,1]$ 的情况, 考虑第五章和第七章中出现过的 n 次 Legendre 多项式
$p_n(x)=\frac{1}{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n\ (n=0,1,2,\cdots)$
它是在 $(-1,1)$ 上恰有 $n$ 个不同的根, 并且 $\{p_n(x)\}$ 是 $[-1,1]$ 上的正交多项式

若用 $n+1$ 次 Legendre 多项式 $p_{n+1}(x)$ 的根 $\{x_i\}_{i=0}^n$ 作为插值节点,
作 $f(x)$ 的 Lagrange 插值多项式并在 $[-1,1]$ 上积分,
由此得到的数值积分公式 $\sum_{i=0}^n a_i^{(n)}f(x_i)$ 是 $[-1,1]$ 上的 Gauss 型求积公式,
一般称为 Gauss-Legendre 求积公式

具体计算时, 可以先对 $p_{n+1}(x)$ 利用函数求根的方法求出 $\{x_i\}_{i=0}^n$,
再按关系式
$a_i^{(n)}=\int_{-1}^1\prod_{\substack{j=0\\j\neq i}}^n\frac{x-x_j}{x_i-x_j}dx$
$=\int_{-1}^1\frac{p_{n+1}(x)}{(x-x_i)p'_{n+1}(x_i)}dx\ (i=0,1,2,\cdots,n-1,n)$
算出其系数

下表给出了节点个数 $n+1\leq5$ 时的 Gauss-Legendre 求积公式的节点 $\{x_i\}_{i=0}^n$ 和系数 $a_i^{(n)}$ 的值

| $n$ | $x_i^*$ | $a_i^{(n)}$ |
|---|---|---|
| 1 | $\pm\sqrt{\frac{1}{3}}\approx\pm0.577\ 350\ 269\ 2$ | $1$ |
| 2 | $\pm\sqrt{\frac{3}{5}}\approx\pm0.774\ 596\ 669\ 2$ | $\frac{5}{9}\approx0.555\ 555\ 555\ 6$ |
| 2 | $0$ | $\frac{8}{9}\approx0.888\ 888\ 888\ 9$ |
| 3 | $\pm\sqrt{\frac{3-4\sqrt{0.3}}{7}}\approx\pm0.339\ 981\ 043\ 6$ | $\frac{1}{2}+\frac{1}{12}\sqrt{\frac{10}{3}}\approx0.652\ 145\ 154\ 9$ |
| 3 | $\pm\sqrt{\frac{3+4\sqrt{0.3}}{7}}\approx\pm0.861\ 136\ 311\ 6$ | $\frac{1}{2}-\frac{1}{12}\sqrt{\frac{10}{3}}\approx0.347\ 854\ 845\ 1$ |
| 4 | $\pm\frac{1}{3}\sqrt{5-2\sqrt{\frac{10}{7}}}\approx\pm0.538\ 469\ 310\ 1$ | $\frac{3(0.7+5\sqrt{0.7})}{10(2+5\sqrt{0.7})}\approx0.478\ 628\ 670\ 5$ |
| 4 | $\pm\frac{1}{3}\sqrt{5+2\sqrt{\frac{10}{7}}}\approx\pm0.906\ 179\ 845\ 9$ | $\frac{3(0.7-5\sqrt{0.7})}{10(2+5\sqrt{0.7})}\approx0.236\ 926\ 885\ 1$ |
| 4 | $0$ | $\frac{128}{225}\approx0.568\ 888\ 888\ 9$ |

[Legendre 多项式的根全部落在 $(-1,1)$ 上(从表中可以看到,
点集 $\{x_i\}_{i=0}^n$ 中不包含 $x=\pm1$ 两点),
也就是说, 用 Gauss-Legendre 公式计算积分的近似值时,
是不用到 $f(x)$ 在积分区间的端点处的函数值的]
[这与 Newton-Cotes 公式不同, 事实上这是所有的 Gauss 型公式的特点]

------


> 例7-49: 用 Gauss-Legendre 公式计算 $\int_{-1}^1 e^xdx$ 的近似值
> $n=1$: $I_1=e^{0.5773502692}+e^{-0.5773502692}=2.342696088\cdots$
>
> $n=2$: $I_2=\frac{1}{9}[5(e^{0.7745966692}+e^{-0.7745966692})+8e^0]=2.350336928\cdots$
> $n=4$: $I_4=0.2369268851(e^{0.9061798459}+e^{-0.9061798459})+0.4786286705(e^{0.5384693101}+e^{-0.5384693101})+0.5688888889$
> $=2.35040238658\cdots$
>
> 它们所花的代价与例7-47 用的梯形公式, Simpson 公式和 Cotes 公式完全相同,
> 但精度却不可同日而语
> 如当 $n=4$ 时, 在同样只计算 $5$ 个函数值的情况下,
> 绝对误差由 $O(10^{-4})$ 减小到 $O(10^{-9})$

当积分区间为 $[a,b]$ 时, 可以先作一个变换 $t=\frac{b-a}{2}x+\frac{b+a}{2}$
于是 $\int_a^b f(t)dt=\frac{b-a}{2}\int_{-1}^1 f\left(\frac{b-a}{2}x+\frac{b+a}{2}\right)dx$
就可以用 Gauss-Legendre 公式求解了

因此在 $[-1,1]$ 上建立的 Gauss-Legendre 公式可以推广到一般的积分区间
除了 Gauss-Legendre 求积公式之外, 还可以构造其他类型 Gauss 型求积公式,
它们的基础都是定义在某个区间上的某一类特定的正交多项式

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
