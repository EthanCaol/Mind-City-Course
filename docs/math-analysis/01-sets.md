


## 集合

集合: 具有某种特定性质的具体或抽象的对象汇集的总体
对象称为该集合的元素
集合用大写字母 $A,B,S,T$ 表示, 元素用小写字母 $a,b,x,y$ 表示

属于: 若 $x$ 是集合 $S$ 的元素, 记 $x\in S$
不属于: 若 $x$ 不是集合 $S$ 的元素, 记 $x\notin S$

------

常用的数集
- 自然数集: $N=\{0,1,2,\cdots\}$
- 正整数集: $N^*=\{1,2,3,\cdots\}$
- 整数集: $Z=\{0,\pm1,\pm2,\cdots\}$
- 有理数集: $Q=\left\{x\mid x=\frac{q}{p},p\in N^*,q\in Z\right\}$
- 正实数集: $R^+=\{x\mid x\in R\text{且}x>0\}$

------

集合的表示
1. 枚举法: 将元素逐一列出, 如 $\{\text{红},\text{绿},\text{蓝}\}$
   元素无法一一列举但变化规律已知时写成 $N^*=\{1,2,3,\cdots,n,\cdots\}$
2. 描述法: 用元素的公共属性 $P$ 刻画, 记为 $S=\{x\mid x\text{具有性质}P\}$
   如 $B=\{x\mid x^2=2\}$

[集合中的元素之间没有次序关系]

------

子集: $\forall x\in A\implies x\in B$, 记 $A\subseteq B$
真子集: $A\subseteq B\land A\neq B$, 记 $A\subsetneq B$
集合相等: $A\subseteq B\land B\subseteq A\iff A=B$
空集: 不含任何元素的集合, 记为 $\emptyset$, 规定 $\emptyset\subseteq A$
全集: 讨论某一问题时所有对象的全体, 记为 $X$

------

实数的区间
- 开区间: $(a,b)=\{x\mid a<x<b\}$
- 闭区间: $[a,b]=\{x\mid a\leq x\leq b\}$
- 半开半闭区间: $[a,b)=\{x\mid a\leq x<b\}$, $(a,b]=\{x\mid a<x\leq b\}$
- 无限区间: $(a,+\infty)=\{x\mid x>a\}$, $[a,+\infty)=\{x\mid x\geq a\}$
- 无限区间: $(-\infty,b)=\{x\mid x<b\}$, $(-\infty,b]=\{x\mid x\leq b\}$, $(-\infty,+\infty)=R$


## 集合运算

并: $S\cup T=\{x\mid x\in S\text{或}x\in T\}$
交: $S\cap T=\{x\mid x\in S\text{且}x\in T\}$
差: $S\setminus T=\{x\mid x\in S\text{且}x\notin T\}$
补: 在集合 $X$ 中讨论问题时, 子集 $S\subseteq X$ 关于 $X$ 的补集为 $S_X^c=X\setminus S$
[不会发生混淆时 $S_X^c$ 简记为 $S^c$]

补与差的关系: $S\setminus T=S\cap T^c$
关于补集: $S\cup S_X^c=X$, $S\cap S_X^c=\emptyset$

图1-1: 集合的并, 交, 差, 补

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956000.png =600x)

------

集合运算的性质
1. 交换律: $A\cup B=B\cup A$, $A\cap B=B\cap A$
2. 结合律: $A\cup(B\cup D)=(A\cup B)\cup D$, $A\cap(B\cap D)=(A\cap B)\cap D$
3. 分配律: $A\cap(B\cup D)=(A\cap B)\cup(A\cap D)$, $A\cup(B\cap D)=(A\cup B)\cap(A\cup D)$
4. 对偶律(De Morgan 公式): $(A\cup B)^c=A^c\cap B^c$, $(A\cap B)^c=A^c\cup B^c$

证明对偶律 $(A\cap B)^c=A^c\cup B^c$
1. $\subseteq$: $x\in(A\cap B)^c\implies x\notin A\cap B$
   $\implies x\notin A\text{或}x\notin B\implies x\in A^c\cup B^c$
2. $\supseteq$: $x\in A^c\cup B^c\implies x\notin A\text{或}x\notin B$
   $\implies x\notin A\cap B\implies x\in(A\cap B)^c$

> 例1-1: 证明分配律 $A\cup(B\cap D)=(A\cup B)\cap(A\cup D)$
> 1. $\subseteq$: 设 $x\in A\cup(B\cap D)$, 则 $x\in A$ 或 ($x\in B$ 且 $x\in D$)
>    两种情形都有 $x\in A\cup B$ 且 $x\in A\cup D$
> 2. $\supseteq$: 设 $x\in(A\cup B)\cap(A\cup D)$, 则 $x\in A\cup B$ 且 $x\in A\cup D$
>    即 $x\in A$, 或 ($x\in B$ 且 $x\in D$), 于是 $x\in A\cup(B\cap D)$

[并交运算不能约去公共项, 如 $A\cup B=A\cup C$ 推不出 $B=C$]


## 有限集与无限集

有限集: 由 $n$ 个元素组成, $n$ 是非负整数
无限集: 不是有限集的集合, 如 $N$, $Z$, $Q$, $R$

可列集: 无限集中的元素可按某种规律排成一个序列, 即集合可表示为 $\{a_1,a_2,\cdots,a_n,\cdots\}$
例: 正整数集 $N^*$, $\{x\mid\sin x=0\}$

[每个无限集必包含可列子集, 但无限集不一定是可列集]

------

命题: 可列集的子集也是可列集
证明: 设 $A_1$ 是可列集 $A=\{a_1,a_2,\cdots\}$ 的子集, 将 $A_1$ 中元素按其在 $A$ 中的下标从小到大排列
去掉重复的, 即得 $A_1$ 的一个排列, 故 $A_1$ 可列

------

命题: 可列个可列集之并也是可列集

证明: 设 $A_n=\{x_{n1},x_{n2},\cdots\}$, 将 $\bigcup\limits_{n=1}^{\infty}A_n$ 的元素排成无穷方块阵
$\begin{aligned}
 &x_{11}\quad x_{12}\quad x_{13}\quad x_{14}\quad\cdots \\
 &x_{21}\quad x_{22}\quad x_{23}\quad x_{24}\quad\cdots \\
 &x_{31}\quad x_{32}\quad x_{33}\quad x_{34}\quad\cdots \\
 &x_{41}\quad x_{42}\quad x_{43}\quad x_{44}\quad\cdots \\
 &\ \ \vdots
\end{aligned}$

按对角线法则排列 $x_{11},x_{12},x_{21},x_{13},x_{22},x_{31},x_{14},x_{23},x_{32},x_{41},\cdots$
不同集合的元素可能重复, 只保留一个即可

------

命题: 有理数集 $Q$ 可列

证明: $(-\infty,+\infty)$ 是可列个区间 $(n,n+1]$ 的并, 只需证 $(0,1]$ 中有理数可列
$(0,1]$ 中的有理数可唯一表示为既约分数 $\frac{q}{p}$, 其中 $p\in N^*,q\in N^*,q\leq p$, $p,q$ 互素

按分母 $p$ 分组排列
1. $p=1$: $x_{11}=1$
2. $p=2$: $x_{21}=\frac{1}{2}$
3. $p=3$: $x_{31}=\frac{1}{3}$, $x_{32}=\frac{2}{3}$
4. $p=4$: $x_{41}=\frac{1}{4}$, $x_{42}=\frac{3}{4}$
一般地 $p=n$ 的既约分数不超过 $n-1$ 个, 记为 $x_{n1},x_{n2},\cdots,x_{nk(n)}$, 其中 $k(n)\leq n$

于是 $(0,1]$ 中的有理数排成
$x_{11},x_{21},x_{31},x_{32},x_{41},x_{42},\cdots,x_{n1},x_{n2},\cdots,x_{nk(n)},\cdots$

> 例1-2: 整数集 $Z$ 是可列集
> 按规则 $0,1,-1,2,-2,\cdots,n,-n,\cdots$ 排成一列


## Descartes 乘积集合

Descartes 乘积: $A\times B=\{(x,y)\mid x\in A\text{且}y\in B\}$
序对 $(x,y)$ 是有序的, 作为新的元素

例: 面料颜色集合 $A=\{\text{红},\text{绿},\text{蓝}\}$
加工工艺集合 $B=\{\text{抽纱},\text{提花},\text{印染},\text{刺绣}\}$
$A\times B$ 含 12 个元素, 每个元素表示一种窗帘品种

$R\times R$ 记为 $R^2$, 表示平面 Descartes 直角坐标系下用坐标表示的点的集合
任意点 $P$ 的坐标 $(x,y)$ 中, $x,y$ 分别是 $P$ 在横轴和纵轴上的投影坐标

[由两个集合的情形可推出更多个集合构成的 Descartes 乘积]


## 映射

映射: 设 $X,Y$ 是两个集合
若按某种规则 $f$, 对 $X$ 中每个元素 $x$, 都能找到 $Y$ 中唯一确定的元素 $y$ 与之对应
则称 $f$ 是 $X$ 到 $Y$ 的一个映射, 记为
$f:X\to Y$, $x\mapsto y=f(x)$

$y$ 称为 $x$ 在映射 $f$ 下的像, $x$ 称为 $y$ 在映射 $f$ 下的一个逆像(原像)
定义域: $X$, 记为 $D_f$
值域: $R_f=\{y\mid y\in Y\text{且}y=f(x),x\in X\}$

构成映射的三个要素
1. 集合 $X$, 即定义域 $D_f=X$
2. 集合 $Y$, 即限制值域的范围 $R_f\subseteq Y$
3. 对应规则 $f$, 使每个 $x\in X$ 有唯一确定的 $y=f(x)$ 与之对应

[映射要求元素的像唯一, 不要求逆像唯一]

------

单射: $\forall x_1,x_2\in X, x_1\neq x_2\implies f(x_1)\neq f(x_2)$
满射: $R_f=Y$
双射: 既是单射又是满射, 又称一一对应

逆映射: 若 $f:X\to Y$ 是双射, 则对任意 $y\in R_f$ 逆像 $x\in X$ 唯一
对应规则 $g:R_f\to X$, $y\mapsto x(f(x)=y)$ 构成 $R_f$ 到 $X$ 的映射, 称为 $f$ 的逆映射, 记为 $f^{-1}$
其定义域 $D_{f^{-1}}=R_f$, 值域 $R_{f^{-1}}=X$
[逆映射 $f^{-1}$ 存在时必是 $R_f$ 到 $X$ 的双射]

复合映射: 已知映射 $g:X\to U_1$ 与 $f:U_2\to Y$
若 $R_g\subseteq D_f=U_2$, 则构成新的对应关系 $f\circ g:X\to Y$, $x\mapsto y=f(g(x))$
称为 $f$ 和 $g$ 的复合映射
[构成复合映射的关键是 $R_g\subseteq D_f$ 是否成立]
[复合是有顺序的, $f\circ g$ 有意义不意味着 $g\circ f$ 有意义, 两者都有意义时一般也不相同]

$f\circ f^{-1}(y)=y,\ y\in R_f$
$f^{-1}\circ f(x)=x,\ x\in X$

------

> 例1-3: 设 $X$ 是平面上所有三角形的全体, $Y$ 是平面上所有圆的全体
> 对应规则 $f$ 使每个三角形 $x$ 对应唯一确定的外接圆 $y$
> 则 $f$ 是映射, $D_f=X$, $R_f=Y$, 是满射, 不是单射

> 例1-4: 记 $X=\{\alpha,\beta,\gamma\}$, $Y=\{a,b,c,d\}$, $f(\alpha)=a$, $f(\beta)=d$, $f(\gamma)=b$
> 则 $f$ 是映射, $D_f=X$, $R_f=\{a,b,d\}\subsetneq Y$, 是单射, 不是满射

> 例1-5: 设 $X=R^+$, $Y=R$, 对应关系 $y^2=x$, 则 $f$ 是映射, 是双射

> 例1-6: 设 $X=Y=R$, 对应关系 $y=x^2$, 则 $f$ 是映射, 既不是单射也不是满射

> 例1-7: 设 $g:X\to U_1$, $x\mapsto u=\sin x$ 与 $f:U_2\to Y$, $u\mapsto y=\frac{u}{1+u^2}$
> 由 $R_g=[-1,1]\subseteq D_f$ 可构成复合映射 $f\circ g:X\to Y$, $x\mapsto y=\frac{\sin x}{1+\sin^2x}$

> 例1-8: $y=\sin x:\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\to[-1,1]$ 是双射, 其逆映射为 $x=\arcsin y$
> 于是有 $\sin(\arcsin y)=y,\ y\in[-1,1]$
> 与 $\arcsin(\sin x)=x,\ x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$


## 一元实函数与初等函数

一元实函数: 在映射的定义中取集合 $X\subseteq R$, 集合 $Y=R$
则映射 $f:X\to Y$, $x\mapsto y=f(x)$ 称为一元实函数, 简称函数
常写成 $y=f(x),\ x\in X(=D_f)$

自变量: 函数关系中主动变化的量 $x$
因变量: 被动变化的量 $y$
函数关系: 因变量对自变量的依赖关系
[一元实函数只有一个自变量与一个因变量, 多元函数与向量值函数另论]

> 例1-9: 边长为 $a$ 的正方形铁皮, 四角各剪去边长为 $x$ 的小正方形, 做成无盖方盒
> 方盒容积 $V=x(a-2x)^2$, 其中 $x$ 的变化范围是 $\left(0,\frac{a}{2}\right)$

图1-2: 无盖方盒的铁皮下料

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956001.png =250x)

------

基本初等函数
- 常数函数: $y=c$
- 幂函数: $y=x^\alpha\ (\alpha\in R)$
- 指数函数: $y=a^x\ (a>0\text{且}a\neq1)$
- 对数函数: $y=\log_a x\ (a>0\text{且}a\neq1)$
- 三角函数: $y=\sin x$, $y=\cos x$, $y=\tan x$, $y=\cot x$ 等
- 反三角函数: $y=\arcsin x$, $y=\arccos x$, $y=\arctan x$ 等

初等函数: 由基本初等函数经过有限次四则运算与复合运算所产生的函数
如 $y=ax^2+bx+c$
如 $y=\frac{\log_a(1+x)}{\sqrt{x^2+1}}$
如 $y=\sin\frac{1}{x}+\cos^2x$
如 $y=e^{-x^2}+\arctan\frac{1}{x}$

自然定义域: 初等函数自变量的最大取值范围
- $x^n$(n 是正整数), $\sin x$, $\arctan x$, $a^x$ 的自然定义域是 $R=(-\infty,+\infty)$
- $\log_a x$ 的自然定义域是 $R^+=(0,+\infty)$
- $\arcsin x$ 的自然定义域是 $[-1,1]$
- $x^\alpha$ 的自然定义域视 $\alpha$ 而定
  如 $x^{\frac{1}{3}}$ 是 $R$, $x^{-\frac{1}{3}}$ 是 $R\setminus\{0\}$
  如 $x^{\frac{1}{2}}$ 是 $[0,+\infty)$

[给出 $f(x)$ 的表达式时应同时指出定义域, 否则默认自然定义域为定义域]
[函数关系式与定义域都相同的两个函数才是相同的函数]

> 例1-10: 求下列初等函数的自然定义域与值域
> 1. $y=x+\frac{1}{x}$: $D=(-\infty,0)\cup(0,+\infty)$, $R=(-\infty,-2]\cup[2,+\infty)$
> 2. $y=\arcsin\frac{2x-1}{3}$: $D=[-1,2]$, $R=\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$
> 3. $y=\sqrt{3+2x-x^2}$: $D=[-1,3]$, $R=[0,2]$
> 4. $y=\log_a\frac{x-2}{x^2-3x-4}\ (a>0,a\neq1)$: $D=(-1,2)\cup(4,+\infty)$, $R=(-\infty,+\infty)$


## 函数的表示方法

显式表示: 函数形式为 $y=f(x)$, 因变量 $y$ 单独放在等式一边, 另一边只含自变量 $x$ 的表达式

隐式表示: 通过方程 $F(x,y)=0$ 来确定变量 $y$ 与 $x$ 之间函数关系的方式
[圆方程 $x^2+y^2=R^2$ 不能整体确定 $y$ 是 $x$ 的函数, 加条件 $y\geq0$ 后才有 $y=\sqrt{R^2-x^2}$]

分段表示: 设 $A,B$ 是两个互不相交的实数集合, $\varphi(x)$ 和 $\psi(x)$ 分别是定义在 $A,B$ 上的函数
则 $f(x)=\begin{cases}\varphi(x), & x\in A,\\ \psi(x), & x\in B\end{cases}$ 是定义在 $A\cup B$ 上的函数
分段可以分成任意有限段, 甚至无限多段

参数表示: 引入第三个变量 $t$, 通过 $t$ 与 $x$, $t$ 与 $y$ 的关系间接确定 $f$
$\begin{cases}x=x(t),\\ y=y(t),\end{cases}\ t\in[a,b]$
对应的函数关系为 $f:X\to Y$, $x=x(t)\mapsto y=y(t)$

------

> 例1-11: 汽车从甲城驶往乙城, 先以 $45\ \text{km/h}$ 驶到高速公路, 花 40 分钟
> 再以 $100\ \text{km/h}$ 在高速公路上行驶 1 小时 45 分钟
> 最后以 $40\ \text{km/h}$ 从高速公路出口驶到目的地, 花 30 分钟
> 路程 $s$(单位 km) 与时间 $t$(单位 h) 的函数关系为
> $s(t)=\begin{cases}45t, & 0\leq t<\frac{2}{3}\\ 30+100\left(t-\frac{2}{3}\right), & \frac{2}{3}\leq t<\frac{29}{12}\\ 205+40\left(t-\frac{29}{12}\right), & \frac{29}{12}\leq t\leq\frac{35}{12}\end{cases}$

------

> 例1-12: 符号函数 $\text{sgn}\,x=\begin{cases}1, & x>0\\ 0, & x=0\\ -1, & x<0\end{cases}$
> 定义域 $D=(-\infty,+\infty)$, 值域 $R=\{-1,0,1\}$

图1-3: 符号函数

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956002.png =350x)

> 例1-13: 整数部分函数 $y=[x]=n$, $n\leq x<n+1$, $n\in Z$
> 定义域 $D=(-\infty,+\infty)$, 值域 $R=Z$

图1-4: 整数部分函数

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956003.png =500x)

> 例1-14: 非负小数部分函数 $y=(x)=x-[x]$, $x\in(-\infty,+\infty)$
> 定义域 $D=(-\infty,+\infty)$, 值域 $R=[0,1)$
> 对任意实数 $x$ 成立 $(x)+[x]=x$

图1-5: 非负小数部分函数

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956004.png =500x)

------

> 例1-15: 圆的标准方程 $x^2+y^2=R^2$ 反映 $x$ 与 $y$ 的特定关系
> 当 $x\in(-R,R)$ 时对应的 $y$ 不唯一, 整体上 $y$ 不能说是 $x$ 的函数

> 例1-16: Kepler 方程 $y=x+\varepsilon\sin y$, 其中 $\varepsilon\in(0,1)$ 是常数
> 这是 $y$ 与 $x$ 的函数关系的隐式表示

> 例1-17: 半径 $R$ 的圆, 引入参数 $t$ 表示 $x$ 轴正向按逆时针旋转至射线 $OP$ 的角的弧度
> 圆上点 $P(x,y)$ 在上半圆周(或下半圆周)上与 $x$ 的函数关系为
> $\begin{cases}x=R\cos t,\\ y=R\sin t,\end{cases}t\in[0,\pi]\ (\text{或}t\in[\pi,2\pi])$

图1-6: 圆的参数表示

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956005.png =300x)

> 例1-18: 半径为 $1$ 的轮子置于平地, 边缘一点 $A$ 与地面接触
> 令参数 $t$ 表示轮子转过的角的弧度, 得摆线的参数表示
> $\begin{cases}x=t-\sin t,\\ y=1-\cos t,\end{cases}t\in[0,\infty)$

图1-7: 摆线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011191956006.png =600x)


## 函数的简单特性

有界性: 存在两个常数 $m$ 和 $M$, 使 $y=f(x),x\in D$ 满足 $m\leq f(x)\leq M$
则称 $f$ 在 $D$ 有界, $m$ 是下界, $M$ 是上界
[有界时上界与下界不唯一, 小于 $m$ 的数也是下界, 大于 $M$ 的数也是上界]
等价定义: 存在常数 $M>0$, 使 $f(x),x\in D$ 满足 $|f(x)|\leq M$

------

单调性: 对 $y=f(x),x\in D$
若 $\forall x_1,x_2\in D, x_1<x_2$ 成立 $f(x_1)\leq f(x_2)$, 则 $f$ 在 $D$ 单调增加, 记 $f\uparrow$
成立 $f(x_1)<f(x_2)$ 时称严格单调增加, 记 $f$ 严格 $\uparrow$
若成立 $f(x_1)\geq f(x_2)$, 则 $f$ 在 $D$ 单调减少, 记 $f\downarrow$
成立 $f(x_1)>f(x_2)$ 时称严格单调减少, 记 $f$ 严格 $\downarrow$

例: $y=x^3$, $y=a^x(a>1)$, $y=\log_a x(a>1)$, $y=\arctan x$ 在定义域上严格单调增加
$y=a^x(0<a<1)$, $y=\log_a x(0<a<1)$, $y=\text{arccot}\,x$ 在定义域上严格单调减少
$y=[x]$ 单调增加, 但不是严格单调增加
[许多函数在自然定义域上非单调, 在较小范围内具有单调性, 如 $y=x^2$ 在 $(-\infty,0]$ 严格单调减少, 在 $[0,+\infty)$ 严格单调增加]

------

奇偶性: 设 $f$ 的定义域 $D$ 关于原点对称, 即 $x\in D\iff-x\in D$
若 $\forall x\in D$ 成立 $f(-x)=f(x)$, 则 $f$ 是偶函数
若 $\forall x\in D$ 成立 $f(-x)=-f(x)$, 则 $f$ 是奇函数
[奇函数的图像关于原点对称, 偶函数的图像关于 $y$ 轴对称]
[只需在 $D\cap[0,+\infty)$ 上讨论性质, 再由对称性推出 $D\cap(-\infty,0]$ 上的性质]

例: $y=x^3$, $y=\sin x$, $y=\tan x$ 是奇函数
$y=x^2$, $y=\cos x$, $y=|x|$ 是偶函数

------

周期性: 存在常数 $T>0$, 使 $\forall x\in D$ 成立 $f(x+T)=f(x)$, 则 $f$ 是周期函数, $T$ 是它的周期
若存在满足上述条件的最小的 $T$, 则称 $T$ 为 $f$ 的最小周期
[周期函数的定义域 $D$ 必满足 $x\in D\implies x\pm T\in D$]

例: $y=\sin x$ 是 $(-\infty,+\infty)$ 上的周期函数, $2n\pi(n\in N^*)$ 都是它的周期, $2\pi$ 是最小周期
$y=\tan x$ 的周期是 $(-\infty,+\infty)\setminus\left\{n\pi+\frac{\pi}{2},n\in Z\right\}$, $\pi$ 是它的最小周期
[并非每个周期函数都有最小周期]

> 例1-19: 判断 $f(x)=\frac{1}{1+a^x}-\frac{1}{2}\ (a>0,a\neq1)$ 的奇偶性
> 由 $f(-x)=\frac{1}{1+a^{-x}}-\frac{1}{2}$
> $=\frac{a^x}{1+a^x}-\frac{1}{2}$
> $=\left(\frac{a^x}{1+a^x}-1\right)+\frac{1}{2}$
> $=-\frac{1}{1+a^x}+\frac{1}{2}=-f(x)$
> 所以 $f(x)$ 是奇函数

> 例1-20: Dirichlet 函数 $D(x)=\begin{cases}0, & x\text{为无理数}\\ 1, & x\text{为有理数}\end{cases}$
> 任何正有理数都是它的周期, 不存在最小正有理数, 所以它不可能有最小周期

[对于周期函数只需研究一个周期上的性质, 再根据周期性推出其他范围上的性质]


## 两个常用不等式

定理(三角不等式): 对任意实数 $a$ 和 $b$ 成立 $||a|-|b||\leq|a+b|\leq|a|+|b|$
证明: 由 $-|a||b|\leq ab\leq|a||b|$ 得
$|a|^2-2|a||b|+|b|^2\leq a^2+2ab+b^2\leq|a|^2+2|a||b|+|b|^2$
开方即得

[若将 $a$ 和 $b$ 理解为向量, 则 $a,b,a+b$ 正好构成一个三角形, 由此得名三角不等式]

------

定理(平均值不等式): 设 $a_1,a_2,\cdots,a_n$ 是 $n$ 个正数, 则
$\frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+\cdots+\frac{1}{a_n}}$
$\leq\sqrt[n]{a_1a_2\cdots a_n}$
$\leq\frac{a_1+a_2+\cdots+a_n}{n}$
即调和平均 $\leq$ 几何平均 $\leq$ 算术平均
等号当且仅当 $a_1=a_2=\cdots=a_n$ 时成立

证明: 先证明算术平均不小于几何平均
1. $n=2$ 时, 由 $\sqrt{a_1a_2}\leq\frac{a_1+a_2}{2}$ 即
   $a_1+a_2-2\sqrt{a_1a_2}=(\sqrt{a_1}-\sqrt{a_2})^2\geq0$ 得证

2. $n=4$ 时, 在 $n=2$ 的结论上两次应用 $\frac{a+b}{2}\geq\sqrt{ab}$
   $\frac{a_1+a_2+a_3+a_4}{4}=\frac{\frac{a_1+a_2}{2}+\frac{a_3+a_4}{2}}{2}$
   $\geq\frac{\sqrt{a_1a_2}+\sqrt{a_3a_4}}{2}$
   $\geq\sqrt{\sqrt{a_1a_2}\cdot\sqrt{a_3a_4}}=\sqrt[4]{a_1a_2a_3a_4}$

3. 当 $n=k$ 时结论成立
   在 $a_1,a_2,\cdots,a_k$ 后补 $a_{k+1}=\frac{a_1+a_2+\cdots+a_k}{k}$
   将这 $2k$ 个正数应用 $n=2k$ 的情形
   得到 $\frac{a_1+\cdots+a_k+a_{k+1}+\cdots+a_{2k}}{2k}$
   $\geq\sqrt[2k]{a_1\cdots a_k a_{k+1}\cdots a_{2k}}$
   整理即得 $\frac{a_1+a_2+\cdots+a_k}{k}\geq\sqrt[k]{a_1a_2\cdots a_k}$
   由此 $n=2^m$ 时结论成立, 且 $n=2^m-2$ 成立时可推出 $n=2^m$ 成立, 故对一切 $n\in N^*$ 成立

4. 再对 $\frac{1}{a_1},\frac{1}{a_2},\cdots,\frac{1}{a_n}$ 使用上述结论
   得 $\sqrt[n]{\frac{1}{a_1}\cdots\frac{1}{a_n}}\leq\frac{\frac{1}{a_1}+\cdots+\frac{1}{a_n}}{n}$
   取倒数即得

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
