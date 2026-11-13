# 第3章 数据和C

## 变量声明与初始化

!!! abstract "语法形式"

    ```c
    类型 变量名;
    类型 变量名1, 变量名2;
    类型 变量名 = 初值;
    类型 变量名1 = 初值1, 变量名2 = 初值2;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int hogs = 21;
        int cows = 32, goats = 14;
        printf("%d %d %d\n", hogs, cows, goats);
        return 0;
    }
    ```

    输出：

    ```text
    21 32 14
    ```

!!! note "说明"

    - 声明为变量分配存储空间，并登记名称与类型
    - 一条声明可列出多个同类型变量，变量名之间用逗号分隔
    - 未初始化的变量保留内存中原有的位组合，不能假定为 `0`
    - `int dogs, cats = 94;` 只初始化 `cats`，`dogs` 仍无初值

!!! warning "常见错误"

    - 声明末尾漏写分号
    - 把 `int dogs, cats = 94;` 理解为 `dogs` 也初始化为 `94`
    - 在同一条声明中混用已初始化和未初始化的变量

## 基本数据类型关键字

!!! note "说明"

    - C 的基本数据类型由 11 个关键字组成，按存储方式分为整数类型与浮点类型两族

    表3-1 基本数据类型关键字

    | 关键字 | 类型 |
    | --- | --- |
    | `int` | 基本整数类型 |
    | `short` | 较小的整数 |
    | `long` | 较大的整数 |
    | `unsigned` | 无符号修饰 |
    | `signed` | 显式声明有符号 |
    | `char` | 字符与小整数 |
    | `float` | 单精度浮点数 |
    | `double` | 双精度浮点数 |
    | `_Bool` | 布尔值，C99 |
    | `_Complex` | 复数，C99 |
    | `_Imaginary` | 虚数，C99 |

    - `long long` 由两个 `long` 拼成，不是独立关键字
    - `unsigned` 与 `signed` 是修饰符，不能单独作为类型使用
    - `_Bool` `_Complex` `_Imaginary` 是 C99 新增的关键字

!!! warning "常见错误"

    - 把 `long long` 当作一个关键字书写
    - 在 C89 编译器上使用 `//` 注释与 `_Bool`

## 整数类型与取值范围

!!! abstract "语法形式"

    ```c
    int 名称;
    short 名称;
    long 名称;
    long long 名称;
    unsigned 类型 名称;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a = 2147483647;
        unsigned int b = 4294967295u;
        printf("%d\n", a);
        printf("%u\n", b);
        return 0;
    }
    ```

    输出：

    ```text
    2147483647
    4294967295
    ```

    表3-2 整数类型 (典型 64 位 Linux 系统)

    | 类型 | 字节 | 取值范围 |
    | --- | --- | --- |
    | `signed char` | 1 | `-128` 到 `127` |
    | `unsigned char` | 1 | `0` 到 `255` |
    | `short` | 2 | `-32768` 到 `32767` |
    | `unsigned short` | 2 | `0` 到 `65535` |
    | `int` | 4 | `-2147483648` 到 `2147483647` |
    | `unsigned int` | 4 | `0` 到 `4294967295` |
    | `long` | 8 | `-9223372036854775808` 到 `9223372036854775807` |
    | `long long` | 8 | 与 `long` 相同 |
    | `unsigned long long` | 8 | `0` 到 `18446744073709551615` |

!!! note "说明"

    - C 标准只规定最小宽度： `short` 至少 16 位，`long` 至少 32 位
    - `long long` 至少 64 位，由 C99 引入
    - `int` 通常等于机器字长，16 位机上为 2 字节
    - Windows 的 `long` 为 4 字节，Linux 与 macOS 上为 8 字节
    - 存储以二进制补码表示，有符号类型最高位为符号位

    ![图3.2 使用二进制编码储存整数7](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00014.jpg)

## 整型常量

!!! abstract "语法形式"

    ```c
    十进制:   42
    八进制:   052
    十六进制: 0x2a
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a = 42;
        int b = 052;
        int c = 0x2a;
        printf("%d %d %d\n", a, b, c);
        return 0;
    }
    ```

    输出：

    ```text
    42 42 42
    ```

!!! note "说明"

    - `0` 前缀表示八进制，`0x` 或 `0X` 前缀表示十六进制
    - 三种写法只在源码中不同，存储时都换成二进制
    - 无后缀整型常量按 `int`，`unsigned int`，`long`，`unsigned long`
      的顺序取第一个能容纳该值的类型
    - 十六进制 1 位对应二进制 4 位，便于观察位组合

!!! warning "常见错误"

    - 在八进制常量中写 `8` 或 `9`，例如 `018`
    - 把 `010` 当作十进制 10，实际为 8

## 打印整数

!!! abstract "语法形式"

    ```c
    printf("%d", 整型表达式);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ten = 10;
        int two = 2;
        printf("Doing it right: ");
        printf("%d minus %d is %d\n", ten, 2, ten - two);
        return 0;
    }
    ```

    输出：

    ```text
    Doing it right: 10 minus 2 is 8
    ```

!!! note "说明"

    - `%d` 是转换说明，指明按有符号十进制打印一个 `int` 值
    - 转换说明的个数与待打印值的个数须一致
    - `printf()` 参数个数可变，编译器不检查个数与类型是否匹配
    - 格式化字符串中的每个 `%d` 按顺序与后面的实参对应

!!! warning "常见错误"

    - 遗漏实参，例如 `printf("%d %d\n", ten);`，缺少的值取自内存中的任意内容
    - 把 `printf()` 的检查指望于编译器，多数编译器只给警告

## 打印不同进制

!!! abstract "语法形式"

    ```c
    printf("%d", 值);   十进制
    printf("%o", 值);   八进制
    printf("%x", 值);   十六进制, 小写
    printf("%X", 值);   十六进制, 大写
    printf("%#o", 值);  八进制, 带前缀 0
    printf("%#x", 值);  十六进制, 带前缀 0x
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int x = 100;
        printf("dec = %d; octal = %o; hex = %x\n", x, x, x);
        printf("dec = %d; octal = %#o; hex = %#x\n", x, x, x);
        return 0;
    }
    ```

    输出：

    ```text
    dec = 100; octal = 144; hex = 64
    dec = 100; octal = 0144; hex = 0x64
    ```

!!! note "说明"

    - 同一个值可用不同转换说明显示，存储不变
    - `#` 修饰符只控制前缀的显示，不改变数值
    - `%X` 输出大写字母，前缀也随之变成 `0X`

!!! warning "常见错误"

    - 认为 `%o` 会把十进制数换算成八进制存储
    - 需要前缀时漏写 `#`

## 整数类型修饰

!!! abstract "语法形式"

    ```c
    short int 名称;
    long int 名称;
    long long int 名称;
    unsigned int 名称;
    signed short int 名称;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned int s_count = 10u;
        unsigned long headcount = 3000000000ul;
        signed short int yesvotes = -5;
        printf("%u %lu %hd\n", s_count, headcount, yesvotes);
        return 0;
    }
    ```

    输出：

    ```text
    10 3000000000 -5
    ```

!!! note "说明"

    - `short` `long` `long long` 后面的 `int` 可省略
    - `short` 的宽度不大于 `int`，`long` 不小于 `int`，`long long` 不小于 `long`
    - `unsigned` 去掉符号位，范围平移到 `0` 到 $2^n-1$
    - `signed` 只用于强调有符号，不改变类型
    - 计数类变量优先用 `unsigned`，需要更大范围时依次考虑 `long` `long long`

!!! warning "常见错误"

    - 写出 `unsigned signed int` 这类互斥修饰
    - 认为 `unsigned` 只是去掉负号，忽略范围上限翻倍

## 整数常量后缀

!!! abstract "语法形式"

    ```c
    7L      long
    3LL     long long
    10U     unsigned int
    10UL    unsigned long
    5ULL    unsigned long long
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        long a = 7L;
        long long b = 3LL;
        unsigned long c = 10UL;
        printf("%ld %lld %lu\n", a, b, c);
        return 0;
    }
    ```

    输出：

    ```text
    7 3 10
    ```

!!! note "说明"

    - 后缀字母大小写均可，可组合
    - `L` 优于 `l`，小写 `l` 与数字 1 容易混淆
    - 后缀决定常量的类型，不改变它的值
    - 默认无后缀的十进制常量是 `int`，超出范围时依次升级

!!! warning "常见错误"

    - 用小写 `l` 结尾，阅读时误认为 `1`
    - 认为加上 `L` 后数值变大

## 整数溢出

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int i = 2147483647;
        unsigned int j = 4294967295u;
        printf("%d %d %d\n", i, i + 1, i + 2);
        printf("%u %u %u\n", j, j + 1, j + 2);
        return 0;
    }
    ```

    输出：

    ```text
    2147483647 -2147483648 -2147483647
    4294967295 0 1
    ```

!!! note "说明"

    - 无符号整数按模 $2^n$ 回绕，超过最大值后回到 `0`
    - 有符号整数溢出属于未定义行为，C 标准不规定结果
    - 常见的实现结果是最高位翻转，得到负数，但不能依赖
    - 溢出时系统不报告错误，需程序自行检查范围

!!! warning "常见错误"

    - 认为溢出会终止程序或给出提示
    - 依赖有符号溢出的具体结果编写逻辑

## 转换说明与整数宽度

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned int un = 3000000000;
        short end = 200;
        long big = 65537;
        printf("un = %u and not %d\n", un, un);
        printf("end = %hd and %d\n", end, end);
        printf("big = %ld and not %hd\n", big, big);
        return 0;
    }
    ```

    输出：

    ```text
    un = 3000000000 and not -1294967296
    end = 200 and 200
    big = 65537 and not 1
    ```

!!! note "说明"

    - `%u` 打印 `unsigned int`，`%ld` 打印 `long`
    - `%hd` 打印 `short`，`h` 前缀只读取低 16 位
    - `short` 在传参时自动提升为 `int`，所以 `%d` 也能打印小值
    - 同样的位组合按有符号或无符号解释，显示结果不同
    - 常量后缀可大写或小写，转换说明中的长度修饰符用小写
    - 例如 `%ld` 不写成 `%LD`，而 `%X` 表示大写的十六进制数字

!!! warning "常见错误"

    - 用 `%d` 打印超出 `int` 范围的 `unsigned` 值
    - 用 `%hd` 打印 `long`，只输出低 16 位

## 字符类型与字符常量

!!! abstract "语法形式"

    ```c
    char 名称 = '字符';
    char 名称 = 整型编码;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        char grade = 'A';
        char code = 65;
        printf("%c %d\n", grade, grade);
        printf("%c\n", code);
        return 0;
    }
    ```

    输出：

    ```text
    A 65
    A
    ```

!!! note "说明"

    - `char` 存储的是字符的整数编码，本质是 1 字节整数
    - 字符常量用单引号括起来，编译器把它换成对应编码值
    - 字符常量本身是 `int` 类型，赋值给 `char` 时发生收窄
    - 用编码 `65` 赋值可行，但只在 ASCII 系统上成立，宜写 `'A'`
    - 多字符常量如 `'FATE'` 把 4 个编码压进一个 `int`，赋给 `char` 后只剩最后一个字符

!!! warning "常见错误"

    - `char c = "A";` 双引号是字符串
    - `char c = A;` 没有引号，`A` 被当作变量名
    - 认为 `'4'` 等于数值 `4`，实际是编码 `52`

## 转义序列

!!! abstract "语法形式"

    ```c
    char 名称 = '\n';
    printf("...\t...");
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        char beep = '\a';
        char nl = '\n';
        printf("Gramps sez, \"a \\ is a backslash.\"\n");
        printf("%c", beep);
        printf("done%c", nl);
        return 0;
    }
    ```

    输出：

    ```text
    Gramps sez, "a \ is a backslash."
    done
    ```

    表3-3 转义序列

    | 转义序列 | 含义 |
    | --- | --- |
    | `\a` | 警报，响铃 |
    | `\b` | 退格 |
    | `\f` | 换页 |
    | `\n` | 换行 |
    | `\r` | 回车，回到行首 |
    | `\t` | 水平制表符 |
    | `\v` | 垂直制表符 |
    | `\\` | 反斜杠 |
    | `\'` | 单引号 |
    | `\"` | 双引号 |
    | `\?` | 问号 |
    | `\ooo` | 1 到 3 位八进制编码 |
    | `\xhh` | 1 到 3 位十六进制编码 |

!!! note "说明"

    - `\ooo` 与 `\xhh` 以八进制或十六进制编码表示字符
    - 编码值取决于系统的字符集，常见系统为 ASCII
    - 八进制写法可省略前导 `0`，`'\07'` 与 `'\7'` 均有效
    - 转义序列写在字符串中时不必再加单引号
    - 优先用 `'\f'` 这类字符写法，比 `'\014'` 可读且可移植
    - `\r` 回到行首，后续输出会覆盖本行已有字符

!!! warning "常见错误"

    - 打印反斜杠时只写 `\`，被当作续行或非法转义
    - 在双引号字符串里放未转义的 `"`

## 打印字符

!!! abstract "语法形式"

    ```c
    printf("%c", 字符变量);
    printf("%d", 字符变量);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        char ch = 'C';
        printf("The code for %c is %d.\n", ch, ch);
        return 0;
    }
    ```

    输出：

    ```text
    The code for C is 67.
    ```

!!! note "说明"

    - `%c` 按字符显示，`%d` 按整数显示同一个值
    - 转换说明决定显示方式，不决定存储方式
    - 字符编码由系统决定，书中的 67 来自 ASCII

    ![图3.6 数据显示和数据存储](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00018.jpg)

!!! warning "常见错误"

    - 用 `%d` 打印字符而期望看到字母
    - 用 `%c` 打印字符串，只输出首字符

## 布尔类型

!!! abstract "语法形式"

    ```c
    _Bool 名称 = 0;
    _Bool 名称 = 1;
    bool 名称 = true;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdbool.h>
    int main(void)
    {
        _Bool on = 1;
        _Bool off = 0;
        bool ok = true;
        printf("%d %d %d\n", on, off, ok);
        printf("%zu\n", sizeof(_Bool));
        return 0;
    }
    ```

    输出：

    ```text
    1 0 1
    1
    ```

!!! note "说明"

    - `_Bool` 由 C99 引入，只能存 `0` 或 `1`
    - 赋非零值给 `_Bool` 时，结果统一为 `1`
    - 包含 `stdbool.h` 后可用 `bool` `true` `false`
    - `_Bool` 是整数类型，可用 `%d` 打印
    - `sizeof(_Bool)` 为 1 字节

    [教材原写法： `_Bool` 原则上仅占用 1 位存储空间
    - 本笔记： `_Bool` 占 1 字节
    - 依据： C 标准要求对象至少占 1 个字节，GCC 与 MSVC 上 `sizeof(_Bool)` 均为 1]

!!! warning "常见错误"

    - 未包含 `stdbool.h` 就使用 `bool`
    - 期望 `printf` 直接输出 `true` 与 `false`

## 可移植整数类型

!!! abstract "语法形式"

    ```c
    #include <stdint.h>
    #include <inttypes.h>
    int32_t 名称;
    printf("%" PRId32 "\n", 值);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <inttypes.h>
    int main(void)
    {
        int32_t me32 = 45933945;
        printf("me32 = %" PRId32 "\n", me32);
        printf("sizeof = %zu\n", sizeof(int32_t));
        return 0;
    }
    ```

    输出：

    ```text
    me32 = 45933945
    sizeof = 4
    ```

!!! note "说明"

    - `int8_t` `int16_t` `int32_t` `int64_t` 为精确宽度类型，宽度固定
    - `int_least8_t` 保证至少 8 位，取满足条件的最小类型
    - `int_fast8_t` 取运算最快的类型，可能更宽
    - `intmax_t` 与 `uintmax_t` 为系统支持的最大整数类型
    - `PRId32` 等宏展开为对应的转换字符，与 `int32_t` 匹配
    - 相邻的字符串字面量会自动拼接，所以 `"%" PRId32` 可用

!!! warning "常见错误"

    - 用 `%d` 打印 `int64_t`，宽度不匹配
    - 把 `PRId32` 写在引号内部，宏不会被展开

## 浮点类型

!!! abstract "语法形式"

    ```c
    float 名称;
    double 名称;
    long double 名称;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float f = 3.14f;
        double d = 3.141592653589793;
        printf("%.2f\n", f);
        printf("%.15f\n", d);
        return 0;
    }
    ```

    输出：

    ```text
    3.14
    3.141592653589793
    ```

    表3-4 浮点类型

    | 类型 | 典型字节数 | 有效数字 | 范围 |
    | --- | --- | --- | --- |
    | `float` | 4 | 至少 6 位 | 约 $10^{-37}$ 到 $10^{37}$ |
    | `double` | 8 | 至少 10 位，通常 15 到 16 位 | 约 $10^{-308}$ 到 $10^{308}$ |
    | `long double` | 8 或 16 | 不少于 `double` | 不少于 `double` |

!!! note "说明"

    - 浮点数由符号，尾数，指数三部分分开存储
    - 尾数决定精度，指数决定范围
    - `float` 的 32 位中通常 8 位存指数，24 位存尾数与符号
    - `double` 的位数多用于尾数，因而精度更高
    - C 只保证 `long double` 的精度不低于 `double`

    ![图3.3 以浮点格式(十进制)储存π的值](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00015.jpg)

!!! warning "常见错误"

    - 认为位数多就一定表示更大的范围，实际可能只是尾数更宽
    - 在同一程序中混用大量 `float` 与 `double`，造成隐式转换

## 浮点常量

!!! abstract "语法形式"

    ```c
    [符号] 数字.数字 [eE][符号] 指数 [后缀]
    0x十六进制数 p[符号] 指数 [后缀]
    后缀: f 或 F 表示 float, l 或 L 表示 long double
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float a = 2.3f;
        double b = 1.23e5;
        long double c = 54.3L;
        double d = 0xa.1fp10;
        printf("%.1f\n", a);
        printf("%.0f\n", b);
        printf("%.1f\n", d);
        return 0;
    }
    ```

    输出：

    ```text
    2.3
    123000
    10364.0
    ```

!!! note "说明"

    - 小数点与指数部分至少有一个，不能都省略
    - `.2` `4e16` `.8E-5` 都是有效的浮点常量
    - 无后缀的浮点常量是 `double`
    - `0xa.1fp10` 是 C99 的十六进制写法，`p10` 表示乘以 $2^{10}$
    - 该值等于 $(10+1/16+15/256)\times 1024=10364.0$
    - `L` 后缀优于 `l`，避免与数字 1 混淆

!!! warning "常见错误"

    - 在常量中间加空格，如 `1.56 E+12`
    - 写成 `e21`，`e` 前至少要有一个数字，如 `1e21`

## 打印浮点值

!!! abstract "语法形式"

    ```c
    printf("%f", 值);    定点记数法
    printf("%e", 值);    指数记数法
    printf("%a", 值);    十六进制 p 记数法
    printf("%Lf", 值);   long double
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float aboat = 32000.0;
        double abet = 2.14e9;
        printf("%f can be written %e\n", aboat, aboat);
        printf("%f can be written %e\n", abet, abet);
        return 0;
    }
    ```

    输出：

    ```text
    32000.000000 can be written 3.200000e+04
    2140000000.000000 can be written 2.140000e+09
    ```

!!! note "说明"

    - `%f` 与 `%e` 默认显示 6 位小数
    - `float` 在传参时自动提升为 `double`，所以 `%f` 可打印 `float`
    - `long double` 要用 `%Lf` `%Le` `%La`
    - `%a` 以十六进制尾数与二进制指数显示，需编译器支持 C99
    - `%.2f` 中的 `.2` 指定小数点后两位

!!! warning "常见错误"

    - 用 `%d` 打印浮点数
    - 用 `%f` 打印 `long double`，宽度不匹配

## 浮点溢出与下溢

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float toobig = 3.4E38f * 100.0f;
        float tiny = 1.17549435e-38f / 2.0f;
        printf("%e\n", toobig);
        printf("%e\n", tiny);
        return 0;
    }
    ```

    输出：

    ```text
    inf
    5.877472e-39
    ```

!!! note "说明"

    - 结果超出类型上限称为上溢，C 规定此时得到无穷大
    - `printf` 把无穷大显示为 `inf` 或 `infinity`
    - 结果小于最小正规数时，指数已无法再减，只能右移尾数
    - 右移损失末尾有效位，这种值称为低于正常值，即下溢
    - 再小下去所有位变为 `0`，结果变成零
    - 对无效运算，如 `asin()` 的参数大于 1，结果为 `NaN`

!!! warning "常见错误"

    - 认为上溢会让程序终止
    - 把下溢得到的小数当作精确结果继续运算

## 浮点舍入误差

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        float a, b;
        b = 2.0e20f + 1.0f;
        a = b - 2.0e20f;
        printf("%f\n", a);
        return 0;
    }
    ```

    输出：

    ```text
    0.000000
    ```

!!! note "说明"

    - `float` 只有 6 到 7 位有效数字
    - `2.0e20` 加 1 需要第 21 位有效数字，超出存储能力
    - 加 1 的结果与 `2.0e20` 相同，相减后得 `0`
    - 换成 `2.0e4` 时，加 1 只改动第 5 位，结果正确
    - 浮点运算结果与系统，编译器，优化级别相关

!!! warning "常见错误"

    - 用 `==` 比较两个浮点数
    - 在累加大量小数时使用 `float`
    - 认为浮点数能精确表示所有十进制小数

## 复数与虚数类型

!!! abstract "语法形式"

    ```c
    float _Complex 名称;
    double _Complex 名称;
    long double _Complex 名称;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <complex.h>
    int main(void)
    {
        double complex z = 1.0 + 2.0 * I;
        printf("%.1f %.1f\n", creal(z), cimag(z));
        return 0;
    }
    ```

    输出：

    ```text
    1.0 2.0
    ```

!!! note "说明"

    - 复数类型由两个浮点数组成，分别存实部与虚部
    - 包含 `complex.h` 后可用 `complex` 代替 `_Complex`
    - `I` 表示虚数单位，即 $\sqrt{-1}$
    - `creal()` 取实部，`cimag()` 取虚部
    - 虚数类型 `float _Imaginary` 等在 C11 中为可选项

!!! warning "常见错误"

    - 未包含 `complex.h` 就使用 `complex` 与 `I`
    - 用 `%f` 打印复数整体，应分别打印实部与虚部

## 类型转换与截断

!!! abstract "语法形式"

    ```c
    目标类型 变量 = 其他类型的值;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int cost = 12.99;
        float pi = 3.1415926536;
        char ch = 'FATE';
        printf("%d %.6f %c\n", cost, pi, ch);
        return 0;
    }
    ```

    输出：

    ```text
    12 3.141593 E
    ```

!!! note "说明"

    - 浮点值赋给整数变量时直接丢弃小数部分，不四舍五入
    - `double` 赋给 `float` 时保留前 6 到 7 位有效数字，其余舍去
    - 多字符常量压缩成 `int`，赋给 `char` 时只留最低 8 位
    - 编译器一般给警告，不阻止转换
    - 表达式中的混合类型按整型提升与类型等级自动转换

!!! warning "常见错误"

    - 认为 `int cost = 12.99;` 得到 `13`
    - 在需要精度的场合用 `float` 代替 `double`

## sizeof 与类型大小

!!! abstract "语法形式"

    ```c
    sizeof(类型)
    sizeof 变量
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        printf("Type int has a size of %zd bytes.\n", sizeof(int));
        printf("Type char has a size of %zd bytes.\n", sizeof(char));
        printf("Type long has a size of %zd bytes.\n", sizeof(long));
        printf("Type long long has a size of %zd bytes.\n",
                sizeof(long long));
        printf("Type double has a size of %zd bytes.\n", sizeof(double));
        printf("Type long double has a size of %zd bytes.\n",
                sizeof(long double));
        return 0;
    }
    ```

    输出 (MinGW，Windows)

    ```text
    Type int has a size of 4 bytes.
    Type char has a size of 1 bytes.
    Type long has a size of 4 bytes.
    Type long long has a size of 8 bytes.
    Type double has a size of 8 bytes.
    Type long double has a size of 16 bytes.
    ```

!!! note "说明"

    - `sizeof` 是运算符，不是函数，以字节为单位返回大小
    - 返回值类型为 `size_t`，C99 起用 `%zd` 打印
    - 参数为类型名时必须加括号，为变量时括号可省略
    - `char` 的大小恒为 1 字节，1 字节的位数由实现决定
    - 其余类型的大小依系统而异，同一类型在 32 位与 64 位系统上可能不同

!!! warning "常见错误"

    - 用 `%d` 打印 `sizeof` 的结果
    - 把书上的字节数当作标准规定，跨平台移植时出问题

## 转换说明与参数匹配

!!! abstract "语法形式"

    ```c
    printf("格式串", 值1, 值2, ...);
    scanf("格式串", &变量1, &变量2, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int cats = 2;
        int cans = 3;
        printf("%d cats ate %d cans of tuna\n", cats, cans);
        return 0;
    }
    ```

    输出：

    ```text
    2 cats ate 3 cans of tuna
    ```

!!! note "说明"

    - 格式串中的转换说明按顺序与后面的实参一一对应
    - `printf` 与 `scanf` 的参数个数可变，编译器不检查个数与类型
    - 转换说明过多或过少时行为未定义，结果随平台而异
    - 一个字符串字面量无论多长都只算一个参数
    - 数量与类型都由程序员保证

!!! warning "常见错误"

    - 遗漏实参，打印出内存中的任意值
    - 用 `%d` 打印 `float`，值不会被自动转换
    - 误以为编译器会拦截这类错误

## scanf 读取数据

!!! abstract "语法形式"

    ```c
    scanf("格式串", &变量);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int age;
        float weight;
        printf("age weight: ");
        scanf("%d %f", &age, &weight);
        printf("%d %.1f\n", age, weight);
        return 0;
    }
    ```

!!! note "说明"

    - `&` 取得变量的地址，告诉 `scanf` 把值写到何处
    - `%d` 读 `int`，`%f` 读 `float`，`%c` 读单个字符
    - `%lf` 用于读 `double`，打印时仍用 `%f`
    - 输入时按 Enter 提交，换行符留在缓冲区
    - 读数失败时不改变变量，返回值小于参数个数

!!! warning "常见错误"

    - 漏写 `&`，程序运行时崩溃
    - 用 `%f` 读 `double` 变量
    - 用 `%c` 读字符时，读到的却是上一次留下的换行符

## 复习题

（1）指出下面各种数据使用的合适数据类型 (有些可使用多种数据类型)
a. East Simpleton 的人口
b. DVD 影碟的价格
c. 本章出现次数最多的字母
d. 本章出现次数最多的字母次数

??? note "答案"

    a. `int`，也可用 `short` 或 `unsigned short`，人口是整数
    b. `float`，也可用 `double`，价格通常不是整数
    c. `char`
    d. `int`，也可用 `unsigned`

（2）在什么情况下要用 `long` 类型的变量代替 `int` 类型的变量

??? note "答案"

    一是要表示的数超出 `int` 的范围
    二是需要一种在所有系统上都保证至少 32 位的类型，以提高可移植性

（3）使用哪些可移植的数据类型可以获得 32 位有符号整数，选择的理由是什么

??? note "答案"

    要正好 32 位，用 `int32_t`
    要可储存至少 32 位的最小类型，用 `int_least32_t`
    要 32 位整数的最快运算，用 `int_fast32_t`

（4）指出下列常量的类型和含义 (如果有的话)
a. `'\b'`
b. `1066`
c. `99.44`
d. `0XAA`
e. `2.0e30`

??? note "答案"

    a. 字符常量，存储为 `int`，表示退格
    b. `int` 常量
    c. `double` 常量
    d. `int` 常量，十六进制写法，值为 170
    e. `double` 常量

    [教材原写法： d 为 `unsigned int` 类型常量
    本笔记： d 为 `int` 类型常量
    依据： 无后缀的十六进制常量按 `int`，`unsigned int`，`long` 的顺序取首个可容纳的类型，170 在 `int` 范围内]

（5）Dottie Cawm 编写了一个程序，请找出程序中的错误
```c
include <stdio.h>
main
(
     float g; h;
     float tax, rate;
     g = e21;
     tax = rate*g;
)
```

??? note "答案"

    第 1 行改为 `#include <stdio.h>`
    第 2 行改为 `int main(void)`
    第 3 行把 `(` 改为 `{`
    第 4 行把 `g` 与 `h` 之间的分号改为逗号
    第 7 行 `e21` 前应至少有一个数字，如 `1.0e21`

    第 9 行把 `)` 改为 `}`
    另缺 `rate` 的赋值，`h` 未被使用，结果未打印，末尾缺 `return`
    参考版本

    ```c
    #include <stdio.h>
    int main(void)
    {
        float g, h;
        float tax, rate;

        rate = 0.08;
        g = 1.0e5;
        tax = rate * g;
        h = g + tax;
        printf("You owe $%f plus $%f in taxes for a total of $%f.\n",
                g, tax, h);
        return 0;
    }
    ```

（6）写出下列常量在声明中使用的数据类型和在 `printf()` 中对应的转换说明

??? note "答案"

    | 常量 | 类型 | 转换说明 |
    | --- | --- | --- |
    | `12` | `int` | `%d` |
    | `0X3` | `int` | `%#X` |
    | `'C'` | `char`，实际为 `int` | `%c` |
    | `2.34E07` | `double` | `%e` |
    | `'\040'` | `char`，实际为 `int` | `%c` |
    | `7.0` | `double` | `%f` |
    | `6L` | `long` | `%ld` |
    | `6.0f` | `float` | `%f` |
    | `0x5.b6p12` | `double` | `%a` |

    [教材原写法： `0X3` 为 `unsigned int`，`0x5.b6p12` 为 `float`
    本笔记： `0X3` 为 `int`，`0x5.b6p12` 为 `double`
    依据： 无后缀整型常量先取 `int`，装不下才升为 `unsigned int`; 十六进制浮点常量无后缀时为 `double`，已用 gcc 的 `_Generic` 实测]

（7）写出下列常量在声明中使用的数据类型和在 `printf()` 中对应的转换说明，假设 `int` 为 16 位

??? note "答案"

    | 常量 | 类型 | 转换说明 |
    | --- | --- | --- |
    | `012` | `int` | `%#o` |
    | `2.9e05L` | `long double` | `%Le` |
    | `'s'` | `char`，实际为 `int` | `%c` |
    | `100000` | `long` | `%ld` |
    | `'\n'` | `char`，实际为 `int` | `%c` |
    | `20.0f` | `float` | `%f` |
    | `0x44` | `int` | `%#x` |
    | `-40` | `int` | `%d` |

    [教材原写法： `012` 与 `0x44` 为 `unsigned int`
    本笔记： 两者均为 `int`，值分别为 10 与 68，都在 16 位 `int` 范围内
    依据： 八进制与十六进制常量按 `int`，`unsigned int`，`long` 的顺序取首个可容纳的类型]

（8）假设程序的开头有下列声明，把下面 `printf()` 语句中的转换字符补充完整
```c
int imate = 2;
long shot = 53456;
char grade = 'A';
float log = 2.71828;
```
```c
printf("The odds against the %__ were %__ to 1.\n", imate, shot);
printf("A score of %__ is not an %__ grade.\n", log, grade);
```

??? note "答案"

    第一句填 `%d` 与 `%ld`
    第二句填 `%f` 与 `%c`

（9）假设 `ch` 是 `char` 类型的变量，分别使用转义序列，十进制值，八进制字符常量和十六进制字符常量把回车字符赋给 `ch`

??? note "答案"

    `ch = '\r';`
    `ch = 13;`
    `ch = '\015';`
    `ch = '\xd';`

（10）修正下面的程序 (`/` 表示除以)
```c
void main(int) / this program is perfect /
{
     cows, legs integer;
     printf("How many cow legs did you count?\n);
     scanf("%c", legs);
     cows = legs / 4;
     printf("That implies there are %f cows.\n", cows)
}
```

??? note "答案"

    最前面补 `#include <stdio.h>`
    第 1 行用 `/* */` 或 `//` 包围注释
    第 3 行改为 `int cows, legs;`
    第 4 行补上结尾的 `\n");`
    第 5 行把 `%c` 改为 `%d`，把 `legs` 改为 `&legs`
    第 7 行把 `%f` 改为 `%d`
    末尾补 `return 0;`
    修改后的版本

    ```c
    #include <stdio.h>
    int main(void) /* this program is perfect */
    {
        int cows, legs;
        printf("How many cow legs did you count?\n");
        scanf("%d", &legs);
        cows = legs / 4;
        printf("That implies there are %d cows.\n", cows);
        return 0;
    }
    ```

（11）指出下列转义序列的含义
a. `\n`
b. `\\`
c. `\"`
d. `\t`

??? note "答案"

    a. 换行字符
    b. 反斜杠字符
    c. 双引号字符
    d. 水平制表字符

## 编程练习

!!! question "编程练习"

    1. 通过试验观察系统如何处理整数上溢，浮点数上溢和浮点数下溢，编写带有这类问题的程序

    2. 编写一个程序，提示输入一个 ASCII 码值 (如 66)，然后打印输入的字符

    3. 编写一个程序，发出一声警报，然后打印下面的文本

    ```text
    Startled by the sudden sound, Sally shouted,
    "By the Great Pumpkin, what was that!"
    ```

    4. 编写一个程序，读取一个浮点数，先打印成小数点形式，再打印成指数形式
    然后如果系统支持，再打印成 `p` 记数法
    输出格式如下

    ```text
    Enter a floating-point value: 64.25

    fixed-point notation: 64.250000
    exponential notation: 6.425000e+01
    p notation: 0x1.01p+6
    ```

    5. 一年大约有 $3.156\times10^7$ 秒
    编写一个程序，提示用户输入年龄，然后显示该年龄对应的秒数

    6. 1 个水分子的质量约为 $3.0\times10^{-23}$ 克
    1 夸脱水约为 950 克
    编写一个程序，提示用户输入水的夸脱数，并显示水分子的数量

    7. 1 英寸相当于 2.54 厘米
    编写一个程序，提示用户输入身高 (英寸)，然后以厘米为单位显示身高

    8. 在美国的体积测量系统中，1 品脱等于 2 杯，1 杯等于 8 盎司
    1 盎司等于 2 大汤勺，1 大汤勺等于 3 茶勺
    编写一个程序，提示用户输入杯数，并以品脱，盎司，汤勺，茶勺为单位显示等价容量
    并说明该程序为何使用浮点类型比整数类型更合适
