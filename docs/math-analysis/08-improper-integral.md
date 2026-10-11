


## 反常积分

反常积分: 积分区间无限或被积函数无界的积分, 又称广义积分
Riemann 积分相应称为正常积分(常义积分)

------

> 例8-1: 由万有引力定律导出物体脱离地球引力范围的最低初速度即第二宇宙速度
> 设从地面垂直向上发射质量为 $m$ 的物体飞出地球引力范围所需的最低初速度为 $v_0$
> 若它从地球表面飞到无穷远处克服地球引力所做的功为 $W$, 则由动能原理, $v_0$ 须满足
> $\frac{1}{2}mv_0^2\geq W$
>
> 以地球质心为原点建立一维坐标, 记地球半径为 $R$, 物体在 $r$ 处所受的地球引力为
> $F(r)\ (r\geq R)$
> 由功的定义和微元法, 有 $dW=-F(r)dr$
> 求 $W$ 就是求函数 $-F(r)$ 在无穷区间 $[a,+\infty)$ 上的积分, 沿用前面的记号,
> 形式地写成
> $W=-\int_R^{+\infty}F(r)\,dr$
>
> 先考虑物体从地面 $(r=R)$ 飞到 $r=x\ (x>R)$ 克服地球引力所做的功 $W(x)$ (图8-1)
> $W(x)=-\int_R^x F(r)\,dr$
> 记 $M$ 为地球的质量, 由万有引力定律, $F(r)=-G\frac{Mm}{r^2}$ ($G$ 为引力常量)
> 在地球表面, 地球的引力即为重力, 记 $g$ 为重力加速度, 有
> $F(R)=-G\frac{Mm}{R^2}=-mg$, 解得 $G=\frac{R^2g}{M}$
>
> 从而
> $W(x)$
> $=R^2mg\int_R^x\frac{1}{r^2}dr$
> $=R^2mg\left(-\frac{1}{r}\right)\Big|_R^x$
> $=Rmg\left(1-\frac{R}{x}\right)$
>
> 显然 $W=\lim\limits_{x\to+\infty}W(x)$, 因此
> $W$
> $=-\int_R^{+\infty}F(r)\,dr$
> $=\lim\limits_{x\to+\infty}\left(-\int_R^x F(r)\,dr\right)$
> $=\lim\limits_{x\to+\infty}Rmg\left(1-\frac{R}{x}\right)$
> $=Rmg$
>
> 将 $W=Rmg$, $g=9.8\ \text{m/s}^2$,
> $R\approx6371\ \text{km}$ 代入 $v_0$ 的不等式, 得到
> $v_0\geq\sqrt{\frac{2W}{m}}$
> $=\sqrt{2Rg}$
> $=\sqrt{2\times6371\times9.8\times10^{-3}}\approx11.2\ \text{(km/s)}$
> 这就是第二宇宙速度

图8-1: 地球引力场中物体的坐标

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192827600.png =300x)

------

需要无穷区间上积分的类似例子在实际应用中比比皆是, 它有三种形式
$\int_a^{+\infty}f(x)dx$, $\int_{-\infty}^b f(x)dx$ 和
$\int_{-\infty}^{+\infty}f(x)dx$

由于形式上有(作代换 $x=-t$)
$\int_{-\infty}^a f(x)dx=-\int_{+\infty}^a f(-t)dt=\int_{-\infty}^{-a}f(-t)dt$
及
$\int_{-\infty}^{+\infty}f(x)dx=\int_{-\infty}^a f(x)dx+\int_a^{+\infty}f(x)dx$
因此下面的讨论仅就 $\int_a^{+\infty}f(x)dx$ 形式展开

定义(无穷区间反常积分): 设函数 $f(x)$ 在 $[a,+\infty)$ 有定义, 且在任意有限区间
$[a,A]\subset[a,+\infty)$ 上可积
若极限
$\lim\limits_{A\to+\infty}\int_a^A f(x)dx$
存在, 则称反常积分 $\int_a^{+\infty}f(x)dx$ 收敛(或称 $f(x)$ 在
$[a,+\infty)$ 上可积), 其积分值为
$\int_a^{+\infty}f(x)dx=\lim\limits_{A\to+\infty}\int_a^A f(x)dx$
否则称反常积分 $\int_a^{+\infty}f(x)dx$ 发散

对反常积分 $\int_{-\infty}^b f(x)dx$ 与
$\int_{-\infty}^{+\infty}f(x)dx$ 可类似地给出敛散性定义
注意只有当 $\int_a^{+\infty}f(x)dx$ 和 $\int_{-\infty}^a f(x)dx$
都收敛时, 才认为 $\int_{-\infty}^{+\infty}f(x)dx$ 是收敛的

------

设 $f(x)$ 在 $[a,+\infty)$ 连续, $F(x)$ 是它在 $[a,+\infty)$
上的一个原函数, 由 Newton-Leibniz 公式
$\int_a^{+\infty}f(x)dx$
$=\lim\limits_{A\to+\infty}\int_a^A f(x)dx$
$=\lim\limits_{A\to+\infty}F(x)\Big|_a^A$
$=\lim\limits_{A\to+\infty}[F(A)-F(a)]$

因此反常积分 $\int_a^{+\infty}f(x)dx$ 的敛散性等价于函数极限
$\lim\limits_{A\to+\infty}F(A)$ 的敛散性
当函数 $f(x)\geq0$ 时, 反常积分 $\int_a^{+\infty}f(x)dx$ 收敛表示由曲线
$y=f(x)$, 直线 $x=a$ 和 $x$ 轴所界定区域的面积(图8-2)是个有限值

图8-2: 收敛的反常积分所界定区域的面积

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192827601.png =500x)

------

> 例8-2: 讨论 $\int_1^{+\infty}\frac{1}{x^p}dx$ 的敛散性 $(p\in R)$
> 当 $p\neq1$ 时
> $\int_1^{+\infty}\frac{1}{x^p}dx$
> $=\lim\limits_{A\to+\infty}\frac{x^{1-p}}{1-p}\Big|_1^A$
> $=\lim\limits_{A\to+\infty}\frac{A^{1-p}-1}{1-p}$
> $=\begin{cases}\frac{1}{p-1}, & p>1\\ +\infty, & p<1\end{cases}$
>
> 当 $p=1$ 时
> $\int_1^{+\infty}\frac{1}{x}dx$
> $=\lim\limits_{A\to+\infty}\ln x\Big|_1^A$
> $=\lim\limits_{A\to+\infty}\ln A$
> $=+\infty$
>
> 因此当 $p>1$ 时, 反常积分 $\int_1^{+\infty}\frac{1}{x^p}dx$ 收敛于
> $\frac{1}{p-1}$; 当 $p\leq1$ 时, 反常积分
> $\int_1^{+\infty}\frac{1}{x^p}dx$ 发散

------

为简便, 一般仿照正常积分的 Newton-Leibniz 公式的表达形式, 将反常积分形式地写成
$\int_a^{+\infty}f(x)dx=F(x)\Big|_a^{+\infty}$
只需将 $F(+\infty)$ 理解为极限值 $\lim\limits_{x\to+\infty}F(x)$

------

> 例8-3: 讨论 $\int_0^{+\infty}e^{-ax}dx$ 的敛散性 $(a\in R)$
> 当 $a\neq0$ 时
> $\int_0^{+\infty}e^{-ax}dx$
> $=-\frac{e^{-ax}}{a}\Big|_0^{+\infty}$
> $=\begin{cases}\frac{1}{a}, & a>0\\ +\infty, & a<0\end{cases}$
>
> 而当 $a=0$ 时上述积分显然发散至 $+\infty$
>
> 因此当 $a>0$ 时, $\int_0^{+\infty}e^{-ax}dx$ 收敛于 $\frac{1}{a}$;
> 当 $a\leq0$ 时, $\int_0^{+\infty}e^{-ax}dx$ 发散

> 例8-4: 计算 $\int_{-\infty}^{+\infty}\frac{1}{1+x^2}dx$
> $\int_{-\infty}^{+\infty}\frac{1}{1+x^2}dx$
> $=\int_0^{+\infty}\frac{1}{1+x^2}dx+\int_{-\infty}^0\frac{1}{1+x^2}dx$
> $=\arctan x\Big|_0^{+\infty}+\arctan x\Big|_{-\infty}^0$
> $=\pi$

------

上一章例 7.4.7 求半径为 $a$ 的圆的周长 $l$ 的第一种解法中, 采用直角坐标系下的显式方程
$y=\sqrt{a^2-x^2}$, 求出
$l=4a\int_0^a\frac{dx}{\sqrt{a^2-x^2}}=4a\cdot\arcsin\frac{x}{a}\Big|_0^a=2\pi a$

Riemann 积分要求被积函数在积分区间上有界, 但 $\frac{1}{\sqrt{a^2-x^2}}$ 在
$[0,a]$ 上却是无界的(当 $x\to a^-$ 时函数值趋于 $+\infty$, 图8-3)
只是由于原函数 $\arcsin\frac{x}{a}$ 在 $[0,a]$ 连续,
按常规将积分上下限代入时没察觉到有什么不妥

图8-3: 无界函数 $\frac{1}{\sqrt{a^2-x^2}}$ 的图像

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192827602.png =400x)

定义(无界函数反常积分): 如果函数 $f(x)$ 在点 $x_0$ 的任何一个去心邻域上是无界的, 则称
$x_0$ 为 $f(x)$ 的奇点
由积分的区间可加性, 假定 $f(x)$ 在 $[a,b]$ 上只有一个奇点 $x=b$
设函数 $f(x)$ 在 $x=b$ 的左邻域无界, 若对于任意 $\eta\in(0,b-a)$, $f(x)$
在区间 $[a,b-\eta]$ 上有界可积, 且极限
$\lim\limits_{\eta\to0+}\int_a^{b-\eta}f(x)dx$
存在, 则称反常积分 $\int_a^b f(x)dx$ 收敛(或称无界函数 $f(x)$ 在 $[a,b]$
上可积), 其积分值为
$\int_a^b f(x)dx=\lim\limits_{\eta\to0+}\int_a^{b-\eta}f(x)dx$
否则称反常积分 $\int_a^b f(x)dx$ 发散

$x=a$ 为奇点和 $x=c\in(a,b)$ 为奇点的情况可以类似定义
当 $x=c$ 为奇点时, 注意只有当 $\int_a^c f(x)dx$ 和 $\int_c^b f(x)dx$
都收敛时, 才认为 $\int_a^b f(x)dx$ 是收敛的, 且规定
$\int_a^b f(x)dx=\int_a^c f(x)dx+\int_c^b f(x)dx$

------

> 例8-5: 讨论 $\int_0^1\frac{1}{x^p}dx$ 的敛散性 $(p\in R)$
> 当 $p\neq1$ 时
> $\int_0^1\frac{1}{x^p}dx$
> $=\lim\limits_{\eta\to0+}\frac{x^{1-p}}{1-p}\Big|_\eta^1$
> $=\lim\limits_{\eta\to0+}\frac{1-\eta^{1-p}}{1-p}$
> $=\begin{cases}+\infty, & p>1\\ \frac{1}{1-p}, & p<1\end{cases}$
>
> 当 $p=1$ 时
> $\int_0^1\frac{1}{x}dx$
> $=\lim\limits_{\eta\to0+}\ln x\Big|_\eta^1$
> $=-\lim\limits_{\eta\to0+}\ln\eta$
> $=+\infty$
>
> 因此当 $p<1$ 时, 反常积分 $\int_0^1\frac{1}{x^p}dx$ 收敛于
> $\frac{1}{1-p}$; 当 $p\geq1$ 时, 反常积分
> $\int_0^1\frac{1}{x^p}dx$ 发散

------

例 8-2 和例 8-5 中的积分一般称为 $p$-积分, 对于判别其他反常积分的敛散性具有十分重要的作用

同样可以将无界函数的反常积分形式地写成
$\int_a^b f(x)dx=F(x)\Big|_a^b$
这时它与正常积分的 Newton-Leibniz 公式完全相同, 但必须把右端理解为极限过程, 即
$F(x)\Big|_a^b=\lim\limits_{x\to b^-}F(x)-F(a)=F(b-)-F(a)$

------

> 例8-6: 讨论反常积分 $\int_{-1}^1\frac{e^{1/x}}{x^2}dx$ 的敛散性
> $x=0$ 是被积函数的唯一奇点, 但这一点在积分区间的内部, 因而将积分分解
> $\int_{-1}^1\frac{e^{1/x}}{x^2}dx=\int_{-1}^0\frac{e^{1/x}}{x^2}dx+\int_0^1\frac{e^{1/x}}{x^2}dx$
>
> 经计算
> $\int_{-1}^0\frac{e^{1/x}}{x^2}dx=\left(-e^{1/x}\right)\Big|_{-1}^0=\frac{1}{e}$,
> $\int_0^1\frac{e^{1/x}}{x^2}dx=\left(-e^{1/x}\right)\Big|_0^1=+\infty$
>
> 所以 $\int_{-1}^1\frac{e^{1/x}}{x^2}dx$ 发散

------

容易看出, 无穷区间上的反常积分与无界函数的反常积分是可以互相转换的
例如当 $a>0$ 时, 对 $\int_a^{+\infty}f(x)dx$ 作代换 $x=\frac{1}{t}$, 得
$\int_a^{+\infty}f(x)dx=-\int_0^{\frac{1}{a}}\frac{1}{t^2}f\left(\frac{1}{t}\right)dt$
令 $g(t)=\frac{1}{t^2}f\left(\frac{1}{t}\right)$, 则
$\int_a^{+\infty}f(x)dx=\int_0^{\frac{1}{a}}g(t)dt$

这就化成了无界函数的反常积分

------

设 $f(x)$ 在 $[a,+\infty)$ 有定义, 由例 8-2 可知
$\lim\limits_{x\to+\infty}f(x)=0$ 并不能保证
$\int_a^{+\infty}f(x)dx$ 收敛
但反过来, 若 $\int_a^{+\infty}f(x)dx$ 收敛, 能否保证
$\lim\limits_{x\to+\infty}f(x)=0$, 或者退一步, 至少保证 $f(x)$ 在
$[a,+\infty)$ 有界? 同样不能

------

> 例8-7: 设 $f(x)$ 在 $[1,+\infty)$ 上按如下方式定义
> $f(x)=\begin{cases}n+1, & x\in\left[n,n+\frac{1}{n(n+1)^2}\right]\\ 0, & x\in\left(n+\frac{1}{n(n+1)^2},n+1\right)\end{cases}$, $n=1,2,\cdots$
>
> 那么对于任意 $A>1$, 总可以取自然数 $n$, 使得 $A\in[n,n+1)$
> 由于 $f(x)\geq0$, 因此
> $\int_1^n f(x)dx\leq\int_1^A f(x)dx\leq\int_1^{n+1}f(x)dx$
>
> 当 $n\to\infty$ 时
> $\lim\limits_{n\to\infty}\int_1^n f(x)dx$
> $=\lim\limits_{n\to\infty}\left[\int_1^2 f(x)dx+\int_2^3 f(x)dx+\cdots+\int_{n-1}^n f(x)dx\right]$
> $=\lim\limits_{n\to\infty}\left[\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\frac{1}{3\cdot4}+\cdots+\frac{1}{(n-1)\cdot n}\right]$
> $=\lim\limits_{n\to\infty}\left[\left(1-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)+\cdots+\left(\frac{1}{n-1}-\frac{1}{n}\right)\right]$
> $=\lim\limits_{n\to\infty}\left(1-\frac{1}{n}\right)=1$
>
> 同理也有
> $\lim\limits_{n\to\infty}\int_1^{n+1}f(x)dx=1$
>
> 由极限的夹逼性,
> $\int_1^{+\infty}f(x)dx=\lim\limits_{A\to+\infty}\int_1^A f(x)dx=1$
>
> 但 $f(x)$ 显然是无界的

------

即使 $f(x)$ 在 $[a,+\infty)$ 连续(甚至 $n$ 次可微), 也可仿照上例构造出使
$\int_a^{+\infty}f(x)dx$ 收敛而 $f(x)$ 在 $[a,+\infty)$ 无界的例子


## 反常积分计算

第七章关于定积分的性质, 对于反常积分大多相应成立, 如线性性质, 保序性, 区间可加性等
但也有一些性质, 如乘积可积性, 却不再成立
定积分的一切计算法则, 如线性运算, 换元积分法, 分部积分法等, 也都可以平行地用于反常积分

------

> 例8-8: 计算 $I_n=\int_0^{+\infty}e^{-x}x^n dx$ ($n$ 是非负整数)
> 由例 8-3, $I_0=\int_0^{+\infty}e^{-x}dx=1$
>
> 当 $n\geq1$ 时, 利用分部积分
> $I_n$
> $=\int_0^{+\infty}e^{-x}x^n dx$
> $=(-e^{-x}x^n)\Big|_0^{+\infty}+n\int_0^{+\infty}e^{-x}x^{n-1}dx$
> $=n\int_0^{+\infty}e^{-x}x^{n-1}dx$
> $=nI_{n-1}$
>
> 因此当 $n\geq1$ 时, $I_n=n!$

> 例8-9: 计算 $\int_0^1\ln x\,dx$
> 应用分部积分法, 注意 $\lim\limits_{x\to0+}x\ln x=0$
> $\int_0^1\ln x\,dx=(x\ln x)\Big|_0^1-\int_0^1 dx=-\int_0^1 dx=-1$
>
> 本例也可以用换元积分法来做. 令 $\ln x=-t$, 则 $\ln x\,dx=te^{-t}dt$, 由例 8-8
> $\int_0^1\ln x\,dx=\int_{+\infty}^0 te^{-t}dt=-I_1=-1$

> 例8-10: 计算 $I_n=\int_0^{+\infty}\frac{dx}{(x^2+a^2)^n}$
> 与例 6.2.18 类似, 对于 $n\geq2$, 利用分部积分, 就有
> $I_n$
> $=\int_0^{+\infty}\frac{1}{(x^2+a^2)^n}dx$
> $=\frac{1}{a^2}\int_0^{+\infty}\frac{x^2+a^2-x^2}{(x^2+a^2)^n}dx$
> $=\frac{I_{n-1}}{a^2}+\frac{1}{a^2}\int_0^{+\infty}\frac{-x^2}{(x^2+a^2)^n}dx=\frac{I_{n-1}}{a^2}+\frac{1}{2a^2(n-1)}\int_0^{+\infty}x\,d\left(\frac{1}{(x^2+a^2)^{n-1}}\right)$
> $=\frac{I_{n-1}}{a^2}-\frac{I_{n-1}}{2a^2(n-1)}+\frac{1}{2a^2(n-1)}\cdot\frac{x}{(x^2+a^2)^{n-1}}\Big|_0^{+\infty}=\frac{1}{a^2}\cdot\frac{2n-3}{2n-2}\cdot I_{n-1}$
>
> 以此类推, 并注意到
> $I_1$
> $=\int_0^{+\infty}\frac{dx}{x^2+a^2}$
> $=\frac{1}{a}\arctan\frac{x}{a}\Big|_0^{+\infty}$
> $=\frac{\pi}{2a}$
>
> 即有
> $I_n=\left(\frac{1}{a^2}\cdot\frac{2n-3}{2n-2}\right)I_{n-1}=\left(\frac{1}{a^2}\cdot\frac{2n-3}{2n-2}\right)\left(\frac{1}{a^2}\cdot\frac{2n-5}{2n-4}\right)I_{n-2}=\cdots$
> $=\frac{1}{a^{2n-2}}\cdot\frac{(2n-3)!!}{(2n-2)!!}\cdot I_1$
> $=\frac{\pi}{2a^{2n-1}}\cdot\frac{(2n-3)!!}{(2n-2)!!}$

> 例8-11: 计算 $I=\int_0^{\frac{\pi}{2}}\ln\sin x\,dx$
> 作变量代换 $x=2t$, 则
> $I$
> $=\int_0^{\frac{\pi}{2}}\ln\sin x\,dx$
> $=2\int_0^{\frac{\pi}{4}}\ln\sin2t\,dt$
> $=2\int_0^{\frac{\pi}{4}}\ln(2\sin t\cos t)dt$
> $=\frac{\pi}{2}\ln2+2\int_0^{\frac{\pi}{4}}\ln\sin t\,dt+2\int_0^{\frac{\pi}{4}}\ln\cos t\,dt$
>
> 对后一积分作代换 $t=\frac{\pi}{2}-u$, 则
> $I=\frac{\pi}{2}\ln2+2\int_0^{\frac{\pi}{4}}\ln\sin t\,dt-2\int_{\frac{\pi}{2}}^{\frac{\pi}{4}}\ln\sin t\,dt=\frac{\pi}{2}\ln2+2I$
>
> 于是求得
> $I=-\frac{\pi}{2}\ln2$

> 例8-12: 求 $\int_0^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$ $(\alpha\in R)$
> $\int_0^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$
> $=\int_0^1\frac{dx}{(1+x^2)(1+x^\alpha)}+\int_1^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$
>
> 在上述右端的第二个积分中令 $x=\frac{1}{t}$, 得到
> $\int_1^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$
> $=\int_1^0\frac{-t^\alpha dt}{(1+t^2)(1+t^\alpha)}$
> $=\int_0^1\frac{x^\alpha dx}{(1+x^2)(1+x^\alpha)}$
>
> 于是
> $\int_0^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$
> $=\int_0^1\frac{dx}{(1+x^2)(1+x^\alpha)}+\int_1^{+\infty}\frac{dx}{(1+x^2)(1+x^\alpha)}$
> $=\int_0^1\frac{dx}{(1+x^2)(1+x^\alpha)}+\int_0^1\frac{x^\alpha dx}{(1+x^2)(1+x^\alpha)}$
> $=\int_0^1\frac{dx}{1+x^2}$
> $=\arctan x\Big|_0^1$
> $=\frac{\pi}{4}$

------

考察反常积分 $\int_{-\infty}^{+\infty}\sin x\,dx$, 由定义
$\int_{-\infty}^{+\infty}\sin x\,dx=-\lim\limits_{A\to+\infty}\cos A+\lim\limits_{A'\to+\infty}\cos A'$
由于这里 $A\to+\infty$ 与 $A'\to-\infty$ 是独立的, 因此极限不存在,
$\int_{-\infty}^{+\infty}\sin x\,dx$ 发散

如果要求 $A\to+\infty$ 与 $A'\to-\infty$ "同步"进行, 即 $A'=-A$, 则有
$\int_{-\infty}^{+\infty}\sin x\,dx=-\lim\limits_{A\to+\infty}[\cos A-\cos(-A)]=0$
即 $\int_{-\infty}^{+\infty}\sin x\,dx$ 在这种意义下是"收敛"的

------

定义(Cauchy 主值): 若
$\lim\limits_{A\to+\infty}\int_{-A}^A f(x)dx=\lim\limits_{A\to+\infty}[F(A)-F(-A)]$
收敛, 则称该极限值为 $\int_{-\infty}^{+\infty}f(x)dx$ 的 Cauchy 主值, 记为
$(\text{cpv})\int_{-\infty}^{+\infty}f(x)dx$

当 $\int_{-\infty}^{+\infty}f(x)dx$ 收敛时, 显然有
$(\text{cpv})\int_{-\infty}^{+\infty}f(x)dx=\int_{-\infty}^{+\infty}f(x)dx$
而当 $\int_{-\infty}^{+\infty}f(x)dx$ 发散时,
它的 Cauchy 主值也有可能存在, 因此 Cauchy 主值推广了反常积分的收敛概念

无界函数的反常积分也有相应的 Cauchy 主值概念

------

> 例8-13: 计算 $\int_{-1}^1\frac{1}{x}dx$ 和 $(\text{cpv})\int_{-1}^1\frac{1}{x}dx$
> $x=0$ 是它的唯一奇点, 将它分解为两部分
> $\int_{-1}^1\frac{1}{x}dx=\int_{-1}^0\frac{1}{x}dx+\int_0^1\frac{1}{x}dx=\lim\limits_{\eta\to0-}\int_{-1}^{\eta}\frac{1}{x}dx+\lim\limits_{\eta'\to0+}\int_{\eta'}^1\frac{1}{x}dx=\lim\limits_{\eta\to0-}\ln(-\eta)-\lim\limits_{\eta'\to0+}\ln\eta'$
>
> 由 $\eta\to0-$ 和 $\eta'\to0+$ 的独立性, 易知 $\int_{-1}^1\frac{1}{x}dx$ 是发散的
>
> 但若取 $\eta'=-\eta$, 则有
> $(\text{cpv})\int_{-1}^1\frac{1}{x}dx=\lim\limits_{\eta\to0+}[\ln\eta-\ln\eta]=0$

------

对于一些已确认收敛的反常积分(有些根据问题的实际背景可以断定其收敛), 如果其原函数不能用初等函数来表示,
那么除了极少数可以通过某些高超的技巧积出之外, 不得不借助数值方法来求积分值

求反常积分值的计算格式首推 Gauss 型求积公式. 除了它的计算精度高之外, 更重要的原因在于,
任何形式的 Gauss 型求积公式都只需用到积分区间的内点,
这是它最突出的优点(基于 Newton-Cotes 公式的数值方法毫无例外地需用到端点). 也就是说,
对于奇点在端点的无界函数的反常积分, 如
$\int_{-1}^1\frac{1}{1+t}\ln\frac{1-t}{2}dt$
(这是由 $\int_0^1\frac{\ln(1-x)}{x}dx$ 通过变换 $x=\frac{1+t}{2}$ 得到的, 其值为
$-\frac{\pi^2}{6}=-1.644\ 934\ 0\cdots$),
可以视其为常义积分而直接套用 Gauss-Legendre 公式, 根本无须对 $t=\pm1$
加以特殊的"关照", 它们在计算过程中是决不会被用到的

Gauss 型节点 $\{x_i^*\}_{i=0}^n$ 和系数 $a_i^{(n)}$ 可在数学工具书中查到,
将它们代入
$\int_{-1}^1 f(x)dx\approx\sum_{i=0}^n a_i^{(n)}f(x_i^*)$
就可以算出积分的近似值了

------

下表是用不同的 $n$ 计算 $\int_{-1}^1\frac{1}{1+t}\ln\frac{1-t}{2}dt$ 的近似值.
因无界函数在端点附近变化较剧烈, 实际计算时 $n$ 应取得大些(如 20 以上), 方能获得较好效果

| $n$ | 5 | 8 | 12 | 20 | 48 |
| --- | --- | --- | --- | --- | --- |
| 计算值 | $-1.6242\cdots$ | $-1.6362\cdots$ | $-1.6408\cdots$ | $-1.6434\cdots$ | $-1.6446\cdots$ |
| 相对误差 | $1.2\times10^{-2}$ | $5.2\times10^{-3}$ | $2.5\times10^{-3}$ | $9.1\times10^{-4}$ | $1.6\times10^{-4}$ |

------

无穷区间的反常积分的处理方法大致有三种
1. 取一个足够大的数 $A$, 用 $\int_a^A f(x)dx$ 作为
   $\int_a^{+\infty}f(x)dx$ 的近似值. 这时问题已化成了常义积分
2. 将 $\int_a^{+\infty}f(x)dx$ 通过变换 $x=\frac{1}{t}$
   化成无界函数在有限区间上的反常积分, 再用针对无界函数的方法
3. 直接使用 $[0,+\infty)$ 或 $(-\infty,+\infty)$ 上的 Gauss 型求积公式

[第 3 种方法的内容已超出本书的范围]


## 反常积分的 Cauchy 收敛原理

一般的被积函数的原函数并不一定是初等函数, 而且即使是初等函数, 也往往不容易求出,
因此有必要建立反常积分敛散性的判别法

下面以 $\int_a^{+\infty}f(x)dx$ 为例来探讨反常积分敛散性的判别法
由于反常积分 $\int_a^{+\infty}f(x)dx$ 收敛即为极限
$\lim\limits_{A\to+\infty}\int_a^A f(x)dx$
存在, 因此对其收敛性最本质的刻画就是极限论中的 Cauchy 收敛原理

定理(Cauchy 收敛原理): 反常积分 $\int_a^{+\infty}f(x)dx$
收敛的充分必要条件是: 对任意给定的 $\varepsilon>0$, 存在 $A_0\geq a$,
使得对任意 $A,A'\geq A_0$, 有
$\left|\int_A^{A'}f(x)dx\right|<\varepsilon$

------

定义(绝对收敛与条件收敛): 设 $f(x)$ 在任意有限区间 $[a,A]\subset[a,+\infty)$
上可积, 且 $\int_a^{+\infty}|f(x)|dx$ 收敛, 则称
$\int_a^{+\infty}f(x)dx$ 绝对收敛(或称 $f(x)$ 在 $[a,+\infty)$
上绝对可积)

若 $\int_a^{+\infty}f(x)dx$ 收敛而非绝对收敛, 则称
$\int_a^{+\infty}f(x)dx$ 条件收敛(或称 $f(x)$ 在 $[a,+\infty)$
上条件可积)

------

由 Cauchy 收敛原理, 可推出绝对收敛的反常积分一定收敛

推论: 若反常积分 $\int_a^{+\infty}f(x)dx$ 绝对收敛, 则它一定收敛

证明: 对任意给定的 $\varepsilon>0$, 由于 $\int_a^{+\infty}|f(x)|dx$
收敛, 所以存在 $A_0\geq a$, 使得对任意 $A,A'\geq A_0$, 成立
$\int_A^{A'}|f(x)|dx<\varepsilon$

利用定积分的性质, 得到
$\left|\int_A^{A'}f(x)dx\right|\leq\int_A^{A'}|f(x)|dx<\varepsilon$
由 Cauchy 收敛原理, 知 $\int_a^{+\infty}f(x)dx$ 收敛

------

虽然 Cauchy 收敛原理是判别反常积分收敛性的充分必要条件, 但是对于具体的反常积分, 在使用上往往比较困难,
因此需要导出一些便于使用的收敛判别法


## 非负函数反常积分的收敛判别法

用 Cauchy 收敛原理可以证明下面的比较判别法

定理(比较判别法): 设在 $[a,+\infty)$ 上恒有
$0\leq f(x)\leq K\varphi(x)$, 其中 $K$ 是正常数, 则
1. 当 $\int_a^{+\infty}\varphi(x)dx$ 收敛时,
   $\int_a^{+\infty}f(x)dx$ 也收敛
2. 当 $\int_a^{+\infty}f(x)dx$ 发散时,
   $\int_a^{+\infty}\varphi(x)dx$ 也发散

[在定理中, 条件"在 $[a,+\infty)$ 上恒有 $0\leq f(x)\leq K\varphi(x)$"可以放宽为
"存在 $A\geq a$, 在 $[A,+\infty)$ 上恒有 $0\leq f(x)\leq K\varphi(x)$"]

------

> 例8-14: 讨论 $\int_1^{+\infty}\frac{\cos2x\sin x}{\sqrt{x^3+a^2}}dx$ 的敛散性($a$ 是常数)
> 因为当 $x\geq1$ 时有
> $\left|\frac{\cos2x\sin x}{\sqrt{x^3+a^2}}\right|\leq\frac{1}{x\sqrt{x}}$
>
> 在例 8-2 中已知 $\int_1^{+\infty}\frac{1}{x\sqrt{x}}dx$ 收敛, 由比较判别法,
> $\int_1^{+\infty}\frac{\cos2x\sin x}{\sqrt{x^3+a^2}}dx$ 绝对收敛
>
> 所以 $\int_1^{+\infty}\frac{\cos2x\sin x}{\sqrt{x^3+a^2}}dx$ 收敛

------

如下形式的比较判别法有时用起来更为方便一些

推论(比较判别法的极限形式): 设在 $[a,+\infty)$ 上恒有 $f(x)\geq0$ 和
$\varphi(x)\geq0$, 且
$\lim\limits_{x\to+\infty}\frac{f(x)}{\varphi(x)}=l$
则
1. 若 $0\leq l<+\infty$, 则 $\int_a^{+\infty}\varphi(x)dx$
   收敛时 $\int_a^{+\infty}f(x)dx$ 也收敛
2. 若 $0<l\leq+\infty$, 则 $\int_a^{+\infty}\varphi(x)dx$
   发散时 $\int_a^{+\infty}f(x)dx$ 也发散

所以当 $0<l<+\infty$ 时, $\int_a^{+\infty}\varphi(x)dx$ 和
$\int_a^{+\infty}f(x)dx$ 同时收敛或同时发散

证明
1. 若 $\lim\limits_{x\to+\infty}\frac{f(x)}{\varphi(x)}=l<+\infty$,
   由极限的性质, 存在常数 $A\ (\geq a)$, 使得当 $x\geq A$ 时成立
   $\frac{f(x)}{\varphi(x)}<l+1$
   即 $f(x)<(l+1)\varphi(x)$, 于是由比较判别法, 当
   $\int_a^{+\infty}\varphi(x)dx$ 收敛时 $\int_a^{+\infty}f(x)dx$ 也收敛

2. 若 $\lim\limits_{x\to+\infty}\frac{f(x)}{\varphi(x)}=l>0$,
   由极限的性质, 存在常数 $A\ (\geq a)$, 使得当 $x\geq A$ 时成立
   $\frac{f(x)}{\varphi(x)}>l'$
   其中 $0<l'<l$(当 $l=+\infty$ 时, $l'$ 可取任意正数), 即
   $f(x)>l'\varphi(x)$
   于是由比较判别法, 当 $\int_a^{+\infty}\varphi(x)dx$ 发散时
   $\int_a^{+\infty}f(x)dx$ 也发散

------

使用比较判别法, 需要有一个敛散性结论明确, 同时又形式简单的函数作为比较对象
在上面的例子中都是取 $\frac{1}{x^p}$ 为比较对象, 因为它们正好能满足这两个条件
(这正是 $p$-积分之所以重要的原因)
将定理中的 $\varphi(x)$ 具体取为 $\frac{1}{x^p}$, 就得到如下的 Cauchy 判别法

定理(Cauchy 判别法): 设在 $[a,+\infty)\subset(0,+\infty)$ 上恒有
$f(x)\geq0$, $K$ 是正常数
1. 若 $f(x)\leq\frac{K}{x^p}$, 且 $p>1$, 则
   $\int_a^{+\infty}f(x)dx$ 收敛
2. 若 $f(x)\geq\frac{K}{x^p}$, 且 $p\leq1$, 则
   $\int_a^{+\infty}f(x)dx$ 发散

------

推论(Cauchy 判别法的极限形式): 设在 $[a,+\infty)\subset(0,+\infty)$
上恒有 $f(x)\geq0$, 且
$\lim\limits_{x\to+\infty}x^pf(x)=l$
则
1. 若 $0\leq l<+\infty$, 且 $p>1$, 则
   $\int_a^{+\infty}f(x)dx$ 收敛
2. 若 $0<l\leq+\infty$, 且 $p\leq1$, 则
   $\int_a^{+\infty}f(x)dx$ 发散

------

> 例8-15: 讨论 $\int_1^{+\infty}\frac{1}{\sqrt[3]{x^4+3x^3+5x^2+2x-1}}dx$ 的敛散性
> 因为
> $\lim\limits_{x\to+\infty}\frac{\sqrt[3]{x^4}}{\sqrt[3]{x^4+3x^3+5x^2+2x-1}}=1$
>
> 而 $\int_1^{+\infty}\frac{1}{\sqrt[3]{x^4}}dx$ 收敛, 所以
> $\int_1^{+\infty}\frac{1}{\sqrt[3]{x^4+3x^3+5x^2+2x-1}}dx$ 收敛

> 例8-16: 讨论 $\int_1^{+\infty}x^ae^{-x}dx$ 的敛散性 $(a\in R)$
> 因为对任意常数 $a\in R$, 有
> $\lim\limits_{x\to+\infty}x^2(x^ae^{-x})=0$
> 由 Cauchy 判别法的极限形式(1), 可知 $\int_1^{+\infty}x^ae^{-x}dx$ 收敛


## 一般函数反常积分的收敛判别法

先证明一个重要的结果

定理(积分第二中值定理): 设 $f(x)$ 在 $[a,b]$ 上可积, $g(x)$ 在 $[a,b]$
上单调, 则存在 $\xi\in[a,b]$, 使得
$\int_a^b f(x)g(x)dx=g(a)\int_a^\xi f(x)dx+g(b)\int_\xi^b f(x)dx$

证明: 这里只对 $f(x)$ 在 $[a,b]$ 上连续, $g(x)$ 在 $[a,b]$ 上单调且
$g'(x)$ 在 $[a,b]$ 上可积的情况加以证明

记 $F(x)=\int_a^x f(t)dt$, 则 $F(x)$ 在 $[a,b]$ 连续, 且
$F(a)=0$
由于 $f(x)$ 在 $[a,b]$ 上连续, 于是 $F(x)$ 是 $f(x)$ 在 $[a,b]$
上的一个原函数, 利用分部积分法
$\int_a^b f(x)g(x)dx=F(x)g(x)\Big|_a^b-\int_a^b F(x)g'(x)dx$

上式右端的第一项
$F(x)g(x)\Big|_a^b=F(b)g(b)=g(b)\int_a^b f(x)dx$
而在第二项中, 由于 $g(x)$ 单调, 因此 $g'(x)$ 保持定号, 由积分第一中值定理, 存在
$\xi\in[a,b]$, 使得
$\int_a^b F(x)g'(x)dx=F(\xi)\int_a^b g'(x)dx=[g(b)-g(a)]\int_a^\xi f(x)dx$

于是
$\int_a^b f(x)g(x)dx$
$=g(b)\int_a^b f(x)dx-[g(b)-g(a)]\int_a^\xi f(x)dx$
$=g(a)\int_a^\xi f(x)dx+g(b)\int_\xi^b f(x)dx$

对于一般的可积函数 $f(x)$ 和单调函数 $g(x)$ 的情况, 由于证明过程比较复杂, 在此从略

------

[在积分第二中值定理的假设下, 还有如下结论
1. 若 $g(x)$ 在 $[a,b]$ 上单调增加, 且 $g(a)\geq0$, 则存在
   $\xi\in[a,b]$, 使得
   $\int_a^b f(x)g(x)dx=g(b)\int_\xi^b f(x)dx$
2. 若 $g(x)$ 在 $[a,b]$ 上单调减少, 且 $g(b)\geq0$, 则存在
   $\xi\in[a,b]$, 使得
   $\int_a^b f(x)g(x)dx=g(a)\int_a^\xi f(x)dx$
   ]

------

由积分第二中值定理可以导出下述适用于一般函数反常积分的收敛判别法

定理(Abel 判别法与 Dirichlet 判别法): 若下列两个条件之一满足, 则
$\int_a^{+\infty}f(x)g(x)dx$ 收敛
1. Abel 判别法: $\int_a^{+\infty}f(x)dx$ 收敛, $g(x)$ 在
   $[a,+\infty)$ 上单调有界
2. Dirichlet 判别法: $F(A)=\int_a^A f(x)dx$ 在 $[a,+\infty)$
   上有界, $g(x)$ 在 $[a,+\infty)$ 上单调且
   $\lim\limits_{x\to+\infty}g(x)=0$

证明: 设 $\varepsilon$ 是任意给定的正数
1. 若 Abel 判别法条件满足, 记 $G$ 是 $|g(x)|$ 在 $[a,+\infty)$ 的一个上界
   因为 $\int_a^{+\infty}f(x)dx$ 收敛, 由 Cauchy 收敛原理, 存在
   $A_0\geq a$, 使得对任意 $A,A'\geq A_0$, 有
   $\left|\int_A^{A'}f(x)dx\right|<\frac{\varepsilon}{2G}$
   由积分第二中值定理
   $\left|\int_A^{A'}f(x)g(x)dx\right|\leq|g(A)|\cdot\left|\int_A^\xi f(x)dx\right|+|g(A')|\cdot\left|\int_\xi^{A'}f(x)dx\right|$
   $\leq G\left|\int_A^\xi f(x)dx\right|+G\left|\int_\xi^{A'}f(x)dx\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon$

2. 若 Dirichlet 判别法条件满足, 记 $M$ 是 $F(A)$ 在 $[a,+\infty)$
   的一个上界, 此时对任意 $A,A'\geq a$ 显然有
   $\left|\int_A^{A'}f(x)dx\right|<2M$
   因为 $\lim\limits_{x\to+\infty}g(x)=0$, 所以存在 $A_0\geq a$, 当
   $x\geq A_0$ 时, 有
   $|g(x)|<\frac{\varepsilon}{4M}$
   于是, 对任意 $A,A'\geq A_0$
   $\left|\int_A^{A'}f(x)g(x)dx\right|\leq|g(A)|\cdot\left|\int_A^\xi f(x)dx\right|+|g(A')|\cdot\left|\int_\xi^{A'}f(x)dx\right|$
   $\leq2M|g(A)|+2M|g(A')|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon$

所以无论哪个判别法条件满足, 由 Cauchy 收敛原理, 都有
$\int_a^{+\infty}f(x)g(x)dx$ 收敛的结论

这两个判别法有时也统称为 A-D 判别法

------

> 例8-17: 讨论 $\int_1^{+\infty}\frac{\sin x}{x}dx$ 的敛散性
> $\int_1^A\sin x\,dx$ 显然有界, $\frac{1}{x}$ 在 $[1,+\infty)$ 上单调且
> $\lim\limits_{x\to+\infty}\frac{1}{x}=0$, 由 Dirichlet 判别法,
> $\int_1^{+\infty}\frac{\sin x}{x}dx$ 收敛
>
> 但在 $[1,+\infty)$ 有
> $\left|\frac{\sin x}{x}\right|\geq\frac{\sin^2x}{x}=\frac{1}{2x}-\frac{\cos2x}{2x}$
> 因 $\int_1^{+\infty}\frac{\cos2x}{2x}dx$ 收敛(仿照上面对 $\int_1^{+\infty}\frac{\sin x}{x}dx$ 的讨论)
> 而 $\int_1^{+\infty}\frac{1}{2x}dx$ 发散, 所以 $\int_1^{+\infty}\frac{\sin^2x}{x}dx$ 发散
> 再由比较判别法, 可知 $\int_1^{+\infty}\left|\frac{\sin x}{x}\right|dx$ 发散
>
> 因此, $\int_1^{+\infty}\frac{\sin x}{x}dx$ 条件收敛

> 例8-18: 讨论 $\int_1^{+\infty}\frac{\sin x\arctan x}{x}dx$ 的敛散性
> 由例 8-17, $\int_1^{+\infty}\frac{\sin x}{x}dx$ 收敛, 而 $\arctan x$ 在 $[1,+\infty)$ 上单调有界,
> 由 Abel 判别法, $\int_1^{+\infty}\frac{\sin x\arctan x}{x}dx$ 收敛
>
> 当 $x\in[\sqrt{3},+\infty)$ 时, 有
> $\left|\frac{\sin x\arctan x}{x}\right|\geq\left|\frac{\sin x}{x}\right|$
> 由比较判别法和 $\int_1^{+\infty}\left|\frac{\sin x}{x}\right|dx$ 发散, 可知
> $\int_1^{+\infty}\frac{\sin x\arctan x}{x}dx$ 非绝对收敛
>
> 因此, $\int_1^{+\infty}\frac{\sin x\arctan x}{x}dx$ 条件收敛


## 无界函数反常积分的收敛判别法

以上关于无穷区间反常积分的结论都可以平行地用于无界函数的反常积分
对于 $f(x)$ 在 $[a,b]$ 上只有一个奇点 $x=b$ 的情况, 列出相应结果, 证明留给读者自己完成

定理(Cauchy 收敛原理): 反常积分 $\int_a^b f(x)dx$
收敛的充分必要条件是: 对任意给定的 $\varepsilon>0$, 存在 $\delta>0$, 使得对任意
$\eta,\eta'\in(0,\delta)$, 有
$\left|\int_{b-\eta}^{b-\eta'}f(x)dx\right|<\varepsilon$

------

定理(Cauchy 判别法): 设在 $[a,b)$ 上恒有 $f(x)\geq0$, 若当 $x$ 属于 $b$
的某个左邻域 $[b-\eta_0,b)$ 时, 存在正常数 $K$, 使得
1. $f(x)\leq\frac{K}{(b-x)^p}$, 且 $p<1$, 则
   $\int_a^b f(x)dx$ 收敛
2. $f(x)\geq\frac{K}{(b-x)^p}$, 且 $p\geq1$, 则
   $\int_a^b f(x)dx$ 发散

------

推论(Cauchy 判别法的极限形式): 设在 $[a,b)$ 上恒有 $f(x)\geq0$, 且
$\lim\limits_{x\to b^-}(b-x)^pf(x)=l$
则
1. 若 $0\leq l<+\infty$, 且 $p<1$, 则 $\int_a^b f(x)dx$ 收敛
2. 若 $0<l\leq+\infty$, 且 $p\geq1$, 则 $\int_a^b f(x)dx$ 发散

------

定理(Abel 判别法与 Dirichlet 判别法): 若下列两个条件之一满足, 则
$\int_a^b f(x)g(x)dx$ 收敛
1. Abel 判别法: $\int_a^b f(x)dx$ 收敛, $g(x)$ 在 $[a,b)$ 上单调有界
2. Dirichlet 判别法: $F(\eta)=\int_a^{b-\eta}f(x)dx$ 在
   $(0,b-a]$ 上有界, $g(x)$ 在 $[a,b)$ 上单调且
   $\lim\limits_{x\to b^-}g(x)=0$

------

> 例8-19: 讨论 $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 的敛散性 $(p\in R^*)$
> 这是个定号的反常积分, $x=0$ 是它的唯一奇点
>
> 当 $0<p<1$ 时, 取 $q=\frac{1+p}{2}\in(p,1)$, 则
> $\lim\limits_{x\to0+}\frac{x^q}{x^p|\ln x|}=0$
> 由 Cauchy 判别法的极限形式, $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 收敛
>
> 类似地, 当 $p>1$ 时, 取 $q=\frac{1+p}{2}\in(1,p)$, 则
> $\lim\limits_{x\to0+}\frac{x^q}{x^p|\ln x|}=+\infty$
> 由 Cauchy 判别法的极限形式, $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 发散
>
> 当 $p=1$ 时, 可以直接用 Newton-Leibniz 公式得到
> $\int_0^{1/e}\frac{dx}{x\ln x}=\lim\limits_{\eta\to0+}\ln|\ln x|\Big|_\eta^{1/e}=-\infty$
>
> 因此, 当 $0<p<1$ 时, 反常积分 $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 收敛;
> 当 $p\geq1$ 时, 反常积分 $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 发散
> [当 $p\leq0$ 时, 由于 $\lim\limits_{x\to0+}\frac{1}{x^p\ln x}=0$,
> 因此 $\int_0^{1/e}\frac{dx}{x^p\ln x}$ 是正常积分]

> 例8-20: 讨论 $\int_0^1\frac{1}{x^p}\sin\frac{1}{x}dx$ 的敛散性 $(p<2)$
> 令 $f(x)=\frac{1}{x^2}\sin\frac{1}{x}$, $g(x)=x^{2-p}$
>
> 对于 $\eta\in(0,1)$, 有
> $\int_\eta^1 f(x)dx$
> $=\int_\eta^1\frac{1}{x^2}\sin\frac{1}{x}dx$
> $=-\int_\eta^1\sin\frac{1}{x}d\left(\frac{1}{x}\right)$
> $=\cos\frac{1}{x}\Big|_\eta^1$
> 所以 $\int_\eta^1 f(x)dx$ 有界; 而 $g(x)$ 显然在 $(0,1]$ 单调, 且当 $p<2$ 时
> $\lim\limits_{x\to0+}g(x)=\lim\limits_{x\to0+}x^{2-p}=0$
> 由无界函数反常积分的 Dirichlet 判别法, $\int_0^1\frac{1}{x^p}\sin\frac{1}{x}dx$ 收敛
>
> 因为当 $p<1$ 时, 有
> $\left|\frac{1}{x^p}\sin\frac{1}{x}\right|<\frac{1}{x^p}$
> 由比较判别法, 此时 $\int_0^1\frac{1}{x^p}\sin\frac{1}{x}dx$ 绝对收敛
>
> 而利用与例 8-17 类似的方法可以得到, 当 $1\leq p<2$ 时,
> $\int_0^1\frac{1}{x^p}\sin\frac{1}{x}dx$ 条件收敛
>
> 事实上, 若对 $\int_0^1\frac{1}{x^p}\sin\frac{1}{x}dx$ 作变量代换 $x=\frac{1}{t}$,
> 就可将它化为 $\int_1^{+\infty}\frac{\sin t}{t^{2-p}}dt$
> 利用无穷区间反常积分的 Dirichlet 判别法, 可以得到同样的结果

------

对两种类型反常积分并存(或多个奇点)的情况, 应先将积分区间适当拆分

> 例8-21: 讨论 $\int_0^{+\infty}\frac{x^{1-p}}{|x-1|^{p+q}}dx$ 的敛散性 $(p,q\in R)$
> 因为 $x=0$ 和 $x=1$ 可能是被积函数的奇点, 积分区间也无界, 所以将其拆成
> $\int_0^{+\infty}\frac{x^{1-p}}{|x-1|^{p+q}}dx$
> $=\int_0^1\frac{dx}{x^{p-1}\cdot(1-x)^{p+q}}+\int_1^{+\infty}\frac{dx}{x^{p-1}\cdot(x-1)^{p+q}}$
>
> 要使积分收敛, 考虑奇点 $x=0$, 应要求 $p-1<1$;
> 考虑奇点 $x=1$, 应要求 $p+q<1$; 而当 $x\to+\infty$ 时, 由于
> $\frac{1}{x^{p-1}\cdot(x-1)^{p+q}}\sim\frac{1}{x^{2p+q-1}}$
> 由 Cauchy 判别法的极限形式知, 当 $2p+q-1>1$ 时积分收敛
>
> 所以, 只有当 $p,q$ 同时满足
> $\begin{cases}p<2\\ 2(1-p)<q<1-p\end{cases}$
> 即 $(p,q)$ 属于图8-4的阴影区域时, 积分 $\int_0^{+\infty}\frac{x^{1-p}}{|x-1|^{p+q}}dx$ 才收敛

图8-4: 积分 $\int_0^{+\infty}\frac{x^{1-p}}{|x-1|^{p+q}}dx$ 收敛时 $(p,q)$ 的区域

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192827603.png =400x)

------

上一节中提到, 在 $\int_a^{+\infty}f(x)dx$ 收敛的情况下, 即使 $f(x)$ 在
$[a,+\infty)$ 上 $n$ 次可微, 也不能导出 $f(x)$ 在 $[a,+\infty)$
有界的结论

作为反常积分 Cauchy 收敛原理的一个应用, 下面证明, 只要把条件换成"$f(x)$
一致连续"(注意: 这个条件并不比"可微"强, 两者是互不包含的), 就可以得到比有界更强的结果

> 例8-22: 设 $\int_a^{+\infty}f(x)dx$ 收敛, 且 $f(x)$ 在 $[a,+\infty)$ 一致连续,
> 则 $\lim\limits_{x\to+\infty}f(x)=0$
>
> 证明: 用反证法
> 在所给的条件下, 当 $x\to+\infty$ 时 $f(x)$ 不趋于零, 则由极限定义, 存在
> $\varepsilon_0>0$, 对于任意给定的 $X>a$, 存在 $x_0>X$, 使得 $|f(x_0)|\geq\varepsilon_0$
>
> 又因为 $f(x)$ 在 $[a,+\infty)$ 一致连续, 所以对于 $\frac{\varepsilon_0}{2}>0$,
> 存在 $\delta_0\in(0,1)$, 使得对于任意 $x',x''>a$, 只要 $|x'-x''|<\delta_0$, 就有
> $|f(x')-f(x'')|<\frac{\varepsilon_0}{2}$
>
> 令 $\varepsilon_1=\frac{\varepsilon_0\delta_0}{2}>0$, 对于任意给定的 $A_0\geq a$,
> 取 $X=A_0+1$, 并设 $x_0>X$ 满足 $|f(x_0)|\geq\varepsilon_0$
> 不妨设 $f(x_0)>0$, 则对于任意满足 $|x-x_0|<\delta_0$ 的 $x$, 有
> $f(x)>f(x_0)-\frac{\varepsilon_0}{2}\geq\frac{\varepsilon_0}{2}>0$
>
> 取 $A$ 和 $A'$ 分别等于 $x_0-\frac{\delta_0}{2}$ 和 $x_0+\frac{\delta_0}{2}$,
> 则 $A'>A>A_0$, 且有
> $\left|\int_A^{A'}f(x)dx\right|=\left|\int_{x_0-\frac{\delta_0}{2}}^{x_0+\frac{\delta_0}{2}}f(x)dx\right|>\frac{\varepsilon_0}{2}\delta_0=\varepsilon_1$
>
> 由 Cauchy 收敛原理, $\int_a^{+\infty}f(x)dx$ 不收敛, 与假设条件矛盾,
> 于是 $\lim\limits_{x\to+\infty}f(x)=0$

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
