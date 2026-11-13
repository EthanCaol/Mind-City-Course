# 第10章 数组和指针

## 一维数组的声明

!!! abstract "语法形式"

    ```c
    类型 数组名[元素个数];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define MONTHS 12
    int main(void)
    {
        int days[MONTHS];  /* 12 个 int 元素 */
        days[0] = 31;
        days[11] = 31;
        printf("%d %d\n", days[0], days[11]);
        return 0;
    }
    ```

    输出：

    ```text
    31 31
    ```

!!! note "说明"

    - 方括号中的数字是元素个数，不是最大下标
    - 元素编号从 `0` 到 `元素个数-1`
    - 元素类型可以是任意基本类型
    - 自动存储类别的数组声明只分配空间，不置初值
    - 数组大小常用符号常量表示，便于统一修改

!!! warning "常见错误"

    - 把 `days[12]` 当作第 12 个元素，它已越界
    - 以为声明后元素自动为 `0`

## 一维数组的初始化

!!! abstract "语法形式"

    ```c
    类型 数组名[元素个数] = {值1, 值2, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define MONTHS 12
    int main(void)
    {
        const int days[MONTHS] =
            {31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31};
        int i;
        for (i = 0; i < MONTHS; i++)
            printf("%d ", days[i]);
        return 0;
    }
    ```

    输出：

    ```text
    31 28 31 30 31 30 31 31 30 31 30 31
    ```

!!! note "说明"

    - 花括号内的值按顺序赋给各元素
    - 初始化列表少于元素个数时，其余元素置 `0`
    - 列表多于元素个数是编译错误
    - `const` 数组只能在声明时初始化
    - 未初始化且非静态的数组元素保留原有位组合

!!! warning "常见错误"

    - 声明之后再用花括号列表赋值
    - 把部分初始化与未初始化混为一谈

## 省略数组大小

!!! abstract "语法形式"

    ```c
    类型 数组名[] = {值1, 值2, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        const int days[] = {31, 28, 31, 30, 31, 30};
        int i;
        for (i = 0; i < sizeof days / sizeof days[0]; i++)
            printf("%d ", days[i]);
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    31 28 31 30 31 30
    ```

!!! note "说明"

    - 编译器按初始化列表的项数确定数组大小
    - `sizeof days` 是整个数组的字节数
    - `sizeof days[0]` 是单个元素的字节数
    - 两者相除得到元素个数
    - 列表项数写错时编译器不会察觉

!!! warning "常见错误"

    - 手算元素个数并与实际列表不一致
    - 在函数内对指针形参使用 `sizeof` 求元素个数

## 指定初始化器

!!! abstract "语法形式"

    ```c
    类型 数组名[元素个数] = {[下标] = 值, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define MONTHS 12
    int main(void)
    {
        int days[MONTHS] =
            {31, 28, [4] = 31, 30, 31, [1] = 29};
        int i;
        for (i = 0; i < MONTHS; i++)
            printf("%d ", days[i]);
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    31 29 0 0 31 30 31 0 0 0 0 0
    ```

!!! note "说明"

    - `[下标] = 值` 指定待初始化的元素，C99 起支持
    - 指定项之后的普通值按位置继续赋给后续元素
    - 同一元素被指定两次时，后一次覆盖前一次
    - 省略数组大小时，大小由最大下标决定
    - 未被指定的元素置 `0`

!!! warning "常见错误"

    - 把 `[4] = 31, 30, 31` 理解为三个值都赋给 `days[4]`
    - 在 C90 编译器上使用该语法
    - 下标写成负数或超出元素个数

## 数组元素赋值

!!! abstract "语法形式"

    ```c
    数组名[下标] = 值;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SIZE 5
    int main(void)
    {
        int evens[SIZE];
        int i;
        for (i = 0; i < SIZE; i++)
            evens[i] = 2 * i;
        printf("%d %d\n", evens[0], evens[4]);
        return 0;
    }
    ```

    输出：

    ```text
    0 8
    ```

!!! note "说明"

    - 声明之后只能借助下标逐个元素赋值
    - 循环是给整个数组赋值的常用方式
    - 数组名不能整体赋值给另一个数组
    - 花括号列表只能出现在声明中
    - 字符串数组有额外的初始化写法，下一章介绍

!!! warning "常见错误"

    - `yaks = oxen;` 用数组名整体赋值
    - `yaks[SIZE] = {5, 3, 2, 8};` 在声明之外使用列表
    - 以为 `yaks[SIZE]` 是最后一个元素

## 数组边界

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SIZE 4
    int main(void)
    {
        int arr[SIZE] = {1, 2, 3, 4};
        int i;
        for (i = 0; i < SIZE; i++)  /* 正确上界 */
            printf("%d ", arr[i]);
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    1 2 3 4
    ```

!!! note "说明"

    - 下标范围是 `0` 到 `SIZE-1`
    - 编译器不检查下标是否有效
    - 越界读写的结果在 C 标准中是未定义的
    - 越界可能改写相邻变量的值或导致程序异常中止
    - 声明数组时用符号常量表示大小，可减少边界错误

!!! warning "常见错误"

    - 循环条件写成 `i <= SIZE`
    - 用负下标访问数组
    - 认为越界只会读到 `0`

## 指定数组的大小

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float a1[5];
        float a2[5 * 2 + 1];
        float a3[sizeof(int) + 1];
        printf("%zu\n", sizeof a1 / sizeof a1[0]);
        return 0;
    }
    ```

    输出：

    ```text
    5
    ```

    表10-1 数组大小的合法写法

    | 声明 | 是否允许 | 说明 |
    | --- | --- | --- |
    | `float a[5];` | 允许 | 整数字面量 |
    | `float a[5 * 2 + 1];` | 允许 | 整型常量表达式 |
    | `float a[sizeof(int) + 1];` | 允许 | `sizeof` 是整型常量 |
    | `float a[-4];` | 不允许 | 必须大于 `0` |
    | `float a[0];` | 不允许 | 必须大于 `0` |
    | `float a[2.5];` | 不允许 | 必须是整数 |
    | `float a[(int) 2.5];` | 允许 | 强制转换后是整型常量 |
    | `float a[n];` | C99 起允许 | 变长数组，`n` 是变量 |

!!! note "说明"

    - C90 只允许方括号内写整型常量表达式
    - `sizeof` 表达式视为整型常量
    - 在 C90 中，`const` 变量不能作为数组大小
    - C99 允许用变量声明变长数组
    - C11 把变长数组改为可选特性

!!! warning "常见错误"

    - 用 `const` 变量作为 C90 数组大小
    - 在方括号内写浮点数
    - 数组大小写成 `0` 或负数

## 二维数组的声明与访问

!!! abstract "语法形式"

    ```c
    类型 数组名[行数][列数];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
        int i, j;
        for (i = 0; i < 2; i++, putchar('\n'))
            for (j = 0; j < 3; j++)
                printf("%d ", a[i][j]);
        return 0;
    }
    ```

    输出：

    ```text
    1 2 3
    4 5 6
    ```

!!! note "说明"

    - `float rain[5][12]` 是内含 5 个元素的数组
    - 每个元素都是内含 12 个 `float` 的数组
    - `rain[0]` 是一维数组，`rain[0][0]` 是 `float` 值
    - 元素在内存中按行连续存放
    - 嵌套循环的两个下标分别对应行与列

    ![图10.1 二维数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00055.jpg)

!!! warning "常见错误"

    - 把 `rain[5][12]` 理解为 5 列 12 行
    - 只用一个下标访问二维数组
    - 行数写成 5 却使用 `rain[5][0]`，已越界

## 二维数组的初始化

!!! abstract "语法形式"

    ```c
    类型 数组名[行数][列数] = {
        {第1行值列表},
        {第2行值列表}
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a[2][3] = {{1, 2}, {4}};
        int b[2][3] = {1, 2, 3, 4};
        printf("%d %d %d\n", a[0][2], a[1][1], a[1][2]);
        printf("%d %d %d\n", b[0][2], b[1][0], b[1][2]);
        return 0;
    }
    ```

    输出：

    ```text
    0 0 0
    3 4 0
    ```

!!! note "说明"

    - 每个内层花括号初始化一行
    - 行内值不足时，该行剩余元素置 `0`
    - 省略内层花括号时，值按行优先顺序依次填入
    - 某行的值多于列数时报错
    - 只读的二维数组用 `const` 声明

    ![图10.2 初始化二维数组的两种方法](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00056.jpg)

!!! warning "常见错误"

    - 内层花括号的个数与行数不一致
    - 认为省略内层花括号仍按行截断
    - 在一行未写满时以为下一行的值仍属于本行

## 多维数组

!!! abstract "语法形式"

    ```c
    类型 数组名[第一维][第二维][第三维];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int box[2][3][4] = {0};
        int i, j, k, sum = 0;
        for (i = 0; i < 2; i++)
            for (j = 0; j < 3; j++)
                for (k = 0; k < 4; k++)
                    sum += box[i][j][k];
        printf("%d\n", sum);
        return 0;
    }
    ```

    输出：

    ```text
    0
    ```

!!! note "说明"

    - `int box[10][20][30]` 可理解为 10 个 20×30 的二维数组
    - 也可理解为数组的数组，逐层嵌套
    - 元素总数是各维大小之积
    - 处理三维数组用三重循环，处理四维数组用四重循环
    - 除第一维外，其余维度的大小都参与地址计算

!!! warning "常见错误"

    - 把各维顺序对应成列，行，层
    - 用循环遍历时下标次序与声明次序不符

## 数组名与首元素地址

!!! abstract "语法形式"

    ```c
    数组名 == &数组名[0];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ar[3] = {10, 20, 30};
        printf("%d\n", ar == &ar[0]);
        printf("%d\n", *ar);
        printf("%d\n", *(ar + 2));
        return 0;
    }
    ```

    输出：

    ```text
    1
    10
    30
    ```

!!! note "说明"

    - 数组名表示首元素的地址
    - 数组名是地址常量，不能修改
    - 可以把数组名赋给同类型的指针变量
    - `&ar` 是整个数组的地址，类型与 `ar` 不同
    - `*ar` 等价于 `ar[0]`，即首元素的值

!!! warning "常见错误"

    - 写 `ar++` 或 `ar = p;`
    - 认为 `&ar + 1` 与 `ar + 1` 相同
    - 把数组名当作可以整体赋值的变量

## 指针算术

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        double bills[3] = {1.0, 2.0, 3.0};
        double *p = bills;
        printf("%p\n", (void *) p);
        printf("%p\n", (void *) (p + 1));
        printf("%.1f\n", *(p + 2));
        return 0;
    }
    ```

    输出：

    ```text
    0x7ffc8a2b3c40
    0x7ffc8a2b3c48
    3.0
    ```

!!! note "说明"

    - 指针加 `1` 增加一个所指向类型的大小
    - `double` 指针加 `1` 增加 8 字节
    - `short` 指针加 `1` 增加 2 字节
    - 指针的值是它所指对象的地址
    - 只知道地址不够，还必须知道所指对象的类型
    - 输出中的地址值随系统不同

    ![图10.3 数组和指针加法](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00057.jpg)

!!! warning "常见错误"

    - 以为指针加 `1` 总是增加一个字节
    - 对两个不同数组的指针做算术
    - 把地址当成普通整数直接相加

## 数组表示法与指针表示法

!!! abstract "语法形式"

    ```c
    数组名[下标] == *(数组名 + 下标);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int days[4] = {31, 28, 31, 30};
        int i;
        for (i = 0; i < 4; i++)
            printf("%d %d\n", days[i], *(days + i));
        return 0;
    }
    ```

    输出：

    ```text
    31 31
    28 28
    31 31
    30 30
    ```

!!! note "说明"

    - C 标准把 `ar[n]` 定义为 `*(ar + n)`
    - 两种写法可互换，生成的代码相同
    - `*(dates + 2)` 是第 3 个元素的值
    - `*dates + 2` 是首元素的值加 `2`
    - 只有指针变量可以写 `ar++`，数组名不行

!!! warning "常见错误"

    - 把 `*dates + 2` 当作 `*(dates + 2)`
    - 对数组名使用递增运算符

## 指针的基本操作

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int urn[5] = {100, 200, 300, 400, 500};
        int *p = urn;
        int *q = &urn[2];
        p++;
        printf("%d %d %td\n", *p, *q, q - p);
        printf("%d\n", *(urn + 4));
        return 0;
    }
    ```

    输出：

    ```text
    200 300 1
    500
    ```

    表10-2 指针的基本操作

    | 操作 | 写法 | 结果 |
    | --- | --- | --- |
    | 赋值 | `p = ar;` | `p` 指向首元素 |
    | 解引用 | `*p` | 取出所指对象的值 |
    | 取址 | `&p` | 指针变量自身的地址 |
    | 加整数 | `p + n` | 前进 `n` 个元素 |
    | 递增 | `p++` | 前进一个元素 |
    | 减整数 | `p - n` | 后退 `n` 个元素 |
    | 递减 | `p--` | 后退一个元素 |
    | 求差 | `q - p` | 相隔的元素个数 |

!!! note "说明"

    - 两个指针求差得到元素个数，不是字节数
    - 求差的两个指针应指向同一数组
    - 关系运算符可以比较同一数组中的指针
    - 指针递减后不能越过数组首元素
    - 地址的类型必须与指针类型兼容

    ![图10.4 递增指向 int 的指针](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00058.jpg)

!!! warning "常见错误"

    - 把 `q - p` 当作字节差
    - 解引用未初始化的指针
    - 比较两个不同数组的指针

## 指针作函数参数

!!! abstract "语法形式"

    ```c
    返回类型 函数名(类型 *形参, int 元素个数);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int sum(int *ar, int n)
    {
        int i, s = 0;
        for (i = 0; i < n; i++) s += ar[i];
        return s;
    }
    int main(void)
    {
        int a[4] = {1, 2, 3, 4};
        printf("%d\n", sum(a, 4));  /* 输出 10 */
    }
    ```

    输出：

    ```text
    10
    ```

!!! note "说明"

    - 数组名作实参时传递的是首元素地址
    - 函数必须另外获得元素个数
    - 函数内的 `sizeof ar` 是指针大小，不是数组大小
    - 形参可写成 `int *ar` 或 `int ar[]`
    - 原型中还可省略形参名，写成 `int sum(int *, int);`

!!! warning "常见错误"

    - 在函数内用 `sizeof ar / sizeof ar[0]` 求元素个数
    - 漏写元素个数形参
    - 把 `int ar[]` 用在函数原型之外

## 用指针区间遍历数组

!!! abstract "语法形式"

    ```c
    类型 *start, 类型 *end;
    while (start < end)
        ... *start++ ...
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int a[4] = {1, 2, 3, 4};
    int sump(int *start, int *end)
    {
        int total = 0;
        while (start < end)
            total += *start++;
        return total;
    }
    int main(void)
    {
        printf("%d\n", sump(a, a + 4));
    }
    ```

    输出：

    ```text
    10
    ```

!!! note "说明"

    - `end` 指向最后一个元素之后的第一个位置
    - 该位置的指针有效，但不能解引用
    - `a + SIZE` 是常用的结束地址写法
    - `*start++` 先取出当前值，再把指针后移
    - 循环结束时 `start` 等于 `end`

    [原书此处漏写 "不"，指向数组末尾后一位置的指针有效，但不能解引用]

!!! warning "常见错误"

    - 用 `a + SIZE` 作为结束地址并解引用
    - 误写 `a + SIZE - 1` 而漏掉最后一个元素
    - 把区间终点当作最后一个元素

## 指针与递增运算符的优先级

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int data[2] = {100, 200};
        int more[2] = {300, 400};
        int *p1 = data, *p2 = data, *p3 = more;
        printf("%d %d %d\n", *p1++, *++p2, (*p3)++);
        printf("%d %d %d\n", *p1, *p2, *p3);
        return 0;
    }
    ```

    输出：

    ```text
    100 200 300
    200 200 301
    ```

!!! note "说明"

    - 后缀 `++` 的优先级高于一元 `*`
    - 前缀 `++` 与一元 `*` 同级，从右向左结合
    - `*p1++` 等价于 `*(p1++)`，先取值再移动指针
    - `*++p2` 等价于 `*(++p2)`，先移动指针再取值
    - `(*p3)++` 递增的是所指的值，指针不动
    - `*(p1++)` 的括号写法更清楚

    [原书写作 "一元运算符 * 和 ++ 的优先级相同"，该说法不严格]

!!! warning "常见错误"

    - 把 `*p++` 读作 `(*p)++`
    - 认为 `*++p` 先取值
    - 在同一个表达式中对同一指针多次修改

## const 保护数组形参

!!! abstract "语法形式"

    ```c
    返回类型 函数名(const 类型 形参[], int 元素个数);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void show(const double ar[], int n)
    {
        for (int i = 0; i < n; i++)
            printf("%.1f ", ar[i]);
        putchar('\n');
    }
    int main(void)
    {
        double dip[3] = {1.5, 2.5, 3.5};
        show(dip, 3);
    }
    ```

    输出：

    ```text
    1.5 2.5 3.5
    ```

!!! note "说明"

    - `const` 告诉编译器函数不修改数组内容
    - 函数内写 `ar[i]++` 会产生编译错误
    - 这不要求实参数组本身是 `const`
    - 加了 `const` 的函数既能接受普通数组，也能接受 `const` 数组
    - 需要修改数组的函数不加 `const`

!!! warning "常见错误"

    - 在 `const` 形参的函数中修改元素
    - 认为 `const` 形参只能接受 `const` 数组

## 指针与 const 的组合

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        double rates[3] = {1.0, 2.0, 3.0};
        const double locked[2] = {4.0, 5.0};
        const double *pc = rates;
        pc = locked;      /* 可以改指向 */
        printf("%.1f\n", *pc);
        /* *pc = 9.0;    错误: 不能改值 */
        return 0;
    }
    ```

    输出：

    ```text
    4.0
    ```

    表10-3 const 与指针的组合

    | 声明 | 改指向 | 改值 |
    | --- | --- | --- |
    | `double *p;` | 可以 | 可以 |
    | `const double *p;` | 可以 | 不可以 |
    | `double * const p;` | 不可以 | 可以 |
    | `const double * const p;` | 不可以 | 不可以 |

!!! note "说明"

    - `const` 在 `*` 左侧表示所指的值只读
    - `const` 在 `*` 右侧表示指针本身只读
    - 非 `const` 数据的地址可以赋给两类指针
    - `const` 数据的地址只能赋给指向 `const` 的指针
    - 函数形参写成指向 `const` 的指针可接受两种实参

!!! warning "常见错误"

    - `double *p = locked;` 用普通指针指向 `const` 数组
    - 把 `const double *p` 理解为指针本身不能改
    - 通过普通指针修改 `const` 数据

## 指向二维数组的指针

!!! abstract "语法形式"

    ```c
    类型 (*指针名)[列数];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int zippo[2][3] = {{1, 2, 3}, {4, 5, 6}};
        int (*pz)[3] = zippo;
        printf("%d %d\n", pz[1][2], *(*(pz + 1) + 2));
        printf("%p %p\n", (void *) pz, (void *) (pz + 1));
        return 0;
    }
    ```

    输出：

    ```text
    6 6
    0x7ffd0a1c2a30 0x7ffd0a1c2a3c
    ```

!!! note "说明"

    - `(*pz)[3]` 表示 `pz` 指向内含 3 个元素的数组
    - 圆括号不能省，`[]` 的优先级高于 `*`
    - `int *pax[2]` 是内含 2 个指针的数组
    - `pz + 1` 跳过一整行，`*pz + 1` 只跳过一个元素
    - 通过指针也可使用 `pz[m][n]` 的数组表示法
    - 输出中的地址值随系统不同

!!! warning "常见错误"

    - 写成 `int *pz[3]`，变成指针数组
    - 用 `int *` 指向二维数组名
    - 以为 `pz + 1` 只前进一个 `int`

## 二维数组的指针表示法

!!! abstract "语法形式"

    ```c
    数组名[m][n] == *(*(数组名 + m) + n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int zippo[2][3] = {{2, 4, 6}, {1, 3, 5}};
        printf("%d %d\n", zippo[1][1], *(*(zippo + 1) + 1));
        printf("%d %d\n", *zippo[0], **zippo);
        printf("%d\n", zippo[0] == *zippo);
        return 0;
    }
    ```

    输出：

    ```text
    3 3
    2 2
    1
    ```

!!! note "说明"

    - `zippo` 与 `&zippo[0]` 的值相同
    - `zippo[0]` 与 `&zippo[0][0]` 的值相同
    - 三者数值相同，但指针类型不同
    - 二维数组名要解引用两次才得到元素值
    - `zippo[0] + 1` 前进一个 `int`，`zippo + 1` 前进一行

    ![图10.5 数组的数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00059.jpg)

!!! warning "常见错误"

    - 认为 `zippo` 与 `zippo[0]` 是同类型指针
    - 对 `zippo` 只解引用一次就当作元素值
    - 把 `**zippo` 与 `*zippo[0]` 当作不同结果

## 指针的兼容性

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ar1[2][3] = {{1, 2, 3}, {4, 5, 6}};
        int *pt = ar1[0];
        int (*pa)[3] = ar1;
        printf("%d %d\n", pt[1], pa[1][2]);
        return 0;
    }
    ```

    输出：

    ```text
    2 6
    ```

!!! note "说明"

    - 指针赋值要求所指类型一致
    - `pt = ar1[0]` 与 `pt = &ar1[0][0]` 都有效
    - `pt = ar1` 无效，两侧类型不同
    - `pa` 指向内含 3 个 `int` 的数组，与 `ar1` 兼容
    - 与内含 2 个 `int` 的数组不兼容
    - 把非 `const` 指针赋给 `const` 指针，一级解引用有效
    - 两级解引用时，`const` 限定可能失效，结果未定义

!!! warning "常见错误"

    - 在不同列数的二维数组指针之间赋值
    - 把 `int **` 与二维数组名互相赋值
    - 忽略嵌套指针赋值中的 `const` 警告

## 二维数组作函数参数

!!! abstract "语法形式"

    ```c
    返回类型 函数名(类型 形参[][列数], int 行数);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int sum2d(int ar[][3], int rows)
    {
        int r, c, s = 0;
        for (r = 0; r < rows; r++)
            for (c = 0; c < 3; c++) s += ar[r][c];
        return s;
    }
    int main(void)
    {
        int junk[2][3] = {{1, 2, 3}, {4, 5, 6}};
        printf("%d\n", sum2d(junk, 2));
    }
    ```

    输出：

    ```text
    21
    ```

!!! note "说明"

    - 形参的第一对方括号必须为空，表示这是指针
    - 列数必须写在第二对方括号中
    - 行数作为独立形参传递
    - `int (*ar)[COLS]` 是等价写法
    - `int ar[3][COLS]` 也有效，但第一维的 `3` 被忽略
    - 编译器靠列数计算 `ar + 1` 的步长

!!! warning "常见错误"

    - 写成 `int ar[][]`，列数缺失
    - 把行数也写死在方括号内并以为能限制大小
    - 传递列数不同的二维数组

## 变长数组

!!! abstract "语法形式"

    ```c
    类型 数组名[变量][变量];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int rows = 2, cols = 3;
        int i, j;
        double a[rows][cols];
        for (i = 0; i < rows; i++)
            for (j = 0; j < cols; j++)
                a[i][j] = i + j;
        printf("%.1f\n", a[1][2]);
        return 0;
    }
    ```

    输出：

    ```text
    3.0
    ```

!!! note "说明"

    - 变长数组的维度在运行时由变量决定
    - 创建之后大小不再改变
    - 必须是自动存储类别
    - 不能使用 `static` 或 `extern`
    - 声明时不能初始化
    - C11 把变长数组设为可选特性

!!! warning "常见错误"

    - 把名称中的 `变长` 理解为创建后还能改大小
    - 在文件作用域声明变长数组
    - 在变长数组声明中写初始化列表

## 变长数组作函数形参

!!! abstract "语法形式"

    ```c
    返回类型 函数名(int 行数, int 列数,
                    类型 形参[行数][列数]);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int sum2d(int rows, int cols, int ar[rows][cols])
    {
        int r, c, s = 0;
        for (r = 0; r < rows; r++)
            for (c = 0; c < cols; c++) s += ar[r][c];
        return s;
    }
    int main(void)
    {
        int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
        printf("%d\n", sum2d(2, 3, a));
    }
    ```

    输出：

    ```text
    21
    ```

!!! note "说明"

    - 维度形参必须在数组形参之前声明
    - 形参中的变长数组不创建新数组，仍是指针
    - 函数直接处理传入的原数组
    - 同一函数可处理任意 `N`×`M` 的数组
    - 原型可省略形参名，此时维度用 `*` 占位

!!! warning "常见错误"

    - 把数组形参写在维度形参之前
    - 认为 VLA 形参会复制一份数组
    - 在原型中省略维度形参名却仍写变量名

## 复合字面量

!!! abstract "语法形式"

    ```c
    (类型名){初始化列表}
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int sum(const int ar[], int n)
    {
        int i, s = 0;
        for (i = 0; i < n; i++) s += ar[i];
        return s;
    }
    int main(void)
    {
        int *p = (int []){10, 20};
        printf("%d %d\n", p[1], sum((int []){4, 4, 5}, 3));
    }
    ```

    输出：

    ```text
    20 13
    ```

!!! note "说明"

    - 复合字面量是匿名的数组或结构常量
    - 类型名由数组声明去掉数组名得到
    - 方括号内可省略大小，由列表项数决定
    - 必须在创建的同时使用
    - 可以赋给指针，也可以直接作为实参
    - 具有块作用域，离开所在块后不保证有效
    - 二维写法： `(int [2][4]){{1, 2, 3, -9}, {4, 5, 6, -8}}`

!!! warning "常见错误"

    - 先创建复合字面量，之后再按名字引用
    - 在字面量所属块之外保存其地址
    - 把复合字面量当作可以重复使用的命名数组

## 复习题

（1）下面的程序将打印什么内容？
```c
#include <stdio.h>
int main(void)
{
    int ref[] = { 8, 4, 0, 2 };
    int *ptr;
    int index;
    for (index = 0, ptr = ref; index < 4; index++, ptr++)
        printf("%d %d\n", ref[index], *ptr);
    return 0;
}
```

??? note "答案"

    打印内容为

    ```text
    8 8
    4 4
    0 0
    2 2
    ```

（2）在复习题 1 中，`ref` 有多少个元素？

??? note "答案"

    4 个，由初始化列表的项数决定

（3）在复习题 1 中，`ref` 的地址是什么？ `ref + 1` 是什么意思？ `++ref` 指向什么？

??? note "答案"

    `ref` 指向首元素 `8`
    `ref + 1` 指向第 2 个元素 `4`
    `++ref` 不是有效表达式，因为 `ref` 是地址常量，不能修改

（4）在下面的代码中，`*ptr` 和 `*(ptr + 2)` 的值分别是什么？
a.
```c
int *ptr;
int torf[2][2] = {12, 14, 16};
ptr = torf[0];
```
b.
```c
int *ptr;
int fort[2][2] = { {12}, {14,16} };
ptr = fort[0];
```

??? note "答案"

    a 中为 `12` 和 `16`; b 中为 `12` 和 `14`

（5）在下面的代码中，`**ptr` 和 `**(ptr + 1)` 的值分别是什么？
a.
```c
int (*ptr)[2];
int torf[2][2] = {12, 14, 16};
ptr = torf;
```
b.
```c
int (*ptr)[2];
int fort[2][2] = { {12}, {14,16} };
ptr = fort;
```

??? note "答案"

    a 中为 `12` 和 `16`; b 中为 `12` 和 `14`

（6）假设有声明 `int grid[30][100];`
a. 用 1 种写法表示 `grid[22][56]` 的地址
b. 用 2 种写法表示 `grid[22][0]` 的地址
c. 用 3 种写法表示 `grid[0][0]` 的地址

??? note "答案"

    a 为 `&grid[22][56]`
    b 为 `&grid[22][0]` 或 `grid[22]`
    c 为 `&grid[0][0]` 或 `grid[0]` 或 `(int *) grid`

（7）正确声明以下各变量
a. `digits` 是一个内含 10 个 `int` 类型值的数组
b. `rates` 是一个内含 6 个 `float` 类型值的数组
c. `mat` 是一个内含 3 个元素的数组，每个元素是内含 5 个整数的数组
d. `psa` 是一个内含 20 个元素的数组，每个元素是指向 `int` 的指针
e. `pstr` 是一个指向数组的指针，该数组内含 20 个 `char` 类型的值

??? note "答案"

    ```c
    int digits[10];
    float rates[6];
    int mat[3][5];
    char *psa[20];
    char (*pstr)[20];
    ```

（8）按要求声明并初始化数组
a. 声明一个内含 6 个 `int` 类型值的数组，
并初始化各元素为 `1`，`2`，`4`，`8`，`16`，`32`
b. 用数组表示法表示 a 声明的数组的第 3 个元素
c. 假设编译器支持 C99/C11，
声明一个内含 100 个 `int` 的数组，
并初始化最后一个元素为 `-1`，其他元素不考虑
d. 假设编译器支持 C99/C11，
声明一个内含 100 个 `int` 的数组，
并初始化下标为 `5`，`10`，`11`，`12`，`13` 的元素为 `101`,
其他元素不考虑

??? note "答案"

    ```c
    int sextet[6] = {1, 2, 4, 8, 16, 32};
    sextet[2]
    int lots[100] = { [99] = -1};
    int pots[100] =
        {[5] = 101, [10] = 101, 101, 101, 101};
    ```

    [原书答案末项写作 `[3] = 101`，与题干的下标不符，此处按题干改正]

（9）内含 10 个元素的数组下标范围是什么？

??? note "答案"

    `0` 到 `9`

（10）假设有下面的声明，判断以下各项是否有效
```c
float rootbeer[10], things[10][5], *pf, value = 2.2;
int i = 3;
```
a. `rootbeer[2] = value;`
b. `scanf("%f", &rootbeer);`
c. `rootbeer = value;`
d. `printf("%f", rootbeer);`
e. `things[4][4] = rootbeer[3];`
f. `things[5] = rootbeer;`
g. `pf = value;`
h. `pf = rootbeer;`

??? note "答案"

    a 有效
    b 无效，`rootbeer` 不是 `float` 类型
    c 无效，数组名不能赋值
    d 无效，`rootbeer` 不是 `float` 类型
    e 有效
    f 无效，不能用数组赋值
    g 无效，`value` 不是地址
    h 有效

（11）声明一个 800×600 的 `int` 类型数组

??? note "答案"

    `int screen[800][600];`

（12）下面声明了 3 个数组
```c
double trots[20];
short clops[10][30];
long shots[5][10][15];
```
a. 分别以传统方式和以变长数组为参数的方式
编写处理 `trots` 数组的 `void` 函数原型和函数调用
b. 分别以传统方式和以变长数组为参数的方式
编写处理 `clops` 数组的 `void` 函数原型和函数调用
c. 分别以传统方式和以变长数组为参数的方式
编写处理 `shots` 数组的 `void` 函数原型和函数调用

??? note "答案"

    ```c
    void process(double ar[], int n);
    void processvla(int n, double ar[n]);
    process(trots, 20);
    processvla(20, trots);

    void process2(short ar2[][30], int n);
    void process2vla(int n, int m,
                     short ar2[n][m]);
    process2(clops, 10);
    process2vla(10, 30, clops);

    void process3(long ar3[][10][15], int n);
    void process3vla(int n, int m, int k,
                     long ar3[n][m][k]);
    process3(shots, 5);
    process3vla(5, 10, 15, shots);
    ```

    [原书传统方式原型写作 `short ar2[30]`,
    该形参实际是指向 `short` 的指针，
    与 `clops` 的类型不符，
    此处改为 `short ar2[][30]`，三维原型同理]

（13）下面有两个函数原型
```c
void show(const double ar[], int n);
void show2(const double ar2[][3], int n);
```
a. 编写一个函数调用，
把一个内含 `8`，`3`，`9`，`2` 的复合字面量
传递给 `show()`
b. 编写一个函数调用，
把一个 2 行 3 列的复合字面量传递给 `show2()`,
第 1 行为 `8`，`3`，`9`，第 2 行为 `5`，`4`，`1`

??? note "答案"

    ```c
    show((double [4]){8, 3, 9, 2}, 4);
    show2((double [][3]){{8, 3, 9}, {5, 4, 1}}, 2);
    ```

    [原书答案使用 `int` 复合字面量，与 `const double` 形参类型不符，此处改为 `double`]

## 编程练习

!!! question "编程练习"

    1. 修改程序清单 10.7 的 `rain.c` 程序，用指针进行计算，仍然要声明并初始化数组

    2. 编写一个程序，初始化一个 `double` 类型的数组，
    然后把该数组的内容拷贝至 3 个其他数组中，
    在 `main()` 中声明这 4 个数组。
    使用带数组表示法的函数进行第 1 份拷贝。
    使用带指针表示法和指针递增的函数进行第 2 份拷贝。
    把目标数组名，源数组名和待拷贝的元素个数
    作为前两个函数的参数。
    第 3 个函数以目标数组名，源数组名
    和指向源数组最后一个元素后面的元素的指针为参数

    ```c
    double source[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
    double target1[5];
    double target2[5];
    double target3[5];
    copy_arr(target1, source, 5);
    copy_ptr(target2, source, 5);
    copy_ptrs(target3, source, source + 5);
    ```

    3. 编写一个函数，返回储存在 `int` 类型数组中的最大值，并在一个简单的程序中测试该函数

    4. 编写一个函数，返回储存在 `double` 类型数组中最大值的下标，并在一个简单的程序中测试该函数

    5. 编写一个函数，返回储存在 `double` 类型数组中最大值和最小值的差值，并在一个简单的程序中测试该函数

    6. 编写一个函数，把 `double` 类型数组中的数据倒序排列，并在一个简单的程序中测试该函数

    7. 编写一个程序，初始化一个 `double` 类型的二维数组，
    使用编程练习 2 中的一个拷贝函数把该数组中的数据
    拷贝至另一个二维数组中。
    二维数组是数组的数组，
    所以可以用处理一维数组的拷贝函数处理数组中的每个子数组

    8. 使用编程练习 2 中的拷贝函数，
    把一个内含 7 个元素的数组中第 3 到第 5 个元素
    拷贝至内含 3 个元素的数组中。
    该函数本身不需要修改，只需选择合适的实际参数，
    实际参数可以是数组元素的地址和待处理元素的个数

    9. 编写一个程序，初始化一个 `double` 类型的 3×5 二维数组，
    使用一个处理变长数组的函数将其拷贝至另一个二维数组中。
    还要编写一个以变长数组为形参的函数以显示两个数组的内容。
    这两个函数应能处理任意 `N`×`M` 数组。
    如果编译器不支持变长数组，
    就使用传统 C 函数处理 `N`×5 的数组

    10. 编写一个函数，把两个数组中相对应的元素相加，
    然后把结果储存到第 3 个数组中。
    例如数组 1 中的值为 `2`，`4`，`5`，`8`,
    数组 2 中的值为 `1`，`0`，`4`，`6`,
    函数把 `3`，`4`，`9`，`14` 赋给第 3 个数组。
    函数接受 3 个数组名和一个数组大小，
    并在一个简单的程序中测试该函数

    11. 编写一个程序，声明一个 `int` 类型的 3×5 二维数组，
    并用合适的值初始化它。
    该程序打印数组中的值，然后各值翻倍，并显示出各元素的新值。
    编写一个函数显示数组的内容，
    再编写一个函数把各元素的值翻倍，
    这两个函数都以数组名和行数作为参数

    12. 重写程序清单 10.7 的 `rain.c` 程序，把 `main()` 中的主要任务都改成用函数来完成

    13. 编写一个程序，提示用户输入 3 组数，
    每组数包含 5 个 `double` 类型的数，
    假设用户都正确响应

    a. 把用户输入的数据储存在 3×5 的数组中

    b. 计算每组 5 个数据的平均值

    c. 计算所有数据的平均值

    d. 找出这 15 个数据中的最大值

    e. 打印结果

    每个任务都用单独的函数完成，使用传统 C 处理数组的方式。
    完成任务 b 时，编写一个计算并返回一维数组平均值的函数，
    利用循环调用该函数 3 次。
    其他任务的处理函数应把整个数组作为参数，
    完成任务 c 和 d 的函数应把结果返回主调函数

    14. 以变长数组作为函数形参，完成编程练习 13
