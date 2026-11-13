# 第5章 运算符、表达式和语句

## `while` 循环

!!! abstract "语法形式"

    `while (测试条件)` 后接一条语句，或后接花括号组成的块

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int shoe = 3;

        while (shoe < 6)
        {
            printf("%d\n", shoe);
            shoe = shoe + 1;
        }
        printf("done\n");
        return 0;
    }
    ```

    输出：

    ```text
    3
    4
    5
    done
    ```

!!! note "说明"

    - 先判断测试条件，条件为真时执行循环体
    - 循环体执行完回到条件处再次判断
    - 条件为假时转到循环后的第一条语句
    - 循环体有多条语句时用花括号组成一个块
    - 每轮循环必须修改被测试的变量，否则形成死循环

!!! warning "常见错误"

    - `while (shoe < 6);` 在条件后多写分号，循环体变成空语句
    - 循环体内不修改 `shoe`，条件始终为真

## 赋值运算符 `=`

!!! abstract "语法形式"

    `变量 = 表达式;`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int bmw;

        bmw = 2002;
        printf("%d\n", bmw);
        return 0;
    }
    ```

    输出：

    ```text
    2002
    ```

!!! note "说明"

    - `=` 不表示相等，表示把右侧的值存入左侧的变量
    - 该语句的意思是，把值 2002 赋给变量 bmw
    - 赋值从右往左进行
    - 赋值表达式的值与赋值后左侧变量的值相同

!!! warning "常见错误"

    - `2002 = bmw;` 左侧必须是可修改的左值
    - `bmw + 1 = 2002;` 左侧是表达式，不是可修改的左值

## 链式赋值

!!! abstract "语法形式"

    `a = b = c = 表达式;`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int jane, tarzan, cheeta;

        cheeta = tarzan = jane = 68;
        printf("%d %d %d\n", cheeta, tarzan, jane);
        return 0;
    }
    ```

    输出：

    ```text
    68 68 68
    ```

!!! note "说明"

    - `=` 的结合性是从右往左
    - 先计算 `jane = 68`，再把该表达式的值赋给 `tarzan`
    - 最后赋给 `cheeta`
    - 三个变量得到同一个值

## 左值与可修改的左值

!!! abstract "语法形式"

    `可修改的左值 = 右值`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int ex, why = 42, zee = 8;
        const int TWO = 2;

        ex = TWO * (why + zee);
        printf("%d\n", ex);
        return 0;
    }
    ```

    输出：

    ```text
    100
    ```

!!! note "说明"

    - 数据对象： 用于储存值的内存区域
    - 左值： 标识数据对象的名称或表达式
    - 可修改的左值： 能放在 `=` 左侧的左值
    - `const` 变量是左值，但不是可修改的左值
    - 右值： 能赋给可修改的左值，本身不是左值的量
    - `42` 与 `(why + zee)` 都是右值，没有固定的内存位置

!!! warning "常见错误"

    - `TWO = 3;` 给 `const` 变量赋值
    - `(why + zee) = 5;` 给右值赋值

## 二元运算符 `+` `-`

!!! abstract "语法形式"

    `a + b` 或 `a - b`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int salary = 100, bribes = 20;
        int income;

        income = salary + bribes;
        printf("%d\n", income);
        return 0;
    }
    ```

    输出：

    ```text
    120
    ```

!!! note "说明"

    - `+` 把两侧的值相加，`-` 用左侧的值减去右侧的值
    - 运算对象可以是变量，也可以是常量
    - 需要两个运算对象的运算符称为二元运算符
    - `salary + bribes` 整体是右值

## 一元符号运算符 `+` `-`

!!! abstract "语法形式"

    `-x` 或 `+x`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int rocky = 12;
        int smokey = -rocky;

        printf("%d %d\n", smokey, rocky);
        return 0;
    }
    ```

    输出：

    ```text
    -12 12
    ```

!!! note "说明"

    - 一元运算符只需要一个运算对象
    - 一元 `-` 改变值的符号，不改变运算对象本身
    - 一元 `+` 不改变值，也不改变符号，C90 起可用
    - `rocky = -12;` 中的 `-` 同样是一元运算符

## 乘法运算符 `*`

!!! abstract "语法形式"

    `a * b`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int num = 3;

        printf("%d %d\n", num, num * num);
        return 0;
    }
    ```

    输出：

    ```text
    3 9
    ```

!!! note "说明"

    - `*` 把两侧的值相乘
    - C 没有指数运算符，平方写成 `num * num`
    - 指数运算调用 `math.h` 中的 `pow()`，例如 `pow(3.5, 2.2)`

## 除法运算符 `/`

!!! abstract "语法形式"

    `a / b`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("%d %d\n", 5 / 4, 7 / 4);
        printf("%.2f %.2f\n", 7. / 4., 7. / 4);
        return 0;
    }
    ```

    输出：

    ```text
    1 1
    1.75 1.75
    ```

!!! note "说明"

    - 两个整数相除时结果取整数，小数部分被丢弃，称为截断
    - 有一个运算对象是浮点数时，结果就是浮点数
    - 混合类型时，编译器先把整数转换成浮点数再除
    - 截断不四舍五入，`5 / 4` 得 1，`7 / 4` 得 1
    - C99 规定整数除法向零截断，`-7 / 4` 得 -1

!!! warning "常见错误"

    - `1 / 2` 得 0，要得到 0.5 应写 `1.0 / 2`

## 运算符优先级与结合性

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        double n = 6.0, SCALE = 2.0;
        double butter;

        butter = 25.0 + 60.0 * n / SCALE;
        printf("%.1f\n", butter);
        return 0;
    }
    ```

    输出：

    ```text
    205.0
    ```

!!! note "说明"

    - 优先级高的运算符先计算，同级的按结合性决定次序
    - `60.0 * n` 先算，再除以 `SCALE`，最后加上 `25.0`
    - 圆括号内的部分最先执行，圆括号可以改变次序
    - `(25.0 + 60.0 * n) / SCALE` 得到 192.5

    表5-1 运算符优先级

    | 运算符 | 结合性 |
    | --- | --- |
    | `()` | 左 |
    | `++` `--` (后缀) | 左 |
    | `++` `--` (前缀)，`+` `-` (一元)，`sizeof`，`(类型名)` | 右 |
    | `*` `/` `%` | 左 |
    | `+` `-` (二元) | 左 |
    | `=` | 右 |

!!! warning "常见错误"

    - 按从左到右依次计算，忽略乘除高于加减

## 优先级与求值顺序

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int top, score;

        top = score = -(2 + 5) * 6 + (4 + 3 * (2 + 3));
        printf("%d %d\n", top, score);
        return 0;
    }
    ```

    输出：

    ```text
    -23 -23
    ```

!!! note "说明"

    - 优先级只决定运算符与哪个运算对象结合
    - 两个同级子表达式先算哪个，标准不作规定
    - `6 * 12 + 5 * 20` 中两个乘法谁先算不影响结果
    - 结合性只在两个运算符共享同一个运算对象时起作用
    - `12 / 3 * 2` 中 `/` 与 `*` 共享 `3`，从左往右算得 8
    - 上式逐步化简为 `-7 * 6 + 19`，再得 `-42 + 19`

!!! warning "常见错误"

    - 把结合性当成所有求值顺序的规则
    - 认为 `6 * 12` 一定先于 `5 * 20` 计算

## `sizeof` 运算符与 `size_t`

!!! abstract "语法形式"

    `sizeof 运算对象` 或 `sizeof(类型名)`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n = 0;
        size_t intsize;

        intsize = sizeof(int);
        printf("%zu %zu\n", sizeof n, intsize);
        return 0;
    }
    ```

    输出：

    ```text
    4 4
    ```

!!! note "说明"

    - 以字节为单位返回运算对象的大小
    - 1 字节定义为 `char` 占用的空间
    - 运算对象是类型名时必须加圆括号
    - 返回值的类型是 `size_t`，一种无符号整数类型
    - 本机 x86-64 上 `int` 占 4 字节，其他平台可能不同
    - `%zu` 用于打印 `size_t`，不支持时可用 `%u` 或 `%lu`

## `typedef`

!!! abstract "语法形式"

    `typedef 已有类型 新名称;`

!!! example "示例"

    ```c
    #include <stdio.h>

    typedef double real;

    int main(void)
    {
        real deal = 1.5;

        printf("%.1f\n", deal);
        return 0;
    }
    ```

    输出：

    ```text
    1.5
    ```

!!! note "说明"

    - 为已有类型创建别名，不创建新类型
    - `size_t` 就是头文件用 `typedef` 定义的别名
    - 不同系统可以把它设为 `unsigned int` 或 `unsigned long`

!!! warning "常见错误"

    - 把 `typedef` 当成变量声明，误写 `typedef double real = 1.5;`

## 求模运算符 `%`

!!! abstract "语法形式"

    `a % b`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int sec = 154;

        printf("%d %d\n", sec / 60, sec % 60);
        return 0;
    }
    ```

    输出：

    ```text
    2 34
    ```

!!! note "说明"

    - 结果是左侧整数除以右侧整数的余数
    - 只能用于整数，不能用于浮点数
    - 余数的符号与被除数相同
    - `11 / 5` 得 2，`11 % 5` 得 1
    - `-11 / 5` 得 -2，`-11 % 5` 得 -1
    - 恒等式为 `a % b == a - (a / b) * b`

!!! warning "常见错误"

    - `13.0 % 5` 不能通过编译

## 递增运算符 `++`

!!! abstract "语法形式"

    `++变量` 或 `变量++`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int a = 1, b = 1;
        int a_post, pre_b;

        a_post = a++;
        pre_b = ++b;
        printf("%d %d %d %d\n", a, a_post, b, pre_b);
        return 0;
    }
    ```

    输出：

    ```text
    2 1 2 2
    ```

!!! note "说明"

    - 前缀形式先加 1，再使用变量的值
    - 后缀形式先使用变量的值，再加 1
    - 单独成句时 (`a++;`)，两种形式没有区别
    - 作为表达式的一部分时，两种形式的结果不同
    - `a_post` 得到 `a` 的旧值，`pre_b` 得到 `b` 的新值
    - `while (++shoe < 18.5)` 先递增再比较，循环次数少一次

!!! warning "常见错误"

    - 把 `while (shoe++ < 18.5)` 与 `while (++shoe < 18.5)` 当成等价写法

## 递减运算符 `--`

!!! abstract "语法形式"

    `--变量` 或 `变量--`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int count = 3;

        while (--count > 0)
            printf("%d ", count);
        printf("\n");
        return 0;
    }
    ```

    输出：

    ```text
    2 1
    ```

!!! note "说明"

    - 前缀形式先减 1，再使用变量的值
    - 后缀形式先使用变量的值，再减 1
    - `--count > 0` 先减 1，再与 0 比较
    - 循环体的执行次数比初值少 1

## 递增递减运算符的优先级

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n = 2, y = 3;

        printf("%d\n", n * y++);
        printf("%d %d\n", n, y);
        return 0;
    }
    ```

    输出：

    ```text
    6
    2 4
    ```

!!! note "说明"

    - `++` `--` 的优先级高于乘除，只有圆括号比它们更高
    - `x * y++` 等价于 `(x) * (y++)`
    - `++` 只作用于一个变量，`(x * y)++` 不合法
    - 递增发生的时间由运算符的形式决定，与优先级无关
    - `n * y++` 先用 `y` 的旧值相乘，再把 `y` 递增

!!! warning "常见错误"

    - 认为 `x * y++` 是 `(x * y)++`
    - 把优先级当成递增发生时间的规则

## 表达式

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int c;

        printf("%d\n", 6 + (c = 3 + 8));
        return 0;
    }
    ```

    输出：

    ```text
    17
    ```

!!! note "说明"

    - 表达式由运算符与运算对象组成
    - 单个常量或变量也是表达式
    - 子表达式是较大表达式中的较小表达式
    - 每个表达式都有一个值
    - 赋值表达式的值等于赋值后左侧变量的值
    - 关系表达式的值为 1 (真) 或 0 (假)

    表5-2 表达式的值

    | 表达式 | 值 |
    | --- | --- |
    | `-4 + 6` | 2 |
    | `c = 3 + 8` | 11 |
    | `5 > 3` | 1 |
    | `6 + (c = 3 + 8)` | 17 |

## 语句

!!! abstract "语法形式"

    `表达式;` 或单独一个分号

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int x = 25;

        ++x;
        ;
        printf("%d\n", x);
        return 0;
    }
    ```

    输出：

    ```text
    26
    ```

!!! note "说明"

    - 语句是程序的基本构建块，大部分以分号结尾
    - 末尾加分号的表达式构成表达式语句
    - 只有一个分号的语句是空语句
    - 声明不是语句，删去声明末尾的分号后没有值
    - `x = 6 + (y = 5);` 中 `y = 5` 只是子表达式

!!! warning "常见错误"

    - 把声明当作语句，以为 `int port` 去掉分号后有值

## 副作用与序列点

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int guests = 1;

        while (guests++ < 3)
            printf("%d ", guests);
        printf("\n");
        return 0;
    }
    ```

    输出：

    ```text
    2 3
    ```

!!! note "说明"

    - 副作用是对数据对象或文件的修改
    - `states = 50;` 的主要目的是求值，修改 `states` 是副作用
    - `printf()` 显示字符是副作用，返回值是显示的字符数
    - 序列点是程序执行中的一个点，之前的副作用全部完成
    - 分号与完整表达式的结束都是序列点
    - `guests++ < 3` 是完整表达式，进入 `printf()` 前已经递增

!!! warning "常见错误"

    - `y = (4 + x++) + (6 + x++);` 两次修改之间没有序列点
    - `printf("%d %d", num, num++);` 参数的求值顺序未规定
    - 以上两种写法都属于未定义行为，结果不可依赖

    [教材把 `printf("%d %d", num, num * num++)` 描述为只能在某些系统上运行，实际属于未定义行为，不是实现相关的正常结果]

## 复合语句 (块)

!!! abstract "语法形式"

    `{ 语句; 语句; }`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int index = 0, sam;

        while (index++ < 3)
        {
            sam = 10 * index + 2;
            printf("%d ", sam);
        }
        printf("\n");
        return 0;
    }
    ```

    输出：

    ```text
    12 22 32
    ```

!!! note "说明"

    - 用花括号括起来的一条或多条语句构成复合语句
    - 复合语句也称为块
    - 整个块在语法上视为一条语句
    - 缩进不改变语义，只影响阅读
    - 省去花括号时，循环体只包含紧随其后的一条语句

!!! warning "常见错误"

    - 缩进了两条语句却省去花括号，只有第一条属于循环

## 自动类型转换

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char ch = 'C';
        int i;
        float fl;

        fl = i = ch;
        printf("%c %d %.2f\n", ch, i, fl);
        printf("%c\n", ch + 1);
        return 0;
    }
    ```

    输出：

    ```text
    C 67 67.00
    D
    ```

!!! note "说明"

    - 基本规则如下
    - 1. 表达式中 `char` 和 `short` 自动升级为 `int`
    - 2. 两种类型参与运算时，都转换成较高级别的类型
    - 3. 级别从高到低依次是
       `long double`，`double`，`float`
       `unsigned long long`，`long long`
       `unsigned long`，`long`
       `unsigned int`，`int`
    - 4. 赋值时结果转换成被赋值变量的类型，可能降级
    - 5. 作为函数实参时，`char` 和 `short` 转成 `int`,
       `float` 转成 `double`

    - 从较小类型到较大类型的转换称为升级，反之为降级
    - `long` 与 `int` 大小相同时，`unsigned int` 的级别高于 `long`
    - 降级可能丢失数据，8 位的 `char` 存不下 22334

!!! warning "常见错误"

    - 依赖降级，把较大的值赋给较窄的类型
    - 混合类型运算时误以为结果仍是整数类型

## 赋值时的类型转换

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char ch = 'C';

        ch = 1107;
        printf("%c\n", ch);
        ch = 80.89;
        printf("%c\n", ch);
        return 0;
    }
    ```

    输出：

    ```text
    S
    P
    ```

!!! note "说明"

    - 目标是无符号整型，待赋值是整数： 忽略额外的高位
    - 8 位无符号类型相当于原值对 256 取模
    - 目标是 `char` 时，超出范围的结果由实现定义
    - 本机 `1107 % 256` 得 83，即字符 `S` 的编码
    - 目标是有符号整型，待赋值是浮点数： 小数部分向零截断
    - 浮点值的整数部分超出目标整型范围时，行为未定义

    [教材原文写作 1107 % 265，应为 1107 % 256]
    [教材称目标类型是整型且待赋的值是浮点数时行为未定义，这一说法过宽； 应限于整数部分超出目标范围的情形，单纯的截断有确定结果]

## 强制类型转换

!!! abstract "语法形式"

    `(类型名) 表达式`

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int mice;

        mice = 1.6 + 1.7;
        printf("%d\n", mice);
        mice = (int)1.6 + (int)1.7;
        printf("%d\n", mice);
        return 0;
    }
    ```

    输出：

    ```text
    3
    2
    ```

!!! note "说明"

    - 圆括号中的类型名构成强制类型转换运算符
    - 只转换紧随其后的运算对象
    - `(int)1.6 + 1.7` 只把 `1.6` 转成 `1`，加得 2.7
    - `(int)(1.6 + 1.7)` 先加得 3.3，再截断为 3
    - 强制转换可以写明意图，避免依赖自动转换

!!! warning "常见错误"

    - 写成 `(int)1.6 + 1.7` 却以为转换了整个和
    - 对超出目标范围的浮点值作强制转换

## 函数参数的类型转换

!!! abstract "语法形式"

    `返回类型 函数名(参数类型 参数名);` 后接 `函数名(实参)`

!!! example "示例"

    ```c
    #include <stdio.h>

    void pound(int n);

    int main(void)
    {
        int times = 5;
        char ch = '!';
        float f = 6.0f;

        pound(times);
        pound(ch);
        pound(f);
        return 0;
    }

    void pound(int n)
    {
        while (n-- > 0)
            printf("#");
        printf("\n");
    }
    ```

    输出：

    ```text
    #####
    #################################
    ######
    ```

!!! note "说明"

    - 函数原型声明返回类型与参数类型
    - 原型告诉编译器把实参转换成参数类型
    - `pound(ch)` 把字符 `!` 的编码 33 转换成 `int`
    - `pound(f)` 把 `float` 的 6.0 转换成 `int` 的 6
    - 无原型时，`char` 和 `short` 升级为 `int`，`float` 升级为 `double`
    - `float` 实参以 `double` 传递，与 `int` 形参不匹配

!!! warning "常见错误"

    - 用 `void pound();` 代替原型，调用 `pound(f)` 输出错误
    - 认为不同函数中的同名变量是同一个变量

## 复习题

（1）假设所有变量的类型都是 `int`，下列各项变量的值是多少
(a) `x = (2 + 3) * 6;`
(b) `x = (12 + 6) / 2 * 3;`
(c) `y = x = (2 + 3) / 4;`
(d) `y = 3 + 2 * (x = 7 / 2);`

??? note "答案"

    (a) 30; (b) 27，不能按 `(12 + 6) / (2 * 3)` 算成 3; (c) `x = 1`，`y = 1`; (d) `x = 3`，`y = 9`

（2）假设所有变量的类型都是 `int`，下列各项变量的值是多少
(a) `x = (int)3.8 + 3.3;`
(b) `x = (2 + 3) * 10.5;`
(c) `x = 3 / 5 * 22.0;`
(d) `x = 22.0 * 3 / 5;`

??? note "答案"

    (a) 6; (b) 52; (c) 0; (d) 13

（3）对下列各表达式求值
(a) `30.0 / 4.0 * 5.0;`
(b) `30.0 / (4.0 * 5.0);`
(c) `30 / 4 * 5;`
(d) `30 * 5 / 4;`
(e) `30 / 4.0 * 5;`
(f) `30 / 4 * 5.0;`

??? note "答案"

    (a) 37.5; (b) 1.5; (c) 35; (d) 37; (e) 37.5; (f) 35.0

（4）请找出下面的程序中的错误
```c
int main(void)
{
    int i = 1,
    float n;
    printf("Watch out! Here come a bunch of fractions!\n");
    while (i < 30)
         n = 1/i;
         printf(" %f", n);
    printf("That's all, folks!\n");
    return;
}
```

??? note "答案"

    缺少 `#include <stdio.h>`; 第 3 行末尾应为分号； `while` 缺花括号，循环体只有 `n = 1/i;`; `i` 不递增，形成无限循环； `1/i` 是整数除法，应写 `1.0/i`; 输出格式缺 `\n`，数字挤在一行； `return;` 应写 `return 0;`

（5）这是程序清单5.9的另一个版本。 从表面上看，该程序只使用了一条 `scanf()` 语句，比原版简单。 请找出不如原版之处
```c
#include <stdio.h>
#define S_TO_M 60
int main(void)
{
    int sec, min, left;
    printf("This program converts seconds to minutes and ");
    printf("seconds.\n");
    printf("Just enter the number of seconds.\n");
    printf("Enter 0 to end the program.\n");
    while (sec > 0) {
       scanf("%d", &sec);
       min = sec/S_TO_M;
       left = sec % S_TO_M;
       printf("%d sec is %d min, %d sec. \n", sec, min, left);
       printf("Next input?\n");
    }
    printf("Bye!\n");
    return 0;
}
```

??? note "答案"

    第一次判断 `sec > 0` 时 `sec` 尚未赋值，比较的是内存中的垃圾值； 输入 0 后仍会先打印一次结果再退出； 正确做法是在循环前读一次，在循环末尾再读一次

（6）下面的程序将打印出什么内容
```c
#include <stdio.h>
#define FORMAT "%s! C is cool!\n"
int main(void)
{
    int num = 10;
    printf(FORMAT, FORMAT);
    printf("%d\n", ++num);
    printf("%d\n", num++);
    printf("%d\n", num--);
    printf("%d\n", num);
    return 0;
}
```

??? note "答案"

    输出如下

    ```text
    %s! C is cool!
    ! C is cool!
    11
    11
    12
    11
    ```

（7）下面的程序将打印出什么内容
```c
#include <stdio.h>
int main(void)
{
    char c1, c2;
    int diff;
    float num;
    c1 = 'S';
    c2 = 'O';
    diff = c1 - c2;
    num = diff;
    printf("%c%c%c:%d %3.2f\n", c1, c2, c1, diff, num);
    return 0;
}
```

??? note "答案"

    `SOS:4 4.00`，`'S'` 与 `'O'` 的编码相差 4

（8）下面的程序将打印出什么内容
```c
#include <stdio.h>
#define TEN 10
int main(void)
{
    int n = 0;
    while (n++ < TEN)
       printf("%5d", n);
    printf("\n");
    return 0;
}
```

??? note "答案"

    把 1 到 10 打印在同一行，每个数字占 5 列

    ```text
        1    2    3    4    5    6    7    8    9   10
    ```

（9）修改上一个程序，使其可以打印字母 a 到 g

??? note "答案"

    字母编码连续时，可以这样写

    ```c
    #include <stdio.h>

    int main(void)
    {
        char ch = 'a';

        while (ch <= 'g')
            printf("%5c", ch++);
        printf("\n");
        return 0;
    }
    ```

（10）假设下面是完整程序中的一部分，它们分别打印什么
(a)
```c
int x = 0;
while (++x < 3)
   printf("%4d", x);
```
(b)
```c
int x = 100;
while (x++ < 103)
   printf("%4d\n",x);
   printf("%4d\n",x);
```
(c)
```c
char ch = 's';
while (ch < 'w')
{
   printf("%c", ch);
   ch++;
}
printf("%c\n",ch);
```

??? note "答案"

    (a) 在同一行打印 `1` 与 `2`; (b) 依次换行打印 101、102、103、104; (c) 打印 `stuvw`

（11）下面的程序会打印出什么
```c
#define MESG "COMPUTER BYTES DOG"
#include <stdio.h>
int main(void)
{
    int n = 0;
    while ( n < 5 )
       printf("%s\n", MESG);
       n++;
    printf("That's all.\n");
    return 0;
}
```

??? note "答案"

    只有 `printf()` 是循环体，程序不断打印 `COMPUTER BYTES DOG`，直到强行结束

（12）分别编写一条语句，完成下列各任务
(a) 将变量 `x` 的值增加 10
(b) 将变量 `x` 的值增加 1
(c) 将 `a` 与 `b` 之和的两倍赋给 `c`
(d) 将 `a` 与 `b` 的两倍之和赋给 `c`

??? note "答案"

    (a) `x = x + 10;` (b) `x++;` (c) `c = 2 * (a + b);` (d) `c = a + 2 * b;`

（13）分别编写一条语句，完成下列各任务
(a) 将变量 `x` 的值减少 1
(b) 将 `n` 除以 `k` 的余数赋给 `m`
(c) `q` 除以 `b` 减去 `a`，并将结果赋给 `p`
(d) `a` 与 `b` 之和除以 `c` 与 `d` 的乘积，并将结果赋给 `x`

??? note "答案"

    (a) `x--;` (b) `m = n % k;` (c) `p = q / (b - a);` (d) `x = (a + b) / (c * d);`

## 编程练习

!!! question "编程练习"

    1. 编写一个程序，把用分钟表示的时间转换成用小时和分钟表示的时间。 使用 `#define` 或 `const` 创建一个表示 60 的符号常量或 `const` 变量。 通过 `while` 循环让用户重复输入值，直到输入小于或等于 0 的值才停止

    2. 编写一个程序，提示用户输入一个整数，然后打印从该数到比该数大 10 的所有整数。 例如输入 5，则打印 5 到 15，包括两端。 打印的各值之间用一个空格，制表符或换行符分开

    3. 编写一个程序，提示用户输入天数，然后将其转换成周数和天数。 例如输入 18，则转换成 2 周 4 天，按下面的格式显示结果

       ```text
       18 days are 2 weeks, 4 days.
       ```

       通过 `while` 循环让用户重复输入天数，输入非正值时循环结束

    4. 编写一个程序，提示用户输入一个身高 (单位： 厘米)，并分别以英尺和英寸为单位显示该值，允许有小数部分。 程序应能让用户重复输入身高，直到输入非正值。 输出示例如下

       ```text
       Enter a height in centimeters: 182
       182.0 cm = 5 feet, 11.7 inches
       Enter a height in centimeters (<=0 to quit): 0
       bye
       ```

    5. 修改程序清单5.13的 `addemup.c`，把它看成计算 20 天里赚钱的程序。 第 1 天赚 1 元，第 2 天赚 2 元，依次类推。 修改程序，用读入的变量代替 20

    6. 修改编程练习 5 的程序，使其计算整数的平方和。 第 1 天赚 1 元，第 2 天赚 4 元，第 3 天赚 9 元，依次类推。 C 没有平方函数，用 `n * n` 表示 `n` 的平方

    7. 编写一个程序，提示用户输入一个 `double` 类型的数，并打印该数的立方值。 自定义一个函数计算并打印立方值，`main()` 把用户输入的值传递给该函数

    8. 编写一个程序，显示求模运算的结果。 把用户输入的第 1 个整数作为 % 号右侧的运算对象，该数在运算过程中保持不变。 用户后面输入的数是左侧的运算对象，输入非正值时程序结束。 输出示例如下

       ```text
       This program computes moduli.
       Enter an integer to serve as the second operand: 256
       Now enter the first operand: 438
       438 % 256 is 182
       Enter next number for first operand (<= 0 to quit): 0
       Done
       ```

    9. 编写一个程序，要求用户输入一个华氏温度。 程序读取 `double` 类型的值，并把它作为实参传递给自定义函数 `Temperatures()`. 该函数计算摄氏温度和开氏温度，并按两位小数显示三种温度。 换算公式为

       `摄氏温度 = 5.0 / 9.0 * (华氏温度 - 32.0)`

       `开氏温度 = 摄氏温度 + 273.16`

       `Temperatures()` 中用 `const` 创建换算用的变量。 `main()` 中用循环让用户重复输入温度，输入 `q` 或其他非数字时循环结束。 `scanf()` 读取成功时返回 1，可以用 `==` 判断返回值是否等于 1
