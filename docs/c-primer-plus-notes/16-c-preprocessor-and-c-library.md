# 第16章 C预处理器和C库

## 类对象宏

!!! abstract "语法形式"

    ```c
    #define 宏名 替换体
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define TWO 2
    #define FOUR TWO * TWO
    #define PX printf("X is %d.\n", x)
    int main(void)
    {
        int x = TWO;
        PX;
        x = FOUR;
        printf("X is %d.\n", x);
        return 0;
    }
    ```

    输出：

    ```text
    X is 2.
    X is 4.
    ```

!!! note "说明"

    - 一行 `#define` 由指令，宏名，替换体三部分组成
    - 宏名不能有空格，只能由字母，数字，下划线组成
    - 首字符不能是数字
    - 替换体可以是常量，表达式，甚至整条语句
    - 预处理器只替换记号，不做计算，不对表达式求值
    - 替换体中若还有宏，继续展开
    - 双引号内的同名文本不替换
    - 定义从指令处生效，到文件末尾或 `#undef` 为止
    - 宏常量属于整型常量表达式，可用作数组大小
    - `const` 变量不是 C 的整型常量表达式，不能用于文件作用域的数组大小

!!! warning "常见错误"

    - 以为 `x = FOUR;` 在预处理阶段就算出 `4`
    - 在字符串里写宏名，期望它被替换

## 宏定义续行

!!! abstract "语法形式"

    ```c
    #define 宏名 替换体\
    续行内容
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define OW "Consistency is the last refuge of the \
    unimaginative. - Oscar Wilde"
    int main(void)
    {
        printf("%s\n", OW);
        return 0;
    }
    ```

    输出：

    ```text
    Consistency is the last refuge of the unimaginative. - Oscar Wilde
    ```

!!! note "说明"

    - 反斜杠紧接换行符时，两者一起被删除
    - 多个物理行由此拼成一个逻辑行
    - 宏定义必须是一条逻辑行，长定义靠续行书写
    - 续行的缩进会进入替换体，字符串中因此多出空格
    - `_Generic` 的多行标签也用同样的写法

!!! warning "常见错误"

    - 反斜杠前留了空格，该空格成为字符串的一部分
    - 把代码中的 `\n` 当成续行符，这里只认按回车产生的换行

## 重定义宏

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SIX 2 * 3
    #define SIX 2 * 3
    int main(void)
    {
        printf("%d\n", SIX);
        return 0;
    }
    ```

    输出：

    ```text
    6
    ```

!!! note "说明"

    - 新定义与旧定义的记号序列完全相同才允许重定义
    - 空白的多少不影响记号序列，替换体按记号比较
    - `2 * 3` 是三个记号，`2*3` 是一个记号
    - 要换成不同的定义，先用 `#undef` 取消原定义
    - 需要可重定义的常量时，用 `const` 加作用域规则更简单

## 类函数宏

!!! abstract "语法形式"

    ```c
    #define 宏名(参数表) 替换体
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SQUARE(X) X*X
    #define PR(X) printf("result = %d\n", X)
    int main(void)
    {
        int x = 5;
        PR(SQUARE(x));
        PR(SQUARE(2));
        return 0;
    }
    ```

    输出：

    ```text
    result = 25
    result = 4
    ```

!!! note "说明"

    - 调用写法与函数调用相同，替换发生在编译之前
    - 替换的是实参记号，不是实参的值
    - 形参名在替换体中原样出现，由实参记号逐一顶替
    - 宏不做类型检查，一个定义可用于多种类型
    - 展开结果是内联代码，没有建立调用与返回的开销
    - 参数表左括号必须紧接宏名，中间不能有空格

!!! warning "常见错误"

    - 写成 `#define SQUARE (X) X*X`，宏名与括号间的空格使参数表失效

## 宏参数的括号

!!! example "示例"

    ```c
    #include <stdio.h>
    #define BAD(X) X*X
    #define GOOD(X) ((X)*(X))
    int main(void)
    {
        int x = 5;
        printf("%d %d\n", BAD(x + 2), GOOD(x + 2));
        printf("%d %d\n", 100 / BAD(2), 100 / GOOD(2));
        return 0;
    }
    ```

    输出：

    ```text
    17 49
    100 25
    ```

!!! note "说明"

    - 参数不加括号时，低优先级的实参被拆开参与运算
    - `BAD(x + 2)` 展开为 `x + 2*x + 2`，得 `17`
    - 替换体不加括号时，宏整体被外部运算符拆开
    - `100/BAD(2)` 展开为 `100/2*2`，从左往右算得 `100`
    - 参数与整个替换体都要加圆括号
    - 圆括号只保证运算顺序，不消除副作用

!!! warning "常见错误"

    - 把 `++x` 作为宏实参，参数在替换体中出现两次就自增两次
    - 依赖自增顺序，`++x*++x` 属未定义行为

    [函数调用先求实参的值再传值，`square(++x)` 只自增一次]

## 字符串化运算符 `#`

!!! abstract "语法形式"

    ```c
    #define 宏名(参数) "文本" #参数 "文本"
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define PSQR(x) printf("The square of " #x " is %d.\n", \
                           ((x)*(x)))
    int main(void)
    {
        int y = 5;
        PSQR(y);
        PSQR(2 + 4);
        return 0;
    }
    ```

    输出：

    ```text
    The square of y is 25.
    The square of 2 + 4 is 36.
    ```

!!! note "说明"

    - `#` 把宏实参转换成字符串字面量，称为字符串化
    - 转换结果保留实参的原样写法，包括其中的空格
    - 相邻的字符串字面量自动拼接成一个
    - `#` 只能出现在类函数宏的替换体中
    - 双引号内的参数名不被替换，取名字只能借 `#`
    - `#` 取实参的原始记号文本，实参中的宏不再展开

## 记号黏合运算符 `##`

!!! example "示例"

    ```c
    #include <stdio.h>
    #define XNAME(n) x ## n
    #define PRINT_XN(n) printf("x" #n " = %d\n", x ## n)
    int main(void)
    {
        int XNAME(1) = 14;
        int XNAME(2) = 20;
        PRINT_XN(1);
        PRINT_XN(2);
        return 0;
    }
    ```

    输出：

    ```text
    x1 = 14
    x2 = 20
    ```

!!! note "说明"

    - `##` 把左右两个记号合并成一个记号
    - 可用于类函数宏，也可用于类对象宏
    - 常与 `#` 配合，由同一个实参同时生成变量名与文本
    - 合并结果必须是合法记号，否则行为未定义
    - 两侧的空格在合并后消失

## 可变参数宏

!!! abstract "语法形式"

    ```c
    #define 宏名(固定参数, ...) 替换体
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define PR(X, ...) printf("Message " #X ": " __VA_ARGS__)
    int main(void)
    {
        double x = 48;
        PR(1, "x = %g\n", x);
        PR(2, "x = %d\n", 7);
        return 0;
    }
    ```

    输出：

    ```text
    Message 1: x = 48
    Message 2: x = 7
    ```

!!! note "说明"

    - `...` 表示数量可变的实参，只能放在参数表末尾
    - `__VA_ARGS__` 展开为 `...` 对应的全部实参，含分隔的逗号
    - `__VA_ARGS__` 只能出现在替换体中
    - 固定参数部分照常可用 `#` 与 `##`
    - 标准要求调用时 `...` 至少对应一个实参
    - C23 增加 `__VA_OPT__(内容)`，实参为空时展开为空

!!! warning "常见错误"

    - 写成 `#define WRONG(X, ..., Y)`，省略号不在末尾
    - 调用 `PR()` 时省略号部分为空，C99 与 C11 下不可移植

    [空实参的写法在 C23 之前没有标准支持，依靠 `__VA_OPT__` 才能安全处理]

## 文件包含 `#include`

!!! abstract "语法形式"

    ```c
    #include <文件名>
    #include "文件名"
    ```

!!! example "示例"

    ```c
    #include <stdio.h>      /* 在系统目录中查找 */
    #include "names.h"      /* 先在当前目录中查找 */
    ```

!!! note "说明"

    - 尖括号形式在系统头文件目录中查找
    - 双引号形式先查当前目录或指定目录，找不到再查系统目录
    - 被包含文件的内容在指令所在位置展开
    - 头文件常放 `#define`，结构声明，`typedef`，函数原型
    - 函数定义一般不放在头文件，内联函数是例外
    - 单个头文件常被多处包含，需加保护防止重复处理
    - 包含大型头文件一般不会显著增大最终程序
    - 头文件只提供声明，对应源文件仍须单独编译并链接

!!! warning "常见错误"

    - 以为包含头文件就等于链接了库函数
    - 在同一程序中用引号形式包含标准头文件

## 取消宏 `#undef`

!!! example "示例"

    ```c
    #include <stdio.h>
    #define LIMIT 400
    #undef LIMIT
    #define LIMIT 100
    int main(void)
    {
        printf("%d\n", LIMIT);
        return 0;
    }
    ```

    输出：

    ```text
    100
    ```

!!! note "说明"

    - `#undef 名字` 取消已有的宏定义，之后可以重新定义
    - 名字本来未定义时，该指令仍然合法
    - 宏的作用范围到 `#undef` 或文件末尾为止
    - 不确定一个名字是否已被使用过时，先 `#undef` 再定义

## 条件编译 `#ifdef`

!!! abstract "语法形式"

    ```c
    #ifdef 标识符
        代码组 1
    #else
        代码组 2
    #endif
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define JUST_CHECKING
    int main(void)
    {
        int i, total = 0;
        for (i = 1; i <= 4; i++)
        {
            total += 2 * i * i + 1;
    #ifdef JUST_CHECKING
            printf("i=%d, total=%d\n", i, total);
    #endif
        }
        printf("Grand total = %d\n", total);
        return 0;
    }
    ```

    输出：

    ```text
    i=1, total=3
    i=2, total=12
    i=3, total=31
    i=4, total=64
    Grand total = 64
    ```

!!! note "说明"

    - 标识符已定义时保留第一组代码，跳过 `#else` 之后的部分
    - 标识符未定义时保留 `#else` 与 `#endif` 之间的代码
    - `#endif` 必须存在，`#else` 可以省略
    - 条件块可以嵌套
    - 预处理器不识别花括号，用 `#else` 与 `#endif` 划分代码块
    - 删除 `#define JUST_CHECKING` 后重新编译，只输出总计
    - 这种写法常用于调试输出开关

## 条件编译 `#ifndef`

!!! example "示例"

    ```c
    #include <stdio.h>
    #ifndef SIZE
    #define SIZE 100
    #endif
    int main(void)
    {
        int a[SIZE];
        printf("%zu\n", sizeof a / sizeof a[0]);
        return 0;
    }
    ```

    输出：

    ```text
    100
    ```

!!! note "说明"

    - `#ifndef` 判断标识符未定义，逻辑与 `#ifdef` 相反
    - 常用作常量的默认值： 外部先定义则沿用，未定义则取名
    - 可与 `#else` 和 `#endif` 配合
    - 先 `#define SIZE 10` 再包含该文件，数组大小变成 `10`

## 头文件保护

!!! example "示例"

    ```c
    /* things.h */
    #ifndef THINGS_H_
    #define THINGS_H_
    #include <string.h>
    #define SLEN 32
    struct names_st
    {
        char first[SLEN];
        char last[SLEN];
    };
    typedef struct names_st names;
    void show_names(const names *);
    #endif
    ```

!!! note "说明"

    - 首次包含时标识符未定义，定义它并处理文件其余部分
    - 再次包含时标识符已定义，整个文件被跳过
    - 结构声明一类内容只能在一个文件中出现一次，因此需要保护
    - 标识符惯例为文件名大写，点换成下划线
    - 不要以下划线开头，下划线开头的名字由标准保留
    - 头文件被多个文件包含是常态，保护不可省

## 条件编译 `#if` 与 `#elif`

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SYS 2
    int main(void)
    {
    #if SYS == 1
        puts("ibmpc");
    #elif SYS == 2
        puts("vax");
    #else
        puts("general");
    #endif
        return 0;
    }
    ```

    输出：

    ```text
    vax
    ```

!!! note "说明"

    - `#if` 后跟整型常量表达式，非零为真
    - 表达式中可用关系运算符与逻辑运算符
    - `#elif` 提供多路分支，与 `else if` 对应
    - `defined 名字` 判断名字是否已定义，结果为 `1` 或 `0`
    - `defined` 可写在 `#if` 与 `#elif` 中，`#ifdef` 不能接 `#elif`
    - 未定义名字在 `#if` 中按 `0` 处理

!!! warning "常见错误"

    - 在 `#if` 中使用运行时变量，预处理器看不到变量

## 预定义宏

!!! abstract "语法形式"

    表16-1 预定义宏

    | 宏 | 含义 |
    |---|---|
    | `__DATE__` | 预处理日期，形如 `"Mmm dd yyyy"` |
    | `__FILE__` | 当前源文件名的字符串字面量 |
    | `__LINE__` | 当前行号的整型常量 |
    | `__STDC__` | 遵循 C 标准时为 `1` |
    | `__STDC_HOSTED__` | 本机环境为 `1`，否则为 `0` |
    | `__STDC_VERSION__` | C99 为 `199901L`，C11 为 `201112L` |
    | `__TIME__` | 翻译代码的时间，形如 `"hh:mm:ss"` |

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        printf("%s\n", __FILE__);
        printf("%d\n", __LINE__);
        printf("%s\n", __func__);
        printf("%ld\n", __STDC_VERSION__);
        printf("%s\n", __DATE__);
        printf("%s\n", __TIME__);
        return 0;
    }
    ```

!!! note "说明"

    - 预定义宏由实现提供，不必 `#define`，也不能 `#undef`
    - `__func__` 是预定义标识符，不是宏，具有函数作用域
    - `__LINE__` 与 `__FILE__` 随位置变化，可用于定位输出
    - `__STDC_VERSION__` 是长整型常量，打印用 `%ld`
    - 日期与时间取编译时刻，不是运行时刻

    [教材表格只列到 C11
    - C17 的值为 `201710L`，C23 的值为 `202311L`]

## `#line`

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
    #line 1000
        printf("%d\n", __LINE__);
    #line 10 "cool.c"
        printf("%s %d\n", __FILE__, __LINE__);
        return 0;
    }
    ```

    输出：

    ```text
    1000
    cool.c 10
    ```

!!! note "说明"

    - `#line 行号` 重置其后的行号计数
    - `#line 行号 "文件名"` 同时重置文件名
    - 只影响 `__LINE__` 与 `__FILE__` 的取值，不移动物理行
    - 行号必须是正整数常量
    - 多用于代码生成器与预处理器的输出

## `#error`

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
    #if __STDC_VERSION__ != 201112L
    #error Not C11
    #endif
        puts("compiled as C11");
        return 0;
    }
    ```

    输出：

    ```text
    error: #error Not C11
    ```

!!! note "说明"

    - 预处理阶段发出诊断信息，消息文本就是指令后的内容
    - 编译器一般就此中止，不再编译
    - 常与 `#if` 配合，检查实现或宏组合是否满足要求
    - 消息不必加引号，整行剩余文本都算消息

## `#pragma`

!!! example "示例"

    ```c
    #include <stdio.h>
    #pragma pack(push, 1)
    struct record
    {
        char c;
        int i;
    };
    #pragma pack(pop)
    int main(void)
    {
        printf("%zu\n", sizeof(struct record));
        return 0;
    }
    ```

    输出：

    ```text
    5
    ```

!!! note "说明"

    - `#pragma` 把编译器专用的指令写进源代码
    - 指令内容由实现定义，不属于可移植部分
    - 常见用途有修改结构对齐，开关警告，控制优化
    - `_Pragma("指令")` 与 `#pragma 指令` 等价
    - `_Pragma` 不以 `#` 开头，可以在宏展开中使用
    - `_Pragma` 的参数是字符串，其中的转义序列按字符串规则还原

!!! warning "常见错误"

    - 在宏定义中直接使用 `#pragma`，`#` 会被当作字符串化运算符

## 泛型选择 `_Generic`

!!! abstract "语法形式"

    ```c
    _Generic(表达式, 类型1: 值1, 类型2: 值2, default: 值3)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define MYTYPE(X) _Generic((X), \
        int: "int", \
        float: "float", \
        double: "double", \
        default: "other")
    int main(void)
    {
        int d = 5;
        printf("%s\n", MYTYPE(d));
        printf("%s\n", MYTYPE(2.0 * d));
        printf("%s\n", MYTYPE(3L));
        printf("%s\n", MYTYPE(&d));
        return 0;
    }
    ```

    输出：

    ```text
    int
    double
    other
    other
    ```

!!! note "说明"

    - 第一项是待判别的表达式，其后每项形如 `类型: 值`
    - 按第一项的类型选择标签，不对该表达式求值
    - 类型都不匹配时取 `default`，没有 `default` 则为编译错误
    - 只对被选中的标签后的表达式求值
    - 判别前先做数组到指针，函数到指针与顶层限定符的转换
    - 常与 `#define` 组合，用一个名字分派到不同类型的函数

!!! warning "常见错误"

    - 把 `_Generic` 当作运行时判断，它只按静态类型选择
    - 以为标签可以写复合类型而漏掉指针形式的写法

## 内联函数 `inline`

!!! abstract "语法形式"

    ```c
    static inline 返回类型 函数名(参数表)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    static inline int square(int x)
    {
        return x * x;
    }
    int main(void)
    {
        printf("%d\n", square(5));
        return 0;
    }
    ```

    输出：

    ```text
    25
    ```

!!! note "说明"

    - `inline` 是函数说明符，作用是建议编译器内联展开
    - 是否内联由实现决定，标准不保证展开
    - 内联函数的定义与调用须在同一文件中，常配 `static`
    - 多个文件共用的内联函数放在头文件中，每个包含者各有一份
    - 取内联函数的地址时，编译器会另生成非内联版本
    - 内联函数不占单独的代码块，调试器中不一定能单步进入
    - 函数体宜短，长函数内联的收益有限
    - C 允许内联定义与外部定义混用，与 C++ 的规则不同

## `_Noreturn` 函数

!!! abstract "语法形式"

    ```c
    _Noreturn void 函数名(参数表)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    _Noreturn void die(const char *msg)
    {
        puts(msg);
        exit(EXIT_FAILURE);
    }
    int main(void)
    {
        die("stop");
        return 0;
    }
    ```

    输出：

    ```text
    stop
    ```

!!! note "说明"

    - `_Noreturn` 声明函数不会把控制返回主调函数
    - 与 `void` 返回类型不同： `void` 函数执行完仍会返回，只是不带值
    - `exit()` 与 `abort()` 是典型例子
    - 告知编译器后，可以省略调用之后的代码并抑制相关警告
    - 函数体内每条路径都不能返回，否则行为未定义
    - C23 另提供 `[[noreturn]]` 属性写法

## 数学库 `math.h`

!!! abstract "语法形式"

    表16-2 math.h 的常用函数

    | 原型 | 说明 |
    |---|---|
    | `double sqrt(double x)` | `x` 的平方根，`x` 不能为负 |
    | `double cbrt(double x)` | `x` 的立方根 |
    | `double pow(double x, double y)` | `x` 的 `y` 次幂 |
    | `double exp(double x)` | `e` 的 `x` 次幂 |
    | `double log(double x)` | `x` 的自然对数 |
    | `double log10(double x)` | `x` 的常用对数 |
    | `double fabs(double x)` | `x` 的绝对值 |
    | `double ceil(double x)` | 不小于 `x` 的最小整数 |
    | `double floor(double x)` | 不大于 `x` 的最大整数 |
    | `double sin(double x)` | `x` 的正弦，`x` 以弧度计 |
    | `double cos(double x)` | `x` 的余弦，`x` 以弧度计 |
    | `double tan(double x)` | `x` 的正切，`x` 以弧度计 |
    | `double asin(double x)` | 正弦值为 `x` 的角度，范围 -π/2 到 π/2 |
    | `double acos(double x)` | 余弦值为 `x` 的角度，范围 0 到 π |
    | `double atan(double x)` | 正切值为 `x` 的角度，范围 -π/2 到 π/2 |
    | `double atan2(double y, double x)` | `y/x` 的反正切，范围 -π 到 π |

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <math.h>
    int main(void)
    {
        double x = 2.0, y = -3.0;
        printf("%.3f %.3f\n", sqrt(x), fabs(y));
        printf("%.3f %.3f\n", pow(x, 3), log(exp(1.0)));
        printf("%.3f %.3f\n", ceil(2.3), floor(2.7));
        printf("%.3f\n", atan2(1.0, 1.0) * 180 / (4 * atan(1)));
        return 0;
    }
    ```

    输出：

    ```text
    1.414 3.000
    8.000 1.000
    3.000 2.000
    45.000
    ```

!!! note "说明"

    - 三角函数与反三角函数的参数和返回值都以弧度计
    - 弧度转度乘 `180/π`，度转弧度乘 `π/180`
    - `atan2(y, x)` 由两个参数的符号确定象限，`atan(y/x)` 会丢失象限
    - 链接时数学库可能要单独指定，GCC 加 `-lm` 并放在命令行末尾
    - `float` 与 `long double` 版本在函数名后加 `f` 或 `l`
    - 包含 `tgmath.h` 后，`sqrt` 等名字变成按实参类型分派的泛型宏
    - 要强制调用真正的函数，写成 `(sqrt)(x)`

!!! warning "常见错误"

    - 认为 `sqrt()` 返回平方值，它返回平方根
    - 忽略 `atan2()` 的参数顺序，写成 `atan2(x, y)`

    [教材表中 `sqrt` 写作"平方值"，`cbrt` 写作"立方值"
    - `atan2` 写作"正弦值为 y/x"，均为笔误]

## `exit()` 与 `atexit()`

!!! abstract "语法形式"

    ```c
    void exit(int 状态);
    int atexit(void (*函数)(void));
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    void bye(void);
    int main(void)
    {
        atexit(bye);
        puts("running");
        exit(EXIT_SUCCESS);
    }
    void bye(void)
    {
        puts("bye");
    }
    ```

    输出：

    ```text
    running
    bye
    ```

!!! note "说明"

    - `atexit(函数名)` 把函数注册到退出时调用的列表
    - 注册函数的执行顺序与注册顺序相反
    - 注册函数不带参数，返回类型为 `void`
    - 标准保证至少可注册 32 个函数
    - `main()` 正常结束等同于隐式调用 `exit()`
    - `exit()` 先执行注册函数，再刷新并关闭所有流
    - `EXIT_SUCCESS` 与 `EXIT_FAILURE` 定义在 `stdlib.h`
    - 在任意函数中调用 `exit()` 都终止整个程序
    - 返回状态为 `0` 也表示成功，`EXIT_FAILURE` 便于移植

## 排序 `qsort()`

!!! abstract "语法形式"

    ```c
    void qsort(void *base, size_t nmemb, size_t size,
               int (*compar)(const void *, const void *));
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int comp(const void *p1, const void *p2)
    {
        const int *a1 = p1, *a2 = p2;
        return (*a1 > *a2) - (*a1 < *a2);
    }
    int main(void)
    {
        int a[5] = {3, 1, 4, 1, 5}, i;
        qsort(a, 5, sizeof(int), comp);
        for (i = 0; i < 5; i++)
            printf("%d ", a[i]);
        return 0;
    }
    ```

    输出：

    ```text
    1 1 3 4 5
    ```

!!! note "说明"

    - 第一个参数是数组首地址，类型为 `void *`
    - 第二个参数是待排序元素的个数
    - 第三个参数是单个元素的字节数，常写 `sizeof 类型`
    - 第四个参数是比较函数的指针，函数名直接传入即可
    - 比较函数返回负数表示第一项排在前，返回 `0` 表示相等
    - 比较函数内先把 `void *` 转成具体类型指针，再解引用
    - 为通用性，元素大小与类型都通过参数告知 `qsort()`
    - `qsort()` 不保证稳定排序
    - C 中从 `void *` 赋给具体类型指针可以不加强制转换，C++ 必须加

## 断言 `assert()`

!!! abstract "语法形式"

    ```c
    void assert(整型表达式);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <assert.h>
    int main(void)
    {
        int n = -1;
        assert(n >= 0);
        printf("%d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    Assertion failed: n >= 0, file assert.c, line 6
    ```

!!! note "说明"

    - 表达式值为 `0` 时触发，值为非零时什么也不做
    - 触发时向 `stderr` 写出测试文本，文件名与行号
    - 随后调用 `abort()` 终止程序，不执行 `atexit()` 注册的函数
    - 头文件为 `assert.h`，`abort()` 的原型在 `stdlib.h`
    - 在包含 `assert.h` 之前定义 `NDEBUG`，所有 `assert` 变成空操作
    - 关闭后参数表达式不再求值，参数中不要放有副作用的操作
    - `assert` 用于检查不应发生的前提，不代替正常的错误处理
    - 报错文本的格式随实现而异

!!! warning "常见错误"

    - 以为 `assert` 只在表达式为真时报警，判据正好相反
    - 用 `assert` 检查用户输入，发布版本中该检查会消失

    [教材此处写作"求值为假(非零)"，判据应为"值为 0"; 且关闭时表达式本身不求值]

## 静态断言 `_Static_assert`

!!! abstract "语法形式"

    ```c
    _Static_assert(整型常量表达式, "消息");
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <limits.h>
    _Static_assert(CHAR_BIT == 8, "8-bit char assumed");
    int main(void)
    {
        _Static_assert(sizeof(double) == 2 * sizeof(int),
                       "double not twice int size");
        puts("ok");
        return 0;
    }
    ```

    输出：

    ```text
    ok
    ```

!!! note "说明"

    - 在编译期检查第一个参数，不生成运行时代码
    - 第一个参数必须是整型常量表达式，`sizeof` 表达式可用
    - 值为 `0` 时显示消息并拒绝编译
    - 按声明处理，可写在函数内，也可写在所有函数之外
    - 与 `assert` 的差别在于检查时刻： 一个编译期，一个运行期
    - 运行期才成立的条件不能用 `_Static_assert`
    - C23 起可省略消息，写成 `static_assert(表达式)`

## 可变参数函数 `stdarg.h`

!!! abstract "语法形式"

    ```c
    返回类型 函数名(固定参数, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdarg.h>
    double sum(int lim, ...)
    {
        va_list ap;
        double total = 0;
        int i;
        va_start(ap, lim);
        for (i = 0; i < lim; i++)
            total += va_arg(ap, double);
        va_end(ap);
        return total;
    }
    int main(void)
    {
        printf("%g\n", sum(3, 1.1, 2.5, 13.3));
        return 0;
    }
    ```

    输出：

    ```text
    16.9
    ```

!!! note "说明"

    - 原型中至少有一个固定参数，省略号放在参数表末尾
    - 省略号前的形参称 `parmN`，常用来传入可变参数的个数
    - `va_list` 类型保存省略号部分的实参
    - `va_start(ap, parmN)` 初始化参数列表
    - `va_arg(ap, 类型)` 依次取出下一项，类型必须与实际实参一致
    - `va_end(ap)` 结束使用，之后须重新 `va_start` 才能再用
    - `va_copy(dest, src)` 复制列表，用于重复遍历
    - 默认实参提升仍生效，`float` 提升为 `double`，小整型提升为 `int`
    - 函数无法自行得知实参个数，必须由固定参数告知

!!! warning "常见错误"

    - 把 `10` 传给以 `double` 取出的位置，类型不匹配导致结果错误
    - 写成 `double f3(...)`，省略号前没有固定参数

## 时间函数 `time.h`

!!! abstract "语法形式"

    表16-3 time.h 的常用函数

    | 原型 | 说明 |
    |---|---|
    | `time_t time(time_t *ptr)` | 返回当前日历时间，单位秒 |
    | `clock_t clock(void)` | 返回处理器时间，失败返回 `-1` |
    | `double difftime(time_t t1, time_t t0)` | 两时间之差，单位秒 |
    | `char *ctime(const time_t *tp)` | 把日历时间转成字符串 |

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <time.h>
    int main(void)
    {
        clock_t start, end;
        double elapsed;
        start = clock();
        while (clock() - start < CLOCKS_PER_SEC)
            continue;
        end = clock();
        elapsed = (double) (end - start) / CLOCKS_PER_SEC;
        printf("%.2f\n", elapsed);
        return 0;
    }
    ```

    输出：

    ```text
    1.00
    ```

!!! note "说明"

    - `clock()` 返回处理器时间，单位由实现决定
    - `CLOCKS_PER_SEC` 是每秒的时钟单位数
    - 两次 `clock()` 之差除以 `CLOCKS_PER_SEC` 得到秒数
    - 相减前转成 `double`，结果才保留小数
    - `time(NULL)` 返回当前时间，常用作 `srand()` 的种子
    - `time_t` 与 `clock_t` 由实现定义为某种整数类型
    - `difftime()` 用 `double` 表示两个 `time_t` 的差

## 复习题

（1）下面的几组代码由一个或多个宏组成，其后是使用宏的源代码
每种情况下代码的结果是什么，这些代码是否有效
假设其中的变量已声明
a.
```c
#define FPM 5280 /* 每英里的英尺数 */
dist = FPM * miles;
```
b.
```c
#define FEET 4
#define POD FEET + FEET
plort = FEET * POD;
```
c.
```c
#define SIX = 6;
nex = SIX;
```
d.
```c
#define NEW(X) X + 5
y = NEW(y);
berg = NEW(berg) * lob;
est = NEW(berg) / NEW(y);
nilp = lob * NEW(-berg);
```

??? note "答案"

    a. `dist = 5280 * miles;` 有效
    b. `plort = 4 * 4 + 4;` 有效，得 `20`
    若需要 `4 * (4 + 4)`，应定义成 `#define POD (FEET + FEET)`
    c. `nex = = 6;;` 无效，预处理器只替换文本，定义中不写 `=`
    d. `y = y + 5;` 有效
    `berg = berg + 5 * lob;` 有效，但可能不是本意
    `est = berg + 5/y + 5;` 有效，但可能不是本意

（2）修改复习题 1 中 d 部分的定义，使其更可靠

??? note "答案"

    `#define NEW(X) ((X) + 5)`

（3）定义一个宏函数，返回两值中的较小值

??? note "答案"

    `#define MIN(X,Y) ( (X) < (Y) ? (X) : (Y) )`

（4）定义 `EVEN_GT(X, Y)` 宏，如果 `X` 为偶数且大于 `Y`，该宏返回 `1`

??? note "答案"

    `#define EVEN_GT(X,Y) ( (X) > (Y) && (X) % 2 == 0 ? 1 : 0 )`

（5）定义一个宏函数，打印两个表达式及其值
例如参数为 `3+4` 和 `4*12`，则打印
```c
3+4 is 7 and 4*12 is 48
```

??? note "答案"

    `#define PR(X,Y) printf(#X " is %d and " #Y " is %d\n", X,Y)`
    宏中没有运算符作用于 `X` 和 `Y`，所以不需要额外加圆括号

（6）创建 `#define` 指令完成下面的任务
a. 创建一个值为 25 的命名常量
b. `SPACE` 表示空格字符
c. `PS()` 代表打印空格字符
d. `BIG(X)` 代表 `X` 的值加 3
e. `SUMSQ(X, Y)` 代表 `X` 和 `Y` 的平方和

??? note "答案"

    a. `#define QUARTERCENTURY 25`
    b. `#define SPACE ' '`
    c. `#define PS() putchar(' ')` 或 `#define PS() putchar(SPACE)`
    d. `#define BIG(X) ((X) + 3)`
    e. `#define SUMSQ(X,Y) ((X)*(X) + (Y)*(Y))`

（7）定义一个宏，以下面的格式打印名称，值和 int 类型变量的地址
```c
name: fop; value: 23; address: ff464016
```

??? note "答案"

    `#define P(X) printf("name: "#X"; value: %d; address: %p\n", X, &X)`
    实现不支持 `%p` 时，可用 `%u` 或 `%lu` 代替

（8）假设在测试程序时要暂时跳过一块代码，如何在不移除这块代码的前提下完成

??? note "答案"

    用条件编译，例如

    ```c
    #define _SKIP_ /* 不需要跳过代码时删除这条指令 */
    #ifndef _SKIP_
    /* 需要跳过的代码 */
    #endif
    ```

（9）编写一段代码，如果定义了 `PR_DATE` 宏，则打印预处理的日期

??? note "答案"

    ```c
    #ifdef PR_DATE
        printf("Date = %s\n", __DATE__);
    #endif
    ```

（10）内联函数部分讨论了 3 种不同版本的 `square()` 函数
从行为方面看，这 3 种版本的函数有何不同

??? note "答案"

    第 1 版返回 `x*x`，即 `square()` 的 `double` 值
    例如 `square(1.3)` 返回 `1.69`
    第 2 版返回 `(int)(x*x)`，计算结果先截断再转回 `double`
    `1.69` 先变成 `1`，再变成 `1.00`
    第 3 版返回 `(int)(x*x + 0.5)`，加 `0.5` 后截断相当于四舍五入
    `1.69+0.5` 得 `2.19`，截断为 `2`，再转成 `2.00`
    `1.44+0.5` 得 `1.94`，截断为 `1`，再转成 `1.00`

（11）创建一个使用泛型选择表达式的宏
如果宏参数是 `_Bool` 类型，对 `"boolean"` 求值，否则对 `"not boolean"` 求值

??? note "答案"

    `#define BOOL(X) _Generic((X), _Bool : "boolean", default : "not boolean")`

（12）下面的程序有什么错误
```c
#include <stdio.h>
int main(int argc, char argv[])
{
    printf("The square root of %f is %f\n", argv[1],sqrt(argv[1]) );
}
```

??? note "答案"

    `argv` 应声明为 `char *argv[]`
    命令行参数以字符串形式存放，`argv[1]` 要先转成 `double`，例如用 `atof()`
    程序用了 `sqrt()`，应包含 `math.h`
    求平方根之前还应排除参数为负的情况，即检查参数大于或等于 `0`

（13）假设 `scores` 是内含 1000 个 `int` 类型元素的数组
要按降序排序该数组中的值，使用 `qsort()` 和 `comp()` 比较函数
a. 如何正确调用 `qsort()`
b. 如何正确定义 `comp()`

??? note "答案"

    a. `qsort(scores, 1000, sizeof(int), comp);`
    b.

    ```c
    int comp(const void * p1, const void * p2)
    {
        const int * a1 = (const int *) p1;
        const int * a2 = (const int *) p2;
        if (*a1 > *a2)
            return -1;
        else if (*a1 == *a2)
            return 0;
        else
            return 1;
    }
    ```

    在 C 中转换可选，在 C++ 中必须转换
    [附录答案第三个参数写作 `sizeof (double)`，与 `scores` 的 `int` 元素不符]

（14）假设 `data1` 是内含 100 个 `double` 类型元素的数组
`data2` 是内含 300 个 `double` 类型元素的数组
a. 编写 `memcpy()` 的函数调用，把 `data2` 中的前 100 个元素拷贝到 `data1`
b. 编写 `memcpy()` 的函数调用，把 `data2` 中的后 100 个元素拷贝到 `data1`

??? note "答案"

    a. `memcpy(data1, data2, 100 * sizeof(double));`
    b. `memcpy(data1, data2 + 200, 100 * sizeof(double));`

## 编程练习

!!! question "编程练习"

    1. 开发一个包含你需要的预处理器定义的头文件

    2. 两数的调和平均数这样计算
    先得到两数的倒数，再计算两个倒数的平均值，最后取结果的倒数
    使用 `#define` 指令定义一个宏"函数"执行该运算
    编写一个简单的程序测试该宏

    3. 极坐标用向量的模和向量相对 `x` 轴逆时针旋转的角度描述该向量
    直角坐标用向量的 `x` 轴和 `y` 轴坐标描述该向量
    编写一个程序，读取向量的模和角度(单位为度)
    然后显示 `x` 轴和 `y` 轴的坐标，相关方程如下

    ```c
    x = r*cos A    y = r*sin A
    ```

    需要一个函数完成转换
    该函数接受一个包含极坐标的结构，返回一个包含直角坐标的结构

    4. ANSI 库这样描述 `clock()` 函数

    ```c
    #include <time.h>
    clock_t clock (void);
    ```

    `clock_t` 是定义在 `time.h` 中的类型
    该函数返回处理器时间，单位取决于实现
    处理器时间不可用或无法表示时，返回 `-1`
    `CLOCKS_PER_SEC` 也定义在 `time.h` 中，表示每秒的处理器时间单位数
    两个 `clock()` 返回值之差除以 `CLOCKS_PER_SEC`，得到两次调用之间经过的秒数
    除法之前把值转成 `double`，可使时间精确到小数点以后
    编写一个函数，接受一个 `double` 类型的参数表示时间延迟数
    然后在这段时间运行一个循环，编写一个简单的程序测试该函数

    5. 编写一个函数接受这些参数
    内含 `int` 类型元素的数组名，数组的大小，一个代表选取次数的值
    该函数从数组中随机选择指定数量的元素并打印
    每个元素只能选择一次，模拟抽奖或挑选陪审团成员
    实现有 `time()` 时，可在 `srand()` 中用它的输出初始化随机数生成器
    编写一个简单的程序测试该函数

    6. 修改程序清单 16.17，使用 `struct names` 元素代替 `double` 类型的数组
    使用较少的元素，并用选定的名字显式初始化数组

    7. 下面是使用变参函数的一个程序段

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <stdarg.h>
    void show_array(const double ar[], int n);
    double * new_d_array(int n, ...);

    int main()
    {
        double * p1;
        double * p2;

        p1 = new_d_array(5, 1.2, 2.3, 3.4, 4.5, 5.6);
        p2 = new_d_array(4, 100.0, 20.00, 8.08, -1890.0);
        show_array(p1, 5);
        show_array(p2, 4);
        free(p1);
        free(p2);

        return 0;
    }
    ```

    `new_d_array()` 接受一个 `int` 类型参数和若干 `double` 类型参数
    该函数返回一个指针，指向由 `malloc()` 分配的内存块
    `int` 类型的参数指定动态数组中的元素个数
    `double` 类型的值用于初始化元素，第 1 个值赋给第 1 个元素
    编写 `show_array()` 和 `new_d_array()` 的代码，完成这个程序
