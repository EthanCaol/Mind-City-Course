


## 微分和导数

微分的思想: 当自变量的改变很小时
用改变量的线性主要部分估计因变量的改变

------

> 例4-1: 求第一宇宙速度
> 卫星沿地球表面附近的水平方向飞行
> 一秒后若不受引力应到达 $B$ 点
> 受地球引力作用实际到达 $C$ 点
> $BC=4.9\ \text{m}$ 是自由落体一秒走过的距离
>
> 地球半径 $OA=OC=6\,371\,000\ \text{m}$
> 由勾股定理
> $AB^2=OC^2-OA^2$
> $=(6\,371\,000+4.9)^2-(6\,371\,000)^2$
>
> 用平方差公式 $a^2-b^2=(a+b)(a-b)$ 改写, 得
> $AB^2=2\times6\,371\,000\times4.9+4.9^2$
> 其中 $4.9^2$ 与 $2\times6\,371\,000\times4.9$ 相比可以忽略
> 于是 $AB\approx7.9\ \text{km}$
>
> 卫星每秒至少飞行 $7.9\ \text{km}$ 才能维持绕地球飞行
> 这就是第一宇宙速度

图4-1: 卫星绕地球飞行

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308200.png =400x)

------

设 $y=f(x)$ 是给定的函数, 在点 $x$ 附近有定义
自变量在 $x$ 处产生增量 $\Delta x$, 变成 $x+\Delta x$
其中 $\Delta x$ 可正可负, 但不为零
函数值相应地产生增量
$\Delta y=f(x+\Delta x)-f(x)$
$\Delta x$ 与 $\Delta y$ 分别称为自变量与因变量的差分

图4-2: 函数值与自变量的增量

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308201.png =500x)

微分: 对函数 $y=f(x)$ 及定义域中的点 $x_0$
若存在一个只与 $x_0$ 有关而与 $\Delta x$ 无关的数 $g(x_0)$
使 $\Delta x\to0$ 时恒成立
$\Delta y=g(x_0)\Delta x+o(\Delta x)$
则称 $f(x)$ 在 $x_0$ 处可微
或称 $f(x)$ 在 $x_0$ 处可导

若 $y=f(x)$ 在区间上的每一点都可微
则称 $f$ 在该区间上可微
$g(x)\Delta x$ 称为 $\Delta y$ 的线性主要部分
$|\Delta x|$ 充分小时
用 $g(x)\Delta x$ 代替 $\Delta y$ 产生的偏差很小

自变量的微分: 将 $\Delta x$ 记为 $dx$
因变量的微分: 将 $\Delta y$ 的线性主要部分 $g(x)dx$
记为 $dy$ 或 $df(x)$
微分关系式
$dy=g(x)dx$

------

> 例4-2: 设 $y=f(x)=x^2$
> 在任意一点 $x\in(-\infty,+\infty)$ 处, 有
> $\Delta y=(x+\Delta x)^2-x^2=2x\Delta x+\Delta x^2$
> 由微分定义, $y=x^2$ 处处可微, 其微分为
> $dy=d(x^2)=2x\,dx$

> 例4-3: 设 $y=f(x)=\sqrt[3]{x}$
> 在 $x=0$ 处, 有
> $\Delta y=f(\Delta x)-f(0)=\sqrt[3]{\Delta x}$
>
> $\Delta x\to0$ 时 $\sqrt[3]{\Delta x}$ 趋于零的阶低于 $\Delta x$ 的阶
> $\Delta y$ 不能表示成 $\Delta x$ 的线性项与高阶项之和
> 由定义, $y=\sqrt[3]{x}$ 在 $x=0$ 处不可微
> $y=\sqrt[3]{x}$ 在 $(-\infty,0)$ 与 $(0,+\infty)$ 上处处可微

------

可微必连续: 若 $f(x)$ 在 $x$ 处可微
则 $\Delta x\to0$ 时必有 $\Delta y\to0$, 即 $f$ 在 $x$ 处连续
[逆命题不成立, 如 $y=\sqrt[3]{x}$ 在 $x=0$ 处连续但不可微]

------

微分和导数

若 $f(x)$ 在 $x_0$ 处可微, 有
$\Delta y=g(x_0)\Delta x+o(\Delta x)$
$g(x_0)$ 与 $\Delta x$ 无关
是差商 $\frac{\Delta y}{\Delta x}$ 的极限

导数: 若函数 $y=f(x)$ 在定义域中的点 $x_0$ 处极限
$\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}$
$=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
存在, 则称 $f(x)$ 在 $x_0$ 处可导
该极限称为 $f(x)$ 在 $x_0$ 处的导数, 记为
$f'(x_0)$ 或 $y'(x_0)$, $\left.\frac{df}{dx}\right|_{x=x_0}$
$\left.\frac{dy}{dx}\right|_{x=x_0}$

等价的定义
$f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$

导函数: $f(x)$ 的所有可导点的集合是定义域的子集
其上 $f'(x)$ 构成一个新的函数
记为 $f'(x)$ 或 $y'(x)$, $\frac{df}{dx}$, $\frac{dy}{dx}$
简称为导数

$\Delta y=f'(x)\Delta x+o(\Delta x)$, $dy=f'(x)dx$
导数可以看成因变量的微分与自变量的微分之比
因此导数也称为微商

定理(可微与可导等价): 函数 $y=f(x)$ 在 $x$ 处可微
的充分必要条件是它在 $x$ 处可导
[对一元函数, 可微性与可导性等价]


## 产生导数的实际背景

速度: 物体在时刻 $t$ 的位移为 $s(t)$
时间区间 $[t,t+\Delta t]$ 内的平均速度为
$\frac{\Delta s}{\Delta t}=\frac{s(t+\Delta t)-s(t)}{\Delta t}$

瞬时速度
$v(t)=\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}$
$=\lim_{\Delta t\to0}\frac{s(t+\Delta t)-s(t)}{\Delta t}$
于是 $v(t)=s'(t)$, 即速度是位移函数的导数

变化率: 涉及某个量变化快慢的问题
如传导率, 反应速率, 资金流动率, 人口增长率
都由导数表示

人口增长率: 人口函数 $p(t)$ 在时刻 $t$ 的增长率
$p'(t)=\lim_{\Delta t\to0}\frac{\Delta p}{\Delta t}$
$=\lim_{\Delta t\to0}\frac{p(t+\Delta t)-p(t)}{\Delta t}$


## 导数的几何意义

曲线的切线: 点 $(x+\Delta x,f(x+\Delta x))$ 沿曲线
趋于点 $(x,f(x))$ 时, 割线趋于的极限位置的直线

割线的斜率
$\frac{\Delta y}{\Delta x}=\frac{f(x+\Delta x)-f(x)}{\Delta x}$
$\Delta x$ 越接近 $0$
$\frac{\Delta y}{\Delta x}$ 越接近切线的斜率
因此切线的斜率是极限
$\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=f'(x)$
这就是导数的几何意义

图4-3: 割线趋于切线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308202.png =500x)

切线方程
$y-f(x_0)=f'(x_0)(x-x_0)$
法线方程: 当 $f'(x_0)\neq0$ 时
$y-f(x_0)=-\frac{1}{f'(x_0)}(x-x_0)$

------

> 例4-4: 求抛物线 $y^2=2px\ (p>0)$ 上
> 任意一点 $(x_0,y_0)$ 处的切线斜率
> 设 $(x_0,y_0)$ 属于上半平面 (属于下半平面时类似)
> 将方程改写成 $y=f(x)=\sqrt{2px}\ (x\geq0)$
>
> 切线斜率
> $\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
> $=\lim_{\Delta x\to0}\frac{\sqrt{2p(x_0+\Delta x)}-\sqrt{2px_0}}{\Delta x}$
> $=\sqrt{2p}\lim_{\Delta x\to0}$
> $\quad\frac{\Delta x}{\left(\sqrt{x_0+\Delta x}+\sqrt{x_0}\right)\cdot\Delta x}$
> $=\frac{\sqrt{p}}{\sqrt{2x_0}}$

------

抛物线的光学性质:
设抛物线 $y^2=2px\ (p>0)$
点 $(x_0,y_0)$ 处的切线与 $x$ 轴的夹角为 $\theta_1$
由 $y_0=\sqrt{2px_0}$ 得
$\tan\theta_1=\frac{\sqrt{p}}{\sqrt{2x_0}}=\frac{p}{y_0}$

记点 $(x_0,y_0)$ 与焦点 $\left(\frac{p}{2},0\right)$ 的连线
与 $x$ 轴的夹角为 $\theta_2$, 该连线与切线夹角为 $\theta$, 则
$\tan\theta_2=\frac{y_0}{x_0-\frac{p}{2}}$
$\tan\theta=\frac{\tan\theta_2-\tan\theta_1}{1+\tan\theta_2\cdot\tan\theta_1}$
$=\frac{\frac{y_0}{x_0-\frac{p}{2}}-\frac{p}{y_0}}{1+\frac{y_0}{x_0-\frac{p}{2}}\cdot\frac{p}{y_0}}$
$=\frac{p}{y_0}=\tan\theta_1$
即 $\theta$ 等于切线与 $x$ 轴的夹角 $\theta_1$

由光的反射定律
入射光线与反射面的夹角等于反射光线与反射面的夹角
从抛物线的焦点出发的光线经反射后与抛物线的对称轴平行
将抛物线绕对称轴旋转得旋转抛物面
焦点处点光源发出的光经反射后成为平行于对称轴的光线
[探照灯, 伞形太阳灶, 抛物面天线由这一原理工作]

图4-4: 抛物线的光学性质

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308203.png =500x)

------

> 例4-5: 求椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\ (a,b>0)$ 上
> 任意一点 $(x_0,y_0)$ 处的切线方程
> 设 $(x_0,y_0)$ 属于上半平面, 将方程改写成
> $y=f(x)=\frac{b}{a}\sqrt{a^2-x^2}\ (-a<x<a)$
>
> 切线斜率
> $\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
> $=\frac{b}{a}\lim_{\Delta x\to0}$
> $\quad\frac{\sqrt{a^2-(x_0+\Delta x)^2}-\sqrt{a^2-x_0^2}}{\Delta x}$
> $=\frac{b}{a}\cdot\frac{-x_0}{\sqrt{a^2-x_0^2}}$
>
> 切线方程为
> $y-y_0=\frac{b}{a}\cdot\frac{-x_0}{\sqrt{a^2-x_0^2}}(x-x_0)$
> 由 $(x_0,y_0)$ 在椭圆上得 $y_0=\frac{b}{a}\sqrt{a^2-x_0^2}$
> 两边整理后得切线方程
> $\frac{x_0\cdot x}{a^2}+\frac{y_0\cdot y}{b^2}=1$

------

椭圆的光学性质: 从一个焦点发出的任意一束光线
经椭圆反射后, 反射光线必经过它的另一个焦点

图4-5: 椭圆的光学性质

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308204.png =500x)

------

微分的几何意义: 用底为 $dx$, 底角为 $\arctan f'(x)$
的直角三角形的高 $dy=f'(x)dx$
近似代替 $\Delta y=f(x+\Delta x)-f(x)$
误差是 $dx$ 的高阶无穷小

图4-6: 微分 $dy$ 的几何意义

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308205.png =600x)


## 单侧导数

由极限存在的定义
$f(x)$ 在 $x_0$ 处可导的充分必要条件是左极限
$f'_-(x_0)=\lim_{\Delta x\to0^-}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
与右极限
$f'_+(x_0)=\lim_{\Delta x\to0^+}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$
存在并且相等
两者分别称为 $f(x)$ 在 $x_0$ 处的左导数与右导数
[左右导数中至少一个不存在, 或都存在但不相等时
$f(x)$ 在 $x_0$ 处不可导]

在闭区间 $[a,b]$ 上定义的函数 $y=f(x)$
若在开区间 $(a,b)$ 可导, 且右导数 $f'_+(a)$ 与左导数 $f'_-(b)$ 存在
则称 $f(x)$ 在闭区间 $[a,b]$ 上可导

------

> 例4-6: 考察函数 $f(x)=|x|$ 在 $x=0$ 处的可导情况
> 当 $x<0$ 时 $f(x)=-x$
> $x=0$ 处的左导数为
> $f'_-(0)=\lim_{\Delta x\to0^-}\frac{-\Delta x}{\Delta x}=-1$
>
> 当 $x>0$ 时 $f(x)=x$
> $x=0$ 处的右导数为
> $f'_+(0)=\lim_{\Delta x\to0^+}\frac{\Delta x}{\Delta x}=1$
>
> 左右导数都存在但不相等
> 由定义 $f(x)=|x|$ 在 $x=0$ 处不可导

图4-7: $y=|x|$ 在原点不可导

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308206.png =400x)

> 例4-7: 考察函数
> $f(x)=\begin{cases}x\sin\frac{1}{x}, & x>0,\\ 0, & x\leq0\end{cases}$
> 在 $x=0$ 处的可导情况
> 当 $\Delta x<0$ 时 $f(\Delta x)=0$, 有
> $f'_-(0)=\lim_{\Delta x\to0^-}\frac{f(\Delta x)-f(0)}{\Delta x}=0$
>
> 当 $\Delta x>0$ 时
> $\frac{f(\Delta x)-f(0)}{\Delta x}$
> $=\frac{\Delta x\cdot\sin\frac{1}{\Delta x}}{\Delta x}=\sin\frac{1}{\Delta x}$
> $\Delta x\to0^+$ 时该极限不存在, 即右导数不存在
> 由定义函数在 $x=0$ 处不可导

> 例4-8: 设函数
> $f(x)=\begin{cases}x^2+b, & x>2,\\ ax+1, & x\leq2\end{cases}$
> 确定 $a,b$, 使 $f(x)$ 在 $x=2$ 处可导
> 在 $x=2$ 处可导必先在 $x=2$ 处连续
> 由 $\lim_{x\to2^-}f(x)=f(2)$ 得 $4+b=2a+1$
>
> 由 $f'_-(2)=f'_+(2)$ 得
> $f'_-(2)=\lim_{x\to2^-}\frac{f(x)-f(2)}{x-2}$
> $=\lim_{x\to2^-}\frac{ax+1-(2a+1)}{x-2}=a$
> $f'_+(2)=\lim_{x\to2^+}\frac{f(x)-f(2)}{x-2}$
> $=\lim_{x\to2^+}\frac{x^2+b-(4+b)}{x-2}$
> $=\lim_{x\to2^+}\frac{x^2-4}{x-2}=4$
>
> 于是 $a=4$, 代入 $4+b=2a+1$ 得 $b=5$
> 此时 $f'(2)=4$


## 从定义出发求导函数

求导: 计算一个函数的导函数的运算

------

> 例4-9: 求 $y=\sin x$ 的导函数
> 由 $\sin(x+\Delta x)-\sin x$
> $=2\cos\left(x+\frac{\Delta x}{2}\right)\sin\frac{\Delta x}{2}$
> 与 $\cos x$ 的连续性, 得
>
> $\lim_{\Delta x\to0}\frac{\sin(x+\Delta x)-\sin x}{\Delta x}$
> $=\lim_{\Delta x\to0}\cos\left(x+\frac{\Delta x}{2}\right)\cdot\frac{\sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}}$
> $=\cos x$
>
> 即 $(\sin x)'=\cos x$
> 同理 $(\cos x)'=-\sin x$

> 例4-10: 求 $y=\ln x$ 的导函数
> 由 $\ln(x+\Delta x)-\ln x=\ln\left(1+\frac{\Delta x}{x}\right)$
> 与 $\ln\left(1+\frac{\Delta x}{x}\right)\sim\frac{\Delta x}{x}\ (\Delta x\to0)$, 得
>
> $\lim_{\Delta x\to0}\frac{\ln(x+\Delta x)-\ln x}{\Delta x}$
> $=\frac{1}{x}\lim_{\Delta x\to0}\frac{\ln\left(1+\frac{\Delta x}{x}\right)}{\frac{\Delta x}{x}}=\frac{1}{x}$
> 即 $(\ln x)'=\frac{1}{x}$

> 例4-11: 求 $y=e^x$ 的导函数
> 由等价关系 $e^{\Delta x}-1\sim\Delta x\ (\Delta x\to0)$, 得
> $\lim_{\Delta x\to0}\frac{e^{x+\Delta x}-e^x}{\Delta x}$
> $=e^x\cdot\lim_{\Delta x\to0}\frac{e^{\Delta x}-1}{\Delta x}=e^x$
> 即 $(e^x)'=e^x$
>
> 进一步由 $a^{\Delta x}-1\sim\Delta x\cdot\ln a\ (a>0,a\neq1)$, 得
> $(a^x)'=(\ln a)a^x$
> [$e^x$ 的导数等于自身, 这是高等数学中将指数函数
> 与对数函数的底数取作 $e$ 的原因]
> [若一个函数的导数等于它本身, 则该函数与 $y=e^x$
> 至多相差一个常数因子, 即形如 $y=Ce^x$]

> 例4-12: 求幂函数 $y=x^\alpha\ (x>0)$ 的导函数
> $\alpha$ 为任意实数
> 由等价关系
> $\left(1+\frac{\Delta x}{x}\right)^\alpha-1\sim\frac{\alpha\Delta x}{x}\ (\Delta x\to0)$, 得
>
> $\lim_{\Delta x\to0}\frac{(x+\Delta x)^\alpha-x^\alpha}{\Delta x}$
> $=\lim_{\Delta x\to0}x^{\alpha-1}\frac{\left(1+\frac{\Delta x}{x}\right)^\alpha-1}{\frac{\Delta x}{x}}$
> $=x^{\alpha-1}\lim_{\Delta x\to0}\frac{\left(1+\frac{\Delta x}{x}\right)^\alpha-1}{\frac{\Delta x}{x}}$
> $=\alpha x^{\alpha-1}$
> 即 $(x^\alpha)'=\alpha x^{\alpha-1}$
>
> 对于具体的实数 $\alpha$, 幂函数的定义域与可导范围可能扩大
> $y=x^n$ ($n$ 为自然数) 的定义域为 $(-\infty,+\infty)$
> 导函数 $y'=nx^{n-1}\ (x\in(-\infty,+\infty))$
> $y=\frac{1}{x^n}$ ($n$ 为自然数) 的定义域为
> $(-\infty,0)\cup(0,+\infty)$
> 导函数 $y'=\frac{-n}{x^{n+1}}\ (x\in(-\infty,0)\cup(0,+\infty))$
> $y=x^{\frac{2}{3}}$ 的定义域为 $(-\infty,+\infty)$
> 导函数 $y'=\frac{2}{3\sqrt[3]{x}}\ (x\in(-\infty,0)\cup(0,+\infty))$
> $y=x^{\frac{1}{2}}$ 的定义域为 $[0,+\infty)$
> 导函数 $y'=\frac{1}{2\sqrt{x}}\ (x\in(0,+\infty))$


## 求导的四则运算法则

定理(线性运算法则): 设 $f(x)$ 与 $g(x)$ 在某一区间上可导
则对任意常数 $c_1,c_2$
线性组合 $c_1f(x)+c_2g(x)$ 在该区间上可导, 且
$[c_1f(x)+c_2g(x)]'=c_1f'(x)+c_2g'(x)$
相应的微分表达式
$d[c_1f(x)+c_2g(x)]=c_1d[f(x)]+c_2d[g(x)]$

证明: 由导数的定义
$\begin{aligned}
 &[c_1f(x)+c_2g(x)]' \\
 &=\lim_{\Delta x\to0}\frac{[c_1f(x+\Delta x)+c_2g(x+\Delta x)]-[c_1f(x)+c_2g(x)]}{\Delta x} \\
 &=c_1\cdot\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x} \\
 &\quad+c_2\cdot\lim_{\Delta x\to0}\frac{g(x+\Delta x)-g(x)}{\Delta x} \\
 &=c_1f'(x)+c_2g'(x)
\end{aligned}$

由 $\log_a x=\frac{\ln x}{\ln a}$ 与 $(\ln x)'=\frac{1}{x}$ 得
$(\log_a x)'=\frac{1}{\ln a}(\ln x)'=\frac{1}{x\ln a}$

------

> 例4-13: 求 $y=5\log_a x+3\sqrt{x}$ 的导数
> $a>0,a\neq1$
> $y'=(5\log_a x+3\sqrt{x})'$
> $=5(\log_a x)'+3(\sqrt{x})'=\frac{5}{x\ln a}+\frac{3}{2\sqrt{x}}$

------

定理(乘积运算法则): 设 $f(x)$ 与 $g(x)$ 在某一区间上可导
则它们的积函数也在该区间上可导, 且
$[f(x)\cdot g(x)]'=f'(x)g(x)+f(x)g'(x)$
相应的微分表达式
$d[f(x)\cdot g(x)]=g(x)d[f(x)]+f(x)d[g(x)]$

证明: 由
$\frac{f(x+\Delta x)\cdot g(x+\Delta x)-f(x)\cdot g(x)}{\Delta x}$
$=\frac{[f(x+\Delta x)-f(x)]\cdot g(x+\Delta x)+f(x)\cdot[g(x+\Delta x)-g(x)]}{\Delta x}$
$=f(x+\Delta x)\frac{g(x+\Delta x)-g(x)}{\Delta x}$
$\quad+g(x)\frac{f(x+\Delta x)-f(x)}{\Delta x}$

由 $f$ 的可导性知 $f$ 连续, 取极限得
$[f(x)\cdot g(x)]'$
$=\lim_{\Delta x\to0}f(x+\Delta x)\lim_{\Delta x\to0}\frac{g(x+\Delta x)-g(x)}{\Delta x}$
$\quad+g(x)\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$
$=f'(x)g(x)+f(x)g'(x)$

------

> 例4-14: 求 $y=3^x\cos x$ 的导函数
> $y'=(3^x\cos x)'=(3^x)'\cos x+3^x(\cos x)'$
> $=\ln3\cdot(3^x)\cdot\cos x-3^x\sin x$
> $=3^x(\ln3\cdot\cos x-\sin x)$

> 例4-15: 求 $y=\frac{\sin x}{x}$ 的导函数
> $y'=\left(\frac{\sin x}{x}\right)'$
> $=(\sin x)'\frac{1}{x}+\sin x\left(\frac{1}{x}\right)'$
> $=\frac{1}{x}\cos x-\frac{1}{x^2}\sin x=\frac{x\cos x-\sin x}{x^2}$

------

定理(倒数运算法则): 设 $g(x)$ 在某一区间上可导
且 $g(x)\neq0$, 则它的倒数也在该区间上可导, 且
$\left[\frac{1}{g(x)}\right]'=-\frac{g'(x)}{[g(x)]^2}$
相应的微分表达式
$d\left[\frac{1}{g(x)}\right]=-\frac{1}{[g(x)]^2}d[g(x)]$

证明: 记 $y=\frac{1}{g(x)}$, 由
$\left[\frac{1}{g(x)}\right]'=\lim_{\Delta x\to0}\frac{\frac{1}{g(x+\Delta x)}-\frac{1}{g(x)}}{\Delta x}$
$=\lim_{\Delta x\to0}\frac{g(x)-g(x+\Delta x)}{g(x+\Delta x)\cdot g(x)\cdot\Delta x}$
$=-\frac{1}{g(x)}\left(\lim_{\Delta x\to0}\frac{g(x+\Delta x)-g(x)}{\Delta x}\right)$
$\quad\left(\lim_{\Delta x\to0}\frac{1}{g(x+\Delta x)}\right)$

由条件 $\lim_{\Delta x\to0}\frac{g(x+\Delta x)-g(x)}{\Delta x}=g'(x)$
且 $\lim_{\Delta x\to0}g(x+\Delta x)=g(x)\neq0$, 代入即得结论

------

> 例4-16: 求 $y=\sec x$ 的导函数
> 由 $\sec x=\frac{1}{\cos x}$ 得
> $(\sec x)'=\left(\frac{1}{\cos x}\right)'=\frac{-(\cos x)'}{\cos^2x}$
> $=\frac{\sin x}{\cos^2x}=\tan x\sec x$
> 同理 $(\csc x)'=-\cot x\csc x$

------

推论(商运算法则): 设 $f(x)$ 与 $g(x)$ 在某一区间上可导
且 $g(x)\neq0$, 则它们的商函数也在该区间上可导, 且
$\left[\frac{f(x)}{g(x)}\right]'=\frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}$
相应的微分表达式
$d\left[\frac{f(x)}{g(x)}\right]=\frac{g(x)d[f(x)]-f(x)d[g(x)]}{[g(x)]^2}$

------

> 例4-17: 求 $y=\tan x$ 的导函数
> 由 $\tan x=\frac{\sin x}{\cos x}$ 得
> $(\tan x)'=\left(\frac{\sin x}{\cos x}\right)'$
> $=\frac{(\sin x)'\cos x-\sin x(\cos x)'}{\cos^2x}$
> $=\frac{\cos^2x+\sin^2x}{\cos^2x}=\sec^2x$
> 同理 $(\cot x)'=-\csc^2x$


## 反函数求导法则

定理(反函数求导定理): 若函数 $y=f(x)$ 在 $(a,b)$ 上连续
严格单调, 可导且 $f'(x)\neq0$
记 $\alpha=\min\{f(a+),f(b-)\}$, $\beta=\max\{f(a+),f(b-)\}$
则它的反函数 $x=f^{-1}(y)$ 在 $(\alpha,\beta)$ 上可导, 且
$[f^{-1}(y)]'=\frac{1}{f'(x)}$

证明: 由连续, 严格单调及反函数连续性
反函数 $x=f^{-1}(y)$ 在 $(\alpha,\beta)$ 上存在, 连续, 严格单调
此时 $\Delta y=f(x+\Delta x)-f(x)\neq0$ 等价于
$\Delta x=f^{-1}(y+\Delta y)-f^{-1}(y)\neq0$
且当 $\Delta y\to0$ 时 $\Delta x\to0$, 因此

$[f^{-1}(y)]'=\lim_{\Delta y\to0}\frac{f^{-1}(y+\Delta y)-f^{-1}(y)}{\Delta y}$
$=\lim_{\Delta x\to0}\frac{\Delta x}{f(x+\Delta x)-f(x)}$
$=\frac{1}{\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}}=\frac{1}{f'(x)}$

------

> 例4-18: 求 $y=\arctan x$ 和 $y=\arcsin x$ 的导函数
> $x=\tan y$ 满足定理的条件
> 将 $y=\arctan x$ 看成它的反函数, 得
> $(\arctan x)'=\frac{1}{(\tan y)'}=\frac{1}{\sec^2y}$
> $=\frac{1}{1+\tan^2y}=\frac{1}{1+x^2}$
>
> 将 $y=\arcsin x$ 看成 $x=\sin y$ 的反函数, 得
> $(\arcsin x)'=\frac{1}{(\sin y)'}=\frac{1}{\cos y}$
> $=\frac{1}{\sqrt{1-\sin^2y}}=\frac{1}{\sqrt{1-x^2}}$
> 同理
> $(\arccos x)'=-\frac{1}{\sqrt{1-x^2}}$
> $(\mathrm{arccot}\,x)'=-\frac{1}{1+x^2}$

> 例4-19: 求双曲函数及反双曲函数的导函数
> $\left(e^{-x}\right)'=\left(\frac{1}{e^x}\right)'=\frac{-(e^x)'}{(e^x)^2}$
> $=\frac{e^x}{e^{2x}}=-e^{-x}$
> $(\mathrm{sh}\,x)'=\left(\frac{e^x-e^{-x}}{2}\right)'$
> $=\frac{e^x+e^{-x}}{2}=\mathrm{ch}\,x$
> 同理 $(\mathrm{ch}\,x)'=\mathrm{sh}\,x$
>
> 由 $\mathrm{th}\,x=\frac{e^x-e^{-x}}{e^x+e^{-x}}=\frac{\mathrm{sh}\,x}{\mathrm{ch}\,x}$
> 与 $\mathrm{cth}\,x=\frac{1}{\mathrm{th}\,x}=\frac{\mathrm{ch}\,x}{\mathrm{sh}\,x}$, 得
> $(\mathrm{th}\,x)'=\frac{1}{\mathrm{ch}^2x}=\mathrm{sech}^2x$
> $(\mathrm{cth}\,x)'=-\frac{1}{\mathrm{sh}^2x}=-\mathrm{csch}^2x$
>
> 反双曲函数按反函数法则导出, 如
> $(\mathrm{sh}^{-1}x)'=\frac{1}{(\mathrm{sh}\,y)'}=\frac{1}{\mathrm{ch}\,y}$
> $=\frac{1}{\sqrt{1+\mathrm{sh}^2y}}=\frac{1}{\sqrt{1+x^2}}$
> 同理
> $(\mathrm{ch}^{-1}x)'=\frac{1}{\sqrt{x^2-1}}$
> $(\mathrm{th}^{-1}x)'=(\mathrm{cth}^{-1}x)'=\frac{1}{1-x^2}$

------

基本初等函数的导数和微分公式

| 导数 | 微分 |
| :--- | :--- |
| $(C)'=0$ | $d(C)=0\cdot dx=0$ |
| $(x^\alpha)'=\alpha x^{\alpha-1}$ | $d(x^\alpha)=\alpha x^{\alpha-1}dx$ |
| $(\sin x)'=\cos x$ | $d(\sin x)=\cos x\,dx$ |
| $(\cos x)'=-\sin x$ | $d(\cos x)=-\sin x\,dx$ |
| $(\tan x)'=\sec^2x$ | $d(\tan x)=\sec^2x\,dx$ |
| $(\cot x)'=-\csc^2x$ | $d(\cot x)=-\csc^2x\,dx$ |
| $(\sec x)'=\tan x\sec x$ | $d(\sec x)=\tan x\sec x\,dx$ |
| $(\csc x)'=-\cot x\csc x$ | $d(\csc x)=-\cot x\csc x\,dx$ |
| $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$ | $d(\arcsin x)=\frac{dx}{\sqrt{1-x^2}}$ |
| $(\arccos x)'=-\frac{1}{\sqrt{1-x^2}}$ | $d(\arccos x)=-\frac{dx}{\sqrt{1-x^2}}$ |
| $(\arctan x)'=\frac{1}{1+x^2}$ | $d(\arctan x)=\frac{dx}{1+x^2}$ |
| $(\mathrm{arccot}\,x)'=-\frac{1}{1+x^2}$ | $d(\mathrm{arccot}\,x)=-\frac{dx}{1+x^2}$ |
| $(a^x)'=\ln a\cdot a^x$ | $d(a^x)=\ln a\cdot a^xdx$ |
| 特别地 $(e^x)'=e^x$ | 特别地 $d(e^x)=e^xdx$ |
| $(\log_a x)'=\frac{1}{\ln a}\cdot\frac{1}{x}$ | $d(\log_a x)=\frac{1}{\ln a}\cdot\frac{dx}{x}$ |
| 特别地 $(\ln x)'=\frac{1}{x}$ | 特别地 $d(\ln x)=\frac{dx}{x}$ |
| $(\mathrm{sh}\,x)'=\mathrm{ch}\,x$ | $d(\mathrm{sh}\,x)=\mathrm{ch}\,x\,dx$ |
| $(\mathrm{ch}\,x)'=\mathrm{sh}\,x$ | $d(\mathrm{ch}\,x)=\mathrm{sh}\,x\,dx$ |
| $(\mathrm{th}\,x)'=\mathrm{sech}^2x$ | $d(\mathrm{th}\,x)=\mathrm{sech}^2x\,dx$ |
| $(\mathrm{cth}\,x)'=-\mathrm{csch}^2x$ | $d(\mathrm{cth}\,x)=-\mathrm{csch}^2x\,dx$ |
| $(\mathrm{sh}^{-1}x)'=\frac{1}{\sqrt{1+x^2}}$ | $d(\mathrm{sh}^{-1}x)=\frac{dx}{\sqrt{1+x^2}}$ |
| $(\mathrm{ch}^{-1}x)'=\frac{1}{\sqrt{x^2-1}}$ | $d(\mathrm{ch}^{-1}x)=\frac{dx}{\sqrt{x^2-1}}$ |
| $(\mathrm{th}^{-1}x)'=(\mathrm{cth}^{-1}x)'=\frac{1}{1-x^2}$ | $d(\mathrm{th}^{-1}x)=d(\mathrm{cth}^{-1}x)=\frac{dx}{1-x^2}$ |

全部基本初等函数的导函数仍是基本初等函数
在其定义域内至多除去有限个点都可导, 且导函数连续
[这些有限个点属于原函数的定义域, 不属于导函数的定义域
如 $y=\sqrt[3]{x}$ 在 $(-\infty,+\infty)$ 上连续
但 $y'=\frac{2}{3\sqrt[3]{x}}$ 在 $x=0$ 处无定义]

------

定理的推广: 多个函数的线性组合与乘积的导函数
1. $\left[\sum_{i=1}^{n}c_if_i(x)\right]'=\sum_{i=1}^{n}c_if_i'(x)$
   其中 $c_i\ (i=1,2,\cdots,n)$ 为常数
2. $\left[\prod_{i=1}^{n}f_i(x)\right]'=\sum_{i=1}^{n}\left\{f_i'(x)\prod_{\substack{j=1\\ j\neq i}}^{n}f_j(x)\right\}$

------

> 例4-20: 求 $n$ 次多项式
> $y=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$ 的导函数
> $y'=(a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0)'$
> $=(a_nx^n)'+(a_{n-1}x^{n-1})'+\cdots+(a_1x)'+(a_0)'$
> $=na_nx^{n-1}+a_{n-1}(n-1)x^{n-2}+\cdots+a_1$
> 即 $n$ 次多项式的导函数是 $n-1$ 次多项式

> 例4-21: 求函数 $y=e^x(x^2+3x-1)\arcsin x$ 的导函数
> $y'=[e^x(x^2+3x-1)\arcsin x]'$
> $=(e^x)'(x^2+3x-1)\arcsin x$
> $\quad+e^x(x^2+3x-1)'\arcsin x$
> $\quad+e^x(x^2+3x-1)(\arcsin x)'$
>
> $=e^x(x^2+3x-1)\arcsin x$
> $\quad+e^x(2x+3)\arcsin x$
> $\quad+e^x\frac{x^2+3x-1}{\sqrt{1-x^2}}$
> $=e^x\left[(x^2+5x+2)\arcsin x+\frac{x^2+3x-1}{\sqrt{1-x^2}}\right]$


## 复合函数求导法则

定理(复合函数求导法则):
设函数 $u=g(x)$ 在 $x=x_0$ 可导
函数 $y=f(u)$ 在 $u_0=g(x_0)$ 可导
则复合函数 $y=f(g(x))$ 在 $x=x_0$ 处可导, 且
$[f(g(x))]'_{x=x_0}=f'(u_0)g'(x_0)=f'(g(x_0))g'(x_0)$

证明: 由 $y=f(u)$ 在 $u_0$ 处可导, 有
$f(u_0+\Delta u)-f(u_0)=f'(u_0)\Delta u+\alpha\Delta u$
其中 $\lim_{\Delta u\to0}\alpha=0$
当 $\Delta u=0$ 时取 $\alpha=0$, 上式对 $\Delta u=0$ 也成立

设 $\Delta u=g(x_0+\Delta x)-g(x_0)$, 两边同除以 $\Delta x$ 得
$\frac{f(g(x_0+\Delta x))-f(g(x_0))}{\Delta x}$
$=f'(u_0)\frac{\Delta u}{\Delta x}+\alpha\frac{\Delta u}{\Delta x}$

由 $u=g(x)$ 在 $x_0$ 可导得
$\lim_{\Delta x\to0}\frac{\Delta u}{\Delta x}=g'(x_0)$
且 $\lim_{\Delta x\to0}\Delta u=0$
$\Delta x\to0$ 时 $\alpha=0$ 或 $\Delta u=0$
故 $\lim_{\Delta x\to0}\alpha=0$, 令 $\Delta x\to0$ 得

$\frac{dy}{dx}=\lim_{\Delta x\to0}\frac{f(g(x_0+\Delta x))-f(g(x_0))}{\Delta x}$
$=f'(u_0)\lim_{\Delta x\to0}\frac{\Delta u}{\Delta x}$
$\quad+\lim_{\Delta x\to0}\alpha\lim_{\Delta x\to0}\frac{\Delta u}{\Delta x}$
$=f'(u_0)g'(x_0)$

链式法则
$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$
复合函数的微分公式
$d[f(g(x))]=f'(u)g'(x)dx$

------

> 例4-22: 求幂函数 $y=x^\alpha\ (x>0)$ 的导函数
> 将 $y=x^\alpha=e^{\alpha\ln x}$ 看成
> $y=e^u$, $u=\alpha\ln x$ 复合而成, 由链式法则
> $(x^\alpha)'=(e^u)'\cdot(\alpha\ln x)'$
> $=\left.(e^u)\right|_{u=\alpha\ln x}\cdot\frac{\alpha}{x}$
> $=x^\alpha\cdot\frac{\alpha}{x}=\alpha x^{\alpha-1}$

> 例4-23: 求 $y=e^{\cos x}$ 的导函数
> 将 $y=e^{\cos x}$ 看成 $y=e^u$, $u=\cos x$ 复合而成
> 由链式法则
> $y'=(e^{\cos x})'=(e^u)'\cdot(\cos x)'$
> $=\left.(e^u)\right|_{u=\cos x}\cdot(-\sin x)$
> $=-e^{\cos x}\cdot\sin x$

------

多条链式法则
$\frac{d}{dx}(f_1(f_2(f_3(\cdots f_n(x)\cdots))))$
$=\frac{df_1}{df_2}\cdot\frac{df_2}{df_3}\cdot\cdots\cdot\frac{df_{n-1}}{df_n}\cdot\frac{df_n}{dx}$

------

> 例4-24: 求函数 $y=e^{\sqrt{1+\cos x}}$ 的导函数
> 将 $y=y(x)=e^{\sqrt{1+\cos x}}$ 看成
> $y=f(u)=e^u$, $u=g(v)=\sqrt{v}$, $v=h(x)=1+\cos x$
> 复合而成
>
> $\frac{dy}{dx}=\frac{df}{du}\cdot\frac{dg}{dv}\cdot\frac{dh}{dx}$
> $=e^u\cdot\frac{1}{2\sqrt{v}}\cdot(-\sin x)$
> $=-\frac{e^{\sqrt{1+\cos x}}\cdot\sin x}{2\sqrt{1+\cos x}}$

------

幂指函数: 形如 $y=f(x)=u(x)^{v(x)}$ 的函数
对数求导法: 两边取对数得
$z(x)=\ln y=v(x)\ln u(x)$

一方面
$z'(x)=[v(x)\ln u(x)]'$
$=v'(x)\ln u(x)+v(x)\frac{u'(x)}{u(x)}$
另一方面将 $z(x)=\ln y$ 看作复合函数得
$z'(x)=\frac{y'}{y}$

综合得
$y'=y\left[v'(x)\ln u(x)+v(x)\frac{u'(x)}{u(x)}\right]$
$=u(x)^{v(x)}\left[v'(x)\ln u(x)+v(x)\frac{u'(x)}{u(x)}\right]$

------

> 例4-25: 求函数 $y=(\sin x)^{\cos x}$ 的导函数
> 两边取对数得 $\ln y=\cos x\ln\sin x$
> $(\ln y)'=(\cos x)'\ln\sin x+\cos x\frac{(\sin x)'}{\sin x}$
> 即 $\frac{y'}{y}=-\sin x\ln\sin x+\cos x\frac{\cos x}{\sin x}$
> 于是 $y'=(\sin x)^{\cos x}\left(\frac{\cos^2x}{\sin x}-\sin x\ln\sin x\right)$

------

求导与求微分的运算规则

| 导数运算法则 | 微分运算法则 |
| :--- | :--- |
| 线性组合 $(c_1f+c_2g)'=c_1f'+c_2g'$ | $d(c_1f+c_2g)=c_1df+c_2dg$ |
| 乘法 $(f\cdot g)'=f'g+fg'$ | $d(f\cdot g)=g\,df+f\,dg$ |
| 除法 $\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2}$ | $d\left(\frac{f}{g}\right)=\frac{g\,df-f\,dg}{g^2}$ |
| 反函数 $[f^{-1}(y)]'=\frac{1}{f'(x)}$ | $dx=\frac{dy}{[f^{-1}(y)]'}$ |
| 复合函数 $[f(g(x))]'=f'(u)g'(x)$ | $d[f(g(x))]=f'(u)g'(x)dx$ |

由基本初等函数的导函数表与上表
初等函数的求导与求微分问题得到解决


## 一阶微分的形式不变性

复合函数的微分公式 $d[f(g(x))]=f'(u)g'(x)dx$
由 $du=g'(x)dx$ 代入得 $d[f(u)]=f'(u)du$
其中 $u=g(x)$ 是中间变量, $x$ 是自变量
上式与以 $u$ 为自变量的函数 $y=f(u)$ 的微分形式
$d[f(u)]=f'(u)du$ 相同

一阶微分的形式不变性: 不论 $u$ 是自变量还是中间变量
函数 $y=f(u)$ 的微分形式都是 $d[f(u)]=f'(u)du$

[有了形式不变性, 得到一个函数 $y=f(u)$ 后
可以按 $u$ 是自变量求它的微分 $f'(u)du$
不必顾及 $u$ 是否受自变量 $x$ 约束]


## 隐函数求导与求微分

隐函数: 在满足一定条件下
方程 $F(x,y)=0$ 确定一个 $y$ 关于 $x$ 的函数 $y=y(x)$

显化: 通过某种方法解出 $y$ 关于 $x$ 的一般变化规律
化成显函数 $y=f(x)$ 的形式
[椭圆标准方程 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 确定了上下半平面上的
两个显函数 $y=\pm\frac{b}{a}\sqrt{a^2-x^2}\ (-a\leq x\leq a)$]
[高次的二元代数方程
$F(x,y)=y^5+axy^2+bxy^2+cxy+d=0$
一般不能求出显函数形式]

隐函数的求导与求微分: 利用复合函数的求导法则
或一阶微分的形式不变性求导
无须从隐函数解出显函数

------

> 例4-26: 求由方程 $e^{xy}+x^2y-1=0$ 确定的隐函数
> $y=y(x)$ 的导函数 $y'(x)$
> 方程两边关于 $x$ 求导
> 注意到 $y$ 是 $x$ 的函数, 由复合函数的求导法则
> $(e^{xy})'+(x^2y)'-1'$
> $=(e^{xy})(xy)'+(x^2y+x^2y')$
> $=(e^{xy})(y+xy')+(2xy+x^2y')=0$
>
> 解出
> $y'=-\frac{e^{xy}y+2xy}{e^{xy}x+x^2}=-\frac{(e^{xy}+2x)y}{(e^{xy}+x)x}$

> 例4-27: 求由方程 $\sin y^2=\cos\sqrt{x}$ 确定的隐函数
> $y=y(x)$ 的导函数 $y'(x)$
> 方程两边求微分
> $d(\sin y^2)=d(\cos\sqrt{x})$
>
> 对等式左边应用一阶微分的形式不变性得
> $d(\sin y^2)=\cos y^2\cdot2y\,dy$
> 右边得 $d(\cos\sqrt{x})=-\frac{\sin\sqrt{x}}{2\sqrt{x}}dx$
> 于是 $2y(\cos y^2)dy=-\frac{\sin\sqrt{x}}{2\sqrt{x}}dx$, 即
> $\frac{dy}{dx}=-\frac{\sin\sqrt{x}}{4\sqrt{x}y(\cos y^2)}$
> 该隐函数的显式形式为 $y=\pm\sqrt{\arcsin(\cos\sqrt{x})}$

用隐函数求导得到的导函数中通常仍含隐函数 $y$
但不影响使用

> 例4-28: 求由方程 $e^{x+y}-xy-e=0$ 所确定的隐函数
> 曲线在点 $(0,1)$ 处的切线方程
> 方程 $e^{x+y}-xy-e=0$ 两边关于 $x$ 求导得
> $y'=\frac{y-e^{x+y}}{e^{x+y}-x}$
>
> 点 $(0,1)$ 在曲线上, 将 $x=0,y=1$ 代入得
> $y'(0)=\frac{1-e}{e}$
> 切线方程为 $y=\left(\frac{1-e}{e}\right)x+1$


## 复合函数求导法则的其他应用

复合函数的求导法则给出一般求导方法
许多求导公式是它的特例

将 $y=\frac{1}{g(x)}$ 看成 $y=\frac{1}{u}$, $u=g(x)$ 复合而成
$\left(\frac{1}{g(x)}\right)'=\left(\frac{1}{u}\right)'\cdot g'(x)$
$=-\frac{g'(x)}{u^2}=-\frac{g'(x)}{[g(x)]^2}$
即倒数求导公式是复合函数求导法则的特例

设 $y=f(x)$ 满足反函数求导定理的条件
记其反函数为 $x=f^{-1}(y)$, 则成立 $x=f^{-1}(f(x))$
两边求导得
$1=(x)'=[f^{-1}(f(x))]'=[f^{-1}(y)]'\cdot f'(x)$
即 $[f^{-1}(y)]'=\frac{1}{f'(x)}$
即反函数求导公式也可看成复合函数求导法则的特殊情况

参数形式函数的导函数
设自变量 $x$ 与因变量 $y$ 的函数关系由参数形式给出
$\begin{cases}x=\varphi(t),\\ y=\psi(t),\end{cases}\alpha\leq t\leq\beta$
$\varphi(t)$ 与 $\psi(t)$ 可微
$\varphi(t)$ 严格单调且 $\varphi'(t)\neq0$

由反函数求导法则
$x=\varphi(t)$ 的反函数 $t=\varphi^{-1}(x)$ 存在, 且
$(\varphi^{-1}(x))'=\frac{1}{\varphi'(t)}$
将 $y$ 关于 $x$ 的函数关系写成
$y=\psi(t)=\psi(\varphi^{-1}(x))$, 由复合函数求导法则得
$\frac{dy}{dx}=\frac{dy}{dt}\cdot\frac{dt}{dx}$
$=\frac{d(\psi(t))}{dt}\cdot\frac{d(\varphi^{-1}(x))}{dx}=\frac{\psi'(t)}{\varphi'(t)}$

也可看成微分形式
$\begin{cases}dy=\psi'(t)dt,\\ dx=\varphi'(t)dt\end{cases}$
两边相除的结果

------

> 例4-29: 求由参数方程
> $\begin{cases}x=t-\sin t,\\ y=1-\cos t,\end{cases}0\leq t\leq\pi$
> 确定的函数 $y=f(x)$ 的导函数
> 由上, 得
> $\frac{dy}{dx}=\frac{(1-\cos t)'}{(t-\sin t)'}=\frac{\sin t}{1-\cos t}=\cot\frac{t}{2}$

> 例4-30: 设抛射体运动在 $t=0$ 时刻的水平速度和垂直速度
> 分别等于 $v_1$ 和 $v_2$
> 问在什么时刻该物体的飞行倾角恰与地面平行
> 将抛射体运动视为水平方向与垂直方向运动的合成
> 得参数方程
> $\begin{cases}x=v_1t,\\ y=v_2t-\frac{1}{2}gt^2,\end{cases}0\leq t\leq\frac{2v_2}{g}$
>
> 由导数的几何意义, 物体在任一时刻 $t$ 的飞行倾角 $\theta$ 为
> $\theta=\arctan\left(\left.\frac{dy}{dx}\right|_{x=v_1t}\right)$
> $=\arctan\frac{\left(v_2t-\frac{1}{2}gt^2\right)'}{(v_1t)'}$
> $=\arctan\frac{v_2-gt}{v_1}$
>
> 要使 $\theta=0$, 只要 $\frac{v_2-gt}{v_1}=0$, 即
> $t=\frac{v_2}{g}$

图4-8: 抛射体的运动轨迹与飞行倾角

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011193308207.png =600x)

显式表示, 隐式表示和参数表示是表达函数的三种重要形式
各有不同的适用场合

求椭圆上某一点的导数
可以从显函数形式 $y=\pm\frac{b}{a}\sqrt{a^2-x^2}\ (-a\leq x\leq a)$ 入手
$y'=\pm\frac{b}{a}\cdot\frac{1}{2}\cdot\frac{-2x}{\sqrt{a^2-x^2}}$
$=\mp\frac{b}{a}\cdot\frac{x}{\sqrt{a^2-x^2}}$
$=\left(-\frac{b^2}{a^2}\cdot\frac{x}{\pm\frac{b}{a}\sqrt{a^2-x^2}}=-\frac{b^2}{a^2}\cdot\frac{x}{y}\right)$

也可以通过参数方程
$\begin{cases}x=a\cos t,\\ y=b\sin t,\end{cases}0\leq t\leq2\pi$ 得
$\frac{dy}{dx}=\frac{(b\sin t)'}{(a\cos t)'}=\frac{b\cos t}{-a\sin t}$
$=\left(-\frac{b^2(a\cos t)}{a^2(b\sin t)}=-\frac{b^2}{a^2}\cdot\frac{x}{y}\right)$

最简洁的是从标准方程
$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 这个隐函数入手, 由
$d\left(\frac{x^2}{a^2}\right)+d\left(\frac{y^2}{b^2}\right)=\frac{2x}{a^2}dx+\frac{2y}{b^2}dy=0$
直接得 $y'=\frac{dy}{dx}=-\frac{b^2}{a^2}\cdot\frac{x}{y}$


## 高阶导数的实际背景及定义

牛顿在研究物体运动规律时发现
一个受力物体的速度改变量 $\Delta v=v(t+\Delta t)-v(t)$
与所受的力 $F$ 及受力时间 $\Delta t$ 成正比, 与质量 $m$ 成反比
取单位使比例系数为 $1$, 得 $F\Delta t=m\Delta v$, 即
$F=m\frac{\Delta v}{\Delta t}$
对匀变速运动, $\frac{\Delta v}{\Delta t}$ 是常数 $a$
得牛顿第二定律 $F=ma$

一般的变速运动中, 加速度 $a$ 是随时间变化的函数 $a(t)$
物体在时刻 $t$ 的瞬时加速度为
$a(t)=\lim_{\Delta t\to0}\frac{\Delta v}{\Delta t}$
$=\lim_{\Delta t\to0}\frac{v(t+\Delta t)-v(t)}{\Delta t}=v'(t)=s''(t)$
即加速度函数 $a(t)$ 是速度函数 $v(t)$ 的导函数
是位移函数 $s(t)$ 的导函数的导函数
称为 $s(t)$ 的二阶导数

二阶导数: 若 $y=f(x)$ 可导, 且 $f'(x)$ 仍可导
则 $f'(x)$ 的导数 $[f'(x)]'$ 称为 $f(x)$ 的二阶导数, 记为
$f''(x)$ 或 $y''(x)$, $\frac{d^2f}{dx^2}$, $\frac{d^2y}{dx^2}$

三阶导数: 若 $f''(x)$ 仍可导
则 $f''(x)$ 的导数称为 $f(x)$ 的三阶导数, 记为
$f'''(x)$ 或 $y'''(x)$, $\frac{d^3f}{dx^3}$, $\frac{d^3y}{dx^3}$

$n$ 阶导数: 设函数 $y=f(x)$ 的 $n-1$ 阶导数 $f^{(n-1)}(x)$
仍是可导函数
则它的导数 $[f^{(n-1)}(x)]'$ 称为 $f(x)$ 的 $n$ 阶导数, 记为
$f^{(n)}(x)$ 或 $y^{(n)}(x)$, $\frac{d^nf}{dx^n}$, $\frac{d^ny}{dx^n}$
$n\geq2$ 时统称为高阶导数
[$f(x)$ 的 $n$ 阶导数存在时, 它的低于 $n$ 阶的导数都存在]

$n$ 阶可导函数: 若 $f(x)$ 的 $n$ 阶导数存在
则称 $f(x)$ 是 $n$ 阶可导函数, 简称 $n$ 阶可导

利用二阶导数记号, 加速度 $a(t)=s''(t)=\frac{d^2s}{dt^2}$
牛顿第二定律写成 $F=m\frac{d^2s}{dt^2}$

------

> 例4-31: 求 $y=e^x$ 的 $n$ 阶导函数
> 由 $(e^x)'=e^x$ 得
> $(e^x)'=(e^x)''=\cdots=(e^x)^{(n)}=e^x$
> 类似可得 $(a^x)^{(n)}=(\ln a)^na^x$

> 例4-32: 求 $y=\sin x$ 和 $y=\cos x$ 的 $n$ 阶导函数
> 由 $(\sin x)'=\cos x=\sin\left(x+\frac{\pi}{2}\right)$
> 与复合函数的求导法则
> $(\sin x)''=\left[\sin\left(x+\frac{\pi}{2}\right)\right]'$
> $=\cos\left(x+\frac{\pi}{2}\right)=\sin\left(x+\frac{2\pi}{2}\right)$
>
> 用数学归纳法可得 $(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}{2}\right)$
> 同理 $(\cos x)^{(n)}=\cos\left(x+\frac{n\pi}{2}\right)$

> 例4-33: 求幂函数 $y=x^m$ ($m$ 是正整数) 的 $n$ 阶导函数
> $(x^m)'=mx^{m-1}$, $(x^m)''=m(m-1)x^{m-2}$
> $(x^m)'''=m(m-1)(m-2)x^{m-3}$
> 一般地
> $(x^m)^{(n)}=\begin{cases}m(m-1)\cdots(m-n+1)x^{m-n}, & n\leq m,\\ 0, & n>m\end{cases}$
> 特别地 $(x^m)^{(m)}=m!$

> 例4-34: 求 $y=\ln x$ 的 $n$ 阶导函数
> 由 $(\ln x)'=\frac{1}{x}=x^{-1}$ 得
> $(\ln x)''=(x^{-1})'=-x^{-2}$
> $(\ln x)'''=(-x^{-2})'=2x^{-3}$
> $(\ln x)^{(4)}=(2x^{-3})'=-3\cdot2x^{-4}$
> 一般地
> $(\ln x)^{(n)}=(-1)^{n-1}(n-1)\cdot(n-2)\cdots3\cdot2x^{-n}$
> $=(-1)^{n-1}\frac{(n-1)!}{x^n}$
>
> 还得到
> $\left(\frac{1}{x}\right)^{(n)}=(\ln x)^{(n+1)}=(-1)^n\frac{n!}{x^{n+1}}$


## 高阶导数的运算法则

定理(线性运算法则): 设 $f(x)$ 和 $g(x)$ 都是 $n$ 阶可导
则对任意常数 $c_1,c_2$
线性组合 $c_1f(x)+c_2g(x)$ 也是 $n$ 阶可导, 且
$[c_1f(x)+c_2g(x)]^{(n)}=c_1f^{(n)}(x)+c_2g^{(n)}(x)$
推广到多个函数
$\left[\sum_{i=1}^{n}c_if_i(x)\right]^{(n)}=\sum_{i=1}^{n}c_if_i^{(n)}(x)$

------

定理(Leibniz 公式): 设 $f(x)$ 和 $g(x)$ 都是 $n$ 阶可导
则它们的积函数也是 $n$ 阶可导, 且
$[f(x)\cdot g(x)]^{(n)}=\sum_{k=0}^{n}C_n^kf^{(n-k)}(x)g^{(k)}(x)$
其中 $C_n^k=\frac{n!}{k!(n-k)!}$ 是组合系数

证明: 用数学归纳法
$n=1$ 时
$[f(x)\cdot g(x)]'=C_1^0f'(x)g(x)+C_1^1f(x)g'(x)$
$=f'(x)g(x)+f(x)g'(x)$, 结论成立

设 $n=m$ 时成立, 即
$[f(x)\cdot g(x)]^{(m)}=\sum_{k=0}^{m}C_m^kf^{(m-k)}(x)g^{(k)}(x)$
则 $n=m+1$ 时
$\begin{aligned}
 [f(x)\cdot g(x)]^{(m+1)} &=\left\{[f(x)\cdot g(x)]^{(m)}\right\}' \\
 &=\sum_{k=0}^{m}C_m^k\left[f^{(m-k)}(x)\cdot g^{(k)}(x)\right]' \\
 &=\sum_{k=0}^{m}C_m^k\left[f^{(m+1-k)}(x)g^{(k)}(x)+f^{(m-k)}(x)g^{(k+1)}(x)\right] \\
 &=\sum_{k=0}^{m}C_m^kf^{(m+1-k)}(x)g^{(k)}(x)+\sum_{k=0}^{m}C_m^kf^{(m-k)}(x)g^{(k+1)}(x)
\end{aligned}$

将第一项改写成
$f^{(m+1)}(x)g^{(0)}(x)+\sum_{k=1}^{m}C_m^kf^{(m+1-k)}(x)g^{(k)}(x)$
第二项改写成
$\sum_{k=1}^{m+1}C_m^{k-1}f^{(m+1-k)}(x)g^{(k)}(x)+f^{(0)}(x)g^{(m+1)}(x)$
两式合并, 由 $C_m^{k-1}+C_m^k=C_{m+1}^k$ 与
$C_m^0=C_{m+1}^0=1$, $C_m^{m+1}=C_{m+1}^{m+1}=1$ 得
$[f(x)\cdot g(x)]^{(m+1)}=\sum_{k=0}^{m+1}C_{m+1}^kf^{(m+1-k)}(x)g^{(k)}(x)$
即公式对 $n=m+1$ 也成立, 从而对任意正整数成立

Leibniz 公式与二项式展开公式
$(a+b)^n=\sum_{k=0}^{n}C_n^ka^{n-k}b^k$ 形式相同

------

> 例4-35: 求函数 $y=(3x^2-2)\sin2x$ 的 100 阶导数
> 由幂函数的高阶导数 $(3x^2-2)'=6x$, $(3x^2-2)''=6$
> $(3x^2-2)^{(n)}=0\ (n\geq3)$
> Leibniz 公式中只有三项不为零
> 由 $(\sin2x)^{(n)}=2^n\sin\left(2x+\frac{n\pi}{2}\right)$, 得
>
> $y^{(100)}=\sum_{k=0}^{100}C_{100}^k(\sin2x)^{(100-k)}(3x^2-2)^{(k)}$
> $=(\sin2x)^{(100)}(3x^2-2)+C_{100}^1(\sin2x)^{(99)}(3x^2-2)'$
> $\quad+C_{100}^2(\sin2x)^{(98)}(3x^2-2)''$
> $=2^{100}(3x^2-2)\sin2x-100\cdot2^{99}\cdot(6x)\cos2x$
> $\quad-4950\cdot2^{98}\cdot6\cdot\sin2x$
> $=2^{98}\left[(12x^2-29708)\sin2x-1200x\cos2x\right]$

------

两个函数之商的 $n$ 阶导数可化为乘积
$[f(x)\cdot\frac{1}{g(x)}]^{(n)}$, 再用 Leibniz 公式计算

复合函数, 隐函数和参数形式函数的高阶导数
复合函数 $y=f(g(x))$, 即 $y=f(u)$, $u=g(x)$
其链式法则为 $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$
由乘积的求导公式, $y$ 关于 $x$ 的二阶导数
$\frac{d}{dx}\left(\frac{dy}{dx}\right)=\frac{d}{dx}\left(\frac{dy}{du}\cdot\frac{du}{dx}\right)$
$=\frac{d}{dx}\left(\frac{dy}{du}\right)\cdot\frac{du}{dx}+\frac{dy}{du}\cdot\frac{d}{dx}\left(\frac{du}{dx}\right)$

其中 $\frac{dy}{du}$ 仍是 $u$ 的函数, 因而仍是 $x$ 的复合函数
它对 $x$ 求导必须遵循链式法则, 即
$\frac{d}{dx}\left(\frac{dy}{du}\right)=\frac{d}{du}\left(\frac{dy}{du}\right)\frac{du}{dx}=\frac{d^2y}{du^2}\frac{du}{dx}$

代入得
$\frac{d}{dx}\left(\frac{dy}{dx}\right)=\frac{d^2y}{du^2}\cdot\left(\frac{du}{dx}\right)^2+\frac{dy}{du}\cdot\frac{d^2u}{dx^2}$
[容易错误地写成
$y''(x)=[f'(u)g'(x)]'=f''(u)g'(x)+f'(u)g''(x)$, 注意区分]

------

> 例4-36: 求复合函数 $y=e^{\sin x}$ 的二阶导数
> 更直截了当的做法是对 $y'=e^{\sin x}\cdot\cos x$ 再求一次导数
> $(e^{\sin x})''=(e^{\sin x}\cdot\cos x)'$
> $=(e^{\sin x})'\cos x+e^{\sin x}(\cos x)'$
> $=e^{\sin x}(\cos^2x-\sin x)$

> 例4-37: 求由方程 $e^{xy}+x^2y-1=0$ 确定的隐函数
> $y=y(x)$ 的二阶导数 $y''(x)$
> 由例4-26 已求得
> $(e^{xy})(y+xy')+(2xy+x^2y')=0$
>
> 两边再次关于 $x$ 求导
> 注意到 $y$ 和 $y'$ 都是 $x$ 的函数
> $[(e^{xy})(y+xy')+(2xy+x^2y')]'$
> $=(e^{xy})'(y+xy')+(e^{xy})(y+xy')'+(2xy+x^2y')'$
> $=(e^{xy})(y+xy')^2+(e^{xy})(y'+y'+xy'')$
> $\quad+(2y+4xy'+x^2y'')=0$
>
> 整理得
> $y''=-\frac{(e^{xy})\left[(y+xy')^2+2y'\right]+(2y+4xy')}{x(e^{xy}+x)}$
> 将已解出的 $y'=-\frac{(e^{xy}+2x)y}{(e^{xy}+x)x}$ 代入, 得
> $y''=\frac{2ye^{3xy}+8xye^{2xy}+(12x^2y-x^3y^2)e^{xy}+6x^3y}{x^2(e^{xy}+x)^3}$

------

参数形式函数的二阶导数
已知 $\frac{dy}{dx}=\frac{\psi'(t)}{\varphi'(t)}$, 它仍是变量 $t$ 的函数
$\frac{d^2y}{dx^2}=\frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}=\frac{\xi'(t)}{\varphi'(t)}$
其中 $\xi(t)=\frac{\psi'(t)}{\varphi'(t)}$, 于是
$\frac{d^2y}{dx^2}=\frac{\psi''(t)\varphi'(t)-\psi'(t)\varphi''(t)}{[\varphi'(t)]^3}$
[注意 $\frac{d^2y}{dx^2}\neq\frac{\psi''(t)}{\varphi''(t)}$]

------

> 例4-38: 求摆线
> $\begin{cases}x=t-\sin t,\\ y=1-\cos t,\end{cases}0\leq t\leq2\pi$
> 在 $t=\pi$ 处的二阶导数 $\left.\frac{d^2y}{dx^2}\right|_{t=\pi}$ 的值
> 由例4-29 得
> $\frac{dy}{dx}=\frac{(1-\cos t)'}{(t-\sin t)'}=\frac{\sin t}{1-\cos t}=\cot\frac{t}{2}$
>
> 再对 $x$ 求导得
> $\frac{d^2y}{dx^2}=\frac{\left(\cot\frac{t}{2}\right)'}{(t-\sin t)'}$
> $=\frac{-\frac{1}{2}\csc^2\frac{t}{2}}{1-\cos t}=-\frac{1}{4}\csc^4\frac{t}{2}$
> 当 $t=\pi$ 时, $\left.\frac{d^2y}{dx^2}\right|_{t=\pi}=-\frac{1}{4}$


## 高阶微分

$dy$ 是函数 $y=f(x)$ 的一阶微分
称 $dy$ 的微分 $d(dy)$ 为 $y$ 的二阶微分, 记为
$d^2y=d(dy)$
一般地, 若 $y$ 的 $n-1$ 阶微分 $d^{n-1}y$ 存在
定义 $y$ 的 $n$ 阶微分为 $d^ny=d(d^{n-1}y)$

由 $dy=f'(x)dx$, 两边求微分, 用乘积的微分公式
$d^2y=d[f'(x)dx]=d[f'(x)]\cdot dx+f'(x)\cdot d(dx)$
其中 $d[f'(x)]=f''(x)dx$
且 $dx$ (即 $\Delta x$) 与自变量 $x$ 无关, 视为常量
有 $d(dx)=0$
于是得二阶微分
$d^2y=f''(x)dx^2$
其中 $dx^2$ 表示 $(dx)^2$

$n$ 阶微分
$d^ny=f^{(n)}(x)dx^n$, $n=2,3,\cdots$
其中 $dx^n$ 表示 $(dx)^n$

该公式建立了高阶导数与高阶微分之间的关系:
$y$ 的 $n$ 阶微分等于它的 $n$ 阶导数乘上自变量的 $n$ 次方
[记号 $\frac{d^ny}{dx^n}$ 由该关系得到
注意与 $d(x^n)=nx^{n-1}dx$, $d^2x=0$ (自变量的两次微分为零) 区分]

------

高阶微分不具有形式不变性
对复合函数 $y=f(u)$, $u=g(x)$
由一阶微分的形式不变性, 一阶微分可写成 $dy=f'(u)du$
但二阶微分不能写成 $d^2y=f''(u)du^2$

------

> 例4-39: 求函数 $y=e^{\sin x}$ 的二阶微分
> 由例4-36 得 $y''=e^{\sin x}(\cos^2x-\sin x)$, 所以
> $d^2y=y''dx^2=e^{\sin x}(\cos^2x-\sin x)dx^2$
>
> 若把 $y=e^{\sin x}$ 看成 $y=e^u$, $u=\sin x$ 复合而成, 则
> $f''(u)=(e^u)''=e^u$
> $du^2=[d(\sin x)]^2=\cos^2x\,dx^2$
> 于是
> $f''(u)du^2=e^u\cos^2x\,dx^2=e^{\sin x}\cos^2x\,dx^2$
> $\neq e^{\sin x}(\cos^2x-\sin x)dx^2$
> 即 $f''(u)du^2\neq d^2y$
>
> 事实上由 $dy=f'(u)du$ 两边求微分, 得
> $d^2y=d[f'(u)]\cdot du+f'(u)\cdot d(du)$
> $=f''(u)du^2+f'(u)d^2u$
> 由于 $u$ 是中间变量, 一般 $d^2u$ 不为零
> 舍弃该项会造成计算错误
> 本例中加上一项
> $f'(u)d^2u=e^u\cdot d^2(\sin x)=e^{\sin x}(-\sin x)dx^2$
> $=-e^{\sin x}\sin x\,dx^2$, 答案就正确

------

关于自变量的微分形式不变性只对一阶微分成立
求高阶微分时要仔细分清自变量和中间变量, 分别对待

<script>MathJax = { chtml: { fontURL: "/assets/fonts/mathjax" } };</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
