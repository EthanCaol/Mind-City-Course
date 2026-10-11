


## 函数极限的定义

函数极限的定义: 设函数 $y=f(x)$ 在点 $x_0$ 的某个去心邻域中有定义,
即存在 $\rho>0$, 使
$O(x_0,\rho)\setminus\{x_0\}\subseteq D_f$
如果存在实数 $A$, 对任意给定的 $\varepsilon>0$, 可以找到
$\delta>0$, 使得 $0<|x-x_0|<\delta$ 时成立
$|f(x)-A|<\varepsilon$
则称 $A$ 是函数 $f(x)$ 在点 $x_0$ 的极限, 记为
$\lim\limits_{x\to x_0}f(x)=A$, 或
$f(x)\to A\ (x\to x_0)$
若不存在这样的实数 $A$, 则称函数 $f(x)$ 在点 $x_0$ 的极限不存在

符号表述: $\lim\limits_{x\to x_0}f(x)$
$=A\iff\forall\varepsilon>0,\ \exists\delta>0,\ \forall x(0<|x-x_0|<\delta):|f(x)-A|<\varepsilon$

$\varepsilon$ 既是任意的又是给定的: 只有 $\varepsilon$
给定后才能确定 $\delta$, 而 $\varepsilon$
的任意性使上下两条横线的距离可以任意收缩, 但无论收缩得多小都能找到正数
$\delta$, 使得 $x$ 处于 $x_0$ 的 $\delta$ 去心邻域时
$f(x)$ 落在两条线界定的范围内

------

几何意义: 在平面直角坐标系 $Oxy$ 的 $y$ 轴上取以 $A$ 为中心
$\varepsilon$ 为半径的开区间
$(A-\varepsilon,A+\varepsilon)$, 即 $A$ 的
$\varepsilon$ 邻域 $O(A,\varepsilon)$
在 $x$ 轴上以 $x_0$ 为中心 $\delta$ 为半径的开区间给出 $x_0$
的 $\delta$ 邻域
$0<|x-x_0|<\delta$ 时 $|f(x)-A|<\varepsilon$
表示 $O(x_0,\delta)$ 中除 $x_0$ 之外所有点的函数值都落在 $A$
的 $\varepsilon$ 邻域中

图3-1: 函数极限定义的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193108100.png =500x)

------

> 例3-1: 证明 $\lim\limits_{x\to0}e^x=1$
>
> 证: 按极限定义, $\forall\varepsilon>0$(不妨设
> $0<\varepsilon<1$), 要找 $\delta>0$, 使得当
> $0<|x|<\delta$ 时成立 $|e^x-1|<\varepsilon$
>
> 上式等价于 $\ln(1-\varepsilon)<x<\ln(1+\varepsilon)$
> 取 $\delta=\min\{\ln(1+\varepsilon),-\ln(1-\varepsilon)\}>0$,
>
> 当 $x$ 满足 $0<|x|<\delta$ 时显然成立
> $|e^x-1|<\varepsilon$
> 从而证得 $\lim\limits_{x\to0}e^x=1$

> 例3-2: 证明 $\lim\limits_{x\to2}x^2=4$
>
> 证: 由 $|x^2-4|=|x-2|\cdot|x+2|$, 保留因子 $|x-2|$,
> 将因子 $|x+2|$ 放大
> 加上条件 $|x-2|<1$, 即 $1<x<3$, 于是 $|x+2|<5$, 从而
> $|x^2-4|<5|x-2|$
>
> 取 $\delta=\min\left\{1,\frac{\varepsilon}{5}\right\}$,
> 当 $0<|x-2|<\delta$ 时成立
> $|x^2-4|<5\cdot\frac{\varepsilon}{5}=\varepsilon$
> 从而证得 $\lim\limits_{x\to2}x^2=4$

> 例3-3: 证明 $\lim\limits_{x\to1}\frac{x(x-1)}{x^2-1}=\frac{1}{2}$
>
> 证: 由 $\left|\frac{x(x-1)}{x^2-1}-\frac{1}{2}\right|=\frac{|x-1|}{2|x+1|}$,
> 保留因子 $|x-1|$, 将因子 $\frac{1}{2|x+1|}$ 放大
> 加上条件 $0<|x-1|<1$, 即 $0<x<2$, 于是
> $\frac{1}{2|x+1|}<\frac{1}{2}$
>
> 取 $\delta=\min\{1,2\varepsilon\}$, 当
> $0<|x-1|<\delta$ 时成立
> $\left|\frac{x(x-1)}{x^2-1}-\frac{1}{2}\right|$
> $=\frac{|x-1|}{2|x+1|}<\frac{1}{2}\cdot2\varepsilon$
> $=\varepsilon$
> 从而证得 $\lim\limits_{x\to1}\frac{x(x-1)}{x^2-1}=\frac{1}{2}$

证明极限时, 正数 $\delta$ 不要求取最大的或最佳的值,
常用与数列极限证明类似的适度放大技巧


## 函数极限的性质

极限的唯一性: 设 $A$ 与 $B$ 都是函数 $f(x)$ 在点 $x_0$ 的极限,
则 $A=B$

证明: 由函数极限的定义, $\forall\varepsilon>0$,
$\exists\delta_1>0,\ \forall x(0<|x-x_0|<\delta_1):|f(x)-A|<\frac{\varepsilon}{2}$
$\exists\delta_2>0,\ \forall x(0<|x-x_0|<\delta_2):|f(x)-B|<\frac{\varepsilon}{2}$

取 $\delta=\min\{\delta_1,\delta_2\}$, 当
$0<|x-x_0|<\delta$ 时
$|A-B|\leq|f(x)-A|+|f(x)-B|<\varepsilon$
由于 $\varepsilon$ 可以任意接近于 $0$, 可知 $A=B$

------

局部保序性: 若 $\lim\limits_{x\to x_0}f(x)=A$,
$\lim\limits_{x\to x_0}g(x)=B$, 且 $A>B$, 则存在
$\delta>0$, 当 $0<|x-x_0|<\delta$ 时成立
$f(x)>g(x)$

证明: 取 $\varepsilon_0=\frac{A-B}{2}>0$
由 $\lim\limits_{x\to x_0}f(x)=A$,
$\exists\delta_1>0,\ \forall x(0<|x-x_0|<\delta_1):|f(x)-A|<\varepsilon_0$,
从而 $\frac{A+B}{2}<f(x)$

由 $\lim\limits_{x\to x_0}g(x)=B$,
$\exists\delta_2>0,\ \forall x(0<|x-x_0|<\delta_2):|g(x)-B|<\varepsilon_0$,
从而 $g(x)<\frac{A+B}{2}$

取 $\delta=\min\{\delta_1,\delta_2\}$, 当
$0<|x-x_0|<\delta$ 时成立
$g(x)<\frac{A+B}{2}<f(x)$

------

推论1: 若 $\lim\limits_{x\to x_0}f(x)=A\neq0$,
则存在 $\delta>0$, 当 $0<|x-x_0|<\delta$ 时成立
$|f(x)|>\frac{|A|}{2}$

证明: 由 $\lim\limits_{x\to x_0}f(x)=A$ 及
$||f(x)|-|A||\leq|f(x)-A|$ 可知
$\lim\limits_{x\to x_0}|f(x)|=|A|$

令 $g(x)=\frac{|A|}{2}$, 由 $\frac{|A|}{2}<|A|$
及局部保序性, 存在 $\delta>0$, 当 $0<|x-x_0|<\delta$
时成立 $|f(x)|>\frac{|A|}{2}$

------

推论2: 若 $\lim\limits_{x\to x_0}f(x)=A$,
$\lim\limits_{x\to x_0}g(x)=B$, 且存在 $r>0$,
使得当 $0<|x-x_0|<r$ 时成立 $g(x)\leq f(x)$, 则
$B\leq A$

证明: 用反证法. 若 $B>A$, 则由局部保序性, 存在 $\delta>0$, 当
$0<|x-x_0|<\delta$ 时 $g(x)>f(x)$
取 $\eta=\min\{\delta,r\}$, 当 $0<|x-x_0|<\eta$
时既有 $g(x)>f(x)$ 又有 $g(x)\leq f(x)$, 产生矛盾

[即使将推论2的条件加强到 $0<|x-x_0|<r$ 时成立 $g(x)<f(x)$,
也只能得到 $B\leq A$, 而不能得到 $B<A$]

------

推论3(局部有界性): 若 $\lim\limits_{x\to x_0}f(x)=A$,
则存在 $\delta>0$, 使 $f(x)$ 在
$O(x_0,\delta)\setminus\{x_0\}$ 中有界

证明: 取常数 $M$ 与 $m$, 满足 $m<A<M$, 令 $g(x)=m$,
$h(x)=M$ 为两个常数函数, 由局部保序性可知存在 $\delta>0$, 当
$0<|x-x_0|<\delta$ 时成立 $m<f(x)<M$

[若 $f(x)$ 在 $x_0$ 有定义, 可取
$G=\max\{|m|,|M|,|f(x_0)|\}$, 则当
$|x-x_0|<\delta$ 时成立 $|f(x)|\leq G$]

$\delta$ 不能随意扩大. 例如 $f(x)=\frac{1}{x}$,
$x_0=1$, 则 $f(x)$ 在
$\left\{x\mid0<|x-1|<\frac{1}{2}\right\}$
上有界, 但在 $\{x\mid0<|x-1|<1\}$ 上是无界的

------

夹逼性: 若存在 $r>0$, 使得当 $0<|x-x_0|<r$ 时成立
$g(x)\leq f(x)\leq h(x)$, 且
$\lim\limits_{x\to x_0}g(x)=\lim\limits_{x\to x_0}h(x)=A$,
则 $\lim\limits_{x\to x_0}f(x)=A$

证明: $\forall\varepsilon>0$
由 $\lim\limits_{x\to x_0}h(x)=A$, 可知
$\exists\delta_1>0,\ \forall x(0<|x-x_0|<\delta_1):h(x)<A+\varepsilon$

由 $\lim\limits_{x\to x_0}g(x)=A$, 可知
$\exists\delta_2>0,\ \forall x(0<|x-x_0|<\delta_2):A-\varepsilon<g(x)$

取 $\delta=\min\{\delta_1,\delta_2,r\}$,
$\forall x(0<|x-x_0|<\delta):A-\varepsilon<g(x)\leq f(x)\leq h(x)<A+\varepsilon$,
即 $\lim\limits_{x\to x_0}f(x)=A$

------

> 例3-4: 证明 $\lim\limits_{x\to0}\frac{\sin x}{x}=1$
>
> 证: 设 $\angle AOB$ 的弧度为 $x$,
> $0<x<\frac{\pi}{2}$
>
> 由 $\triangle OAB$ 面积 $<$ 扇形 $OAB$ 面积
> $<\triangle OBC$ 面积, 可得 $\sin x<x<\tan x$,
> $0<x<\frac{\pi}{2}$
>
> 从而有 $\cos x<\frac{\sin x}{x}<1$,
> $0<x<\frac{\pi}{2}$, 且上式对于
> $-\frac{\pi}{2}<x<0$ 也成立
>
> 由于 $|\cos x-1|=2\sin^2\frac{x}{2}\leq\frac{x^2}{2}$,
> 可知 $\lim\limits_{x\to0}\cos x=1$
> 应用极限的夹逼性, 得到 $\lim\limits_{x\to0}\frac{\sin x}{x}=1$

图3-2: 单位圆中的面积比较

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193108101.png =400x)


## 函数极限的四则运算

四则运算: 设 $\lim\limits_{x\to x_0}f(x)=A$,
$\lim\limits_{x\to x_0}g(x)=B$, 则
1. $\lim\limits_{x\to x_0}(\alpha f(x)+\beta g(x))=\alpha A+\beta B$
   ($\alpha,\beta$ 是常数)
2. $\lim\limits_{x\to x_0}(f(x)g(x))=AB$
3. $\lim\limits_{x\to x_0}\frac{f(x)}{g(x)}=\frac{A}{B}$
   ($B\neq0$)

证明: 因 $\lim\limits_{x\to x_0}f(x)=A$, 由局部有界性,
$\exists\delta_0>0,\ \forall x(0<|x-x_0|<\delta_0):|f(x)|\leq X$
且 $\forall\varepsilon>0,\ \exists\delta_1>0,\ \forall x(0<|x-x_0|<\delta_1):|f(x)-A|<\varepsilon$
再由 $\lim\limits_{x\to x_0}g(x)=B$ 可知
$\exists\delta_2>0,\ \forall x(0<|x-x_0|<\delta_2):|g(x)-B|<\varepsilon$

取 $\delta=\min\{\delta_0,\delta_1,\delta_2\}$,
则 $\forall x(0<|x-x_0|<\delta)$:
$|(\alpha f(x)+\beta g(x))-(\alpha A+\beta B)|\leq|\alpha|\cdot|f(x)-A|+|\beta|\cdot|g(x)-B|<(|\alpha|+|\beta|)\varepsilon$
$|f(x)g(x)-AB|=|f(x)(g(x)-B)+B(f(x)-A)|<(X+|B|)\varepsilon$
因此 (1) 与 (2) 成立

对 (3), 利用推论1 可知
$\exists\delta_0>0,\ \forall x(0<|x-x_0|<\delta_0):|g(x)|>\frac{|B|}{2}$
取 $\delta=\min\{\delta_0,\delta_1,\delta_2\}$,
$\forall x(0<|x-x_0|<\delta)$:
$\left|\frac{f(x)}{g(x)}-\frac{A}{B}\right|$
$=\left|\frac{B(f(x)-A)-A(g(x)-B)}{Bg(x)}\right|<\frac{2(|A|+|B|)}{|B|^2}\varepsilon$

------

> 例3-5: 对于任意实数 $\alpha\neq0$, 有
>
> $\lim\limits_{x\to0}\frac{\sin\alpha x}{x}$
> $=\lim\limits_{x\to0}\left(\frac{\sin\alpha x}{\alpha x}\cdot\alpha\right)$
> $=\alpha$
>
> 对于任意实数 $\alpha,\beta\neq0$, 有
> $\lim\limits_{x\to0}\frac{\sin\alpha x}{\sin\beta x}$
> $=\lim\limits_{x\to0}\left(\frac{\sin\alpha x}{\alpha x}\cdot\frac{\beta x}{\sin\beta x}\cdot\frac{\alpha}{\beta}\right)$
> $=\frac{\alpha}{\beta}$


## 函数极限与数列极限的关系

Heine 定理: $\lim\limits_{x\to x_0}f(x)=A$
的充分必要条件是: 对于任意满足条件
$\lim\limits_{n\to\infty}x_n=x_0$, 且
$x_n\neq x_0\ (n=1,2,3,\cdots)$ 的数列
$\{x_n\}$, 相应的函数值数列 $\{f(x_n)\}$ 成立
$\lim\limits_{n\to\infty}f(x_n)=A$

证明: 必要性. 由 $\lim\limits_{x\to x_0}f(x)=A$ 可知
$\forall\varepsilon>0$, $\exists\delta>0$,
$\forall x(0<|x-x_0|<\delta):|f(x)-A|<\varepsilon$
因为 $\lim\limits_{n\to\infty}x_n=x_0$ 且
$x_n\neq x_0(n=1,2,3,\cdots)$, 对上述 $\delta>0$
有 $\exists N,\forall n>N:0<|x_n-x_0|<\delta$
于是当 $n>N$ 时成立 $|f(x_n)-A|<\varepsilon$, 即
$\lim\limits_{n\to\infty}f(x_n)=A$

充分性. 用反证法. 命题 "$f(x)$ 在 $x_0$ 点以 $A$
为极限" 的否定命题可表述为
$\exists\varepsilon_0>0,\ \forall\delta>0,\ \exists x(0<|x-x_0|<\delta):|f(x)-A|\geq\varepsilon_0$
即存在某个固定正数 $\varepsilon_0$, 不管 $\delta$ 取得多么小,
总能在 $O(x_0,\delta)\setminus\{x_0\}$ 中找到一点
$x$, 使 $|f(x)-A|\geq\varepsilon_0$

取一列 $\{\delta_k\}$,
$\delta_k=\frac{1}{k}\ (k=1,2,3,\cdots)$
对 $\delta_1=1$ 存在 $x_1(0<|x_1-x_0|<\delta_1)$
使 $|f(x_1)-A|\geq\varepsilon_0$
对 $\delta_2=\frac{1}{2}$ 存在
$x_2(0<|x_2-x_0|<\delta_2)$ 使
$|f(x_2)-A|\geq\varepsilon_0$
一般地对 $\delta_k=\frac{1}{k}$ 存在
$x_k(0<|x_k-x_0|<\delta_k)$ 使
$|f(x_k)-A|\geq\varepsilon_0$

于是得到数列 $\{x_n\}$ 满足 $x_n\neq x_0$,
$\lim\limits_{n\to\infty}x_n=x_0$, 但相应的函数值数列
$\{f(x_n)\}$ 不可能以 $A$ 为极限
由此推翻假定, 得到 $f(x)$ 在 $x_0$ 点以 $A$ 为极限

[该性质常用于证明某个函数极限的不存在性]

------

> 例3-6: 证明 $\sin\frac{1}{x}$ 在 $x=0$ 没有极限
>
> 证: 取 $x_n^{(1)}=\frac{1}{n\pi}$,
> $x_n^{(2)}=\frac{1}{2n\pi+\frac{\pi}{2}}\ (n=1,2,3,\cdots)$
> 则显然有 $x_n^{(1)}\neq0$,
> $\lim\limits_{n\to\infty}x_n^{(1)}=0$ 与
> $x_n^{(2)}\neq0$,
> $\lim\limits_{n\to\infty}x_n^{(2)}=0$
>
> 但 $\lim\limits_{n\to\infty}\sin\frac{1}{x_n^{(1)}}=0$,
> 而 $\lim\limits_{n\to\infty}\sin\frac{1}{x_n^{(2)}}=1$
> 根据 Heine 定理, 可知 $\sin\frac{1}{x}$ 在 $x=0$ 没有极限

图3-3: 函数 $y=\sin\frac{1}{x}$ 在 $x=0$ 附近的振荡

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193108102.png =500x)

注: 若只关心函数 $f(x)$ 在点 $x_0$ 的极限是否存在, 而不论极限值是多少,
Heine 定理有另一种表述
$\lim\limits_{x\to x_0}f(x)$
存在的充分必要条件是: 对于任意满足条件
$\lim\limits_{n\to\infty}x_n=x_0$ 且
$x_n\neq x_0(n=1,2,3,\cdots)$ 的数列 $\{x_n\}$,
相应的函数值数列 $\{f(x_n)\}$ 收敛


## 单侧极限

左极限: 设 $f(x)$ 在 $(x_0-\rho,x_0)$ 有定义 ($\rho>0$).
如果存在实数 $B$, 对任意给定的 $\varepsilon>0$ 可以找到
$\delta>0$, 使得当 $-\delta<x-x_0<0$ 时成立
$|f(x)-B|<\varepsilon$, 则称 $B$ 是 $f(x)$ 在点
$x_0$ 的左极限, 记为
$\lim\limits_{x\to x_0^-}f(x)=f(x_0-)=B$

------

右极限: 设 $f(x)$ 在 $(x_0,x_0+\rho)$ 有定义 ($\rho>0$),
且存在实数 $C$, 对任意给定的 $\varepsilon>0$ 可以找到
$\delta>0$, 使得当 $0<x-x_0<\delta$ 时成立
$|f(x)-C|<\varepsilon$, 则称 $C$ 是 $f(x)$ 在点
$x_0$ 的右极限, 记为
$\lim\limits_{x\to x_0^+}f(x)=f(x_0+)=C$

------

极限存在的充要条件: $\lim\limits_{x\to x_0}f(x)$
$=A\iff\lim\limits_{x\to x_0^-}f(x)$
$=\lim\limits_{x\to x_0^+}f(x)$
$=A$

------

> 例3-7: 符号函数 $\text{sgn}\,x$ 在原点有单侧极限但不相等:
> $\lim\limits_{x\to0^-}\text{sgn}\,x=-1$,
> $\lim\limits_{x\to0^+}\text{sgn}\,x=1$
> 因此符号函数在 $x=0$ 处没有极限

> 例3-8: 设 $f(x)=\begin{cases}\frac{\sin 2x}{x}, & x<0\\ 2\cos x^2, & x\geq0\end{cases}$
> 问当 $x$ 趋于 $0$ 时, $f(x)$ 的极限是否存在
> 解: 由于 $\lim\limits_{x\to0^-}f(x)=\lim\limits_{x\to0^-}\frac{\sin 2x}{x}=2$,
> $\lim\limits_{x\to0^+}f(x)=\lim\limits_{x\to0^+}2\cos x^2=2$
> 因此当 $x$ 趋于 $0$ 时 $f(x)$ 的极限存在, 且
> $\lim\limits_{x\to0}f(x)=2$


## 函数极限定义的扩充

自变量的极限过程有六种情形: $x\to x_0$, $x\to x_0^+$,
$x\to x_0^-$, $x\to\infty$, $x\to+\infty$,
$x\to-\infty$

函数值的极限情况有四种情形: $f(x)\to A$(有限数),
$f(x)\to+\infty$, $f(x)\to-\infty$,
$f(x)\to\infty$

函数值的极限的表述
- "$f(x)\to A$(有限数)":
  $\forall\varepsilon>0,\cdots:|f(x)-A|<\varepsilon$
- "$f(x)\to+\infty$":
  $\forall G>0,\cdots:f(x)>G$
- "$f(x)\to-\infty$":
  $\forall G>0,\cdots:f(x)<-G$
- "$f(x)\to\infty$":
  $\forall G>0,\cdots:|f(x)|>G$

自变量的极限过程的表述
- "$x\to x_0$":
  $\cdots,\exists\delta>0,\forall x(0<|x-x_0|<\delta):\cdots$
- "$x\to x_0^+$":
  $\cdots,\exists\delta>0,\forall x(0<x-x_0<\delta):\cdots$
- "$x\to x_0^-$":
  $\cdots,\exists\delta>0,\forall x(-\delta<x-x_0<0):\cdots$
- "$x\to\infty$":
  $\cdots,\exists X>0,\forall x(|x|>X):\cdots$
- "$x\to+\infty$":
  $\cdots,\exists X>0,\forall x(x>X):\cdots$
- "$x\to-\infty$":
  $\cdots,\exists X>0,\forall x(x<-X):\cdots$

[例如 $\lim\limits_{x\to x_0^+}f(x)=\infty$
的定义为 $\forall G>0,\exists\delta>0,\forall x(0<x-x_0<\delta):|f(x)|>G$;
$\lim\limits_{x\to\infty}f(x)=A$ 的定义为
$\forall\varepsilon>0,\exists X>0,\forall x(x>X):|f(x)-A|<\varepsilon$]

------

关于扩充定义的函数极限的几点说明
1. 局部保序性与夹逼性只当函数极限 $A$ 为有限数, $+\infty$ 与
   $-\infty$ 时才成立, 即须排除 $A$ 是未定号无穷大 $\infty$ 的情况
   这是因为无法将 $\infty$ 与任意有限数作大小的比较, 而对于定号无穷大
   $+\infty$ 或 $-\infty$, 可以规定
   $-\infty<A<+\infty$ ($A$ 为任意实数)
2. 四则运算法则只要不是待定型, 如 $\infty\pm\infty$,
   $(+\infty)-(+\infty)$, $(+\infty)+(-\infty)$,
   $0\cdot\infty$, $\frac{0}{0}$,
   $\frac{\infty}{\infty}$ 等, 就总是成立的
   出现待定型时需要对具体的函数极限作具体的讨论
3. 对于不同的函数极限, 分别有相应的 Heine 定理, 它们的叙述,
   证明方法和作用都是类似的

------

> 例3-9: 证明 $\lim\limits_{x\to-\infty}e^x=0$
> 证: 对于任意给定的 $\varepsilon\in(0,1)$, 取
> $X=\ln\frac{1}{\varepsilon}>0$, 当 $x<-X$ 时成立
> $0<e^x<e^{-X}=\varepsilon$
> 于是得到 $\lim\limits_{x\to-\infty}e^x=0$

> 例3-10: 证明 $\lim\limits_{x\to1^+}\frac{x^2}{x-1}=-\infty$
>
> 证: 对于任意给定的 $G>0$, 要找 $\delta>0$, 使当
> $-\delta<x-1<0$ 时成立 $\frac{x^2}{x-1}<-G$
> 为了适度放大不等式的左边, 先加上条件 $-\frac{1}{2}<x-1<0$, 于是
> $x^2>\frac{1}{4}$, 从而
> $\frac{x^2}{x-1}<\frac{1}{4(x-1)}$
>
> 令 $\delta=\min\left\{\frac{1}{2},\frac{1}{4G}\right\}$,
> 则当 $-\delta<x-1<0$ 时
> $\frac{x^2}{x-1}<\frac{1}{4(x-1)}<-\frac{1}{4\delta}\leq-G$

> 例3-11: 证明 $\lim\limits_{x\to-\infty}e^x=0$,
> $\lim\limits_{x\to0^+}e^{\frac{1}{x}}=+\infty$
>
> 证: 令 $y=\frac{1}{x}$, 可知函数
> $f(x)=e^{\frac{1}{x}}$ 在 $x=0$ 的左极限存在, 且
> $\lim\limits_{x\to0^-}e^{\frac{1}{x}}=0$
> 而当 $x\to0^+$ 时, 函数 $f(x)$ 趋于 $+\infty$, 即
> $\lim\limits_{x\to0^+}e^{\frac{1}{x}}=+\infty$

图3-4: 函数 $y=e^{\frac{1}{x}}$ 的图像

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193108103.png =400x)

> 例3-12: 讨论极限 $L$
> $=\lim\limits_{x\to\infty}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_kx^k}{b_mx^m+b_{m-1}x^{m-1}+\cdots+b_jx^j}$
> 与 $l=\lim\limits_{x\to0}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_kx^k}{b_mx^m+b_{m-1}x^{m-1}+\cdots+b_jx^j}$,
> 其中 $a_n,a_k,b_m,b_j$ 都是非零实数
>
> 解: (1) $x\to\infty$ 情形
> 当 $n=m$ 时, $L$
> $=\lim\limits_{x\to\infty}\frac{a_n+\frac{a_{n-1}}{x}+\cdots+\frac{a_k}{x^{n-k}}}{b_m+\frac{b_{m-1}}{x}+\cdots+\frac{b_j}{x^{m-j}}}$
> $=\frac{a_n}{b_m}$
>
> 当 $n<m$ 时, $L$
> $=\lim\limits_{x\to\infty}\left(\frac{1}{x^{m-n}}\cdot\frac{a_n+\frac{a_{n-1}}{x}+\cdots+\frac{a_k}{x^{n-k}}}{b_m+\frac{b_{m-1}}{x}+\cdots+\frac{b_j}{x^{m-j}}}\right)$
> $=0$
>
> 当 $n>m$ 时, $L$
> $=\lim\limits_{x\to\infty}\left(x^{n-m}\cdot\frac{a_n+\frac{a_{n-1}}{x}+\cdots+\frac{a_k}{x^{n-k}}}{b_m+\frac{b_{m-1}}{x}+\cdots+\frac{b_j}{x^{m-j}}}\right)$
> $=\infty$
>
> (2) $x\to0$ 情形
> 当 $k=j$ 时, $l$
> $=\lim\limits_{x\to0}\frac{a_kx^k+a_{k+1}x^{k+1}+\cdots+a_nx^n}{b_jx^j+b_{j+1}x^{j+1}+\cdots+b_mx^m}$
> $=\frac{a_k}{b_j}$
>
> 当 $k>j$ 时, $l$
> $=\lim\limits_{x\to0}\left(x^{k-j}\cdot\frac{a_k+a_{k+1}x+\cdots+a_nx^{n-k}}{b_j+b_{j+1}x+\cdots+b_mx^{m-j}}\right)$
> $=0$
>
> 当 $k<j$ 时, $l$
> $=\lim\limits_{x\to0}\left(\frac{1}{x^{j-k}}\cdot\frac{a_k+a_{k+1}x+\cdots+a_nx^{n-k}}{b_j+b_{j+1}x+\cdots+b_mx^{m-j}}\right)$
> $=\infty$
>
> 所以
> $L$
> $=\lim\limits_{x\to\infty}\frac{a_nx^n+\cdots+a_kx^k}{b_mx^m+\cdots+b_jx^j}$
> $=\begin{cases}\frac{a_n}{b_m}, & n=m\\ 0, & n<m\\ \infty, & n>m\end{cases}$
> $l$
> $=\lim\limits_{x\to0}\frac{a_nx^n+\cdots+a_kx^k}{b_mx^m+\cdots+b_jx^j}$
> $=\begin{cases}\frac{a_k}{b_j}, & k=j\\ 0, & k>j\\ \infty, & k<j\end{cases}$

> 例3-13: $\lim\limits_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e$
>
> 证: 先证 $\lim\limits_{x\to+\infty}\left(1+\frac{1}{x}\right)^x=e$
> 对于任意 $x\geq1$, 有
> $\left(1+\frac{1}{[x]+1}\right)^{[x]}<\left(1+\frac{1}{x}\right)^x<\left(1+\frac{1}{[x]}\right)^{[x]+1}$,
> 其中 $[x]$ 表示 $x$ 的整数部分
>
> 当 $x\to+\infty$ 时, 不等式左, 右两侧表现为两个数列极限
> $\lim\limits_{n\to\infty}\left(1+\frac{1}{n+1}\right)^n=e$
> 与 $\lim\limits_{n\to\infty}\left(1+\frac{1}{n}\right)^{n+1}=e$
> 利用函数极限的夹逼性, 得到
> $\lim\limits_{x\to+\infty}\left(1+\frac{1}{x}\right)^x=e$
>
> 再证 $\lim\limits_{x\to-\infty}\left(1+\frac{1}{x}\right)^x=e$
> 为此令 $y=-x$, 于是当 $x\to-\infty$ 时
> $y\to+\infty$, 从而
> $\lim\limits_{x\to-\infty}\left(1+\frac{1}{x}\right)^x$
> $=\lim\limits_{y\to+\infty}\left(1-\frac{1}{y}\right)^{-y}$
> $=\lim\limits_{y\to+\infty}\left[\left(1+\frac{1}{y-1}\right)^{y-1}\cdot\left(1+\frac{1}{y-1}\right)\right]$
> $=e$
>
> 将 $\lim\limits_{x\to+\infty}\left(1+\frac{1}{x}\right)^x=e$
> 与 $\lim\limits_{x\to-\infty}\left(1+\frac{1}{x}\right)^x=e$
> 结合起来, 就得到 $\lim\limits_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e$

注: 例3-13 的证明中包含下述结果:
$\lim\limits_{x\to\infty}\left(1-\frac{1}{x}\right)^x=\frac{1}{e}$

------

Cauchy 收敛原理: 函数极限
$\lim\limits_{x\to+\infty}f(x)$
存在而且有限的充分必要条件是: 对于任意给定的 $\varepsilon>0$, 存在
$X>0$, 使得对一切 $x',x''>X$ 成立
$|f(x')-f(x'')|<\varepsilon$

证明: 必要性. 设 $\lim\limits_{x\to+\infty}f(x)=A$,
按定义 $\forall\varepsilon>0$, $\exists X>0$,
$\forall x',x''>X$:
$|f(x')-A|<\frac{\varepsilon}{2}$,
$|f(x'')-A|<\frac{\varepsilon}{2}$
于是 $|f(x')-f(x'')|\leq|f(x')-A|+|f(x'')-A|<\varepsilon$

充分性. 设 $\forall\varepsilon>0$, $\exists X>0$,
$\forall x',x''>X:|f(x')-f(x'')|<\varepsilon$
任意选取数列 $\{x_n\}$,
$\lim\limits_{n\to\infty}x_n=+\infty$, 对上述
$X>0$, $\exists N,\forall n>N:x_n>X$, 于是当
$m>n>N$ 时成立 $|f(x_n)-f(x_m)|<\varepsilon$
这说明函数值数列 $\{f(x_n)\}$ 是基本数列, 因而必定收敛
根据相应的 Heine 定理, 可知
$\lim\limits_{x\to+\infty}f(x)$ 存在而且有限

[对 $\lim\limits_{x\to x_0}f(x)$,
$\lim\limits_{x\to x_0^+}f(x)$,
$\lim\limits_{x\to-\infty}f(x)$
存在而且有限的 Cauchy 收敛原理可仿此写出并证明]


## 连续函数的定义

连续函数的定义: 设函数 $f(x)$ 在点 $x_0$ 的某个邻域中有定义, 并且成立
$\lim\limits_{x\to x_0}f(x)=f(x_0)$, 则称函数
$f(x)$ 在点 $x_0$ 连续, 称 $x_0$ 是函数 $f(x)$ 的连续点

符号表述: $\forall\varepsilon>0,\ \exists\delta>0,\ \forall x(|x-x_0|<\delta):|f(x)-f(x_0)|<\varepsilon$

[在 $x_0$ 连续只是函数极限
$\lim\limits_{x\to x_0}f(x)=A$ 中 $A$ 为
$f(x_0)$ 的特殊情况, 只需将极限值 $A$ 换成 $f(x_0)$, 并去掉
$|x-x_0|>0$ 的要求, 因为 $x=x_0$ 时显然有
$|f(x)-f(x_0)|=0$]

------

开区间上的连续性: 若函数 $f(x)$ 在区间 $(a,b)$ 的每一点都连续,
则称函数 $f(x)$ 在开区间 $(a,b)$ 上连续

------

> 例3-14: 函数 $f(x)=\frac{1}{x}$ 在区间 $(0,1)$ 连续
>
> 证: 设 $x_0\in(0,1)$ 是任意一点, 对于任意给定的
> $\varepsilon>0$, 要找 $\delta>0$, 使得当
> $|x-x_0|<\delta$ 时
> $\left|\frac{1}{x}-\frac{1}{x_0}\right|=\frac{|x-x_0|}{xx_0}<\varepsilon$
>
> 为了放大不等式左边, 加上条件 $|x-x_0|<\frac{x_0}{2}$, 于是
> $x>\frac{x_0}{2}$, 从而 $xx_0>\frac{x_0^2}{2}$
>
> 取 $\delta=\min\left\{\frac{x_0}{2},\frac{x_0^2}{2}\varepsilon\right\}$,
> 当 $|x-x_0|<\delta$ 时
> $\left|\frac{1}{x}-\frac{1}{x_0}\right|<\frac{2|x-x_0|}{x_0^2}<\varepsilon$
> 所以 $f(x)=\frac{1}{x}$ 在 $(0,1)$ 连续

------

左连续与右连续
- 若 $\lim\limits_{x\to x_0^-}f(x)=f(x_0)$, 则称函数
  $f(x)$ 在 $x_0$ 左连续
- 若 $\lim\limits_{x\to x_0^+}f(x)=f(x_0)$, 则称函数
  $f(x)$ 在 $x_0$ 右连续

------

闭区间上的连续性: 若 $f(x)$ 在 $(a,b)$ 连续, 且在左端点 $a$
右连续, 在右端点 $b$ 左连续, 则称函数 $f(x)$ 在闭区间 $[a,b]$
上连续

[上述定义可统一表述为: 设函数 $f(x)$ 定义在某区间 $X$ 上, $X$
可以是开区间, 闭区间或半开半闭区间. 若 $\forall x_0\in X$ 与
$\forall\varepsilon>0$, $\exists\delta>0$,
$\forall x\in X(|x-x_0|<\delta):|f(x)-f(x_0)|<\varepsilon$,
则称 $f(x)$ 在区间 $X$ 上连续]

------

> 例3-15: $f(x)=\sqrt{x(1-x)}$ 在闭区间 $[0,1]$ 上连续
>
> 证: 设 $x_0\in(0,1)$ 是任意一点, 令
> $\eta=\min\{x_0,1-x_0\}>0$
> 当 $|x-x_0|<\eta$ 时 $x\in(0,1)$, 因而
> $|\sqrt{x(1-x)}-\sqrt{x_0(1-x_0)}|$
> $=\frac{|1-x-x_0|}{\sqrt{x(1-x)}+\sqrt{x_0(1-x_0)}}|x-x_0|<\frac{1}{\sqrt{x_0(1-x_0)}}|x-x_0|$
>
> 对任意给定的 $\varepsilon>0$, 取
> $\delta=\min\{\eta,\sqrt{x_0(1-x_0)}\varepsilon\}$,
> 当 $|x-x_0|<\delta$ 时成立
> $|\sqrt{x(1-x)}-\sqrt{x_0(1-x_0)}|<\varepsilon$
> 所以 $f(x)=\sqrt{x(1-x)}$ 在 $(0,1)$ 上连续
>
> 考虑区间的端点, 对任意给定的 $\varepsilon>0$, 取
> $\delta=\varepsilon^2$, 当 $0\leq x<\delta$ 时
> $|f(x)-f(0)|\leq\sqrt{x}<\varepsilon$; 当
> $-\delta<x-1\leq0$ 时
> $|f(x)-f(1)|\leq\sqrt{1-x}<\varepsilon$
>
> 这说明 $f(x)$ 在 $x=0$ 右连续, 在 $x=1$ 左连续
> 由此得出 $f(x)=\sqrt{x(1-x)}$ 在闭区间 $[0,1]$ 上连续

> 例3-16: $f(x)=\sin x$ 在 $(-\infty,+\infty)$ 上连续
>
> 证: 设 $x_0\in(-\infty,+\infty)$ 是任意一点, 由于
> $|\sin x-\sin x_0|=2\left|\cos\frac{x+x_0}{2}\sin\frac{x-x_0}{2}\right|\leq|x-x_0|$
>
> 对任意给定的 $\varepsilon>0$, 取
> $\delta=\varepsilon$, 当 $|x-x_0|<\delta$ 时成立
> $|\sin x-\sin x_0|\leq|x-x_0|<\varepsilon$
> 所以 $f(x)=\sin x$ 在 $(-\infty,+\infty)$ 上连续
>
> 同样可以按定义证明 $f(x)=\cos x$ 在 $(-\infty,+\infty)$
> 上连续

> 例3-17: 指数函数 $f(x)=a^x\ (a>0,a\neq1)$ 在
> $(-\infty,+\infty)$ 上连续
>
> 证: 对任意一点 $x_0\in(-\infty,+\infty)$, 有
> $a^x-a^{x_0}=a^{x_0}(a^{x-x_0}-1)$
> 所以证 $\lim\limits_{x\to x_0}a^x=a^{x_0}$ 就归结为证
> $\lim\limits_{t\to0}a^t=1$
>
> 若 $t\to0+$, 则当 $a>1$ 时成立
> $1<a^t<a^{\left[\frac{1}{t}\right]}$, 因
> $\lim\limits_{n\to\infty}\sqrt[n]{a}=1$,
> 由夹逼性得 $\lim\limits_{t\to0+}a^t=1$
>
> 当 $0<a<1$ 时, 由极限的除法运算得
> $\lim\limits_{t\to0+}a^t$
> $=\lim\limits_{t\to0+}\frac{1}{\left(\frac{1}{a}\right)^t}$
> $=\frac{1}{\lim\limits_{t\to0+}\left(\frac{1}{a}\right)^t}$
> $=1$
>
> 若 $t\to0-$, 则令 $u=-t$, 于是
> $\lim\limits_{t\to0-}a^t=\lim\limits_{u\to0+}\frac{1}{a^u}=1$
> 综合起来得到 $\lim\limits_{t\to0}a^t=1$, 从而有
> $\lim\limits_{x\to x_0}a^x=a^{x_0}$


## 连续函数的四则运算

设 $\lim\limits_{x\to x_0}f(x)=f(x_0)$,
$\lim\limits_{x\to x_0}g(x)=g(x_0)$, 则
1. $\lim\limits_{x\to x_0}(\alpha f(x)+\beta g(x))=\alpha f(x_0)+\beta g(x_0)$
   ($\alpha,\beta$ 是常数)
2. $\lim\limits_{x\to x_0}(f(x)g(x))=f(x_0)g(x_0)$
3. $\lim\limits_{x\to x_0}\frac{f(x)}{g(x)}=\frac{f(x_0)}{g(x_0)}$
   ($g(x_0)\neq0$)

有限个函数在某个区间连续, 则它们之间进行有限次加, 减, 乘, 除四则运算后,
所得的函数在该区间除去使分母为零的点后的范围连续

------

> 例3-18: 对于常数函数 $f(x)=c$ 与恒等函数 $g(x)=x$,
> 容易从定义出发证明它们在 $(-\infty,+\infty)$ 上连续,
> 再由连续函数的四则运算规则可知
>
> 1. 任意多项式 $p_n(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$
>    在 $(-\infty,+\infty)$ 上连续
> 2. 任意有理函数 $Q(x)=\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0}{b_mx^m+b_{m-1}x^{m-1}+\cdots+b_1x+b_0}$
>    在其定义域上连续, 即 $Q(x)$ 在 $(-\infty,+\infty)$
>    中去掉分母 $b_mx^m+b_{m-1}x^{m-1}+\cdots+b_1x+b_0$
>    的零点 (至多 $m$ 个点) 的范围连续

> 例3-19: 由例3-16 证明了三角函数 $\sin x$ 与 $\cos x$
> 的连续性, 由连续函数的四则运算规则可知
>
> 正切函数 $\tan x=\frac{\sin x}{\cos x}$, 正割函数
> $\sec x=\frac{1}{\cos x}$ 在其定义域
> $\{x\mid x\in R,x\neq k\pi+\frac{\pi}{2},k\in Z\}$
> 上连续
>
> 余切函数 $\cot x=\frac{\cos x}{\sin x}$, 余割函数
> $\csc x=\frac{1}{\sin x}$ 在其定义域
> $\{x\mid x\in R,x\neq k\pi,k\in Z\}$ 上连续


## 不连续点类型

按连续性定义, 函数 $f(x)$ 在点 $x_0$ 连续必须满足
1. 函数 $f(x)$ 在点 $x_0$ 有定义, 即 $f(x_0)$ 为有限值
2. 函数 $f(x)$ 在点 $x_0$ 有左极限, 且 $f(x_0-)=f(x_0)$
3. 函数 $f(x)$ 在点 $x_0$ 有右极限, 且 $f(x_0+)=f(x_0)$

三者缺一不可, 否则函数 $f(x)$ 在点 $x_0$ 不连续, 此时点 $x_0$
是函数 $f(x)$ 的不连续点, 亦称间断点

------

不连续点的分类
1. 第一类不连续点: $f(x)$ 在点 $x_0$ 的左, 右极限都存在但不相等, 即
   $f(x_0+)\neq f(x_0-)$
2. 第二类不连续点: $f(x)$ 在点 $x_0$ 的左, 右极限中至少有一个不存在
3. 第三类不连续点: $f(x)$ 在点 $x_0$ 的左, 右极限都存在而且相等, 但不等于
   $f(x_0)$ 或者 $f(x)$ 在点 $x_0$ 无定义

第一类不连续点在函数图像中出现一个跳跃, 故称跳跃点, 而右极限与左极限之差
$f(x_0+)-f(x_0-)$ 称为函数 $f(x)$ 在点 $x_0$ 的跃度
[符号函数 $\text{sgn}\,x$ 在 $x=0$ 的跃度为 2]

第三类不连续点可以通过重新定义在该点的函数值使之成为连续点, 故又称可去不连续点或可去间断点

例: $f(x)=e^{\frac{1}{x}}$ 的 $x=0$ 是第二类不连续点,
因为 $f(0-)=\lim\limits_{x\to0^-}e^{\frac{1}{x}}=0$,
$f(0+)=\lim\limits_{x\to0^+}e^{\frac{1}{x}}=+\infty$

例: $f(x)=\sin\frac{1}{x}$ 的 $x=0$ 也是第二类不连续点

例: $f(x)=x\sin\frac{1}{x}$ 在 $x=0$ 没有定义, 但在
$x=0$ 的左, 右极限都等于 $0$, 所以 $x=0$ 是它的第三类不连续点
通过重新定义 $f(x)=\begin{cases}x\sin\frac{1}{x}, & x\neq0\\ 0, & x=0\end{cases}$,
则 $f(x)$ 就是 $(-\infty,+\infty)$ 上的连续函数

------

> 例3-20: Riemann 函数 $R(x)$
> $=\begin{cases}\frac{1}{p}, & x=\frac{q}{p}\ (p\in N^*,q\in Z\setminus\{0\},p,q\text{互素})\\ 1, & x=0\\ 0, & x\text{是无理数}\end{cases}$
> 其中定义 $R(0)=1$ 是因为 $x=0$ 可写成 $x=\frac{0}{1}$,
> 同时也保证了 $R(x)$ 的周期性
> 证明 $R(x)$ 在任意点 $x_0$ 的极限存在, 且极限值为 $0$. 换言之,
> 一切无理点是 $R(x)$ 的连续点, 而一切有理点是 $R(x)$ 的第三类不连续点
>
> 证: $R(x)$ 是以 $1$ 为周期的周期函数, 所以只要讨论区间 $[0,1]$
> 上的函数性质
>
> 在 $[0,1]$ 上, 分母为 $1$ 的有理点只有两个: $\frac{0}{1}$
> 和 $\frac{1}{1}$; 分母为 $2$ 的有理点只有一个:
> $\frac{1}{2}$; 分母为 $3$ 的有理点只有两个: $\frac{1}{3}$
> 和 $\frac{2}{3}$; 分母为 $4$ 的有理点只有两个:
> $\frac{1}{4}$ 和 $\frac{3}{4}$; 分母为 $5$
> 的有理点只有四个: $\frac{1}{5},\frac{2}{5},\frac{3}{5}$
> 和 $\frac{4}{5}$
> 总之, 对任意正整数 $k$, 在 $[0,1]$ 上分母不超过 $k$
> 的有理点个数是有限的
>
> 设 $x_0\in[0,1]$ 是任意一点, 对任意给定的
> $\varepsilon>0$, 取
> $k=\left[\frac{1}{\varepsilon}\right]$, 因为在
> $[0,1]$ 上分母不超过 $k$ 的有理点个数有限, 设它们为
> $r_1,r_2,\cdots,r_s$
>
> 令 $\delta=\min\limits_{r_i\neq x_0}\{|r_i-x_0|\}$,
> 显然 $\delta>0$
> 当 $x\in[0,1]$ 且 $0<|x-x_0|<\delta$ 时, 若 $x$
> 是无理数则 $R(x)=0$; 若 $x$ 是有理数, 其分母必大于
> $\left[\frac{1}{\varepsilon}\right]$, 于是
> $R(x)\leq\frac{1}{\left[\frac{1}{\varepsilon}\right]+1}<\varepsilon$
> 因此成立 $|R(x)-0|<\varepsilon$
>
> 此即表明 $R(x)$ 在 $x_0$ 的极限为 $0$ ($x_0=0$ 时是指右极限,
> $x_0=1$ 时是指左极限)
> 根据 $R(x)$ 的周期性, 对一切 $x_0\in(-\infty,+\infty)$
> 成立 $\lim\limits_{x\to x_0}R(x)=0$

> 例3-21: 区间 $(a,b)$ 上单调函数的不连续点必为第一类不连续点

> 证: 不妨设 $f(x)$ 在 $(a,b)$ 单调增加
> 设 $x_0\in(a,b)$ 是任意一点, 显然集合
> $\{f(x)\mid x\in(a,x_0)\}$ 有上界, 由确界存在定理,
> 必定存在上确界, 记它为 $\alpha=\sup\{f(x)\mid x\in(a,x_0)\}$
> 对一切 $x\in(a,x_0)$ 成立 $f(x)\leq\alpha$;
> 而对任意给定的 $\varepsilon>0$, 必存在 $x'\in(a,x_0)$
> 使得 $f(x')>\alpha-\varepsilon$
>
> 取 $\delta=x_0-x'>0$, 则当 $-\delta<x-x_0<0$ 时,
> 有 $x'<x<x_0$, 于是成立
> $-\varepsilon<f(x')-\alpha\leq f(x)-\alpha\leq0$,
> 即 $|f(x)-\alpha|<\varepsilon$
> 这就说明 $\lim\limits_{x\to x_0^-}f(x)=\alpha$.
> 同理可证 $\lim\limits_{x\to x_0^+}f(x)=\beta$, 其中
> $\beta=\inf\{f(x)\mid x\in(x_0,b)\}$

[单调函数在任意点的左, 右极限都存在, 换言之, 单调函数的不连续点必定是跳跃点]


## 反函数连续性定理

反函数存在性定理: 若函数 $y=f(x)$, $x\in D_f$
是严格单调增加 (减少) 的, 则存在它的反函数 $x=f^{-1}(y)$,
$y\in R_f$, 并且 $f^{-1}(y)$ 也是严格单调增加 (减少) 的

证明: 不妨设 $y=f(x)$, $x\in D_f$ 严格单调增加. 对任意两点
$x',x''\in D_f$ 及它们相应的函数值 $y'=f(x')$,
$y''=f(x'')$, 由 $f$ 严格单调增加可知
$x'<x''\iff y'<y''$, 显然它保证了逆像的唯一性, 所以存在反函数
$x=f^{-1}(y)$, $y\in R_f$

设 $y_1,y_2\in R_f$, $y_1<y_2$, 它们的逆像相应地记为
$x_1=f^{-1}(y_1)$, $x_2=f^{-1}(y_2)$, 则
$x_1,x_2$ 的大小只有三种可能: (1) $x_1>x_2$; (2)
$x_1=x_2$; (3) $x_1<x_2$

但 $x_1>x_2$ 违背 $f$ 的严格单调增加性, $x_1=x_2$ 违背 $f$
具有像的唯一性, 于是必然有 $x_1<x_2$
这表明 $f^{-1}(y)$ 也是严格单调增加的

------

反函数连续性定理: 设函数 $y=f(x)$ 在闭区间 $[a,b]$
上连续且严格单调增加, $f(a)=\alpha$, $f(b)=\beta$,
则它的反函数 $x=f^{-1}(y)$ 在 $[\alpha,\beta]$
连续且严格单调增加

证明: 先证明 $f([a,b])=[\alpha,\beta]$, 即 $f$
的值域 (也就是 $f^{-1}$ 的定义域) 是 $[\alpha,\beta]$

显然 $\alpha,\beta\in f([a,b])$. 设
$\gamma\in(\alpha,\beta)$ 是任意一点, 记
$S=\{x\mid x\in[a,b],f(x)<\gamma\}$
则集合 $S$ 非空且有上界, 由确界存在定理, $S$ 必有上确界, 记
$x_0=\sup S$, 则 $x_0\in(a,b)$

根据 $f(x)$ 的严格单调增加性, 当 $x<x_0$ 时
$f(x)<\gamma$; 当 $x>x_0$ 时 $f(x)>\gamma$
于是由单调函数的单侧极限, 得到
$f(x_0-)\leq\gamma\leq f(x_0+)$

由 $f(x)$ 在点 $x_0$ 的连续性, 得到
$f(x_0)=f(x_0+)=f(x_0-)=\gamma$. 这就说明 $f(x)$
的值域是闭区间 $[\alpha,\beta]$
根据反函数存在性定理, 在 $[\alpha,\beta]$ 上必定存在 $f$ 的反函数
$x=f^{-1}(y)$, 且 $f^{-1}(y)$ 也是严格单调增加函数

再证明反函数 $x=f^{-1}(y)$ 在 $[\alpha,\beta]$ 上的连续性

设 $y_0\in(\alpha,\beta)$, 相应地有
$f^{-1}(y_0)=x_0\in(a,b)$
对于任意给定的 $\varepsilon>0$, 要找出 $\delta>0$, 使当
$|y-y_0|<\delta$ 时成立
$|f^{-1}(y)-f^{-1}(y_0)|=|f^{-1}(y)-x_0|<\varepsilon$,
即 $x_0-\varepsilon<f^{-1}(y)<x_0+\varepsilon$

令 $y_1=f(x_0-\varepsilon)$,
$y_2=f(x_0+\varepsilon)$, 取
$\delta=\min\{y_0-y_1,y_2-y_0\}>0$

显然当 $|y-y_0|<\delta$ 时成立
$|f^{-1}(y)-f^{-1}(y_0)|<\varepsilon$

如果 $y_0=\alpha$, 则只要证明右连续性; 如果 $y_0=\beta$,
则只要证明左连续性

图3-5: 反函数连续性的证明

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193108104.png =400x)

------

> 例3-22: 由 $\sin x$ 的连续性, 三角函数的连续性与反函数连续性定理,
> 可知下述反三角函数在它们的定义域连续
>
> $y=\arcsin x$, $x\in[-1,1]$,
> $y\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$
> $y=\arccos x$, $x\in[-1,1]$, $y\in[0,\pi]$
> $y=\arctan x$, $x\in(-\infty,+\infty)$,
> $y\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$
> $y=\text{arccot}\,x$,
> $x\in(-\infty,+\infty)$, $y\in(0,\pi)$
>
> 由指数函数 $y=a^x\ (a>0,a\neq1)$ 在 $(0,+\infty)$
> 连续, 可知指数函数 $y=a^x$ 的反函数
> $y=\log_a x\ (a>0,a\neq1)$ 在 $(0,+\infty)$ 连续


## 复合函数的连续性

设 $\lim\limits_{x\to x_0}g(x)=u_0$,
$\lim\limits_{u\to u_0}f(u)=A$, 对于复合函数
$f\circ g(x)$ 不能得出
$\lim\limits_{x\to x_0}f\circ g(x)=A$ 的结论

反例: $y=f(u)=\begin{cases}0, & u=0\\ 1, & u\neq0\end{cases}$,
$u=g(x)=x\sin\frac{1}{x}$
显然有 $\lim\limits_{x\to0}g(x)=0$,
$\lim\limits_{u\to0}f(u)=1$, 但是复合函数
$f\circ g(x)$ 在 $x=0$ 没有极限
但当 $f$ 与 $g$ 都是连续函数时, 则上述结论是成立的

------

复合函数的连续性: 若 $u=g(x)$ 在点 $x_0$ 连续,
$g(x_0)=u_0$, 又 $y=f(u)$ 在点 $u_0$ 连续, 则复合函数
$y=f\circ g(x)$ 在点 $x_0$ 连续

证明: 对于任意给定的 $\varepsilon>0$, 由于
$\lim\limits_{u\to u_0}f(u)=f(u_0)$, 所以存在
$\eta>0$, 当 $|u-u_0|<\eta$ 时成立
$|f(u)-f(u_0)|<\varepsilon$

对上面的 $\eta>0$, 由于
$\lim\limits_{x\to x_0}g(x)=g(x_0)=u_0$, 所以存在
$\delta>0$, 当 $|x-x_0|<\delta$ 时成立
$|g(x)-u_0|<\eta$

由此得出, 当 $|x-x_0|<\delta$ 时
$|f\circ g(x)-f\circ g(x_0)|=|f\circ g(x)-f(u_0)|<\varepsilon$,
即 $\lim\limits_{x\to x_0}f\circ g(x)=f\circ g(x_0)$

------

> 例3-23: 双曲正弦函数
> $\text{sh}\,x=\frac{e^x-e^{-x}}{2}$ 与双曲余弦函数
> $\text{ch}\,x=\frac{e^x+e^{-x}}{2}$
> 是实际问题中经常遇到的两个初等函数
>
> 因为它们可以看成由连续函数 $y=f(u)=\frac{u\pm u^{-1}}{2}$,
> $D_f=(-\infty,0)\cup(0,+\infty)$ 与
> $u=g(x)=e^x$, $D_g=(-\infty,+\infty)$,
> $R_g=(0,+\infty)$ 复合而成, 所以它们在
> $(-\infty,+\infty)$ 连续

> 例3-24: 对于任意实数 $\alpha$, 幂函数 $f(x)=x^\alpha$ 在
> $(0,+\infty)$ 连续
>
> 解: 幂函数 $f(x)=x^\alpha$ 是由
> $f(x)=x^\alpha=e^{\alpha\ln x}$,
> $x\in(0,+\infty)$ 定义的, 即它是由 $y=e^u$,
> $u\in(-\infty,+\infty)$ 与 $u=\alpha\ln x$,
> $x\in(0,+\infty)$ 复合而成
> 根据复合函数的连续性, $f(x)=x^\alpha$ 在 $(0,+\infty)$ 连续

注: 对于具体给定的实数 $\alpha$, $f(x)=x^\alpha$
的定义域可以扩大. 例如当 $\alpha$ 是正整数 $n$ 时, $f(x)=x^n$
的定义域是 $(-\infty,+\infty)$; 当 $\alpha$ 是负整数
$-n$ 时 $f(x)=x^{-n}$ 的定义域是
$(-\infty,0)\cup(0,+\infty)$; 当 $\alpha$ 是有理数
$\frac{q}{p}$ (既约分数), 若 $p$ 是奇数则定义域是
$(-\infty,+\infty)$, 若 $p$ 是偶数则定义域是
$[0,+\infty)$

总之, 幂函数 $f(x)=x^\alpha$ 在其定义域连续

------

初等函数的连续性: 一切初等函数在其定义区间上连续
[初等函数由常数函数, 幂函数, 指数函数, 对数函数, 三角函数,
反三角函数这 6 类基本初等函数经过有限次四则运算及复合运算产生]

------

> 例3-25: 计算极限 $\lim\limits_{x\to0}(\cos x)^{\frac{1}{x^2}}$
>
> 解: 利用对数恒等式, 有 $(\cos x)^{\frac{1}{x^2}}=e^u$,
> 其中
> $u$
> $=g(x)$
> $=\frac{1}{x^2}\ln(\cos x)$
> $=\frac{1}{x^2}\ln\left(1-2\sin^2\frac{x}{2}\right)$
> $=-\frac{2\sin^2\frac{x}{2}}{x^2}\ln\left(1-2\sin^2\frac{x}{2}\right)^{-\frac{1}{2\sin^2\frac{x}{2}}}$
>
> 由 $\lim\limits_{x\to0}\frac{\sin x}{x}=1$,
> 有理式极限的结论和对数函数的连续性
> $\lim\limits_{x\to0}g(x)$
> $=\lim\limits_{x\to0}\frac{2\sin^2\frac{x}{2}}{x^2}\ln\left(1-2\sin^2\frac{x}{2}\right)^{-\frac{1}{2\sin^2\frac{x}{2}}}$
> $=\frac{1}{2}\ln\frac{1}{e}$
> $=-\frac{1}{2}$
>
> 再由指数函数 $e^u$ 的连续性, 得到
> $\lim\limits_{x\to0}(\cos x)^{\frac{1}{x^2}}$
> $=\lim\limits_{x\to0}e^{g(x)}$
> $=\frac{1}{\sqrt{e}}$

> 例3-26: 放射性物质的质量变化规律
> 设时刻 $t=0$ 时有质量为 $m$ 的某种放射性物质,
> 它的瞬时放射速率与该时刻放射性物质的质量成正比, 比例系数为 $k$
> 求时刻 $t$ 该放射性物质的质量 $m(t)$
>
> 解: 随着时间从 $0$ 变到 $t$, 放射性物质的质量在连续不断地减少,
> 而放射速率也随之连续地减小
>
> 为便于计算, 将时间区间 $[0,t]$ 平均分成 $n$ 个小间区
> $(0,t]=\bigcup\limits_{i=1}^{n}\Delta_i$,
> $\Delta_i=\left(\frac{(i-1)t}{n},\frac{it}{n}\right]$
> 并在每个小区间 $\Delta_i$ 上, 将放射速率近似地取为常数
> $km\left(\frac{(i-1)t}{n}\right)$
>
> 在时间段 $\Delta_1$ 上, 因放射速率近似为 $km$, 于是
> $m\left(\frac{t}{n}\right)\approx m-km\frac{t}{n}=m\left(1-\frac{k}{n}t\right)$
> 在时间段 $\Delta_2$ 上, 因放射速率近似为
> $km\left(\frac{t}{n}\right)$, 于是
> $m\left(\frac{2t}{n}\right)\approx m\left(1-\frac{k}{n}t\right)-km\left(1-\frac{k}{n}t\right)\frac{t}{n}$
> $=m\left(1-\frac{k}{n}t\right)^2$
>
> 继续不断地做下去, 可得到 $m(t)$ 的近似值
> $m(t)\approx m\left(1-\frac{k}{n}t\right)^n$
>
> 很自然地认为, 分割的区间数 $n$ 越大, 近似值就越接近 $m(t)$ 的精确值, 于是
> $m(t)$
> $=\lim\limits_{n\to\infty}m\left(1-\frac{k}{n}t\right)^n$
> $=m\lim\limits_{n\to\infty}e^{n\ln\left(1-\frac{k}{n}t\right)}$
> $=me^{-kt}$


## 无穷小量的比较

无穷小量: 若 $\lim\limits_{x\to x_0}f(x)=0$, 则称当
$x\to x_0$ 时 $f(x)$ 是无穷小量

[无穷小量是以零为极限的变量, 极限过程 $x\to x_0$ 可以扩充到
$x\to x_0^+$, $x\to x_0^-$, $x\to\infty$,
$x\to+\infty$, $x\to-\infty$ 等情况]

------

设 $u(x),v(x)$ 是两个变量, 当 $x\to x_0$ 时它们都是无穷小量,
为了比较两者趋于零的速度快慢, 讨论 $\frac{u(x)}{v(x)}$ 的极限情况

1. 若 $\lim\limits_{x\to x_0}\frac{u(x)}{v(x)}=0$,
   则表示当 $x\to x_0$ 时 $u(x)$ 趋于零的速度比 $v(x)$ 快
   称当 $x\to x_0$ 时 $u(x)$ 关于 $v(x)$ 是高阶无穷小量 (或
   $v(x)$ 关于 $u(x)$ 是低阶无穷小量), 记为
   $u(x)=o(v(x))\ (x\to x_0)$
   例如 $\lim\limits_{x\to0}\frac{1-\cos x}{x}=\lim\limits_{x\to0}\frac{2\sin^2\frac{x}{2}}{x}=0$,
   可表示为 $1-\cos x=o(x)\ (x\to0)$
   又如 $\lim\limits_{x\to0}\frac{\tan x-\sin x}{x^2}=\lim\limits_{x\to0}\left(\frac{\sin x}{\cos x}\cdot\frac{1-\cos x}{x}\right)=0$,
   可表示为 $\tan x-\sin x=o(x^2)\ (x\to0)$

2. 若存在 $A>0$, 当 $x$ 在 $x_0$ 的某个去心邻域中时成立
   $\left|\frac{u(x)}{v(x)}\right|\leq A$, 则称当
   $x\to x_0$ 时 $\frac{u(x)}{v(x)}$ 是有界量, 记为
   $u(x)=O(v(x))\ (x\to x_0)$
   例如当 $x\to0$ 时 $x\sin\frac{1}{x}$ 与 $x$
   都是无穷小量, 且 $\left|\frac{x\sin\frac{1}{x}}{x}\right|\leq1$,
   从而 $x\sin\frac{1}{x}=O(x)\ (x\to0)$
   若又存在 $a>0$, 当 $x$ 在 $x_0$ 的某个去心邻域中时成立
   $a\leq\left|\frac{u(x)}{v(x)}\right|\leq A$,
   则称当 $x\to x_0$ 时 $u(x)$ 与 $v(x)$ 是同阶无穷小量

3. 若 $\lim\limits_{x\to x_0}\frac{u(x)}{v(x)}=1$,
   则称当 $x\to x_0$ 时 $u(x)$ 与 $v(x)$ 是等价无穷小量, 记为
   $u(x)\sim v(x)\ (x\to x_0)$
   上式也可写成 $u(x)=v(x)+o(v(x))\ (x\to x_0)$, 它表示当
   $x\to x_0$ 时 $u(x)$ 与 $v(x)$ 并不一定相等, 两者相差一个关于
   $v(x)$ 的高阶无穷小量
   例如 $\lim\limits_{x\to0}\frac{\sin x}{x}=1$
   可表示为 $\sin x\sim x\ (x\to0)$ 或者
   $\sin x=x+o(x)\ (x\to0)$
   $\lim\limits_{x\to0}\frac{1-\cos x}{\frac{1}{2}x^2}$
   $=\lim\limits_{x\to0}\frac{2\sin^2\frac{x}{2}}{\frac{1}{2}x^2}$
   $=1$ 可表示为 $1-\cos x\sim\frac{1}{2}x^2\ (x\to0)$
   或者 $1-\cos x=\frac{1}{2}x^2+o(x^2)\ (x\to0)$
   $\lim\limits_{x\to0}\frac{\tan x-\sin x}{\frac{1}{2}x^3}$
   $=\lim\limits_{x\to0}\left(\frac{\sin x}{\cos x}\cdot\frac{1-\cos x}{\frac{1}{2}x^2}\right)$
   $=1$ 可表示为 $\tan x-\sin x\sim\frac{1}{2}x^3\ (x\to0)$
   或者 $\tan x-\sin x=\frac{1}{2}x^3+o(x^3)\ (x\to0)$

[记号 $o$, $O$ 和 $\sim$ 都是相对于一定的极限过程的,
在使用时应附上记号 $(x\to x_0)$ 以说明相应的极限过程,
唯有在意义明确不会发生误解的前提下才能省略]

选取 $v(x)=(x-x_0)^k$ 作为与 $u(x)$
进行比较的无穷小量 (如果极限过程是 $x\to\infty$, 则选取
$v(x)=\frac{1}{x^k}$), 便于得出 $u(x)$ 作为无穷小量的确切阶数
例如由 $1-\cos x\sim\frac{1}{2}x^2\ (x\to0)$ 可知
$1-\cos x$ 是二阶无穷小量; 由
$\tan x-\sin x\sim\frac{1}{2}x^3\ (x\to0)$ 可知
$\tan x-\sin x$ 是三阶无穷小量

常用记号
- $u(x)=o(1)\ (x\to x_0)$ 表示当 $x\to x_0$ 时
  $u(x)$ 是无穷小量
- $u(x)=O(1)\ (x\to x_0)$ 表示当 $x\to x_0$ 时
  $u(x)$ 是有界量

例: 当 $x\to0+$ 时 $\frac{1}{\ln x}$ 是无穷小量,
但它关于无穷小量 $x^\alpha$ ($\alpha$
为任意小的正数) 总是低阶无穷小量, 所以它只能表示为
$\frac{1}{\ln x}=o(1)\ (x\to0+)$

例: 当 $x\to0$ 时 $e^x\sin\frac{1}{x}$ 是有界量,
所以可表示为 $e^x\sin\frac{1}{x}=O(1)\ (x\to0)$

------

> 例3-27: 证明当 $x\to0+$ 时, 对任意的正整数 $k$,
> $\left(\frac{1}{\ln x}\right)^k$ 关于 $x$
> 是低阶无穷小量
>
> 证: 令 $y=-\ln x$, 则当 $x\to0+$ 时 $y\to+\infty$,
> 于是 $\lim\limits_{x\to0+}\frac{x}{\left(\frac{1}{\ln x}\right)^k}$
> $=\lim\limits_{y\to+\infty}\frac{y^k}{e^y}$
> $=0$

> 例3-28: 证明当 $x\to0+$ 时, 对任意的正整数 $k$,
> $e^{-\frac{1}{x}}$ 关于 $x^k$ 是高阶无穷小量
>
> 证: 令 $y=\frac{1}{x}$, 则当 $x\to0+$ 时
> $y\to+\infty$, 于是
> $\lim\limits_{x\to0+}\frac{e^{-\frac{1}{x}}}{x^k}$
> $=\lim\limits_{y\to+\infty}\frac{y^k}{e^y}$
> $=0$


## 无穷大量的比较

无穷大量: 若 $\lim\limits_{x\to x_0}f(x)=\infty$
(或 $\pm\infty$), 则称当 $x\to x_0$ 时 $f(x)$
是无穷大量 (或正, 负无穷大量)

[定义中的极限过程同样可以扩充到 $x\to x_0^+$, $x\to x_0^-$,
$x\to\infty$, $x\to+\infty$, $x\to-\infty$
等情况]

------

设 $u(x),v(x)$ 是两个变量, 当 $x\to x_0$ 时它们都是无穷大量,
为了比较两者趋于无穷大的速度, 同样讨论 $\frac{u(x)}{v(x)}$ 的极限情况

1. 若 $\lim\limits_{x\to x_0}\frac{u(x)}{v(x)}=\infty$,
   则称当 $x\to x_0$ 时 $u(x)$ 关于 $v(x)$ 是高阶无穷大量 (或
   $v(x)$ 关于 $u(x)$ 是低阶无穷大量)
   例如对任意正整数 $k$, 有
   $\lim\limits_{x\to+\infty}\frac{a^x}{x^k}=\infty\ (a>1)$
   和 $\lim\limits_{x\to+\infty}\frac{\ln^k x}{x}=0$,
   所以当 $x\to+\infty$ 时 $a^x(a>1)$ 关于 $x^k$
   是高阶无穷大量, $\ln^k x$ 关于 $x$ 是低阶无穷大量

2. 若存在 $A>0$, 当 $x$ 在 $x_0$ 的某个去心邻域中时成立
   $\left|\frac{u(x)}{v(x)}\right|\leq A$, 则称当
   $x\to x_0$ 时 $\frac{u(x)}{v(x)}$ 是有界量, 记为
   $u(x)=O(v(x))\ (x\to x_0)$
   例如当 $x\to+\infty$ 时 $x(\arctan x+\sin x)$ 与
   $x$ 都是无穷大量, 且
   $\left|\frac{x(\arctan x+\sin x)}{x}\right|\leq3$,
   从而 $x(\arctan x+\sin x)=O(x)\ (x\to+\infty)$
   若又存在 $a>0$, 当 $x$ 在 $x_0$ 的某个去心邻域中时成立
   $a\leq\left|\frac{u(x)}{v(x)}\right|\leq A$,
   则称当 $x\to x_0$ 时 $u(x)$ 与 $v(x)$ 是同阶无穷大量

3. 若 $\lim\limits_{x\to x_0}\frac{u(x)}{v(x)}=1$,
   则称当 $x\to x_0$ 时 $u(x)$ 与 $v(x)$ 是等价无穷大量, 记为
   $u(x)\sim v(x)\ (x\to x_0)$
   例如 $\lim\limits_{x\to\infty}\frac{x^3\sin\frac{1}{x}}{x^2}$
   $=\lim\limits_{x\to\infty}\frac{\sin\frac{1}{x}}{\frac{1}{x}}$
   $=1$ 可表示为 $x^3\sin\frac{1}{x}\sim x^2\ (x\to\infty)$
   对于极限 $\lim\limits_{x\to\frac{\pi}{2}}\left(\frac{\pi}{2}-x\right)\tan x$,
   令 $y=\frac{\pi}{2}-x$, 得到
   $\lim\limits_{x\to\frac{\pi}{2}}\left(\frac{\pi}{2}-x\right)\tan x=\lim\limits_{y\to0+}\frac{y\cos y}{\sin y}=1$,
   此即可表示为 $\tan x\sim\frac{1}{\frac{\pi}{2}-x}\ \left(x\to\frac{\pi}{2}\right)$

[在进行无穷大量阶的比较时, 习惯上不使用记号 $o$, 但仍使用记号 $O$ 和
$\sim$]


## 等价量

等价量: 就是等价无穷小量或等价无穷大量, 在极限计算中起重要作用

------

> 例3-29: 证明 $\ln(1+x)\sim x\ (x\to0)$
> 证: 由 $\lim\limits_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e$
> 得到等价于 $\lim\limits_{x\to0}(1+x)^{\frac{1}{x}}=e$
> 利用对数函数的连续性, 得到
> $\lim\limits_{x\to0}\frac{\ln(1+x)}{x}=\lim\limits_{x\to0}\ln(1+x)^{\frac{1}{x}}=1$

> 例3-30: 证明 $e^x-1\sim x\ (x\to0)$
> 证: 令 $y=e^x-1$, 则当 $x\to0$ 时 $y\to0$, 且
> $x=\ln(1+y)$, 于是
> $\lim\limits_{x\to0}\frac{e^x-1}{x}=\lim\limits_{y\to0}\frac{y}{\ln(1+y)}=1$

> 例3-31: 证明 $(1+x)^\alpha-1\sim\alpha x\ (x\to0)$
>
> 证: 令 $(1+x)^\alpha-1=y$, 则当 $x\to0$ 时
> $y\to0$, 于是
> $\lim\limits_{x\to0}\frac{(1+x)^\alpha-1}{x}$
> $=\lim\limits_{y\to0}\frac{(1+x)^\alpha-1}{\alpha\ln(1+x)}\cdot\frac{\alpha\ln(1+x)}{x}$
> $=\lim\limits_{y\to0}\frac{y}{\ln(1+y)}\cdot\lim\limits_{x\to0}\frac{\alpha\ln(1+x)}{x}$
> $=\alpha$

常用等价量: $\sin x\sim x$, $\ln(1+x)\sim x$,
$e^x-1\sim x$, $(1+x)^\alpha-1\sim\alpha x$ (
$x\to0$)

> 例3-32: 设 $u(x)=\sqrt{x+\sqrt{x}}$
>
> 当 $x\to+\infty$ 时,
> $\lim\limits_{x\to+\infty}\frac{\sqrt{x+\sqrt{x}}}{\sqrt{x}}=\lim\limits_{x\to+\infty}\sqrt{1+\frac{1}{\sqrt{x}}}=1$,
> 所以有 $u(x)\sim x^{\frac{1}{2}}\ (x\to+\infty)$
>
> 当 $x\to0+$ 时,
> $\lim\limits_{x\to0+}\frac{\sqrt{x+\sqrt{x}}}{\sqrt[4]{x}}=\lim\limits_{x\to0+}\sqrt{1+\sqrt{x}}=1$,
> 所以有 $u(x)\sim x^{\frac{1}{4}}\ (x\to0+)$

> 例3-33: 设 $v(x)=2x^3+3x^5$
> 当 $x\to\infty$ 时,
> $\lim\limits_{x\to\infty}\frac{2x^3+3x^5}{3x^5}=1$,
> 所以有 $v(x)\sim 3x^5\ (x\to\infty)$
> 当 $x\to0$ 时, $\lim\limits_{x\to0}\frac{2x^3+3x^5}{2x^3}=1$,
> 所以有 $v(x)\sim 2x^3\ (x\to0)$

设一个变量由几个相互不同阶的成分相加而成,
则当它是无穷大量时与阶数最高的那个无穷大量成分等价;
当它是无穷小量时与阶数最低的那个无穷小量成分等价

------

等价量替换定理: 设 $u(x)$, $v(x)$ 和 $w(x)$ 在 $x_0$
的某个去心邻域 $U$ 上有定义, 且
$\lim\limits_{x\to x_0}\frac{v(x)}{u(x)}=1$
(即 $v(x)\sim u(x)\ (x\to x_0)$), 那么
1. 当 $\lim\limits_{x\to x_0}u(x)w(x)=A$ 时,
   $\lim\limits_{x\to x_0}v(x)w(x)=A$
2. 当 $\lim\limits_{x\to x_0}\frac{w(x)}{u(x)}=A$
   时, $\lim\limits_{x\to x_0}\frac{w(x)}{v(x)}=A$

[定理的证明可由极限的四则运算法则直接得到, 其中的极限过程 $x\to x_0$
可以相应地改为 $x\to x_0^+$, $x\to x_0^-$,
$x\to\infty$, $x\to+\infty$, $x\to-\infty$
等情况]

------

> 例3-34: 应用等价量替换定理,
>
> $\lim\limits_{x\to\infty}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_mx^m}{b_kx^k+b_{k-1}x^{k-1}+\cdots+b_jx^j}$
> $=\lim\limits_{x\to\infty}\frac{a_nx^n}{b_kx^k}$
> $=\frac{a_n}{b_k}\ (a_n,b_k\neq0)$
>
> 与 $\lim\limits_{x\to0}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_mx^m}{b_kx^k+b_{k-1}x^{k-1}+\cdots+b_jx^j}$
> $=\lim\limits_{x\to0}\frac{a_mx^m}{b_jx^j}$
> $=\frac{a_m}{b_j}\ (a_m,b_j\neq0)$

> 例3-35: 计算 $\lim\limits_{x\to0}\frac{\ln(1+x^2)}{(e^{2x}-1)\tan x}$
> 解: 由于 $\tan x\sim x$, $e^{2x}-1\sim 2x$,
> $\ln(1+x^2)\sim x^2\ (x\to0)$, 由等价量替换定理得
> $\lim\limits_{x\to0}\frac{\ln(1+x^2)}{(e^{2x}-1)\tan x}$
> $=\lim\limits_{x\to0}\frac{x^2}{2x\cdot x}$
> $=\frac{1}{2}$

> 例3-36: 计算 $\lim\limits_{x\to0}\frac{\sqrt{1+x}-e^{\frac{x}{3}}}{\ln(1+2x)}$
> 解: $\lim\limits_{x\to0}\frac{\sqrt{1+x}-e^{\frac{x}{3}}}{\ln(1+2x)}$
> $=\lim\limits_{x\to0}\frac{(\sqrt{1+x}-1)-(e^{\frac{x}{3}}-1)}{\ln(1+2x)}$
> $=\lim\limits_{x\to0}\frac{\left[\frac{x}{2}+o(x)\right]-\left[\frac{x}{3}+o(x)\right]}{2x}$
> $=\lim\limits_{x\to0}\frac{\frac{x}{6}+o(x)}{2x}$
> $=\frac{1}{12}$

> 例3-37: 计算 $\lim\limits_{x\to\infty}x\left(\sqrt[3]{x^3+x}-\sqrt[3]{x^3-x}\right)$
> 解: $\lim\limits_{x\to\infty}x\left(\sqrt[3]{x^3+x}-\sqrt[3]{x^3-x}\right)$
> $=\lim\limits_{x\to\infty}x^2\left[\left(\sqrt[3]{1+\frac{1}{x^2}}-1\right)-\left(\sqrt[3]{1-\frac{1}{x^2}}-1\right)\right]$
> $=\lim\limits_{x\to\infty}x^2\left\{\left[\frac{1}{3x^2}+o\left(\frac{1}{x^2}\right)\right]-\left[-\frac{1}{3x^2}+o\left(\frac{1}{x^2}\right)\right]\right\}$
> $=\lim\limits_{x\to\infty}x^2\left[\frac{2}{3x^2}+o\left(\frac{1}{x^2}\right)\right]$
> $=\frac{2}{3}$

> 例3-38: 计算 $\lim\limits_{x\to0}(\cos x)^{\frac{1}{x^2}}$
>
> 解: $\lim\limits_{x\to0}(\cos x)^{\frac{1}{x^2}}$
> $=\lim\limits_{x\to0}\left[1-(1-\cos x)\right]^{\frac{1}{x^2}}$
> $=\lim\limits_{x\to0}\left(1-\frac{x^2}{2}\right)^{\frac{1}{x^2}}$
> $=\lim\limits_{x\to0}\left[\left(1-\frac{x^2}{2}\right)^{\frac{2}{x^2}}\right]^{\frac{1}{2}}$
> $=\frac{1}{\sqrt{e}}$
>
> 利用等价关系 $1-\cos x\sim\frac{x^2}{2}\ (x\to0)$,
> 问题比按对数恒等式计算时简单得多

[使用等价量替换时, 若计算中出现无穷小量 (或无穷大量) 相加或相减,
就不能不加考虑地直接进行替换]

[例如求 $\lim\limits_{x\to0}\frac{\tan x-\sin x}{x^3}$
时, 若用 $\tan x\sim x$ 与 $\sin x\sim x$ 进行替换,
得到 $\lim\limits_{x\to0}\frac{x-x}{x^3}=0$
的错误结论, 实际 $\lim\limits_{x\to0}\frac{\tan x-\sin x}{x^3}=\frac{1}{2}$]

[这是因为 $\tan x-\sin x$ 虽然与 $x$ 的等价量相关, 但省略了关于
$x$ 的高阶无穷小量部分后, 两者之差并不等于 $0$, 而是等价于 $x$
的高阶无穷小量 $\frac{x^3}{2}$]

[若用 $\tan x=x+o(x)$ 和 $\sin x=x+o(x)$ 进行替换,
则得到 $\lim\limits_{x\to0}\frac{\tan x-\sin x}{x^3}=\lim\limits_{x\to0}\frac{o(x)}{x^3}$,
虽不能据此判断极限是否存在, 但至少可以避免上述错误]

[再如求 $\lim\limits_{x\to0}\frac{\sqrt{1+x}-1-\frac{1}{2}x}{x^2}$
时, 也不能直接用 $x\to0$ 时的等价关系
$\sqrt{1+x}-1\sim\frac{1}{2}x$ 代入, 事实上
$\lim\limits_{x\to0}\frac{\sqrt{1+x}-1-\frac{1}{2}x}{x^2}$
$=\lim\limits_{x\to0}\frac{(1+x)-\left(1+\frac{1}{2}x\right)^2}{x^2\left(\sqrt{1+x}+1+\frac{1}{2}x\right)}$
$=\lim\limits_{x\to0}\frac{-\frac{1}{4}x^2}{x^2\left(\sqrt{1+x}+1+\frac{1}{2}x\right)}$
$=-\frac{1}{8}$]


## 有界性定理

有界性定理: 若函数 $f(x)$ 在闭区间 $[a,b]$ 上连续, 则它在
$[a,b]$ 上有界

证明: 用反证法
若 $f(x)$ 在 $[a,b]$ 上无界, 将 $[a,b]$ 等分为两个小区间
$\left[a,\frac{a+b}{2}\right]$ 与
$\left[\frac{a+b}{2},b\right]$, 则 $f(x)$
至少在其中之一上无界, 把它记为 $[a_1,b_1]$
再将闭区间 $[a_1,b_1]$ 等分为两个小区间
$\left[a_1,\frac{a_1+b_1}{2}\right]$ 与
$\left[\frac{a_1+b_1}{2},b_1\right]$, 同样
$f(x)$ 至少在其中之一上无界, 把它记为 $[a_2,b_2]$
这样的步骤一直做下去, 便得到一个闭区间套 $\{[a_n,b_n]\}$, $f(x)$
在其中任何一个闭区间 $[a_n,b_n]$ 上都是无界的

根据闭区间套定理, 存在惟一的实数 $\xi$ 属于所有的闭区间 $[a_n,b_n]$,
并且 $\xi=\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n$
因为 $\xi\in[a,b]$, 而 $f(x)$ 在点 $\xi$ 连续,
由局部有界性, 存在 $\delta>0$, $M>0$, 对于一切
$x\in O(\xi,\delta)\cap[a,b]$ 成立
$|f(x)|\leq M$

由于 $\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n=\xi$,
又可知道对于充分大的 $n$,
$[a_n,b_n]\subset O(\xi,\delta)\cap[a,b]$

于是得到 $f(x)$ 在这些闭区间 $[a_n,b_n]$ ($n$
充分大) 上有界的结论, 从而产生矛盾
这说明所作的假设不能成立, 即函数 $f(x)$ 在 $[a,b]$ 上必定有界

[开区间上的连续函数就不一定是有界的, 例如 $f(x)=\frac{1}{x}$
在开区间 $(0,1)$ 上连续, 但显然是无界的]


## 最值定理

最值定理: 若函数 $f(x)$ 在闭区间 $[a,b]$ 上连续, 则它在 $[a,b]$
上必能取到最大值与最小值, 即存在 $\xi$ 和 $\eta\in[a,b]$,
对于一切 $x\in[a,b]$ 成立
$f(\xi)\leq f(x)\leq f(\eta)$

证明: 由有界性定理, 集合 $R_f=\{f(x)\mid x\in[a,b]\}$
是一个有界数集, 所以必有上确界与下确界, 记 $\alpha=\inf R_f$,
$\beta=\sup R_f$

现在证明存在 $\xi\in[a,b]$ 使得 $f(\xi)=\alpha$
按照下确界的定义, 对一切 $x\in[a,b]$ 成立
$f(x)\geq\alpha$; 另一方面对任意给定的 $\varepsilon>0$,
存在 $x\in[a,b]$ 使得 $f(x)<\alpha+\varepsilon$

于是取 $\varepsilon_n=\frac{1}{n}\ (n=1,2,3,\cdots)$,
相应地得到一个数列 $\{x_n\}$, $x_n\in[a,b]$, 并且满足
$\alpha\leq f(x_n)<\alpha+\frac{1}{n}$

因为 $\{x_n\}$ 是有界数列,
应用 Bolzano-Weierstrass 定理, 存在收敛子列
$\{x_{n_k}\}$:
$\lim\limits_{k\to\infty}x_{n_k}=\xi$, 且
$\xi\in[a,b]$

考虑不等式 $\alpha\leq f(x_{n_k})<\alpha+\frac{1}{n_k}$,
$k=1,2,3,\cdots$, 令 $k\to\infty$, 由极限的夹逼性与
$f(x)$ 在点 $\xi$ 的连续性, 得到 $f(\xi)=\alpha$

这说明 $f(x)$ 在 $[a,b]$ 上取到最小值 $\alpha$, 即
$\alpha=\min R_f$
同样可以证明存在 $\eta\in[a,b]$ 使得
$f(\eta)=\beta=\max R_f$

[开区间上的连续函数即使有界, 也不一定能取到它的最大 (小) 值. 例如 $f(x)=x$
在 $(0,1)$ 连续而且有界, 因而有上确界与下确界
$\alpha=\inf\{f(x)\mid x\in(0,1)\}=0$ 和
$\beta=\sup\{f(x)\mid x\in(0,1)\}=1$, 但是
$f(x)$ 在区间 $(0,1)$ 上取不到 $\alpha=0$ 与 $\beta=1$]


## 零点存在定理

零点存在定理: 若函数 $f(x)$ 在闭区间 $[a,b]$ 连续, 且
$f(a)\cdot f(b)<0$, 则一定存在 $\xi\in(a,b)$ 使
$f(\xi)=0$

证明: 不失一般性, 设 $f(a)<0$, $f(b)>0$, 定义集合
$V=\{x\mid f(x)<0,x\in[a,b]\}$
显然, 集合 $V$ 有界, 非空, 所以必有上确界, 令 $\xi=\sup V$

现证 $\xi\in(a,b)$, 且 $f(\xi)=0$
由 $f(x)$ 的连续性及 $f(a)<0$, $\exists\delta_1>0$,
$\forall x\in[a,a+\delta_1):f(x)<0$; 再由
$f(b)>0$, $\exists\delta_2>0$,
$\forall x\in(b-\delta_2,b]:f(x)>0$
于是可知 $a+\delta_1\leq\xi\leq b-\delta_2$, 即
$\xi\in(a,b)$

取 $x_n\in V\ (n=1,2,\cdots)$,
$x_n\to\xi\ (n\to\infty)$, 因 $f(x_n)<0$, 可以得到
$f(\xi)=\lim\limits_{n\to\infty}f(x_n)\leq0$

若 $f(\xi)<0$, 由 $f(x)$ 在点 $\xi$ 的连续性,
$\exists\delta>0$,
$\forall x\in O(\xi,\delta):f(x)<0$, 这就与
$\xi=\sup V$ 产生矛盾
于是必然有 $f(\xi)=0$

------

> 例3-39: 讨论多项式 $p(x)=2x^3-3x^2-3x+2$ 零点 (亦称为方程
> $p(x)=0$ 的"根") 的位置
>
> 解: 通过简单的计算, 可以得到

| $x$ | $-2$ | $0$ | $1$ | $3$ |
| --- | --- | --- | --- | --- |
| $p(x)$ | $-20$ | $2$ | $-2$ | $20$ |

> 由此得知 $p(x)$ 的三个零点 (或根) 分别落在区间 $(-2,0)$,
> $(0,1)$ 与 $(1,3)$ 内
> 事实上, $p(x)=2(x+1)\left(x-\frac{1}{2}\right)(x-2)$,
> 它的三个零点为 $x_1=-1$, $x_2=\frac{1}{2}$, $x_3=2$

> 例3-40: 设函数 $f(x)$ 在闭区间 $[a,b]$ 上连续, 且
> $f([a,b])\subset[a,b]$, 则存在 $\xi\in[a,b]$ 使
> $f(\xi)=\xi$. 这样的 $\xi$ 称为 $f(x)$ 的一个不动点
>
> 证: 设 $g(x)=f(x)-x$, 则 $g(x)$ 在 $[a,b]$ 上连续, 由
> $f([a,b])\subset[a,b]$ 可知 $g(a)\geq0$,
> $g(b)\leq0$
>
> 若 $g(a)=0$, 则有 $\xi=a$; 若 $g(b)=0$, 则有 $\xi=b$
> 若 $g(a)>0$, $g(b)<0$, 则由零点存在定理, 必存在
> $\xi\in(a,b)$, 使得 $g(\xi)=0$, 即 $f(\xi)=\xi$

[本例中闭区间 $[a,b]$ 不能改为开区间. 例如 $f(x)=\frac{x}{2}$
在开区间 $(0,1)$ 上连续, 且 $f((0,1))\subset(0,1)$,
但 $f(x)$ 在开区间 $(0,1)$ 中没有不动点]


## 中间值定理

中间值定理: 若函数 $f(x)$ 在闭区间 $[a,b]$ 上连续,
则它一定能取到最大值 $M=\max\{f(x)\mid x\in[a,b]\}$
和最小值 $m=\min\{f(x)\mid x\in[a,b]\}$ 之间的任何一个值

证明: 由最值定理, 存在 $\xi,\eta\in[a,b]$, 使得
$f(\xi)=m$, $f(\eta)=M$

不妨设 $\xi<\eta$, 对任何一个中间值 $C$, $m<C<M$, 考察辅助函数
$\varphi(x)=f(x)-C$

因为 $\varphi(x)$ 在闭区间 $[\xi,\eta]$ 上连续,
$\varphi(\xi)=f(\xi)-C<0$,
$\varphi(\eta)=f(\eta)-C>0$, 由零点存在定理, 必有
$\zeta\in(\xi,\eta)$, 使得 $\varphi(\zeta)=0$,
即 $f(\zeta)=C$

------

推论: 若函数 $f(x)$ 在闭区间 $[a,b]$ 连续, $m$ 是最小值, $M$
是最大值, 则 $f(x)$ 的值域是闭区间 $R_f=[m,M]$


## 一致连续概念

函数 $f(x)$ 在某个区间 $X$ 上连续, 是指 $f(x)$ 在区间 $X$
上的每一点连续 (对区间端点是指左连续与右连续), 而 $f(x)$ 在一点
$x_0\in X$ 的连续性可以表述为
$\forall\varepsilon>0,\ \exists\delta>0,\ \forall x\in X(|x-x_0|<\delta):|f(x)-f(x_0)|<\varepsilon$

其中 $\delta>0$ 与两个因素有关: 它既依赖于 $\varepsilon$,
同时也依赖于所讨论的点 $x_0$, 即 $\delta$ 应表示为
$\delta=\delta(x_0,\varepsilon)$

------

一致连续的定义: 设函数 $f(x)$ 在区间 $X$ 上定义, 若对于任意给定的
$\varepsilon>0$, 存在 $\delta>0$, 只要
$x',x''\in X$ 满足 $|x'-x''|<\delta$, 就成立
$|f(x')-f(x'')|<\varepsilon$, 则称函数 $f(x)$ 在区间
$X$ 上一致连续

[在上述定义中若固定 $x''=x_0\in X$, 就得到 $f(x)$ 在点 $x_0$
的连续性. 由于 $x_0$ 可以是 $X$ 中的任意一点, 于是得到 $f(x)$
在区间 $X$ 上一致连续 $\implies f(x)$ 在区间 $X$ 上连续.
反之则不一定成立]

------

> 例3-41: $f(x)=\sin x$ 在 $(-\infty,+\infty)$
> 上连续, 且一致连续
>
> 证: 由不等式 $|\sin x'-\sin x''|=2\left|\cos\frac{x'+x''}{2}\sin\frac{x'-x''}{2}\right|\leq|x'-x''|$
> 对于任意给定的 $\varepsilon>0$, 取
> $\delta=\varepsilon$, 则对于任意两点
> $x',x''\in(-\infty,+\infty)$, 只要
> $|x'-x''|<\delta$, 就一定成立
> $|\sin x'-\sin x''|\leq|x'-x''|<\delta=\varepsilon$
> 由定义, $\sin x$ 在 $(-\infty,+\infty)$ 上是一致连续的

> 例3-42: $f(x)=\frac{1}{x}$ 在 $(0,1)$ 上连续,
> 但非一致连续
>
> 证: 对于任意给定的 $\varepsilon$, $0<\varepsilon<1$,
> 通过精确地解出 $\delta(x_0,\varepsilon)$
> 来说明不存在适用于整个区间 $(0,1)$ 的
> $\delta(\varepsilon)>0$
>
> 对任意 $x,x_0\in(0,1)$, 关系式
> $\left|\frac{1}{x}-\frac{1}{x_0}\right|<\varepsilon$
> 即为 $\frac{1}{x_0}-\varepsilon<\frac{1}{x}<\frac{1}{x_0}+\varepsilon$,
> 它等价于 $\frac{x_0}{1+x_0\varepsilon}<x<\frac{x_0}{1-x_0\varepsilon}$,
> 即 $-\frac{x_0^2\varepsilon}{1+x_0\varepsilon}<x-x_0<\frac{x_0^2\varepsilon}{1-x_0\varepsilon}$
>
> 由此得到 $\delta(x_0,\varepsilon)$
> $=\min\left\{\frac{x_0^2\varepsilon}{1+x_0\varepsilon},\frac{x_0^2\varepsilon}{1-x_0\varepsilon}\right\}$
> $=\frac{x_0^2\varepsilon}{1+x_0\varepsilon}$
> 显然, 这就是 $\delta^*(x_0,\varepsilon)$
>
> 但当 $x_0\to0$ 时, 有
> $\delta^*(x_0,\varepsilon)\to0$, 换言之, 不存在对区间
> $(0,1)$ 中一切点都适用的 $\delta(\varepsilon)>0$, 因此
> $f(x)=\frac{1}{x}$ 在 $(0,1)$ 上非一致连续

------

判定非一致连续的定理: 设函数 $f(x)$ 在区间 $X$ 上定义, 则 $f(x)$
在 $X$ 上一致连续的充分必要条件是: 对任何点列
$\{x_n'\}\ (\{x_n'\}\in X)$ 和
$\{x_n''\}\ (\{x_n''\}\in X)$, 只要满足
$\lim\limits_{n\to\infty}(x_n'-x_n'')=0$, 就成立
$\lim\limits_{n\to\infty}(f(x_n')-f(x_n''))=0$

证明: 必要性. 函数 $f(x)$ 在 $X$ 上的一致连续性可表述为
$\forall\varepsilon>0,\ \exists\delta>0,\ \forall x',x''\in X(|x'-x''|<\delta):|f(x')-f(x'')|<\varepsilon$

对上述的 $\delta>0$, 由
$\lim\limits_{n\to\infty}(x_n'-x_n'')=0$, 可知
$\exists N,\forall n>N:|x_n'-x_n''|<\delta$,
从而得到 $|f(x_n')-f(x_n'')|<\varepsilon$
这就证明了 $\lim\limits_{n\to\infty}(f(x_n')-f(x_n''))=0$

充分性. 采用反证法. 函数 $f(x)$ 在 $X$ 上的非一致连续性可表述为
$\exists\varepsilon_0>0,\ \forall\delta>0,\ \exists x',x''\in X(|x'-x''|<\delta):|f(x')-f(x'')|\geq\varepsilon_0$

取 $\delta_n=\frac{1}{n}\ (n=1,2,3,\cdots)$,
于是存在 $x_n',x_n''\in X$, 满足
$|x_n'-x_n''|<\frac{1}{n}$,
$|f(x_n')-f(x_n'')|\geq\varepsilon_0$
显然 $\lim\limits_{n\to\infty}(x_n'-x_n'')=0$,
但 $|f(x_n')-f(x_n'')|$ 不可能收敛于 $0$, 这就产生矛盾

[对例3-42, 只要取 $x_n'=\frac{1}{2n}$,
$x_n''=\frac{1}{n}$, 就有
$\lim\limits_{n\to\infty}(x_n'-x_n'')=0$, 但
$\lim\limits_{n\to\infty}(f(x_n')-f(x_n''))=\lim\limits_{n\to\infty}(2n-n)=\infty$,
由本定理即可知道 $f(x)=\frac{1}{x}$ 在 $(0,1)$ 上非一致连续]
[若将区间 $(0,1)$ 换成 $[\eta,1)$ ($\eta>0$), 则
$f(x)=\frac{1}{x}$ 就在 $[\eta,1)$ 上一致连续,
因为对任意给定的 $\varepsilon>0$, 只要取
$\delta=\eta^2\varepsilon>0$ 即可]

------

> 例3-43: $f(x)=x^2$ 在 $[0,+\infty)$ 上非一致连续, 但在
> $[0,A]$ 上一致连续 ($A$ 为任意有限正数)
>
> 证: 取 $x_n'=\sqrt{n+1}$,
> $x_n''=\sqrt{n}\ (n=1,2,3,\cdots)$, 于是
> $\lim\limits_{n\to\infty}(x_n'-x_n'')=\lim\limits_{n\to\infty}(\sqrt{n+1}-\sqrt{n})=0$
> 但是 $\lim\limits_{n\to\infty}(f(x_n')-f(x_n''))=1$,
> 由判定非一致连续的定理可知 $f(x)$ 在 $[0,+\infty)$ 上非一致连续
>
> 当区间限制在 $[0,A]$ 时, 有
> $|x'^2-x''^2|=|(x'+x'')(x'-x'')|\leq2A|x'-x''|$
> 对于任意给定的 $\varepsilon>0$, 可以取
> $\delta=\frac{\varepsilon}{2A}>0$, 对任意
> $x',x''\in[0,A]$, 只要 $|x'-x''|<\delta$, 就成立
> $|x'^2-x''^2|<\varepsilon$, 即 $f(x)=x^2$ 在
> $[0,A]$ 上一致连续

------

Cantor 定理: 若函数 $f(x)$ 在闭区间 $[a,b]$ 上连续, 则它在
$[a,b]$ 上一致连续

证明: 采用反证法
假设 $f(x)$ 在 $[a,b]$ 上非一致连续, 由判定非一致连续的定理的证明过程,
可知存在 $\varepsilon_0>0$ 及两列点列 $\{x_n'\}$ 和
$\{x_n''\}$, $x_n',x_n''\in[a,b]$, 满足
$|x_n'-x_n''|<\frac{1}{n}$, 且
$|f(x_n')-f(x_n'')|\geq\varepsilon_0\ (n=1,2,3,\cdots)$

因为 $\{x_n'\}$ 有界, 由 Bolzano-Weierstrass 定理,
存在收敛子列 $\{x_{n_k}'\}$:
$\lim\limits_{k\to\infty}x_{n_k}'=\xi$,
$\xi\in[a,b]$

在点列 $\{x_n'\}$ 中取子列 $\{x_{n_k}'\}$, 其下标与
$\{x_{n_k}'\}$ 下标相同, 则由
$|x_{n_k}'-x_{n_k}''|<\frac{1}{n_k}$,
$k=1,2,3,\cdots$, 又得到
$\lim\limits_{k\to\infty}x_{n_k}''$
$=\lim\limits_{k\to\infty}\left[x_{n_k}'+(x_{n_k}''-x_{n_k}')\right]$
$=\lim\limits_{k\to\infty}x_{n_k}'$
$=\xi$

由于函数 $f(x)$ 在点 $\xi$ 连续, 因而有
$\lim\limits_{k\to\infty}f(x_{n_k}')=\lim\limits_{k\to\infty}f(x_{n_k}'')=f(\xi)$
于是得到 $\lim\limits_{k\to\infty}(f(x_{n_k}')-f(x_{n_k}''))=0$,
但这与 $|f(x_n')-f(x_n'')|\geq\varepsilon_0$ 产生矛盾
从而推翻假设, 得到 $f(x)$ 在 $[a,b]$ 上的一致连续性结论

------

有限开区间上一致连续的判别: 函数 $f(x)$ 在有限开区间 $(a,b)$ 连续, 则
$f(x)$ 在 $(a,b)$ 上一致连续的充分必要条件是 $f(a+)$ 与
$f(b-)$ 存在

证明: 充分性. 设 $f(a+)=A$, $f(b-)=B$, 定义函数
$\tilde{f}(x)=\begin{cases}A, & x=a\\ f(x), & a<x<b\\ B, & x=b\end{cases}$

则 $\tilde{f}(x)$ 是闭区间 $[a,b]$ 上的连续函数
由 Cantor 定理, $\tilde{f}(x)$ 在 $[a,b]$ 上一致连续,
显然对于一致连续的函数, 当定义域缩小时其一致连续性仍然保持, 于是函数 $f(x)$
在开区间 $(a,b)$ 上也是一致连续的
必要性. 设函数 $f(x)$ 在开区间 $(a,b)$ 上一致连续, 则
$\forall\varepsilon>0$, $\exists\delta>0$,
$\forall x',x''\in(a,b)(|x'-x''|<\delta):|f(x')-f(x'')|<\varepsilon$

在区间 $(a,b)$ 上任意选取数列 $\{x_n\}$ ($x_n\in(a,b)$)
且 $\lim\limits_{n\to\infty}x_n=a$

因数列 $\{x_n\}$ 是基本数列, 对上述 $\delta>0$,
$\exists N,\forall m,n>N:|x_n-x_m|<\delta$,
从而 $|f(x_n)-f(x_m)|<\varepsilon$
这说明了函数值数列 $\{f(x_n)\}$ 也是基本数列, 因而必定收敛

由 Heine 定理, 可知
$f(a+)=\lim\limits_{x\to a+}f(x)$ 存在. 同理可以证明
$f(b-)=\lim\limits_{x\to b-}f(x)$ 存在

[上述判别法不适用于无限开区间. 例如 $f(x)=\sin x$ 在
$(-\infty,+\infty)$ 上是一致连续的, 但 $f(-\infty)$ 与
$f(+\infty)$ 都不存在]

------

闭区间上的连续函数小结
1. 5 个定理: 有界性定理, 最值定理, 零点存在定理, 中间值定理,
   Cantor 定理 (即一致连续定理), 是闭区间上连续函数最重要的分析性质
2. 5 个定理的证明分别采用了确界存在定理, 闭区间套定理,
   Bolzano-Weierstrass 定理和 Cauchy 收敛原理
   由于实数系的 5 个基本定理是等价的,
   理论上可以采用从实数系的连续性到实数系的完备性中的任何一个定理,
   来证明上述闭区间上连续函数的任何一个性质, 只是证明的难度稍有差别

<script>MathJax = { chtml: { fontURL: "/assets/fonts/mathjax" } };</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
