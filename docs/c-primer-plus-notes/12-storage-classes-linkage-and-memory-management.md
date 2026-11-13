# 第12章 存储类别、链接和内存管理

## 块作用域

!!! abstract "语法形式"

    ```c
    {
        类型 变量名;   /* 可见范围到块末尾 */
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int x = 30;
        {
            int x = 77;   /* 内层新变量, 隐藏外层 x */
            printf("inner: %d\n", x);
        }
        printf("outer: %d\n", x);
        return 0;
    }
    ```

    输出：

    ```text
    inner: 77
    outer: 30
    ```

!!! note "说明"

    - 块由一对花括号围成，函数体与复合语句都是块
    - 块作用域从定义处开始，到所在块末尾结束
    - 函数形参也具有块作用域，属于函数体这个块
    - 内层块的同名变量隐藏外层变量，离开后外层恢复可见
    - C99 起可以在块中任意位置声明变量
    - for，while，if 控制的语句即使没有花括号也算块

!!! warning "常见错误"

    - 以为内层赋值会改变外层同名变量
    - 在定义之前使用块内变量

## 函数作用域

!!! abstract "语法形式"

    ```c
    标签名:
    goto 标签名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int i = 0;
        goto done;           /* 跳入内层块 */
        {
            done:            /* 标签作用域是整个函数 */
            printf("i = %d\n", i);
        }
        return 0;
    }
    ```

    输出：

    ```text
    i = 0
    ```

!!! note "说明"

    - 函数作用域只用于 goto 语句的标签
    - 标签即使定义在内层块，作用域也延伸到整个函数
    - 同一函数内不能有两个同名标签

!!! warning "常见错误"

    - 以为内层块的标签只在该块内有效
    - 在两个块中使用同一标签名

## 函数原型作用域

!!! abstract "语法形式"

    ```c
    返回类型 函数名(类型 形参名, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int mighty(int mouse, double large);
    int main(void)
    {
        printf("%d\n", mighty(3, 4.0));
        return 0;
    }
    int mighty(int a, double b)   /* 形参名不必相同 */
    {
        return (int)(a + b);
    }
    ```

    输出：

    ```text
    7
    ```

!!! note "说明"

    - 范围从形参定义处到原型声明结束
    - 编译器只关心形参类型，形参名可以省略
    - 原型中的形参名不必与函数定义中的一致
    - 变长数组形参例外，方括号中的名字必须已声明

!!! warning "常见错误"

    - 以为原型中的形参名会与定义中的形参名绑定

## 文件作用域

!!! abstract "语法形式"

    ```c
    类型 变量名;   /* 写在所有函数之外 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int units = 0;          /* 文件作用域 */
    void add(void);
    int main(void)
    {
        add();
        printf("%d\n", units);
        return 0;
    }
    void add(void)
    {
        units++;
    }
    ```

    输出：

    ```text
    1
    ```

!!! note "说明"

    - 从定义处到文件末尾可见
    - 可用于多个函数，也称全局变量
    - 实际可见范围是整个翻译单元，含所包含的头文件
    - 文件作用域变量具有静态存储期

!!! warning "常见错误"

    - 以为在函数之间共享数据就必须传参
    - 把定义写在文件末尾，却在前面使用

## 链接属性

!!! abstract "语法形式"

    表12-1 三种链接属性

    | 链接 | 可见范围 | 典型声明 |
    | --- | --- | --- |
    | 外部链接 | 程序的所有翻译单元 | 函数外的 `int x;` |
    | 内部链接 | 本翻译单元 | 函数外的 `static int x;` |
    | 无链接 | 定义所在的块或函数 | 块内变量，形参 |

!!! note "说明"

    - 块作用域，函数作用域，函数原型作用域的变量都无链接
    - 文件作用域变量可以是外部链接或内部链接
    - 外部链接的变量可在多文件程序中使用
    - 内部链接的变量只用于一个翻译单元
    - 函数外的 `static` 决定链接属性，不决定存储期

## 存储期

!!! abstract "语法形式"

    表12-2 四种存储期

    | 存储期 | 存在时间 | 典型对象 |
    | --- | --- | --- |
    | 静态 | 程序执行期间 | 文件作用域变量，块内 static |
    | 线程 | 线程开始到线程结束 | `_Thread_local` 变量 |
    | 自动 | 进入块到离开块 | 块内普通变量，形参 |
    | 动态分配 | `malloc()` 到 `free()` | 堆上的内存块 |

!!! note "说明"

    - 存储期描述对象，作用域和链接描述标识符
    - 文件作用域变量无论内部还是外部链接都有静态存储期
    - 块作用域变量默认自动存储期，加 `static` 改为静态
    - 变长数组的存储期从声明处到块末尾
    - `_Thread_local` 声明时每个线程各有一份副本

## 五种存储类别

!!! abstract "语法形式"

    表12-3 五种存储类别

    | 存储类别 | 存储期 | 作用域 | 链接 | 声明方式 |
    | --- | --- | --- | --- | --- |
    | 自动 | 自动 | 块 | 无 | 块内 |
    | 寄存器 | 自动 | 块 | 无 | 块内加 `register` |
    | 静态外部链接 | 静态 | 文件 | 外部 | 所有函数外 |
    | 静态内部链接 | 静态 | 文件 | 内部 | 函数外加 `static` |
    | 静态无链接 | 静态 | 块 | 无 | 块内加 `static` |

!!! note "说明"

    - 自动变量是默认类别，其余类别都要显式声明
    - 静态变量在程序载入时创建，未初始化则置 `0`
    - 自动变量未初始化时值不确定
    - 寄存器变量只是请求，编译器可以忽略
    - 线程存储期用于并发程序，本章不展开

## auto 说明符

!!! abstract "语法形式"

    ```c
    auto 类型 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int units = 5;          /* 外部变量 */
    int main(void)
    {
        {
            auto int units = 9;  /* 显式声明为自动 */
            printf("inner: %d\n", units);
        }
        printf("outer: %d\n", units);
        return 0;
    }
    ```

    输出：

    ```text
    inner: 9
    outer: 5
    ```

!!! note "说明"

    - `auto` 只能用于块作用域的变量声明
    - 块内变量默认就是自动类别，写出 `auto` 只为表明意图
    - 用于覆盖同名的外部变量时，意图更清楚
    - C++ 中 `auto` 是类型推导，含义不同

!!! warning "常见错误"

    - 在函数外使用 `auto`
    - 在 C/C++ 兼容代码中用 `auto` 作存储类别

## 自动变量的初始化

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int repid;              /* 未初始化, 值不确定 */
        int tents = 5;
        int ruth = 1;
        int rance = 5 * ruth;   /* 可用非常量表达式 */
        printf("%d %d\n", tents, rance);
        return 0;
    }
    ```

    输出：

    ```text
    5 5
    ```

!!! note "说明"

    - 自动变量只在显式初始化时赋值
    - 未初始化的自动变量保留该内存原有的位组合
    - 初始化表达式可以引用前面已定义的变量
    - 每次进入块都会重新初始化

!!! warning "常见错误"

    - 以为局部变量默认初始化为 `0`
    - 依赖未初始化变量的值

## register 说明符

!!! abstract "语法形式"

    ```c
    register 类型 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        register int i;
        int sum = 0;
        for (i = 0; i < 5; i++)
            sum += i;
        printf("%d\n", sum);
        return 0;
    }
    ```

    输出：

    ```text
    10
    ```

!!! note "说明"

    - 请求把变量存放在 CPU 寄存器或最快的可用内存
    - 存储期，作用域，链接与自动变量相同
    - 编译器可以忽略请求，此时变量等同于普通自动变量
    - 无论是否被忽略，都不能对 register 变量取地址
    - 函数形参也可用 `register` 声明

!!! warning "常见错误"

    - 对 register 变量写 `&i`
    - 认为 register 一定能提高速度

## 块作用域的静态变量

!!! abstract "语法形式"

    ```c
    static 类型 变量名 = 初值;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void trystat(void);
    int main(void)
    {
        int count;
        for (count = 1; count <= 3; count++)
            trystat();
        return 0;
    }
    void trystat(void)
    {
        int fade = 1;
        static int stay = 1;   /* 只初始化一次 */
        printf("fade = %d, stay = %d\n", fade++, stay++);
    }
    ```

    输出：

    ```text
    fade = 1, stay = 1
    fade = 1, stay = 2
    fade = 1, stay = 3
    ```

!!! note "说明"

    - 具有块作用域，无链接，静态存储期
    - 静态变量的初始化在程序载入时完成，不在运行时执行
    - 多次调用之间保留上一次的值
    - 未显式初始化时置为 `0`
    - 函数外看不到该变量，只能通过所在函数访问

!!! warning "常见错误"

    - 在形参声明中使用 `static`
    - 以为每次调用都会重新把静态变量置为初值

## extern 声明外部变量

!!! abstract "语法形式"

    ```c
    extern 类型 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int units = 0;          /* 定义式声明 */
    void critic(void);
    int main(void)
    {
        extern int units;   /* 引用式声明, 可省略 */
        units = 56;
        critic();
        return 0;
    }
    void critic(void)
    {
        printf("%d\n", units);   /* 直接用外部变量 */
    }
    ```

    输出：

    ```text
    56
    ```

!!! note "说明"

    - 外部变量定义在所有函数之外，文件作用域，外部链接
    - 函数内使用 `extern` 表明引用的是别处定义的变量
    - 外部变量具有静态存储期，各函数共享同一个对象
    - 同一文件中外部变量从定义处起对后面的函数可见
    - 与外部变量同名的局部变量会隐藏外部变量

!!! warning "常见错误"

    - 在函数内写 `int units;`，创建了同名自动变量
    - 在另一文件中对已定义的变量再次写定义式声明

## 外部变量的初始化

!!! example "示例"

    ```c
    #include <stdio.h>
    int x = 10;              /* 常量表达式 */
    int y = 3 + 20;
    size_t z = sizeof(int);
    int w;                   /* 未初始化, 置 0 */
    int main(void)
    {
        printf("%d %d %zu %d\n", x, y, z, w);
        return 0;
    }
    ```

    输出：

    ```text
    10 23 4 0
    ```

!!! note "说明"

    - 未初始化的外部变量置为 `0`，数组元素同样
    - 只能用常量表达式初始化文件作用域变量
    - `sizeof` 表达式在非变长数组时算常量表达式
    - 初始化在程序载入时完成，只做一次

!!! warning "常见错误"

    - 写成 `int x2 = 2 * x;`，用变量初始化

## 定义式声明与引用式声明

!!! abstract "语法形式"

    ```c
    类型 变量名 = 初值;   /* 定义式, 分配空间 */
    extern 类型 变量名;   /* 引用式, 不分配空间 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int tern = 1;           /* 定义式声明 */
    int main(void)
    {
        extern int tern;    /* 引用式声明 */
        printf("%d\n", tern);
        return 0;
    }
    ```

    输出：

    ```text
    1
    ```

!!! note "说明"

    - 定义式声明为变量分配存储空间，一个变量只能有一个
    - 引用式声明告诉编译器变量定义在别处，可以有多个
    - 只有定义式声明能够初始化变量
    - 外部变量只能初始化一次，且在定义处进行
    - 文件作用域中带初始化的 extern 声明仍构成定义

!!! warning "常见错误"

    - 两个文件都写定义式声明，链接时报重复定义
    - 在头文件中写入不带 `extern` 的变量定义

## static 在函数内外的含义

!!! abstract "语法形式"

    表12-4 static 的两种作用

    | 位置 | 决定 | 不决定 |
    | --- | --- | --- |
    | 所有函数之外 | 内部链接 | 存储期，本就是静态 |
    | 函数或块之内 | 静态存储期 | 链接，本就无链接 |

!!! example "示例"

    ```c
    #include <stdio.h>
    static int stayhome = 3;   /* 内部链接 */
    void show(void);
    int main(void)
    {
        show();
        printf("%d\n", stayhome);
        return 0;
    }
    void show(void)
    {
        static int ct = 0;     /* 静态存储期 */
        printf("%d\n", ++ct);
    }
    ```

    输出：

    ```text
    1
    3
    ```

!!! note "说明"

    - 函数外： 文件作用域，内部链接，静态存储期
    - 函数内： 块作用域，无链接，静态存储期
    - 两种情况下变量都存续到程序结束，都只初始化一次
    - 内部链接的静态变量只用于本翻译单元
    - 块内静态变量只能通过所在块访问

## 多文件共享外部变量

!!! example "示例"

    ```c
    /* parta.c */
    #include <stdio.h>
    int count = 0;             /* 定义 */
    void accumulate(void);
    int main(void)
    {
        count = 2;
        accumulate();
        return 0;
    }
    ```

    ```c
    /* partb.c, 与 parta.c 一起编译 */
    #include <stdio.h>
    extern int count;          /* 引用 */
    static int total = 0;      /* 本文件私有 */
    void accumulate(void)
    {
        total += count;
        printf("%d\n", total);
    }
    ```

    输出：

    ```text
    2
    ```

!!! note "说明"

    - 在一个文件中定义，其他文件用 `extern` 声明
    - 只有定义式声明能够初始化变量
    - 其他文件在使用前必须先有 `extern` 声明
    - 编译命令： `gcc parta.c partb.c`

!!! warning "常见错误"

    - 两个文件都写 `int count = 0;`
    - 头文件中直接定义变量，又被多个文件包含

## 静态函数

!!! abstract "语法形式"

    ```c
    static 返回类型 函数名(形参列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    static int twice(int x)   /* 只在本文件可见 */
    {
        return 2 * x;
    }
    int main(void)
    {
        printf("%d\n", twice(21));
        return 0;
    }
    ```

    输出：

    ```text
    42
    ```

!!! note "说明"

    - 函数默认具有外部链接，其他文件可以调用
    - 加 `static` 后只在本文件可见，属于模块私有
    - 其他文件可以定义同名函数，不会冲突
    - 声明其他文件中的函数常用 `extern`，该关键字可省略

## rand() 与 srand()

!!! abstract "语法形式"

    ```c
    #include <stdlib.h>
    int rand(void);
    void srand(unsigned int seed);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    int main(void)
    {
        int i;
        srand((unsigned int) time(0));   /* 用时间做种子 */
        for (i = 0; i < 3; i++)
            printf("%d\n", rand());
        return 0;
    }
    ```

!!! note "说明"

    - `rand()` 返回 `0` 到 `RAND_MAX` 之间的伪随机整数
    - 序列由种子决定，相同的种子产生相同的序列
    - 不调用 `srand()` 时，种子默认为 `1`
    - `srand()` 的参数类型是 `unsigned int`，`time()` 的返回值需强制转换
    - 种子应在程序开头设置一次，不要放在循环内

!!! warning "常见错误"

    - 在循环内反复调用 `srand()`，得到重复序列
    - 以为 `rand()` 返回真正的随机数

## 生成指定范围的随机数

!!! abstract "语法形式"

    ```c
    rand() % 范围 + 起点;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    int rollem(int sides)
    {
        return rand() % sides + 1;
    }
    int main(void)
    {
        srand((unsigned int) time(0));
        printf("%d\n", rollem(6));   /* 掷一次六面骰 */
        return 0;
    }
    ```

    输出：

    ```text
    1 到 6 之间的一个整数
    ```

!!! note "说明"

    - `rand() % n` 得 `0` 到 `n-1`，加 `1` 得 `1` 到 `n`
    - 把面数写成参数，便于支持不同面数的骰子
    - 模运算会使各结果的出现次数略有偏差

!!! warning "常见错误"

    - 写成 `rand() % sides` 得到 `0` 到 `sides-1`
    - 对负数范围直接取模

## malloc() 与 free()

!!! abstract "语法形式"

    ```c
    #include <stdlib.h>
    void *malloc(size_t size);
    void free(void *ptr);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        double * ptd;
        ptd = (double *) malloc(3 * sizeof(double));
        if (ptd == NULL)          /* 分配失败 */
        {
            puts("allocation failed");
            exit(EXIT_FAILURE);
        }
        ptd[0] = 1.5;
        ptd[1] = 2.5;
        ptd[2] = ptd[0] + ptd[1];
        printf("%.1f\n", ptd[2]);
        free(ptd);                /* 归还内存 */
        return 0;
    }
    ```

    输出：

    ```text
    4.0
    ```

!!! note "说明"

    - `malloc()` 的参数是所需字节数，返回块首地址
    - 返回类型为 `void *`，通常强制转换为目标指针类型
    - 分配的内存匿名，只能通过指针访问
    - 分配失败返回空指针，使用前应检查
    - `free()` 的参数必须是 `malloc()` 或 `calloc()` 返回的地址
    - 动态分配内存的存储期从 `malloc()` 到 `free()`

!!! warning "常见错误"

    - 不检查 `ptd == NULL` 就直接使用
    - `free()` 同一块内存两次
    - 用 `free()` 释放数组或普通变量的地址

## 动态数组

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        int n = 5;
        int i;
        int * ar = (int *) malloc(n * sizeof(int));
        if (ar == NULL)
            exit(EXIT_FAILURE);
        for (i = 0; i < n; i++)
            ar[i] = i * i;
        for (i = 0; i < n; i++)
            printf("%d ", ar[i]);
        putchar('\n');
        free(ar);
        return 0;
    }
    ```

    输出：

    ```text
    0 1 4 9 16
    ```

!!! note "说明"

    - 指针可像数组名一样用下标访问
    - 元素个数 `n` 可以在运行时确定
    - 比变长数组灵活，数组可跨函数使用
    - 指针本身可以是静态的或自动的，指向的内存来自堆

## 内存泄漏

!!! example "示例"

    ```c
    #include <stdlib.h>
    void gobble(int n)
    {
        double * temp = malloc(n * sizeof(double));
        /* 遗漏 free(temp), 内存块无法再访问 */
    }
    int main(void)
    {
        int i;
        for (i = 0; i < 1000; i++)
            gobble(2000);
        return 0;
    }
    ```

!!! note "说明"

    - 指针 `temp` 是自动变量，函数返回后消失
    - 它指向的堆内存不会随指针消失而释放
    - 循环累积，占用的内存只增不减
    - 每次 `malloc()` 都应有对应的 `free()`

!!! warning "常见错误"

    - 函数返回前遗漏 `free()`
    - `free()` 后继续通过原指针访问内存
    - 丢失指向已分配内存的唯一指针

## calloc()

!!! abstract "语法形式"

    ```c
    #include <stdlib.h>
    void *calloc(size_t n, size_t size);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        int i;
        int * ar = (int *) calloc(5, sizeof(int));
        if (ar == NULL)
            exit(EXIT_FAILURE);
        for (i = 0; i < 5; i++)
            printf("%d ", ar[i]);   /* 全部为 0 */
        putchar('\n');
        free(ar);
        return 0;
    }
    ```

    输出：

    ```text
    0 0 0 0 0
    ```

!!! note "说明"

    - 参数为元素个数与单个元素大小，以字节计
    - 分配后把整块内存的所有位清零
    - 返回值同样需要检查是否为空指针
    - 用 `free()` 释放
    - 元素大小写成 `sizeof(类型)`，便于移植

## 动态分配二维数组

!!! abstract "语法形式"

    ```c
    类型 (*指针名)[列数];
    指针名 = (类型 (*)[列数]) malloc(行数 * 列数 * sizeof(类型));
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        int n = 3;
        int i, j;
        int (*p2)[4];
        p2 = (int (*)[4]) malloc(n * 4 * sizeof(int));
        for (i = 0; i < n; i++)
            for (j = 0; j < 4; j++)
                p2[i][j] = i + j;
        printf("%d\n", p2[2][3]);
        free(p2);
        return 0;
    }
    ```

    输出：

    ```text
    5
    ```

!!! note "说明"

    - `int (*p2)[4]` 表示 `p2` 指向含 4 个 `int` 的数组
    - `p2[i]` 是一行，`p2[i][j]` 是一个元素
    - 列数固定时用这种写法，语法比指针数组简单
    - 列数在运行时确定时，可写 `int (*p3)[m]`，需 C99
    - 变长数组由系统自动释放，`malloc()` 数组需手动 `free()`

## const 限定变量

!!! abstract "语法形式"

    ```c
    const 类型 变量名 = 初值;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        const int nochange = 12;      /* 只读 */
        const int days[3] = {31, 28, 31};
        printf("%d %d\n", nochange, days[2]);
        /* nochange = 13;   编译错误 */
        return 0;
    }
    ```

    输出：

    ```text
    12 31
    ```

!!! note "说明"

    - `const` 对象只能初始化，不能赋值，递增或递减
    - 可以用 `const` 创建不允许修改的数组
    - C99 起限定符是幂等的，重复书写多余的会被忽略
    - `const` 数据适合作为全局数据共享

!!! warning "常见错误"

    - 声明时不给初值，之后又想赋值
    - 以为 `const` 变量在运行时仍可修改

## const 与指针的位置

!!! abstract "语法形式"

    ```c
    const 类型 * p;             /* 指向的值只读 */
    类型 * const p = 地址;      /* 指针本身只读 */
    const 类型 * const p = 地址;  /* 两者都只读 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a = 1, b = 2;
        const int * p = &a;   /* 指向的值只读 */
        int * const q = &a;   /* 指针本身只读 */
        p = &b;               /* 合法 */
        *q = 3;               /* 合法 */
        printf("%d %d\n", *p, a);
        return 0;
    }
    ```

    输出：

    ```text
    2 3
    ```

!!! note "说明"

    - `const` 在 `*` 左侧，限定指针指向的数据
    - `const` 在 `*` 右侧，限定指针本身
    - 两侧都有，指针与所指数据都不能改
    - `float const * pfc` 与 `const float * pfc` 等价
    - const 指针必须在声明时初始化

!!! warning "常见错误"

    - `const int *p; *p = 5;` 修改只读数据
    - `int * const q;` 未初始化，之后无法赋值

## const 形参

!!! abstract "语法形式"

    ```c
    void 函数名(const 类型 数组名[], int n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void display(const int array[], int limit)
    {
        int i;
        for (i = 0; i < limit; i++)
            printf("%d ", array[i]);
        putchar('\n');
    }
    int main(void)
    {
        int data[3] = {3, 1, 4};
        display(data, 3);
        return 0;
    }
    ```

    输出：

    ```text
    3 1 4
    ```

!!! note "说明"

    - `const int array[]` 与 `const int *array` 等价
    - 数组名传参传的是地址，`const` 保证函数不改数据
    - 仅读取数据时加 `const`，需要修改时不加
    - 标准库 `strcat()` 第 2 个参数带 `const`，第 1 个不带

## 文件间共享 const 数据

!!! example "示例"

    ```c
    /* constant.h */
    static const double PI = 3.14159;
    ```

    ```c
    /* main.c */
    #include <stdio.h>
    #include "constant.h"
    int main(void)
    {
        printf("%.5f\n", PI);
        return 0;
    }
    ```

    输出：

    ```text
    3.14159
    ```

!!! note "说明"

    - 头文件中用 `static` 声明，每个包含它的文件各有一份副本
    - 副本只对本文件可见，不能用于文件间通信
    - 去掉 `static` 会在多个文件中重复定义
    - 另一种做法： 一个文件定义，其他文件写 `extern const char * MONTHS[]`
    - 副本方案便于使用，但数据量大时浪费内存

    [源教材此处的引用式声明印作 `extern const * MONTHS[]`
    - 缺少 `char`，与定义的类型不符，gcc 报 implicit-int 错误
    - 上面按标准写法补全]

## volatile 限定符

!!! abstract "语法形式"

    ```c
    volatile 类型 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    volatile int loc1;      /* 可能被外部修改 */
    int main(void)
    {
        loc1 = 1;
        loc1 = 2;
        printf("%d\n", loc1);
        return 0;
    }
    ```

    输出：

    ```text
    2
    ```

!!! note "说明"

    - 告知编译器，变量的值可能由程序之外的因素改变
    - 用于硬件地址，其他程序或线程共享的数据
    - 编译器不把该值长期缓存在寄存器中，每次都重新读取
    - 语法与 `const` 相同，可与 `const` 同时使用
    - 同时使用时两个限定符的顺序不重要

!!! warning "常见错误"

    - 认为 `volatile` 能保证多线程同步
    - 把需要在中断中修改的变量漏写 `volatile`

## restrict 限定符

!!! abstract "语法形式"

    ```c
    类型 * restrict 指针名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        int i;
        int * restrict p;
        p = (int *) malloc(4 * sizeof(int));
        for (i = 0; i < 4; i++)
            p[i] = i;
        p[0] += 5;
        p[0] += 3;      /* 编译器可合并为加 8 */
        printf("%d\n", p[0]);
        free(p);
        return 0;
    }
    ```

    输出：

    ```text
    8
    ```

!!! note "说明"

    - 只能用于指针，表明它是访问该数据的唯一且初始方式
    - 告知编译器可以按数据不重叠的假设优化
    - 也常用于函数形参，如 `memcpy()` 的两个指针
    - `memmove()` 允许重叠，不使用 `restrict`
    - 编译器不检查是否满足约束，违反后结果自负

## _Atomic 限定符

!!! abstract "语法形式"

    ```c
    _Atomic 类型 变量名;
    atomic_store(&变量名, 值);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdatomic.h>
    int main(void)
    {
        _Atomic int hogs;
        atomic_store(&hogs, 12);
        printf("%d\n", atomic_load(&hogs));
        return 0;
    }
    ```

    输出：

    ```text
    12
    ```

!!! note "说明"

    - C11 新增，属于可选支持特性
    - 原子操作期间，其他线程不能访问该对象
    - 通过 `stdatomic.h` 中的宏函数访问
    - 需要编译器与库支持才能使用

## 方括号中的限定符与 static

!!! abstract "语法形式"

    ```c
    void 函数名(int a[const], int b[static 3]);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void show(int a[const], int b[static 3])
    {
        printf("%d %d\n", a[0], b[0]);
    }
    int main(void)
    {
        int x[3] = {1, 2, 3};
        show(x, x);
        return 0;
    }
    ```

    输出：

    ```text
    1 1
    ```

!!! note "说明"

    - C99 允许把 `const` 和 `restrict` 写进形参的方括号
    - `int a[const]` 等价于 `int * const a`
    - `int b[static 3]` 表示实参至少指向 3 个元素
    - 这里的 `static` 与存储类别无关，只用于优化
    - 该写法只出现在函数原型与函数头中

## 复习题

（1）哪些类别的变量可以成为它所在函数的局部变量？

??? note "答案"

    自动存储类别，寄存器存储类别，静态无链接存储类别

（2）哪些类别的变量在它所在程序的运行期一直存在？

??? note "答案"

    静态无链接存储类别，静态内部链接存储类别，静态外部链接存储类别

（3）哪些类别的变量可以被多个文件使用？ 哪些类别的变量仅限于在一个文件中使用？

??? note "答案"

    静态外部链接存储类别可以被多个文件使用
    静态内部链接存储类别只能在一个文件中使用

（4）块作用域变量具有什么链接属性？

??? note "答案"

    无链接

（5）`extern` 关键字有什么用途？

??? note "答案"

    关键字 `extern` 用于声明中，表明该变量或函数已定义在别处

（6）考虑下面两行代码，就输出的结果而言有何异同：
```c
int * p1 = (int *)malloc(100 * sizeof(int));
int * p1 = (int *)calloc(100, sizeof(int));
```

??? note "答案"

    两者都分配了一个内含 100 个 `int` 类型值的数组
    第 2 行代码使用 `calloc()` 把数组中的每个元素都设置为 `0`

（7）下面的变量对哪些函数可见？ 程序是否有误？
```c
/* 文件 1 */
int daisy;
int main(void)
{
    int lily;
    ...;
}
int petal()
{
    extern int daisy, lily;
    ...;
}
/* 文件 2 */
extern int daisy;
static int lily;
int rose;
int stem()
{
    int rose;
    ...;
}
void root()
{
    ...;
}
```

??? note "答案"

    默认情况下，`daisy` 只对 `main()` 可见
    以 `extern` 声明的 `daisy` 才对 `petal()`，`stem()` 和 `root()` 可见
    文件 2 中的 `extern int daisy;` 声明使得 `daisy` 对文件 2 中的所有函数都可见
    第 1 个 `lily` 是 `main()` 的局部变量
    `petal()` 函数中引用的 `lily` 是错误的，因为两个文件中都没有外部链接的 `lily`
    虽然文件 2 中有一个静态的 `lily`，但是它只对文件 2 可见
    外部 `rose` 对 `root()` 函数可见
    但是 `stem()` 中的局部 `rose` 覆盖了外部的 `rose`

（8）下面程序会打印什么？
```c
#include <stdio.h>
char color = 'B';
void first(void);
void second(void);
int main(void)
{
    extern char color;
    printf("color in main() is %c\n", color);
    first();
    printf("color in main() is %c\n", color);
    second();
    printf("color in main() is %c\n", color);
    return 0;
}
void first(void)
{
    char color;
    color = 'R';
    printf("color in first() is %c\n", color);
}
void second(void)
{
    color = 'G';
    printf("color in second() is %c\n", color);
}
```

??? note "答案"

    ```text
    color in main() is B
    color in first() is R
    color in main() is B
    color in second() is G
    color in main() is G
    ```

    `first()` 函数没有使用外部 `color` 变量，它使用了局部变量
    `second()` 函数使用了外部 `color` 变量

（9）假设文件的开始处有如下声明：
```c
static int plink;
int value_ct(const int arr[], int value, int n);
```
a. 以上声明表明了程序员的什么意图？

??? note "答案"

    程序将使用一个变量 `plink`，该文件包含的函数都可以使用这个变量
    `value_ct()` 函数的第 1 个参数是指向一个整数的指针
    并假定它指向内含 `n` 个元素的数组
    这里关键是要理解该程序不允许使用指针 `arr` 修改原始数组中的值

    b. 用 `const int value` 和 `const int n`
    分别替换 `int value` 和 `int n`，是否对主调程序的值加强保护？

    不会
    `value` 和 `n` 已经是原始数据的备份，所以该函数无法更改主调函数中相应的值
    这些声明的作用是防止函数修改 `value` 和 `n` 的值
    例如，如果用 `const` 限定 `n`，就不能使用 `n++` 表达式

## 编程练习

!!! question "编程练习"

    1. 不使用全局变量，重写程序清单 12.4

    2. 在美国，通常以英里/加仑计算油耗； 在欧洲，以升/100 公里计算
    程序提示用户选择计算模式 (美制或公制)，然后接收数据并计算油耗
    下面是程序的一部分：

    ```c
    // pe12-2b.c
    // 与 pe12-2a.c 一起编译
    #include <stdio.h>
    #include "pe12-2a.h"
    int main(void)
    {
        int mode;

        printf("Enter 0 for metric mode, 1 for US mode: ");
        scanf("%d", &mode);
        while (mode >= 0)
        {
            set_mode(mode);
            get_info();
            show_info();
            printf("Enter 0 for metric mode, 1 for US mode");
            printf(" (-1 to quit): ");
            scanf("%d", &mode);
        }
        printf("Done.\n");
        return 0;
    }
    ```

    输出示例

    ```text
    Enter 0 for metric mode, 1 for US mode: 0
    Enter distance traveled in kilometers: 600
    Enter fuel consumed in liters: 78.8
    Fuel consumption is 13.13 liters per 100 km.
    Enter 0 for metric mode, 1 for US mode (-1 to quit): 1
    Enter distance traveled in miles: 434
    Enter fuel consumed in gallons: 12.7
    Fuel consumption is 34.2 miles per gallon.
    ```

    如果用户输入了不正确的模式，程序给出提示消息并使用上一次输入的正确模式
    提供 `pe12-2a.h` 头文件和 `pe12-2a.c` 源文件
    源文件应定义 3 个具有文件作用域，内部链接的变量
    分别表示模式，距离和消耗的燃料
    `get_info()` 根据模式提示输入相应数据，并储存到文件作用域变量中
    `show_info()` 根据设置的模式计算并显示油耗
    可以假设用户输入的都是数值数据

    3. 重新设计编程练习 2，要求只使用自动变量
    用户界面不变，即提示用户输入模式等，但函数调用要作相应变化

    4. 在一个循环中编写并测试一个函数，该函数返回它被调用的次数

    5. 编写一个程序，生成 100 个 1 到 10 范围内的随机数，并以降序排列
    可以把第 11 章的排序算法稍加改动，用于整数排序

    6. 编写一个程序，生成 1000 个 1 到 10 范围内的随机数
    不用保存或打印这些数字，仅打印每个数出现的次数
    用 10 个不同的种子值运行，生成的数字出现次数是否相同？
    可以使用本章自定义的函数或 ANSI C 的 `rand()` 和 `srand()`
    这是测试特定随机数生成器随机性的方法

    7. 修改程序清单 12.13，使其输出类似：

    ```text
    Enter the number of sets; enter q to stop : 18
    How many sides and how many dice? 6 3
    Here are 18 sets of 3 6-sided throws.
      12 10 6 9 8 14 8 15 9 14 12 17 11 7 10
      13 8 14
    How many sets? Enter q to stop: q
    ```

    8. 下面是程序的一部分：

    ```c
    // pe12-8.c
    #include <stdio.h>
    int * make_array(int elem, int val);
    void show_array(const int ar [], int n);
    int main(void)
    {
        int * pa;
        int size;
        int value;

        printf("Enter the number of elements: ");
        while (scanf("%d", &size) == 1 && size > 0)
        {
            printf("Enter the initialization value: ");
            scanf("%d", &value);
            pa = make_array(size, value);
            if (pa)
            {
                show_array(pa, size);
                free(pa);
            }
            printf("Enter the number of elements"
                   " (<1 to quit): ");
        }
        printf("Done.\n");
        return 0;
    }
    ```

    提供 `make_array()` 和 `show_array()` 函数的定义，完成该程序
    `make_array()` 接受两个参数，第 1 个是数组的元素个数，第 2 个是赋给每个元素的值
    该函数调用 `malloc()` 创建一个大小合适的数组
    把每个元素设为指定的值，并返回指向该数组的指针
    `show_array()` 显示数组的内容，一行显示 8 个数

    9. 编写一个符合以下描述的函数
    先询问用户需要输入多少个单词，然后接收单词并显示出来
    用 `malloc()` 按单词个数创建一个动态数组
    数组的每个元素都是指向 `char` 的指针
    因此用于储存 `malloc()` 返回值的指针是一个指向指针的指针
    读入单词时先把单词读进一个临时 `char` 数组
    再用 `malloc()` 分配刚好容纳该单词的空间
    把地址存入指针数组，并从临时数组把单词拷贝过去
    运行示例如下：

    ```text
    How many words do you wish to enter? 5
    Enter 5 words now:
    I enjoyed doing this exercise
    Here are your words:
    I
    enjoyed
    doing
    this
    exercise
    ```
