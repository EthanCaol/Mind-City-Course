


## 原函数与不定积分

原函数: 设在某区间上, 函数 $F(x)$ 与 $f(x)$ 成立关系
$F'(x)=f(x)$
或等价地成立 $d(F(x))=f(x)dx$
则称 $F(x)$ 是 $f(x)$ 在该区间上的一个原函数

[原函数不唯一
若 $F(x)$ 是 $f(x)$ 的原函数
则对任意常数 $C$, $F(x)+C$ 也是 $f(x)$ 的原函数]

不定积分的定义: $f(x)$ 的原函数全体称为该函数的不定积分
记作 $\int f(x)dx$
其中 $\int$ 称为积分号
$f(x)$ 称为被积函数
$x$ 称为积分变量
积分变量采用的字母无关紧要, 即
$\int f(x)dx=\int f(u)du=\int f(t)dt$

------

定理: 若 $G(x)$ 是 $f(x)$ 的任一个原函数
则 $f(x)$ 的全部原函数为 $G(x)+C$
其中 $C$ 是任意常数

证明: 设 $F(x)$ 也是 $f(x)$ 的任一个原函数
则 $F'(x)=G'(x)=f(x)$

于是 $[F(x)-G(x)]'=0$
由定理 5.1.4 知 $F(x)-G(x)=C$
即 $F(x)=G(x)+C$

[求出 $f(x)$ 的任意一个原函数 $F(x)$ 后
就可用 $F(x)+C$ 表示 $f(x)$ 的全部原函数]

------

不定积分是微分的逆运算
$d\left(\int f(x)dx\right)=f(x)dx$
即 $\frac{d}{dx}\left(\int f(x)dx\right)=f(x)$
$\int dF(x)=F(x)+C$
[先做微分运算后做不定积分运算, 结果要相差一个常数]

------

> 例6-1: 求 $\int\sin x\,dx$
> 由 $d(\cos x)=-\sin x\,dx$ 得 $d(-\cos x)=\sin x\,dx$
> 于是 $\int\sin x\,dx=-\cos x+C$

> 例6-2: 求 $\int x^\alpha dx\ (\alpha\neq-1)$
> 由 $\left(\frac{1}{\alpha+1}x^{\alpha+1}\right)'=x^\alpha$ 得
> $\int x^\alpha dx=\frac{1}{\alpha+1}x^{\alpha+1}+C$

> 例6-3: 求 $\int\frac{dx}{x}$
> $x>0$ 时由 $(\ln x)'=\frac{1}{x}$ 得
> $\int\frac{dx}{x}=\ln x+C$
> $x<0$ 时由 $[\ln(-x)]'=\frac{1}{x}$ 得
> $\int\frac{dx}{x}=\ln(-x)+C$
> 合并两式得 $\int\frac{dx}{x}=\ln|x|+C$


## 不定积分的线性性质

定理(线性性): 若函数 $f(x)$ 与 $g(x)$ 的原函数都存在
则对任意常数 $k_1$ 和 $k_2$
函数 $k_1f(x)+k_2g(x)$ 的原函数也存在, 且
$\int[k_1f(x)+k_2g(x)]dx=k_1\int f(x)dx+k_2\int g(x)dx$
[当 $k_1=k_2=0$ 时右端理解为常数 $C$]

证明: 设 $F(x)$ 与 $G(x)$ 分别是 $f(x)$ 与 $g(x)$ 的原函数
则对任意常数 $k_1,k_2$
$k_1F(x)+k_2G(x)$ 是 $k_1f(x)+k_2g(x)$ 的一个原函数
于是 $\int[k_1f(x)+k_2g(x)]dx=k_1F(x)+k_2G(x)+C$

而 $k_1\int f(x)dx+k_2\int g(x)dx$
$=k_1(F(x)+C_1)+k_2(G(x)+C_2)$
$=k_1F(x)+k_2G(x)+(k_1C_1+k_2C_2)$

$C,C_1,C_2$ 都代表任意常数
故两式右端表示的函数族相同

------

由微分公式与不定积分的关系得到的基本公式

| 微分 | 不定积分 |
| --- | --- |
| $d(e^x)=e^x dx$ | $\int e^x dx=e^x+C$ |
| $d(\ln x)=\frac{dx}{x}$ | $\int\frac{dx}{x}=\ln|x|+C$ |
| $d(x^\alpha)=\alpha x^{\alpha-1}dx$ | $\int x^\alpha dx=\frac{1}{\alpha+1}x^{\alpha+1}+C\ (\alpha\neq-1)$ |
| $d(\sin x)=\cos x\,dx$ | $\int\cos x\,dx=\sin x+C$ |
| $d(\cos x)=-\sin x\,dx$ | $\int\sin x\,dx=-\cos x+C$ |
| $d(\tan x)=\sec^2x\,dx$ | $\int\sec^2x\,dx=\tan x+C$ |
| $d(\cot x)=-\csc^2x\,dx$ | $\int\csc^2x\,dx=-\cot x+C$ |
| $d(\sec x)=\tan x\sec x\,dx$ | $\int\tan x\sec x\,dx=\sec x+C$ |
| $d(\csc x)=-\cot x\csc x\,dx$ | $\int\cot x\csc x\,dx=-\csc x+C$ |
| $d(\arcsin x)=\frac{dx}{\sqrt{1-x^2}}$ | $\int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C$ |
| $d(\arctan x)=\frac{dx}{1+x^2}$ | $\int\frac{dx}{1+x^2}=\arctan x+C$ |

------

> 例6-4: 求 $\int\tan^2x\,dx$
> 用三角恒等式 $\tan^2x=\sec^2x-1$, 得
> $\int\tan^2x\,dx=\int(\sec^2x-1)dx$
> $=\int\sec^2x\,dx-\int 1\,dx=\tan x-x+C$

> 例6-5: 求 $\int\sin^2\frac{x}{2}dx$
> 用半角公式 $\sin^2\frac{x}{2}=\frac{1-\cos x}{2}$, 得
> $\int\sin^2\frac{x}{2}dx=\frac{1}{2}\int(1-\cos x)dx$
> $=\frac{1}{2}(x-\sin x)+C$

> 例6-6: 求 $\int\frac{(x+\sqrt{x})(x-2\sqrt{x})^2}{\sqrt{x}}dx$
> 分子展开后与分母 $\sqrt{x}$ 相除
> 被积函数化为几个幂函数之和
>
> $\int\frac{(x+\sqrt{x})(x-2\sqrt{x})^2}{\sqrt{x}}dx$
> $=\int\frac{x^3-3x^2\sqrt{x}+4x\sqrt{x}}{\sqrt{x}}dx$
> $=\int\left(x^{\frac{5}{2}}-3x^2+4x\right)dx$
> $=\frac{2}{7}x^{\frac{7}{2}}-x^3+2x^2+C$

> 例6-7: 求 $\int\frac{x^4}{1+x^2}dx$
> $\int\frac{x^4}{1+x^2}dx=\int\frac{x^4+x^2-x^2}{1+x^2}dx$
> $=\int x^2dx-\int\frac{x^2}{1+x^2}dx$
> $=\frac{1}{3}x^3-\int\frac{1+x^2-1}{1+x^2}dx$
> $=\frac{1}{3}x^3-\int dx+\int\frac{dx}{1+x^2}$
> $=\frac{1}{3}x^3-x+\arctan x+C$

> 例6-8: 已知曲线 $y=f(x)$ 在任意一点 $(x,f(x))$ 处的切线斜率都等于 $x^2$
> 且曲线经过点 $(3,2)$, 求该曲线的方程
> 由题意有 $y'=x^2$, 因此
> $y=\int x^2dx=\frac{x^3}{3}+C$
> 这是一族曲线
> 它们在横坐标相同的点上的切线互相平行
>
> 将 $x=3,y=2$ 代入得 $C=-7$
> 所求曲线为 $y=\frac{x^3}{3}-7$

图6-1: 一族切线互相平行的曲线

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20261011192757400.png =400x)


## 换元积分法

第一类换元积分法(凑微分法):
在不定积分 $\int f(x)dx$ 中
若 $f(x)$ 可化为 $\tilde{f}(g(x))g'(x)$
且 $\tilde{f}(u)$ 的原函数容易求, 则

$\int f(x)dx=\int\tilde{f}(g(x))g'(x)dx$
$=\int\tilde{f}(g(x))d(g(x))$
$=\int\tilde{f}(u)du=\tilde{F}(u)+C=\tilde{F}(g(x))+C$

[运算时令 $u=g(x)$, 相应有 $du=g'(x)dx$]

------

> 例6-9: 求 $\int\frac{dx}{x-a}$
> 将 $\frac{1}{x-a}$ 看成 $\tilde{f}(u)=\frac{1}{u}$ 与 $u=x-a$ 的复合函数
> 因 $d(x-a)=dx$, 令 $u=x-a$ 得
> $\int\frac{dx}{x-a}=\int\frac{d(x-a)}{x-a}$
> $=\int\frac{du}{u}=\ln|u|+C=\ln|x-a|+C$
>
> 同理可得
> $\int\frac{dx}{(x-a)^n}=-\frac{1}{n-1}\cdot\frac{1}{(x-a)^{n-1}}+C\ (n>1)$
> $\int\frac{dx}{x^2-a^2}=\frac{1}{2a}\int\left(\frac{dx}{x-a}-\frac{dx}{x+a}\right)$
> $=\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C$

> 例6-10: 求 $\int\frac{dx}{x^2+a^2}$
> 令 $u=\frac{x}{a}$ 得
> $\int\frac{dx}{x^2+a^2}=\frac{1}{a}\int\frac{d\left(\frac{x}{a}\right)}{1+\left(\frac{x}{a}\right)^2}$
> $=\frac{1}{a}\int\frac{du}{1+u^2}=\frac{1}{a}\arctan u+C$
> $=\frac{1}{a}\arctan\frac{x}{a}+C$
> 同理可得 $\int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac{x}{a}+C$

> 例6-11: 求 $\int\tan x\,dx$
> 令 $u=\cos x$ 得
> $\int\tan x\,dx=\int\frac{\sin x}{\cos x}dx=-\int\frac{(\cos x)'}{\cos x}dx$
> $=-\int\frac{du}{u}=-\ln|u|+C=-\ln|\cos x|+C$

> 例6-12: 求 $\int\sec x\,dx$
> 将 $\sec x$ 写成 $\frac{\cos x}{\cos^2x}=\frac{d(\sin x)}{1-\sin^2x}$
> 令 $u=\sin x$, 用例6-9的公式得
> $\int\sec x\,dx=\frac{1}{2}\ln\frac{1+\sin x}{1-\sin x}+C$
> $=\frac{1}{2}\ln\frac{(1+\sin x)^2}{1-\sin^2x}+C$
> $=\ln\left|\frac{1+\sin x}{\cos x}\right|+C=\ln|\sec x+\tan x|+C$
>
> 类似地可得
> $\int\cot x\,dx=\ln|\sin x|+C$
> $\int\csc x\,dx=\ln|\csc x-\cot x|+C$

> 例6-13: 求 $\int\frac{dx}{\sqrt{x}(1+x)}$
> $\int\frac{dx}{\sqrt{x}(1+x)}=2\int\frac{d(\sqrt{x})}{1+(\sqrt{x})^2}$
> $=2\arctan\sqrt{x}+C$

> 例6-14: 求 $\int\sin mx\cos nx\,dx\ (m\neq n)$
> 用积化和差公式
> $\int\sin mx\cos nx\,dx$
> $=\frac{1}{2}\int[\sin(m+n)x+\sin(m-n)x]dx$
> $=-\frac{1}{2}\left[\frac{\cos(m+n)x}{m+n}+\frac{\cos(m-n)x}{m-n}\right]+C$

------

第二类换元积分法: 令 $x=\varphi(t)$
其中 $\varphi(t)$ 的反函数 $t=\varphi^{-1}(x)$ 存在, 则

$\int f(x)dx=\int f(\varphi(t))d\varphi(t)$
$=\int f(\varphi(t))\varphi'(t)dt=\tilde{F}(t)+C$
$=\tilde{F}(\varphi^{-1}(x))+C$

------

> 例6-15: 求 $\int\sqrt{a^2-x^2}dx$
> 为去掉根号, 令 $x=a\sin t\ \left(-\frac{\pi}{2}\leq t\leq\frac{\pi}{2}\right)$
> 则 $\sqrt{a^2-x^2}=a\cos t$, $dx=a\cos t\,dt$, 于是
> $\int\sqrt{a^2-x^2}dx=a^2\int\cos^2t\,dt$
> $=\frac{a^2}{2}\int(1+\cos 2t)dt$
> $=\frac{a^2}{2}\left(t+\frac{\sin 2t}{2}\right)+C$
>
> 用 $t=\arcsin\frac{x}{a}$ 代回得
> $\int\sqrt{a^2-x^2}dx=\frac{1}{2}x\sqrt{a^2-x^2}+\frac{a^2}{2}\arcsin\frac{x}{a}+C$

> 例6-16: 求 $\int\frac{dx}{\sqrt{x^2-a^2}}$ 和 $\int\frac{dx}{\sqrt{x^2+a^2}}$
> 对 $\int\frac{dx}{\sqrt{x^2-a^2}}$, 令 $x=a\sec t$
> $x>a$ 时 $t\in\left(0,\frac{\pi}{2}\right)$
> $x<-a$ 时 $t\in\left(\pi,\frac{3\pi}{2}\right)$
> 于是 $\sqrt{x^2-a^2}=a\tan t$
>
> $dx=a\tan t\sec t\,dt$, 用例6-12的结果得
> $\int\frac{dx}{\sqrt{x^2-a^2}}=\int\sec t\,dt=\ln|\sec t+\tan t|+C$
>
> 用 $\sec t=\frac{x}{a}$ 和 $\tan t=\sqrt{\sec^2t-1}=\frac{\sqrt{x^2-a^2}}{a}$ 代回得
> $\int\frac{dx}{\sqrt{x^2-a^2}}=\ln\left|\frac{x}{a}+\frac{\sqrt{x^2-a^2}}{a}\right|+C$
> $=\ln\left|x+\sqrt{x^2-a^2}\right|+C$
>
> 类似地 $\int\frac{dx}{\sqrt{x^2+a^2}}=\ln\left|x+\sqrt{x^2+a^2}\right|+C$
>
> 被积函数含 $\sqrt{a^2-x^2}$, $\sqrt{x^2-a^2}$, $\sqrt{x^2+a^2}$ 形式时
> 分别令 $x=a\sin t$, $x=a\sec t$, $x=a\tan t$ 以去掉根号

> 例6-17: 求 $\int x(2x-1)^{100}dx$
> 令 $2x-1=t$, 即 $x=\frac{t+1}{2}$, $dx=\frac{1}{2}dt$, 于是
> $\int x(2x-1)^{100}dx=\frac{1}{4}\int(t+1)t^{100}dt$
> $=\frac{1}{4}\left(\frac{t^{102}}{102}+\frac{t^{101}}{101}\right)+C$
> $=\frac{(2x-1)^{101}}{4}\left(\frac{2x-1}{102}+\frac{1}{101}\right)+C$

> 例6-18: 求 $\int\frac{dx}{x^2\sqrt{1+x^2}}$
> 解法一: 用第一类换元积分法
> 当 $x>0$ 时用 $d\left(\frac{1}{x}\right)=-\frac{2}{x^3}dx$, 得
> $\int\frac{dx}{x^2\sqrt{1+x^2}}=-\int\frac{1}{2\sqrt{1+\frac{1}{x^2}}}d\left(1+\frac{1}{x^2}\right)$
> $=-\sqrt{1+\frac{1}{x^2}}+C=-\frac{\sqrt{1+x^2}}{x}+C$
>
> 解法二: 用第二类换元积分法
> 令 $x=\frac{1}{t}$, 则 $dx=-\frac{1}{t^2}dt$, 得
> $\int\frac{dx}{x^2\sqrt{1+x^2}}=-\int\frac{tdt}{\sqrt{1+t^2}}$
> $=-\sqrt{1+t^2}+C=-\frac{\sqrt{1+x^2}}{x}+C$
>
> 解法三: 两种换元法结合
> 令 $x=\tan t$, 则 $dx=\sec^2t\,dt$, 得
> $\int\frac{dx}{x^2\sqrt{1+x^2}}=\int\frac{\sec^2t\,dt}{\tan^2t\sec t}=\int\frac{\cos t}{\sin^2t}dt$
> $=-\frac{1}{\sin t}+C=-\frac{\sqrt{1+x^2}}{x}+C$


## 分部积分法

分部积分法由函数乘积的微分公式出发
对两个可微函数 $u(x)$ 和 $v(x)$ 成立
$d[u(x)v(x)]=v(x)d[u(x)]+u(x)d[v(x)]$

两边同时求不定积分并移项得
$\int u(x)d[v(x)]=u(x)v(x)-\int v(x)d[u(x)]$

分部积分公式:
$\int u(x)v'(x)dx=u(x)v(x)-\int v(x)u'(x)dx$

------

> 例6-19: 求 $\int x\cos x\,dx$
> 将 $x$ 看成 $u(x)$, $\cos x$ 看成 $v'(x)$
> 则 $u'(x)=1$, $v(x)=\sin x$, 代入公式得
> $\int x\cos x\,dx=\int x\,d(\sin x)=x\sin x-\int\sin x\,dx$
> $=x\sin x+\cos x+C$

> 例6-20: 求 $\int x^2e^x dx$
> 将 $x^2$ 看成 $u(x)$, $e^x$ 看成 $v'(x)$, 代入公式得
> $\int x^2e^x dx=\int x^2d(e^x)=x^2e^x-\int e^x d(x^2)$
> $=x^2e^x-2\int xe^x dx$
> 对后一项再用一次分部积分, 得
> $\int xe^x dx=\int x\,d(e^x)=xe^x-\int e^x dx=xe^x-e^x+C$
> 于是 $\int x^2e^x dx=e^x(x^2-2x+2)+C$

------

分部积分公式的几种主要使用模式

1. 通过对 $u(x)$ 求导降低它的复杂程度
   而 $v'(x)$ 与 $v(x)$ 的类型相似或复杂程度相当
   记 $p_n(x)$ 为 $n$ 次多项式
   对 $\int p_n(x)\sin ax\,dx$, $\int p_n(x)\cos bx\,dx$
   以及 $\int p_n(x)e^{cx}dx$ 类不定积分
   均取 $p_n(x)$ 为 $u(x)$, 另一函数为 $v'(x)$
   这时 $v(x)$ 容易求
   且 $p_n(x)$ 的次数随求导逐次降低
2. 通过对 $u(x)$ 求导使它的类型与 $v(x)$ 相同或相近
   对 $\int p_n(x)\arcsin x\,dx$, $\int p_n(x)\arctan x\,dx$
   以及 $\int p_n(x)\ln x\,dx$ 类不定积分
   取 $p_n(x)$ 为 $v'(x)$, 另一函数为 $u(x)$
3. 利用函数经数次求导后形式复原的性质
   通过若干次分部积分使等式右边也出现 $\int u(x)v'(x)dx$
   再用解方程的办法求出
4. 对 $\int f^{(n)}(x)dx$ 类不定积分
   用分部积分法降低幂指数, 导出递推公式

------

> 例6-21: 求 $\int\ln x\,dx$
> 将 $\ln x$ 看成 $u(x)$, $1$ 看成 $v'(x)$
> 则 $u'(x)=\frac{1}{x}$, $v(x)=x$, 代入公式得
> $\int\ln x\,dx=x\ln x-\int x\cdot\frac{1}{x}dx=x(\ln x-1)+C$

> 例6-22: 求 $\int x\arctan x\,dx$
> 将 $\arctan x$ 看成 $u(x)$, $x$ 看成 $v'(x)$
> 则 $u'(x)=\frac{1}{1+x^2}$, $v(x)=\frac{x^2}{2}$, 代入公式得
> $\int x\arctan x\,dx=\frac{x^2}{2}\arctan x-\frac{1}{2}\int\frac{x^2}{1+x^2}dx$
> $=\frac{x^2}{2}\arctan x-\frac{1}{2}\int\left(1-\frac{1}{1+x^2}\right)dx$
> $=\frac{1+x^2}{2}\arctan x-\frac{x}{2}+C$

> 例6-23: 求 $\int\frac{x}{1+\cos x}dx$
> 用分部积分法和换元积分法得
> $\int\frac{x}{1+\cos x}dx=\int\frac{x}{2\cos^2\frac{x}{2}}dx=\int x\,d\left(\tan\frac{x}{2}\right)$
> $=x\tan\frac{x}{2}-\int\tan\frac{x}{2}dx$
> $=x\tan\frac{x}{2}+2\ln\left|\cos\frac{x}{2}\right|+C$

> 例6-24: 求 $\int e^x\sin x\,dx$
> 将 $\sin x$ 看成 $u(x)$, $e^x$ 看成 $v'(x)$
> 应用分部积分公式得
> $\int e^x\sin x\,dx=e^x\sin x-\int e^x\cos x\,dx$
>
> 对等式右端的积分将 $\cos x$ 看成 $u(x)$
> $e^x$ 看成 $v'(x)$ 再分部积分, 得到
> $\int e^x\sin x\,dx=e^x\sin x-e^x\cos x-\int e^x\sin x\,dx$
>
> 两边都出现所求的 $\int e^x\sin x\,dx$
> 移到等式左边解出
> $\int e^x\sin x\,dx=\frac{e^x(\sin x-\cos x)}{2}+C$
> 类似地 $\int e^x\cos x\,dx=\frac{e^x(\sin x+\cos x)}{2}+C$

> 例6-25: 求 $\int\sqrt{x^2+a^2}dx$ 和 $\int\sqrt{x^2-a^2}dx$
> 以 $\int\sqrt{x^2+a^2}dx$ 为例
> $\int\sqrt{x^2+a^2}dx=x\sqrt{x^2+a^2}-\int\frac{x^2}{\sqrt{x^2+a^2}}dx$
> $=x\sqrt{x^2+a^2}-\int\frac{x^2+a^2-a^2}{\sqrt{x^2+a^2}}dx$
> $=x\sqrt{x^2+a^2}+\int\frac{a^2}{\sqrt{x^2+a^2}}dx-\int\sqrt{x^2+a^2}dx$
>
> 移项解出
> $\int\sqrt{x^2+a^2}dx=\frac{1}{2}\left(x\sqrt{x^2+a^2}+a^2\ln\left|x+\sqrt{x^2+a^2}\right|\right)+C$
> 类似地
> $\int\sqrt{x^2-a^2}dx=\frac{1}{2}\left(x\sqrt{x^2-a^2}-a^2\ln\left|x+\sqrt{x^2-a^2}\right|\right)+C$

> 例6-26: 求 $I_n=\int\frac{dx}{(x^2+a^2)^n}$
> 由例6-10, $I_1=\int\frac{dx}{x^2+a^2}=\frac{1}{a}\arctan\frac{x}{a}+C$
> 对 $n\geq 2$, 用 $1=\frac{1}{a^2}(x^2+a^2-x^2)$ 得
> $I_n=\frac{1}{a^2}\int\frac{x^2+a^2-x^2}{(x^2+a^2)^n}dx$
> $=\frac{1}{a^2}I_{n-1}-\frac{1}{a^2}\int\frac{x^2}{(x^2+a^2)^n}dx$
>
> 对最后一项用分部积分得
> $I_n=\frac{1}{a^2}I_{n-1}+\frac{1}{2a^2(n-1)}\cdot\frac{x}{(x^2+a^2)^{n-1}}$
> $-\frac{1}{2a^2(n-1)}I_{n-1}$
>
> 于是递推公式
> $I_n=\frac{2n-3}{2a^2(n-1)}I_{n-1}+\frac{1}{2a^2(n-1)}\cdot\frac{x}{(x^2+a^2)^{n-1}}$
> 其中 $n\geq 2$
> $I_1=\frac{1}{a}\arctan\frac{x}{a}+C$


## 基本积分表

1. $\int x^\alpha dx=\frac{1}{\alpha+1}x^{\alpha+1}+C\ (\alpha\neq-1)$
   $\int\frac{dx}{x}=\ln|x|+C$
2. $\int a^x dx=\frac{a^x}{\ln a}+C$
   特别地 $\int e^x dx=e^x+C$
3. $\int\sin x\,dx=-\cos x+C$
   $\int\cos x\,dx=\sin x+C$
4. $\int\tan x\,dx=-\ln|\cos x|+C$
   $\int\cot x\,dx=\ln|\sin x|+C$
5. $\int\sec x\,dx=\ln|\sec x+\tan x|+C$
   $\int\csc x\,dx=\ln|\csc x-\cot x|+C$
6. $\int\text{sh}\,x\,dx=\text{ch}\,x+C$
   $\int\text{ch}\,x\,dx=\text{sh}\,x+C$
7. $\int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac{x}{a}+C$
   $\int\frac{dx}{\sqrt{x^2\pm a^2}}=\ln\left|x+\sqrt{x^2\pm a^2}\right|+C$
8. $\int\frac{dx}{x^2-a^2}=\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C$
   $\int\frac{dx}{x^2+a^2}=\frac{1}{a}\arctan\frac{x}{a}+C$
9. $\int\sqrt{a^2-x^2}dx=\frac{1}{2}\left(x\sqrt{a^2-x^2}+a^2\arcsin\frac{x}{a}\right)+C$
10. $\int\sqrt{x^2\pm a^2}dx$
    $=\frac{1}{2}\left(x\sqrt{x^2\pm a^2}\pm a^2\ln\left|x+\sqrt{x^2\pm a^2}\right|\right)+C$

[任一二次多项式 $ax^2+bx+c$ 必能配方成 $a[(x-p)^2\pm q^2]$ 形式
因此后六个公式对 $f(ax^2+bx+c)$ 型的不定积分很有用]

------

> 例6-27: 求 $\int(x+1)\sqrt{x^2-2x+5}dx$
> 解法一: 作变量变换 $x-1=2\tan t$
> 则 $dx=2\sec^2t\,dt$, 于是
> $\int(x+1)\sqrt{x^2-2x+5}dx=\int(x+1)\sqrt{(x-1)^2+4}dx$
> $=\int 8(1+\tan t)\sec^3t\,dt$
> $=8\int\sec^3t\,dt+8\int\tan t\sec^2t\,dt$
>
> 由例6-12和分部积分得
> $\int\sec^3t\,dt=\int\sec t\,d(\tan t)$
> $=\sec t\tan t-\int\tan^2t\sec t\,dt$
> $=\sec t\tan t-\int(\sec^2t-1)\sec t\,dt$
> $=\sec t\tan t-\int\sec^3t\,dt+\int\sec t\,dt$
>
> 移项得
> $\int\sec^3t\,dt=\frac{1}{2}[\sec t\tan t+\ln|\sec t+\tan t|]+C$
> 代回并整理, 结果为
> $\int(x+1)\sqrt{x^2-2x+5}dx=\frac{1}{3}(x^2-2x+5)^{\frac{3}{2}}$
> $+(x-1)\sqrt{x^2-2x+5}+4\ln\left|(x-1)+\sqrt{x^2-2x+5}\right|+C$
>
> 解法二: 直接用例6-25的结果, 得相同结果

> 例6-28: 求 $\int\frac{dx}{\sqrt{x^2+2\xi x+\eta^2}}$
> 将 $x^2+2\xi x+\eta^2$ 配方成 $(x+\xi)^2\pm|\eta^2-\xi^2|$
> 把 $|\eta^2-\xi^2|$ 看作 $a^2$, 有
> $\int\frac{dx}{\sqrt{x^2+2\xi x+\eta^2}}=\int\frac{d(x+\xi)}{\sqrt{(x+\xi)^2\pm|\eta^2-\xi^2|}}$
> $=\ln\left|(x+\xi)+\sqrt{x^2+2\xi x+\eta^2}\right|+C$
>
> 例如当 $\xi=-2,\eta=\sqrt{5}$ 时得
> $\int\frac{dx}{\sqrt{x^2-4x+5}}=\ln\left|(x-2)+\sqrt{x^2-4x+5}\right|+C$


## 有理函数的不定积分

有理函数: 形如 $\frac{p_m(x)}{q_n(x)}$ 的函数
其中 $p_m(x)$ 与 $q_n(x)$ 分别是 $m$ 次和 $n$ 次多项式
[有理函数的原函数一定是初等函数, 本节给出求法并证明这一点]

真分式: 分母次数大于分子次数, 即 $m<n$ 时的有理函数

假分式: $m\geq n$ 时的有理函数
可通过多项式的带余除法化为整式与真分式之和
$\frac{p_m(x)}{q_n(x)}=p_{m-n}(x)+\frac{r(x)}{q_n(x)}$
其中 $p_{m-n}(x)$ 是 $m-n$ 次多项式
$r(x)$ 是次数不超过 $n-1$ 的多项式, 于是
$\int\frac{p_m(x)}{q_n(x)}dx=\int p_{m-n}(x)dx+\int\frac{r(x)}{q_n(x)}dx$
[一般假定 $q_n(x)$ 的最高次项系数为 $1$]

设 $q_n(x)$ 的全部实根为 $\alpha_1,\alpha_2,\cdots,\alpha_i$
重数分别为 $m_1,m_2,\cdots,m_i$
全部复根为 $\beta_1\pm i\gamma_1,\beta_2\pm i\gamma_2,\cdots,\beta_j\pm i\gamma_j$
重数分别为 $n_1,n_2,\cdots,n_j$
记 $\xi_k=-\beta_k$, $\eta_k^2=\beta_k^2+\gamma_k^2\ (\xi_k^2<\eta_k^2)$
在实数域上可将 $q_n(x)$ 分解为
$q_n(x)=\prod_{k=1}^{i}(x-\alpha_k)^{m_k}\cdot\prod_{k=1}^{j}(x^2+2\xi_kx+\eta_k^2)^{n_k}$

------

定理: 设有理函数 $\frac{p(x)}{q(x)}$ 是真分式
多项式 $q(x)$ 有 $k$ 重实根 $\alpha$
即 $q(x)=(x-\alpha)^kq_1(x)$, $q_1(\alpha)\neq 0$
则存在实数 $\lambda$ 与多项式 $p_1(x)$
$p_1(x)$ 的次数低于 $(x-\alpha)^{k-1}q_1(x)$ 的次数, 成立
$\frac{p(x)}{q(x)}=\frac{\lambda}{(x-\alpha)^k}+\frac{p_1(x)}{(x-\alpha)^{k-1}q_1(x)}$

证明: 令 $\frac{p(\alpha)}{q_1(\alpha)}=\lambda$
则 $x=\alpha$ 是多项式 $p(x)-\lambda q_1(x)$ 的根, 设
$p(x)-\lambda q_1(x)=(x-\alpha)p_1(x)$

就得到
$\frac{p(x)}{q(x)}=\frac{\lambda}{(x-\alpha)^k}+\frac{p_1(x)}{(x-\alpha)^{k-1}q_1(x)}$

------

定理: 设有理函数 $\frac{p(x)}{q(x)}$ 是真分式
多项式 $q(x)$ 有 $l$ 重共轭复根 $\beta\pm i\gamma$
即 $q(x)=(x^2+2\xi x+\eta^2)^lq^*(x)$, $q^*(\beta\pm i\gamma)\neq 0$
其中 $\xi=-\beta$, $\eta^2=\beta^2+\gamma^2\ (\xi^2<\eta^2)$
则存在实数 $\mu,\nu$ 和多项式 $p^*(x)$
$p^*(x)$ 的次数低于 $(x^2+2\xi x+\eta^2)^{l-1}q^*(x)$ 的次数, 成立
$\frac{p(x)}{q(x)}=\frac{\mu x+\nu}{(x^2+2\xi x+\eta^2)^l}+\frac{p^*(x)}{(x^2+2\xi x+\eta^2)^{l-1}q^*(x)}$

证明: 令 $\frac{p(\beta+i\gamma)}{q^*(\beta+i\gamma)}=\mu(\beta+i\gamma)+\nu$
其中 $\mu,\nu$ 为实数, 取共轭得
$\frac{p(\beta-i\gamma)}{q^*(\beta-i\gamma)}=\mu(\beta-i\gamma)+\nu$

于是 $x=\beta\pm i\gamma$ 是多项式 $p(x)-(\mu x+\nu)q^*(x)$ 的根, 设
$p(x)-(\mu x+\nu)q^*(x)=(x^2+2\xi x+\eta^2)p^*(x)$
就得到上式

------

重复应用上述两个定理, 可将有理函数
$\frac{p_m(x)}{q_n(x)}=\frac{p_m(x)}{\prod\limits_{k=1}^{i}(x-\alpha_k)^{m_k}\cdot\prod\limits_{k=1}^{j}(x^2+2\xi_kx+\eta_k^2)^{n_k}}$
分解成简单分式之和, 即
$\frac{p_m(x)}{q_n(x)}=\sum_{k=1}^{i}\sum_{r=1}^{m_k}\frac{\lambda_{kr}}{(x-\alpha_k)^r}$
$+\sum_{k=1}^{j}\sum_{r=1}^{n_k}\frac{\mu_{kr}x+\nu_{kr}}{(x^2+2\xi_kx+\eta_k^2)^r}$
其中 $\lambda_{kr},\mu_{kr},\nu_{kr}$ 可用待定系数法算出

由不定积分的线性性质
有理函数的不定积分归结为两种类型

1. $\int\frac{dx}{(x-\alpha)^n}\ (n\geq 1)$
   由例6-9得
   $\int\frac{dx}{(x-\alpha)^n}=\begin{cases}\ln|x-\alpha|+C, & n=1\\ -\frac{1}{n-1}\cdot\frac{1}{(x-\alpha)^{n-1}}+C, & n\geq 2\end{cases}$
2. $\int\frac{\mu x+\nu}{(x^2+2\xi x+\eta^2)^n}dx\ (n\geq 1,\xi^2<\eta^2)$
   将原式化成
   $\int\frac{\mu x+\nu}{(x^2+2\xi x+\eta^2)^n}dx$
   $=\frac{\mu}{2}\int\frac{2x+2\xi}{(x^2+2\xi x+\eta^2)^n}dx$
   $+(\nu-\mu\xi)\int\frac{dx}{(x^2+2\xi x+\eta^2)^n}$
   右端第一项用第一类换元积分法
   $\int\frac{2x+2\xi}{(x^2+2\xi x+\eta^2)^n}dx$
   $=\begin{cases}\ln|x^2+2\xi x+\eta^2|+C, & n=1\\ -\frac{1}{n-1}\cdot\frac{1}{(x^2+2\xi x+\eta^2)^{n-1}}+C, & n\geq 2\end{cases}$
   右端第二项配方成
   $\int\frac{dx}{[(x+\xi)^2+(\eta^2-\xi^2)]^n}$
   再用例6-26的递推公式

综上, 求有理函数的不定积分归结为解决上述两种类型
于是有理函数的原函数一定是初等函数

------

> 例6-29: 求 $\int\frac{4x^3-13x^2+3x+8}{(x+1)(x-2)(x-1)^2}dx$
> 将被积函数分解成简单分式之和, 设
> $\frac{4x^3-13x^2+3x+8}{(x+1)(x-2)(x-1)^2}$
> $=\frac{A}{x+1}+\frac{B}{x-2}+\frac{C}{x-1}+\frac{D}{(x-1)^2}$
> 通分后两边分子应相等
>
> $4x^3-13x^2+3x+8=A(x-2)(x-1)^2$
> $+B(x+1)(x-1)^2+C(x+1)(x-2)(x-1)+D(x+1)(x-2)$
>
> 令 $x=-1$ 得 $A=1$
> 令 $x=2$ 得 $B=-2$
> 令 $x=1$ 得 $D=-1$
> 比较 $x^3$ 的系数得 $C=4-A-B=5$, 于是
>
> $\int\frac{4x^3-13x^2+3x+8}{(x+1)(x-2)(x-1)^2}dx$
> $=\int\left[\frac{1}{x+1}-\frac{2}{x-2}+\frac{5}{x-1}-\frac{1}{(x-1)^2}\right]dx$
> $=\ln\left|\frac{(x+1)(x-1)^5}{(x-2)^2}\right|+\frac{1}{x-1}+C$
> [除非万不得已, 避免将右式全部展开后与左边比较系数建立线性方程组]

> 例6-30: 求 $\int\frac{x^4+x^3+3x^2-1}{(x^2+1)^2(x-1)}dx$
> 设 $\frac{x^4+x^3+3x^2-1}{(x^2+1)^2(x-1)}$
> $=\frac{A}{x-1}+\frac{Bx+C}{x^2+1}+\frac{Dx+E}{(x^2+1)^2}$
> 则 $x^4+x^3+3x^2-1=A(x^2+1)^2$
> $+(Bx+C)(x-1)(x^2+1)+(Dx+E)(x-1)$
>
> 令 $x=1$ 得 $A=1$
> 比较 $x^4$ 的系数得 $B=1-A=0$
> 比较 $x^3$ 的系数得 $C=1$
> 令 $x^2=-1$ 即 $x=i$ 得 $-3-i=(-D-E)+(E-D)i$
> 实部与虚部分别相等得 $D=2$ 和 $E=1$
>
> 于是
> $\int\frac{x^4+x^3+3x^2-1}{(x^2+1)^2(x-1)}dx$
> $=\int\left[\frac{1}{x-1}+\frac{1}{x^2+1}+\frac{2x+1}{(x^2+1)^2}\right]dx$
> $=\ln|x-1|+\frac{3}{2}\arctan x-\frac{1}{x^2+1}+\frac{x}{2(x^2+1)}+C$


## 可化成有理函数不定积分的情况

含根式的情形:
$R\left(x,\sqrt[n]{\frac{\xi x+\eta}{\mu x+\nu}}\right)$ 类不定积分
这里 $R(u,v)$ 表示关于 $u,v$ 的有理函数
即分子和分母都是关于 $u,v$ 的二元多项式
作变量变换 $\sqrt[n]{\frac{\xi x+\eta}{\mu x+\nu}}=t$
则 $x=\varphi(t)=\frac{-\nu t^n+\eta}{\mu t^n-\xi}$

有理函数与有理函数的复合仍为有理函数
有理函数的导数也是有理函数, 因此
$\int R\left(x,\sqrt[n]{\frac{\xi x+\eta}{\mu x+\nu}}\right)dx$
$=\int R\left(\frac{-\nu t^n+\eta}{\mu t^n-\xi},t\right)\varphi'(t)dt$
右端的被积函数是关于 $t$ 的有理函数
用前面的方法求出

[最常见的情形是 $\mu=0$
这时被积函数变成 $R(x,\sqrt[n]{\xi x+\eta})$]

------

> 例6-31: 求 $\int\frac{x\,dx}{\sqrt{4x-3}}$
> 令 $\sqrt{4x-3}=t$
> 则 $x=\frac{1}{4}(t^2+3)$, $dx=\frac{t}{2}dt$, 所以
> $\int\frac{x\,dx}{\sqrt{4x-3}}=\frac{1}{8}\int(t^2+3)dt$
> $=\frac{t^3}{24}+\frac{3t}{8}+C=\frac{\sqrt{4x-3}}{12}(2x+3)+C$

> 例6-32: 求 $\int\frac{dx}{x(\sqrt[3]{x}-\sqrt{x})}$
> 为同时去掉 $\sqrt[3]{x}$ 和 $\sqrt{x}$ 的根号, 令 $x=t^6$
>
> 于是 $dx=6t^5dt$, 所以
> $\int\frac{dx}{x(\sqrt[3]{x}-\sqrt{x})}=6\int\frac{dt}{t^3(1-t)}$
> $=6\int\left(\frac{1}{t}+\frac{1}{t^2}+\frac{1}{t^3}-\frac{1}{t-1}\right)dt$
> $=6\left(\ln\left|\frac{\sqrt[6]{x}}{\sqrt[6]{x}-1}\right|-\frac{1}{\sqrt[6]{x}}-\frac{1}{2\sqrt[3]{x}}\right)+C$

> 例6-33: 求 $\int\frac{\sqrt{1+x}}{x\sqrt{1-x}}dx$
> 令 $\sqrt{\frac{1+x}{1-x}}=t$
>
> 则 $x=\frac{t^2-1}{t^2+1}$, $dx=\frac{4t}{(t^2+1)^2}dt$, 所以
> $\int\frac{\sqrt{1+x}}{x\sqrt{1-x}}dx=4\int\frac{t^2dt}{(t^2-1)(t^2+1)}$
> $=\int\left(\frac{1}{t-1}-\frac{1}{t+1}+\frac{2}{t^2+1}\right)dt$
> $=\ln\left|\frac{t-1}{t+1}\right|+2\arctan t+C$
> $=\ln\left|\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right|+2\arctan\sqrt{\frac{1+x}{1-x}}+C$

------

对于 $\sqrt[n]{(\xi x+\eta)^i(\mu x+\nu)^j}\ (i+j=kn)$ 类型的函数, 先化成
$\sqrt[n]{(\xi x+\eta)^i(\mu x+\nu)^j}=(\xi x+\eta)^k\cdot\sqrt[n]{\frac{(\mu x+\nu)^j}{(\xi x+\eta)^i}}$
再作变换 $\sqrt[n]{\frac{\mu x+\nu}{\xi x+\eta}}=t$

------

> 例6-34: 求 $\int\frac{dx}{\sqrt[3]{(x-1)^2(x+1)^4}}$
> 将 $\int\frac{dx}{\sqrt[3]{(x-1)^2(x+1)^4}}$ 化为等价形式
> $\int\frac{1}{(x+1)^2}\cdot\sqrt[3]{\frac{(x+1)^2}{(x-1)^2}}dx$
> 令 $\sqrt[3]{\frac{x+1}{x-1}}=t$
>
> 则 $\frac{x+1}{x-1}=t^3$, $x=\frac{t^3+1}{t^3-1}$
> $\frac{1}{x+1}=\frac{t^3-1}{2t^3}$, $dx=\frac{-6t^2}{(t^3-1)^2}dt$, 于是
> $\int\frac{dx}{\sqrt[3]{(x-1)^2(x+1)^4}}=-\frac{3}{2}\int\frac{1}{t^2}dt$
> $=\frac{3}{2t}+C=\frac{3}{2}\sqrt[3]{\frac{x-1}{x+1}}+C$

------

三角函数有理式的情形:
$R(\sin x,\cos x)$ 类不定积分
$\tan x,\cot x,\sec x,\csc x$ 都是 $\sin x$ 和 $\cos x$ 的有理函数
故凡是三角函数的有理函数都可化成 $\sin x$ 和 $\cos x$ 的有理函数
用万能公式 $\tan\frac{x}{2}=t$ 作变换, 则
$\sin x=2\sin\frac{x}{2}\cos\frac{x}{2}=\frac{2t}{1+t^2}$
$\cos x=\cos^2\frac{x}{2}-\sin^2\frac{x}{2}=\frac{1-t^2}{1+t^2}$
$dx=d\left(2\arctan t\right)=\frac{2dt}{1+t^2}$

于是原式化成求有理函数
$\int R\left(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\right)\frac{2}{1+t^2}dt$
的不定积分

------

> 例6-35: 求 $\int\frac{dx}{4+4\sin x+\cos x}$
> 作变换 $\tan\frac{x}{2}=t$, 则
> $\int\frac{dx}{4+4\sin x+\cos x}=\int\frac{\frac{2}{1+t^2}dt}{4+4\cdot\frac{2t}{1+t^2}+\frac{1-t^2}{1+t^2}}$
> $=2\int\frac{dt}{3t^2+8t+5}=2\int\frac{dt}{(3t+5)(t+1)}$
>
> $=\int\left(\frac{1}{t+1}-\frac{3}{3t+5}\right)dt$
> $=\ln|t+1|-\ln|3t+5|+C$
> $=\ln\left|\tan\frac{x}{2}+1\right|-\ln\left|3\tan\frac{x}{2}+5\right|+C$

> 例6-36: 求 $\int\frac{\cot x\,dx}{1+\sin x}$
> 用万能公式, 作代换 $\tan\frac{x}{2}=t$
> 则 $\cot x=\frac{\cos x}{\sin x}=\frac{1-t^2}{2t}$
> $\int\frac{\cot x\,dx}{1+\sin x}=\int\frac{1-t^2}{t^3+2t^2+t}dt$
> $=\int\left[\frac{1}{t}-\frac{2}{t+1}\right]dt=\ln\left|\frac{\tan\frac{x}{2}}{\left(\tan\frac{x}{2}+1\right)^2}\right|+C$
>
> 事实上, 利用三角关系式和换元积分法
> $\int\frac{\cot x\,dx}{1+\sin x}=\int\frac{\cos x\,dx}{\sin x(1+\sin x)}$
> $=\int\left[\frac{1}{\sin x}-\frac{1}{1+\sin x}\right]d(\sin x)$
> $=\ln\left|\frac{\sin x}{1+\sin x}\right|+C$
>
> 计算过程简洁, 结果更为简明
> 两种方法算出的解只相差一个常数

[万能公式能确保求出所有 $R(\sin x,\cos x)$ 类函数的不定积分
但利用三角函数的性质或其他方法在很多情况下更简便
求三角函数有理式的不定积分时不要滥用万能公式]

<script>MathJax = { chtml: { fontURL: "/assets/fonts/mathjax" } };</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
