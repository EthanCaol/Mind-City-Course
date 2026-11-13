# 第9章 函数

## 函数定义

!!! abstract "语法形式"

    ```c
    返回类型 函数名(形参声明列表)
    {
        声明与语句;
        return 表达式;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define WIDTH 20
    void starbar(void);       /* 原型 */

    int main(void)
    {
        starbar();
        printf("GIGATHINK, INC.\n");
        starbar();
        return 0;
    }

    void starbar(void)        /* 定义, 函数头后无分号 */
    {
        int count;

        for (count = 1; count <= WIDTH; count++)
            putchar('*');
        putchar('\n');
    }
    ```

    输出：

    ```text
    ********************
    GIGATHINK, INC.
    ********************
    ```

!!! note "说明"

    - 函数定义由函数头和函数体组成
    - 函数头的圆括号后没有分号，带分号的是函数原型
    - `count` 是局部变量，只属于 `starbar()`
    - 返回类型 `void` 表示函数不返回值
    - 参数表中的 `void` 表示函数不带参数
    - 函数定义放在首次调用之前时，定义同时起原型作用

!!! warning "常见错误"

    - 在函数头后加分号，函数变成原型，函数体失去函数头
    - 省略返回类型，C99 起不再允许隐式 `int`
    - 把只在 `starbar()` 内有效的 `count` 拿到 `main()` 中使用

## 函数调用

!!! abstract "语法形式"

    ```c
    函数名(实际参数列表);
    变量 = 函数名(实际参数列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void show_n_char(char ch, int num);

    int main(void)
    {
        show_n_char('*', 12);     /* 常量作为实参 */
        putchar('\n');
        show_n_char(' ', 4);      /* 字符常量作为实参 */
        printf("NAME\n");
        return 0;
    }

    void show_n_char(char ch, int num)
    {
        int count;

        for (count = 1; count <= num; count++)
            putchar(ch);
    }
    ```

    输出：

    ```text
    ************
        NAME
    ```

!!! note "说明"

    - 调用时先对实际参数求值，再把值拷贝给形式参数
    - 实际参数可以是常量，变量，也可以是表达式
    - 被调函数执行完，控制返回调用处继续执行下一句
    - `show_n_char('*', 12);` 是语句，圆括号不能省略

!!! warning "常见错误"

    - 调用无参函数写成 `starbar;`，漏掉圆括号
    - 实际参数的个数或类型与原型不一致
    - 调用语句末尾漏写分号

## 函数原型

!!! abstract "语法形式"

    ```c
    返回类型 函数名(类型 形参名, ...);
    返回类型 函数名(类型, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int imin(int, int);          /* 原型, 省略形参名 */

    int main(void)
    {
        printf("%d\n", imin(9, 4));
        return 0;
    }

    int imin(int n, int m)       /* 定义 */
    {
        return n < m ? n : m;
    }
    ```

    输出：

    ```text
    4
    ```

!!! note "说明"

    - 原型告知编译器返回类型，参数个数与每个参数的类型
    - 原型中的形参名可以省略，写了也不会创建变量
    - 原型可放在 `main()` 之前，也可放在 `main()` 内的声明处
    - 原型末尾的分号是声明与定义的区别
    - 函数定义的形参类型必须与原型逐一对应

!!! warning "常见错误"

    - 漏写末尾分号，把原型写成了函数定义的开头
    - 原型与定义的参数类型不一致
    - 认为原型中的形参名必须与定义中的相同

## 无参数与未指定参数

!!! abstract "语法形式"

    ```c
    void f(void);    /* 明确不带参数 */
    void f();        /* C17 及以前: 参数未指定 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void greet(void);

    int main(void)
    {
        greet();
        return 0;
    }

    void greet(void)
    {
        printf("hello\n");
    }
    ```

    输出：

    ```text
    hello
    ```

!!! note "说明"

    - 圆括号中写 `void` 表示函数确实不接受参数
    - 调用带 `void` 原型的函数时，编译器检查有没有多传参数
    - `int printf(const char *fmt, ...);` 中的 `...` 表示可变参数
    - 旧式 `f()` 不构成原型，编译器不检查参数个数与类型
    - 可变参数函数至少要有一个固定参数

    [C23 已移除无原型声明与 K&R 旧式定义，`f()` 与 `f(void)` 均表示不带参数]

!!! warning "常见错误"

    - 以为 `void f();` 表示不接受参数
    - 在可变参数原型中漏写第一个固定参数
    - 在 C17 编译器上依赖 `f()` 的参数检查

## 形式参数与实际参数

!!! abstract "语法形式"

    ```c
    返回类型 f(类型 形参名, ...);   /* 定义处 */
    f(表达式, ...);                 /* 调用处 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void show(char ch, int num);

    int main(void)
    {
        int n = 3;

        show('*', n + 1);    /* 实参: 常量与表达式 */
        return 0;
    }

    void show(char ch, int num)    /* 形参: ch 与 num */
    {
        while (num-- > 0)
            putchar(ch);
        putchar('\n');
    }
    ```

    输出：

    ```text
    ****
    ```

!!! note "说明"

    - 形式参数是函数定义中声明的变量，属于被调函数
    - 实际参数是函数调用圆括号中的表达式
    - 实参先求值，再把值拷贝给形参
    - 形参名与实参名无关，不必相同
    - 被调函数修改形参，不影响主调函数中的实参
    - `(WIDTH - strlen(PLACE)) / 2` 这类表达式会先算出结果再传入

    ![图9.3 形式参数和实际参数](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00051.jpg)

!!! warning "常见错误"

    - 函数头写成 `void f(int x, y)`，漏掉 `y` 的类型
    - 认为实参变量本身被传入函数，在函数内改形参就能改实参
    - 实参用表达式时加了多余的类型名

## return 语句与返回值

!!! abstract "语法形式"

    ```c
    return 表达式;
    return;          /* 只用于 void 函数 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int imin(int n, int m);

    int main(void)
    {
        int a = 7, b = 3;

        printf("%d\n", 2 * imin(a, b) + 1);
        return 0;
    }

    int imin(int n, int m)
    {
        if (n < m)
            return n;
        else
            return m;
    }
    ```

    输出：

    ```text
    7
    ```

!!! note "说明"

    - `return` 后的表达式值成为函数调用表达式的值
    - 返回值可赋给变量，也可参与更大的表达式
    - `return` 同时终止函数，把控制交回调用处
    - 函数可有多条 `return`，执行到第一条即返回
    - `void` 函数可直接写 `return;`，不带返回值
    - `main()` 末尾的 `return 0;` 可省略

!!! warning "常见错误"

    - 写成 `imin(a, b); x = min;`，想用被调函数的局部变量
    - 在非 `void` 函数中写 `return;`
    - 以为 `return` 之后的语句还会执行

## 返回值类型转换

!!! abstract "语法形式"

    ```c
    返回类型 f(形参列表)
    {
        return 表达式;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int what_if(int n);

    int main(void)
    {
        printf("%d\n", what_if(64));
        return 0;
    }

    int what_if(int n)
    {
        double z = 100.0 / (double) n;

        return z;
    }
    ```

    输出：

    ```text
    1
    ```

!!! note "说明"

    - 返回值类型与函数声明类型不一致时，按声明类型转换
    - 上例 `z` 的值为 `1.5625`，返回时截断为 `1`
    - 函数类型指返回值的类型，与参数类型无关
    - `double klink(int a, int b)` 返回 `double`，参数为两个 `int`

!!! warning "常见错误"

    - 以为函数会按 `return` 表达式的原始类型返回
    - 把参数类型当作函数类型
    - 依赖浮点转整数的截断，丢失小数部分

## 函数类型与签名

!!! abstract "语法形式"

    ```c
    返回类型 函数名(参数类型列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    double duff(double, int);    /* 原型 */

    int main(void)
    {
        printf("%.2f\n", duff(6.0, 2));
        return 0;
    }

    double duff(double u, int k)
    {
        return u / k;
    }
    ```

    输出：

    ```text
    3.00
    ```

!!! note "说明"

    - 函数的返回类型与参数列表共同决定函数的类型
    - 无返回值时返回类型写 `void`
    - 未声明返回类型时旧编译器假定 `int`，C99 起不再支持
    - 原型给出返回类型，参数个数与每个参数的类型
    - 同一函数的所有声明与定义必须一致
    - 头文件只提供声明，函数代码在库文件中

    [通行术语中的函数签名只含函数名与参数类型，不含返回类型
    - 教材把返回类型计入签名，并把函数类型等同于返回类型]

!!! warning "常见错误"

    - 定义与原型中的返回类型不一致
    - 把 `void` 函数的返回值赋给变量
    - 认为参数名是签名的一部分

## 函数原型的检查作用

!!! abstract "语法形式"

    ```c
    int imax(int, int);    /* 完整原型 */
    int imax();            /* 旧式声明, 无参数信息 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int imax(int, int);

    int main(void)
    {
        printf("%d\n", imax(3.0, 5.0));
        return 0;
    }

    int imax(int n, int m)
    {
        return n > m ? n : m;
    }
    ```

    输出：

    ```text
    5
    ```

!!! note "说明"

    - 完整原型使编译器检查实际参数的个数
    - 个数不符时编译报错，程序无法生成
    - 类型不符但可转换时，编译器按形参类型转换实参
    - `3.0` 与 `5.0` 被转换成 `3` 与 `5`
    - 转换可能丢失数据，编译器可给出警告
    - 旧式声明不带参数信息，编译器无法检查，可能读到栈中的无关值

!!! warning "常见错误"

    - 用 `int imax();` 后传错参数个数或类型，程序仍能编译
    - 忽略 `double` 转 `int` 的丢失数据警告
    - 把警告当作错误，或把错误当作警告

## 递归调用

!!! abstract "语法形式"

    ```c
    返回类型 f(参数)
    {
        if (终止条件)
            return 基值;
        return f(规模更小的参数);
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void up_and_down(int);

    int main(void)
    {
        up_and_down(1);
        return 0;
    }

    void up_and_down(int n)
    {
        printf("Level %d: n at %p\n", n, (void *) &n);
        if (n < 4)
            up_and_down(n + 1);
        printf("LEVEL %d: n at %p\n", n, (void *) &n);
    }
    ```

    输出：

    ```text
    Level 1: n at 0x7ffeefbff5ac
    Level 2: n at 0x7ffeefbff58c
    Level 3: n at 0x7ffeefbff56c
    Level 4: n at 0x7ffeefbff54c
    LEVEL 4: n at 0x7ffeefbff54c
    LEVEL 3: n at 0x7ffeefbff56c
    LEVEL 2: n at 0x7ffeefbff58c
    LEVEL 1: n at 0x7ffeefbff5ac
    ```

!!! note "说明"

    - 每级递归调用有独立的形参与局部变量，地址各不相同
    - 递归调用之前的语句按调用顺序执行
    - 递归调用之后的语句按相反顺序执行
    - 函数结束后控制返回上一级，不能跳级返回
    - 递归函数必须有终止条件
    - 每次调用的参数都要向终止条件靠近
    - 地址的具体值随系统与运行环境不同，关键看各级的对应关系

    ![图9.4 递归中的变量](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00052.jpg)

!!! warning "常见错误"

    - 缺少终止条件，无限递归直到栈溢出
    - 递归调用的参数没有变化
    - 认为不同级的同名变量共用同一块存储

## 尾递归

!!! abstract "语法形式"

    ```c
    返回类型 f(累加器, int n)
    {
        if (n <= 1)
            return 累加器;
        return f(累加器 * n, n - 1);    /* 调用之后无运算 */
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    long rfact(long acc, int n);

    int main(void)
    {
        printf("%ld\n", rfact(1, 5));
        return 0;
    }

    long rfact(long acc, int n)
    {
        if (n > 1)
            return rfact(acc * n, n - 1);
        return acc;
    }
    ```

    输出：

    ```text
    120
    ```

!!! note "说明"

    - 尾递归指递归调用处于函数的尾位置，调用返回后不再有运算
    - `return n * rfact(n - 1);` 在调用返回后还要做乘法，不是尾递归
    - 把中间结果放入累加器参数，可把递归写成尾调用形式
    - 阶乘满足 `n! = n * (n-1)!`，适合写成递归
    - 每次递归调用仍创建一组新变量，递归更占内存
    - 循环版使用固定大小的栈空间，执行更快

    [教材把 `return n * rfact(n - 1);` 称为尾递归
    - 通行定义要求调用返回后不再有运算，该形式不属于尾递归]

    [C 标准不要求编译器做尾调用优化，是否把尾递归改成循环由编译器和优化选项决定]

!!! warning "常见错误"

    - 认为尾递归一定会被优化成循环
    - 把 `return n * f(n - 1);` 当作尾递归
    - 忘记 `0! = 1` 这一终止值

## 递归实现倒序输出

!!! abstract "语法形式"

    ```c
    void f(unsigned long n)
    {
        if (n >= 2)
            f(n / 2);
        putchar(...);
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void to_binary(unsigned long n);

    int main(void)
    {
        to_binary(9);
        putchar('\n');
        return 0;
    }

    void to_binary(unsigned long n)
    {
        int r = n % 2;

        if (n >= 2)
            to_binary(n / 2);
        putchar(r == 0 ? '0' : '1');
    }
    ```

    输出：

    ```text
    1001
    ```

!!! note "说明"

    - `n % 2` 得到当前最低位的值
    - 先算当前位，再递归处理高位
    - 最深一层先打印最高位，逐层返回时打印其余位
    - 终止条件是 `n < 2`，此时只剩一位
    - 不用递归时，要先用数组保存各位再逆序输出

!!! warning "常见错误"

    - 把 `putchar` 写在递归调用之前，输出变成逆序
    - 终止条件写成 `n > 2`，漏掉最高位
    - 用有符号类型接收负数

## 递归的代价

!!! example "示例"

    ```c
    #include <stdio.h>
    unsigned long Fibonacci(unsigned n);

    int main(void)
    {
        printf("%lu\n", Fibonacci(10));
        return 0;
    }

    unsigned long Fibonacci(unsigned n)
    {
        if (n > 2)
            return Fibonacci(n - 1) + Fibonacci(n - 2);
        else
            return 1;
    }
    ```

    输出：

    ```text
    55
    ```

!!! note "说明"

    - 该函数每级调用自身两次，称为双递归
    - 第 `k` 层共有 $2^{k-1}$ 个调用，各自创建一个 `n`
    - 调用次数随 `n` 指数增长，很快耗尽时间与内存
    - `Fibonacci(40)` 会产生大量重复计算
    - 递归适合倒序输出，分治等结构自然的问题
    - 参数规模大或效率优先时，改用循环或记忆化

!!! warning "常见错误"

    - 对较大的 `n` 使用双递归
    - 认为递归写法总是比循环简洁高效
    - 把递归当作可以替代一切循环的手段

## 地址运算符 &

!!! abstract "语法形式"

    ```c
    &变量
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void mikado(int);

    int main(void)
    {
        int pooh = 2;

        printf("pooh = %d, &pooh = %p\n", pooh, (void *) &pooh);
        mikado(pooh);
        return 0;
    }

    void mikado(int bah)
    {
        int pooh = 10;

        printf("pooh = %d, &pooh = %p\n", pooh, (void *) &pooh);
        printf("bah = %d, &bah = %p\n", bah, (void *) &bah);
    }
    ```

    输出：

    ```text
    pooh = 2, &pooh = 0x7fff5fbff8e8
    pooh = 10, &pooh = 0x7fff5fbff8b8
    bah = 2, &bah = 0x7fff5fbff8bc
    ```

!!! note "说明"

    - `&` 是一元运算符，给出变量的存储地址
    - 地址是变量在内存中的位置
    - `%p` 是打印地址的转换说明，参数转换为 `void *`
    - 不同函数中的同名变量地址不同，是彼此独立的变量
    - `&变量` 的结果是常量，不能放在赋值号左边
    - `scanf("%d", &num)` 需要地址才能把读入的值写回变量
    - 地址的具体数值随系统与运行环境不同

!!! warning "常见错误"

    - 用 `%d` 打印地址
    - 试图给 `&x` 赋值
    - 把不同函数中的同名变量当作同一个变量

## 指针声明

!!! abstract "语法形式"

    ```c
    类型 * 指针名;
    类型 * 指针名1, * 指针名2;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int bah = 5;
        int *ptr;            /* 指向 int 的指针 */

        ptr = &bah;
        printf("%d\n", *ptr);
        return 0;
    }
    ```

    输出：

    ```text
    5
    ```

!!! note "说明"

    - 指针是值为内存地址的变量
    - 声明指针时必须写明所指向对象的类型
    - `int *pi;` 表示 `*pi` 是 `int`，`pi` 是指向 `int` 的指针
    - `*` 与指针名之间的空格不影响含义
    - 指针不是整数类型，不能把两个指针相乘
    - 未初始化的指针不指向任何有效对象，解引用是未定义行为

    ![图9.5 声明并使用指针](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00053.jpg)

!!! warning "常见错误"

    - 写成 `pointer ptr;`，C 中没有这种类型
    - 在 `int *p, q;` 中把 `q` 也当作指针
    - 声明后未赋值就写 `*p = 5;`

## 间接运算符 *

!!! abstract "语法形式"

    ```c
    *指针
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int nurse = 22;
        int *ptr = &nurse;
        int val = *ptr;      /* 取出地址上的值 */

        *ptr = 30;           /* 改写地址上的值 */
        printf("%d %d\n", val, nurse);
        return 0;
    }
    ```

    输出：

    ```text
    22 30
    ```

!!! note "说明"

    - `*` 是一元间接运算符，也称解引用运算符
    - `*ptr` 表示 `ptr` 所指向地址上的值
    - `ptr = &bah; val = *ptr;` 等价于 `val = bah;`
    - `*` 用作二元运算符时表示乘法，两者语法功能不同
    - 只有指向有效对象的指针才能解引用
    - 指针变量以地址为基本量，值由 `*` 取得

!!! warning "常见错误"

    - 混淆乘法的 `*` 与解引用的 `*`
    - 解引用空指针或未初始化的指针
    - 解引用已释放的地址

## 指针参数

!!! abstract "语法形式"

    ```c
    返回类型 f(类型 * 形参名, ...);
    f(&实参, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void interchange(int *u, int *v);

    int main(void)
    {
        int x = 5, y = 10;

        interchange(&x, &y);     /* 传地址 */
        printf("x = %d, y = %d\n", x, y);
        return 0;
    }

    void interchange(int *u, int *v)
    {
        int temp = *u;

        *u = *v;
        *v = temp;
    }
    ```

    输出：

    ```text
    x = 10, y = 5
    ```

!!! note "说明"

    - 传地址使被调函数能改写主调函数中的变量
    - 形参声明为指针，调用时传 `&x`
    - `*u` 就是 `x`，对 `*u` 赋值即改写 `x`
    - `temp = u;` 得到的是地址，不是值
    - `return` 只能传回一个值，要传回多个值需用指针
    - 只读取值不求改写时传值，需要改写时传地址

!!! warning "常见错误"

    - 定义写成 `int u`，调用时却传 `&x`
    - 交换 `u` 与 `v` 的地址，而不是 `*u` 与 `*v` 的值
    - 原型写成 `int *`，定义写成 `int`，类型不一致

## 按值传递

!!! abstract "语法形式"

    ```c
    f(x);      /* 传值: 拷贝变量的值 */
    f(&x);     /* 传地址: 拷贝变量的地址 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void interchange(int u, int v);

    int main(void)
    {
        int x = 5, y = 10;

        interchange(x, y);
        printf("x = %d, y = %d\n", x, y);
        return 0;
    }

    void interchange(int u, int v)
    {
        int temp = u;

        u = v;
        v = temp;
    }
    ```

    输出：

    ```text
    x = 5, y = 10
    ```

!!! note "说明"

    - C 的参数传递都是按值传递
    - 形参得到实参的副本，修改副本不影响原变量
    - 传地址也是传值，复制的是地址
    - 地址副本指向原变量，通过 `*` 才能改写原变量
    - 普通变量以值为基本量，指针变量以地址为基本量
    - 编译器为每次函数调用建立独立的变量组

    ![图9.6 变量的名称，地址和值](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00054.jpg)

!!! warning "常见错误"

    - 认为把变量名传给函数就能在函数内改写它
    - 把按值传递与按引用传递混为一谈，C 没有引用参数
    - 交换函数只交换形参后以为主调变量已改变

## 多源文件编译

!!! abstract "语法形式"

    ```c
    gcc file1.c file2.c       /* 编译并链接, 生成可执行文件 */
    gcc -c file1.c            /* 只生成目标文件 file1.o */
    gcc file1.c file2.o       /* 编译 file1.c 并链接 file2.o */
    ```

!!! example "示例"

    ```c
    /* main.c */
    #include <stdio.h>
    int imin(int, int);       /* 使用函数前需要原型 */

    int main(void)
    {
        printf("%d\n", imin(8, 3));
        return 0;
    }
    ```

    ```c
    /* imin.c */
    int imin(int n, int m)
    {
        return n < m ? n : m;
    }
    ```

    输出：

    ```text
    3
    ```

!!! note "说明"

    - 每个 `.c` 文件单独编译成目标文件，再链接成可执行文件
    - 改动一个源文件时，只需重新编译该文件再链接
    - 各文件独立编译，使用函数的文件必须能看到原型
    - IDE 中要把所有源文件加入同一个项目
    - 编译命令只列 `.c` 文件，头文件由 `#include` 引入
    - `make` 可自动判断哪些文件需要重新编译

!!! warning "常见错误"

    - 多个源文件定义同名函数，链接时报重复定义
    - 在 `main.c` 中漏写 `imin` 的原型
    - 只编译改动过的 `.c` 文件，忘记重新链接

## 头文件组织

!!! abstract "语法形式"

    ```c
    #include "文件名.h"    /* 先在当前目录查找 */
    #include <文件名.h>    /* 在系统目录查找 */
    ```

!!! example "示例"

    ```c
    /* hotel.h */
    #ifndef HOTEL_H
    #define HOTEL_H

    #define QUIT 5
    #define HOTEL1 180.00

    int menu(void);
    void showprice(double rate, int nights);

    #endif
    ```

    ```c
    /* usehotel.c */
    #include <stdio.h>
    #include "hotel.h"       /* 引入符号常量与原型 */

    int main(void)
    {
        if (menu() == QUIT)
            printf("bye\n");
        showprice(HOTEL1, 2);
        return 0;
    }
    ```

!!! note "说明"

    - 头文件放函数原型与 `#define` 符号常量
    - 源文件用 `#include "hotel.h"` 引入自定义头文件
    - 双引号表示先查当前目录，尖括号表示查系统目录
    - 头文件被多个文件包含时，用包含守卫防止重复定义
    - 修改头文件中的常量后，所有包含它的文件同时生效
    - 头文件只放声明，函数体放在 `.c` 文件中

!!! warning "常见错误"

    - 在头文件中定义函数体，被多个文件包含后重复定义
    - 把自定义头文件写成 `#include <hotel.h>`，找不到文件
    - 修改头文件后忘记重新编译依赖它的源文件

## 复习题

（1）实际参数和形式参数的区别是什么？

??? note "答案"

    形式参数是定义在被调函数中的变量。 实际参数是出现在函数调用中的值，该值被拷贝给形式参数

（2）根据下面各函数的描述，分别编写它们的 ANSI C 函数头，只需写出函数头
a. `donut()` 接受一个 `int` 类型的参数，打印参数指定数目的 `0`
b. `gear()` 接受两个 `int` 类型的参数，返回 `int` 类型的值
c. `guess()` 不接受参数，返回一个 `int` 类型的值
d. `stuff_it()` 接受一个 `double` 类型的值和一个 `double` 变量的地址
把第 1 个值储存在指定位置

??? note "答案"

    - a. `void donut(int n)`
    - b. `int gear(int t1, int t2)`
    - c. `int guess(void)`
    - d. `void stuff_it(double d, double *pd)`

（3）根据下面各函数的描述，分别编写它们的 ANSI C 函数头，只需写出函数头
a. `n_to_char()` 接受一个 `int` 类型的参数，返回一个 `char` 类型的值
b. `digit()` 接受一个 `double` 类型的参数和一个 `int` 类型的参数
返回 `int` 类型的值
c. `which()` 接受两个可储存 `double` 类型变量的地址，返回一个 `double` 类型的地址
d. `random()` 不接受参数，返回一个 `int` 类型的值

??? note "答案"

    - a. `char n_to_char(int n)`
    - b. `int digits(double x, int n)`
    - c. `double * which(double * p1, double * p2)`
    - d. `int random(void)`

（4）设计一个函数，返回两整数之和

??? note "答案"

    ```c
    int sum(int a, int b)
    {
        return a + b;
    }
    ```

（5）如果把复习题 4 改成返回两个 `double` 类型的值之和，应如何修改函数？

??? note "答案"

    把类型换成 `double`

    ```c
    double sum(double a, double b)
    {
        return a + b;
    }
    ```

（6）设计一个名为 `alter()` 的函数，接受两个 `int` 类型的变量 `x` 和 `y`
把它们的值分别改成两变量之和以及两变量之差

??? note "答案"

    该函数要使用指针

    ```c
    void alter(int *pa, int *pb)
    {
        int temp;

        temp = *pa + *pb;
        *pb = *pa - *pb;
        *pa = temp;
    }
    ```

（7）下面的函数定义是否正确？
```c
void salami(num)
{
    int num, count;
    for (count = 1; count <= num; num++)
        printf(" O salami mio!\n");
}
```

??? note "答案"

    不正确。 `num` 应声明在 `salami()` 的参数列表中
    而不是声明在函数体中。 另外，把 `num++` 改成 `count++`

（8）编写一个函数，返回 3 个整数参数中的最大值

??? note "答案"

    ```c
    int largest(int a, int b, int c)
    {
        int max = a;

        if (b > max)
            max = b;
        if (c > max)
            max = c;
        return max;
    }
    ```

（9）给定下面的输出
```
Please choose one of the following:
1) copy files           2) move files
3) remove files         4) quit
Enter the number of your choice:
```
a. 编写一个函数，显示一份有 4 个选项的菜单，提示用户进行选择，输出如上所示
b. 编写一个函数，接受两个 `int` 类型的参数分别表示上限和下限
该函数从用户的输入中读取整数
如果整数超出规定上下限，函数再次打印菜单，提示用户输入
然后获取一个新值
如果用户输入的整数在规定范围内，该函数把该整数返回主调函数
如果用户输入一个非整数字符，该函数返回 `4`
c. 使用本题 a 和 b 部分的函数编写一个最小型的程序
程序不需要实现菜单中各选项的功能
只需显示这些选项并获取有效的响应

??? note "答案"

    ```c
    #include <stdio.h>
    void showmenu(void);
    int getchoice(int, int);

    int main(void)
    {
        int res;

        showmenu();
        while ((res = getchoice(1, 4)) != 4)
        {
            printf("I like choice %d.\n", res);
            showmenu();
        }
        printf("Bye!\n");
        return 0;
    }

    void showmenu(void)
    {
        printf("Please choose one of the following:\n");
        printf("1) copy files           2) move files\n");
        printf("3) remove files         4) quit\n");
        printf("Enter the number of your choice:\n");
    }

    int getchoice(int low, int high)
    {
        int ans;
        int good;

        good = scanf("%d", &ans);
        while (good == 1 && (ans < low || ans > high))
        {
            printf("%d is not a valid choice; try again\n", ans);
            showmenu();
            scanf("%d", &ans);
        }
        if (good != 1)
        {
            printf("Non-numeric input. ");
            ans = 4;
        }
        return ans;
    }
    ```

## 编程练习

!!! question "编程练习"

    1. 设计一个函数 `min(x, y)`，返回两个 `double` 类型值的较小值
    在一个简单的驱动程序中测试该函数

    2. 设计一个函数 `chline(ch, i, j)`，打印指定的字符 `j` 行 `i` 列
    在一个简单的驱动程序中测试该函数

    3. 编写一个函数，接受 3 个参数： 一个字符和两个整数
    字符参数是待打印的字符
    第 1 个整数指定一行中打印字符的次数
    第 2 个整数指定打印字符的行数
    编写一个调用该函数的程序

    4. 两数的调和平均数这样计算： 先得到两数的倒数
    然后计算两个倒数的平均值，最后取计算结果的倒数
    编写一个函数，接受两个 `double` 类型的参数
    返回这两个参数的调和平均数

    5. 编写并测试一个函数 `larger_of()`
    该函数把两个 `double` 类型变量的值替换为较大的值
    例如，`larger_of(x, y)` 会把 `x` 和 `y` 中较大的值重新赋给两个变量

    6. 编写并测试一个函数，该函数以 3 个 `double` 变量的地址作为参数
    把最小值放入第 1 个变量，中间值放入第 2 个变量
    最大值放入第 3 个变量

    7. 编写一个函数，从标准输入中读取字符，直到遇到文件结尾
    程序要报告每个字符是否是字母
    如果是，还要报告该字母在字母表中的数值位置
    例如，`c` 和 `C` 在字母表中的位置都是 3
    合并一个函数，以一个字符作为参数
    如果该字符是一个字母则返回一个数值位置，否则返回 `-1`

    8. 第 6 章的程序清单 6.20 中，`power()` 函数返回一个 `double` 类型数的正整数次幂
    改进该函数，使其能正确计算负幂
    另外，函数要处理 0 的任何次幂都为 0，任何数的 0 次幂都为 1
    函数应报告 0 的 0 次幂未定义，因此把该值处理为 1
    要使用一个循环，并在程序中测试该函数

    9. 使用递归函数重写编程练习 8

    10. 为了让程序清单 9.8 中的 `to_binary()` 函数更通用
    编写一个 `to_base_n()` 函数接受两个参数
    且第二个参数在 2 到 10 范围内
    然后以第 2 个参数中指定的进制打印第 1 个参数的数值
    例如，`to_base_n(129, 8)` 显示的结果为 `201`，也就是 129 的八进制数
    在一个完整的程序中测试该函数

    11. 编写并测试 `Fibonacci()` 函数，该函数用循环代替递归计算斐波那契数
