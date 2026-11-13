# 第2章 C语言概述

## 简单程序的完整结构

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        声明
        语句
        return 0;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int num;

        num = 1;
        printf("My favorite number is %d.\n", num);

        return 0;
    }
    ```

    输出：

    ```text
    My favorite number is 1.
    ```

!!! note "说明"

    - 程序由一个或多个函数组成，必须有 `main()`
    - 函数由函数头和函数体组成
    - 函数体由声明和语句组成，大部分语句以分号结尾
    - 源文件以 `.c` 结尾

!!! warning "常见错误"

    - 用圆括号代替花括号
    - 语句末尾漏分号
    - 漏写 `#include`

## #include 指令与头文件

!!! abstract "语法形式"

    ```c
    #include <头文件名.h>
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("stdio.h 提供 printf 的声明\n");
        return 0;
    }
    ```

    输出：

    ```text
    stdio.h 提供 printf 的声明
    ```

!!! note "说明"

    - `#include` 是预处理指令，编译前由预处理器处理
    - 作用是把头文件内容复制到该行所在位置
    - `stdio.h` 是标准输入输出头文件，提供 `printf()` 等的声明
    - 函数的实际代码在预编译的库文件中，头文件只供编译器使用
    - 标准规定使用 `printf()` 必须包含 `stdio.h`

!!! warning "常见错误"

    - 漏写 `#`，写成 `include <stdio.h>`
    - 漏写尖括号，写成 `#include stdio.h`
    - 头文件名拼错，如写成 `studio.h`

## main() 函数

!!! abstract "语法形式"

    ```c
    int main(void)
    {
        语句
        return 0;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("所有 C 程序从 main() 开始执行\n");
        return 0;
    }
    ```

    输出：

    ```text
    所有 C 程序从 main() 开始执行
    ```

!!! note "说明"

    - `main` 是唯一固定的函数名，程序从这里开始执行
    - 圆括号表明 `main` 是函数名
    - `int` 是返回类型，返回值交给操作系统
    - `void` 表示函数不接收参数
    - 其他函数可以任意命名，是否执行由是否被调用决定

!!! warning "常见错误"

    - 写成 `main()`，C99 与 C11 不接受省略返回类型
    - 写成 `void main()`，所有标准都未认可
    - 把 `main` 写成 `Main`，名称区分大小写

## 注释

!!! abstract "语法形式"

    ```c
    /* 块注释, 可以跨行 */
    // 行注释, 到行末结束
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int rigue;              /* 块注释可放在行尾 */

        // 行注释独占一行
        rigue = 1;
        printf("%d\n", rigue);  // 也可放在行尾
        return 0;
    }
    ```

    输出：

    ```text
    1
    ```

!!! note "说明"

    - `/*` 与 `*/` 之间的内容由编译器忽略
    - 注释可以单独占一行，也可以放在语句后面
    - `//` 注释从符号处到行末，C99 新增
    - 注释用于说明程序意图，不改变程序行为

!!! warning "常见错误"

    - 漏写 `*/`，后面的代码全被当作注释
    - 在 `/* */` 内再写 `/* */`，内层的 `*/` 提前结束注释

## 花括号与函数体

!!! abstract "语法形式"

    ```c
    int main(void)
    {
        声明
        语句
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n;

        n = 3;
        {
            printf("块内可以访问 n = %d\n", n);
        }
        return 0;
    }
    ```

    输出：

    ```text
    块内可以访问 n = 3
    ```

!!! note "说明"

    - 花括号标记函数体的开始与结束，不能省略
    - 只有花括号起这个作用，圆括号与方括号不行
    - 花括号也可把若干语句合并为一个块
    - 函数体由声明和语句组成

!!! warning "常见错误"

    - 用 `(` `)` 代替 `{` `}`
    - 漏写右花括号，报错位置常在文件末尾

## 声明

!!! abstract "语法形式"

    ```c
    类型 变量名;
    类型 变量名1, 变量名2;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int feet, fathoms;

        fathoms = 2;
        feet = 6 * fathoms;
        printf("%d 英寻 = %d 英尺\n", fathoms, feet);
        return 0;
    }
    ```

    输出：

    ```text
    2 英寻 = 12 英尺
    ```

!!! note "说明"

    - 声明确定变量名与数据类型，编译器据此分配内存
    - 所有变量必须先声明再使用
    - `int feet, fathoms;` 与分两行声明等价
    - C99 起声明可放在块中任意位置，使用前声明即可
    - C90 要求所有声明位于块的开头

!!! warning "常见错误"

    - 直接使用未声明的变量
    - 逗号声明中重复写类型，写成 `int n, int n2;`
    - 声明后漏分号

## 标识符命名

!!! abstract "语法形式"

    ```c
    标识符: 由字母, 数字, 下划线组成
    首字符必须是字母或下划线
    ```

!!! example "示例"

    ```c
    int wiggles;    /* 有效 */
    int cat2;       /* 有效 */
    int Hot_Tub;    /* 有效 */
    int taxRate;    /* 有效 */
    int _kcab;      /* 有效, 但属于保留标识符 */
    ```

!!! note "说明"

    - 名称区分大小写，`stars`，`Stars`，`STARS` 是三个名称
    - C99 与 C11 要求编译器至少识别前 63 个字符
    - 外部标识符至少识别前 31 个字符
    - 以一个或两个下划线开头的名称由系统与标准库保留
    - 名称应表达用途，如用 `sheep_count` 而不用 `x3`
    [原书称 C90 只允许 6 个字符，6 个是 C90 对外部标识符的保证值，内部标识符为 31 个]

!!! warning "常见错误"

    - `2cat`，数字开头
    - `Hot-Tub`，含减号
    - `tax rate`，含空格
    - `don't`，含撇号
    - 用关键字作名称，如 `int`

## 赋值

!!! abstract "语法形式"

    ```c
    变量 = 表达式;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int num;

        num = 1;
        printf("num = %d\n", num);
        num = 7;
        printf("num = %d\n", num);
        return 0;
    }
    ```

    输出：

    ```text
    num = 1
    num = 7
    ```

!!! note "说明"

    - 赋值从右向左进行，先求右边表达式的值，再存入左边变量
    - 赋值是表达式，末尾加分号构成表达式语句
    - `=` 是赋值运算符，不是相等判断
    - 变量的值可以反复修改

!!! warning "常见错误"

    - 把 `=` 写成 `==`
    - 赋值方向理解反，写成 `1 = num;`
    - 漏分号

## printf() 基本用法

!!! abstract "语法形式"

    ```c
    printf("格式串", 参数1, 参数2, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("I am a simple ");
        printf("computer.\n");
        return 0;
    }
    ```

    输出：

    ```text
    I am a simple computer.
    ```

!!! note "说明"

    - 双引号内的文本按原样输出
    - 圆括号中的内容传给函数，称为实参
    - 函数执行完，控制权返回调用它的函数
    - 连续调用多次 `printf()`，输出按调用顺序相接
    - 函数名中的 `f` 表示格式化打印

!!! warning "常见错误"

    - 漏写双引号
    - 漏写分号
    - 漏写 `#include <stdio.h>`

## 转义序列

!!! abstract "语法形式"

    ```c
    \n  \t  \b  \\  \"
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("Begone!\nO creature of lard!\n");
        printf("Name\tAge\n");
        return 0;
    }
    ```

    输出：

    ```text
    Begone!
    O creature of lard!
    Name	Age
    ```

!!! note "说明"

    - 反斜杠加一个字符组成转义序列，表示难以输入或不可见的字符
    - `\n` 是换行符，使光标移到下一行最左边
    - `\t` 是制表符，`\b` 是退格符
    - 转义序列写在双引号内，不按字面输出
    - 换行符只影响输出显示，不打断源代码行

!!! warning "常见错误"

    - 在字符串中间直接按 Enter 换行
    - 把 `\n` 写成 `/n`
    - 漏写反斜杠

## 格式符 %d 与多个参数

!!! abstract "语法形式"

    ```c
    printf("格式串", 参数1, 参数2, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int feet, fathoms;
        fathoms = 2;
        feet = 6 * fathoms;
        printf("There are %d feet in %d fathoms!\n", feet, fathoms);
        printf("Yes, I said %d feet!\n", 6 * fathoms);
        return 0;
    }
    ```

    输出：

    ```text
    There are 12 feet in 2 fathoms!
    Yes, I said 12 feet!
    ```

!!! note "说明"

    - `%d` 是占位符，指明以十进制整数输出对应参数
    - 参数按顺序替换格式串中的 `%d`
    - 格式符数量应与参数数量一致
    - 参数可以是表达式，如 `6 * fathoms`，先求值再输出
    - 参数之间用逗号分隔，参数列在双引号之后

!!! warning "常见错误"

    - 参数顺序与格式符顺序不一致
    - `%d` 数量多于参数，输出随机值
    - 把变量名写进双引号内

## return 语句

!!! abstract "语法形式"

    ```c
    return 表达式;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("程序结束\n");
        return 0;
    }
    ```

    输出：

    ```text
    程序结束
    ```

!!! note "说明"

    - `return` 结束函数并把值交回调用方
    - `main()` 的返回值交给操作系统，0 表示正常结束
    - 有返回值的函数应写 `return`
    - `main()` 末尾省略 `return` 时，执行到右花括号返回 0
    - 其他有返回值的函数不能省略

!!! warning "常见错误"

    - 在其他函数中漏写 `return`
    - 返回值的类型与函数头的返回类型不一致

## 提高可读性的写法

!!! abstract "语法形式"

    ```c
    int main(void)
    {
        int four;

        four = 4;
        printf("%d\n", four);
        return 0;
    }
    ```

!!! note "说明"

    - 选择能说明用途的函数名与变量名
    - 写注释解释用途，名称已说明的不重复注释
    - 用空行分隔概念上不同的部分
    - 每条语句各占一行
    - C 语言的格式自由，分号决定语句边界，上述写法不改变语义

!!! warning "常见错误"

    - 多条语句挤在一行
    - 把一条语句拆成多行，分号位置混乱
    - 注释重复变量名已表达的内容

## 多个函数与函数原型

!!! abstract "语法形式"

    ```c
    返回类型 函数名(参数表);      /* 函数原型 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void butler(void);              /* 函数原型 */
    int main(void)
    {
        printf("I will summon the butler function.\n");
        butler();
        return 0;
    }
    void butler(void)               /* 函数定义 */
    {
        printf("You rang, sir?\n");
    }
    ```

    输出：

    ```text
    I will summon the butler function.
    You rang, sir?
    ```

!!! note "说明"

    - 同一函数在程序中可出现三次： 原型，调用，定义
    - 原型告知编译器函数的返回类型与参数，C90 新增
    - 定义是函数本身的源代码
    - 执行顺序由调用位置决定，与定义在文件中的位置无关
    - 所有程序都从 `main()` 开始执行，惯例把 `main()` 放在开头

!!! warning "常见错误"

    - 写成旧式声明 `void butler();`，不描述参数
    - 调用前既无原型也无定义
    - 把定义放在调用之后却不写原型

## 形参与实参

!!! abstract "语法形式"

    ```c
    void 函数名(类型 形参)
    主调函数中调用: 函数名(实参);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    void show(int n);
    int main(void)
    {
        show(7);
        return 0;
    }
    void show(int n)
    {
        printf("n = %d\n", n);
    }
    ```

    输出：

    ```text
    n = 7
    ```

!!! note "说明"

    - 实参是调用时传给函数的具体值
    - 形参是函数中接收该值的变量
    - `printf()` 圆括号中的内容也是实参
    - 调用的参数个数与类型应与原型一致

!!! warning "常见错误"

    - 原型与定义中的参数类型不一致
    - 调用时漏写参数或参数个数不符

## 语法错误

!!! abstract "语法形式"

    ```c
    int n, n2, n3;      /* 正确 */
    int n, int n2;      /* 错误, 重复写类型 */
    ```

!!! example "示例"

    ```c
    /* nogood.c -- 有错误的程序 */
    #include <stdio.h>
    int main(void)
    (
        int n, int n2, int n3;

        n = 5;
        printf("%d\n", n)

        return 0;
    )
    ```

!!! note "说明"

    - 语法错误是把有效的 C 符号放在错误的位置
    - 编译器能发现语法错误，报出性质与位置
    - 报错位置可能比真正的错误晚一行
    - 修正前几处错误后，错误信息常会减少
    - 按提示逐条修改，直到编译通过

!!! warning "常见错误"

    - 用圆括号代替花括号
    - 声明中重复写类型
    - `printf()` 语句末尾漏分号
    - 注释漏写 `*/`

## 语义错误

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n, n2, n3;

        n = 5;
        n2 = n * n;
        n3 = n2 * n2;
        printf("n = %d, n3 = %d\n", n, n3);
        return 0;
    }
    ```

    输出：

    ```text
    n = 5, n3 = 625
    ```

!!! note "说明"

    - 语义错误指程序含义与意图不符，语法上合法
    - 编译器无法检测语义错误
    - `n3` 应写成 `n * n2`，写成 `n2 * n2` 得到 625
    - 只能通过跟踪程序状态或插入 `printf()` 发现

!!! warning "常见错误"

    - 把 `n` 的立方写成 `n` 的四次方
    - 按设想而不是按代码推演执行过程

## 程序状态与调试

!!! example "示例"

    ```c
    n = 5;          /* n = 5 */
    n2 = n * n;     /* n2 = 25 */
    n3 = n2 * n2;   /* n3 = 625 */
    ```

!!! note "说明"

    - 程序状态是某执行点上所有变量值的集合
    - 方法一： 人工逐步执行，记录每个变量的值
    - 方法二： 在关键位置插入 `printf()`，打印变量值
    - 方法三： 用调试器逐行运行并查看变量
    - 逐步执行时要按实际代码模拟，不按自己的设想

## 关键字与保留标识符

!!! abstract "语法形式"

    ```c
    auto break case char const continue default do double else
    enum extern float for goto if inline int long register
    restrict return short signed sizeof static struct switch
    typedef union unsigned void volatile while
    _Alignas _Alignof _Atomic _Bool _Complex _Generic
    _Imaginary _Noreturn _Static_assert _Thread_local
    ```

!!! note "说明"

    - 关键字是语言定义的单词，不能用作变量名或函数名
    - `inline` 与 `restrict` 是 C99 新增
    - `_Bool`，`_Complex`，`_Imaginary` 是 C99 新增
    - 其余下划线开头的是 C11 新增
    - 保留标识符还包括下划线开头的名称与标准库函数名
    - 用保留标识符不报语法错误，但可能与系统或库中的名称冲突

!!! warning "常见错误"

    - 用 `int`，`if`，`return` 作变量名
    - 自定义函数命名为 `printf` 或 `malloc`

## 复习题

（1）C 语言的基本模块是什么？

??? note "答案"

    函数

（2）什么是语法错误？ 写出一个英语例子和 C 语言例子

??? note "答案"

    语法错误是违反组成语句或程序的规则的错误
    英语例子： `Me speak English good.`
    C 语言例子： `printf"Where are the parentheses?";`

（3）什么是语义错误？ 写出一个英语例子和 C 语言例子

??? note "答案"

    语义错误是含义上的错误，程序符合语法规则但结果不是本意
    英语例子： `This sentence is excellent Czech.`
    C 语言例子： `thrice_n = 3 + n;`，原意是 3 倍 n

（4）Indiana Sloth 编写了下面的程序，请评定
```c
include studio.h
int main{void} / * 该程序打印一年有多少周 / *
(
    int s
    s := 56;
    print(There are s weeks in a year.);
    return 0;
```

??? note "答案"

    1. 第 1 行： 以 `#` 开头，`studio.h` 改成 `stdio.h`，并用尖括号括起
    2. 第 2 行： 把 `{}` 改成 `()`，注释末尾的 `/*` 改成 `*/`
    3. 第 3 行： 把 `(` 改成 `{`
    4. 第 4 行： `int s` 末尾加分号
    5. 第 5 行无误
    6. 第 6 行： 把 `:=` 改成 `=`，一年的周数改成 52
    7. 第 7 行： 写成 `printf("There are %d weeks in a year.\n", s);`
    8. 第 9 行： 原程序没有这一行，应补上右花括号

    修改后的程序

    ```c
    #include <stdio.h>
    int main(void) /* 打印一年有多少周 */
    {
        int s;

        s = 52;
        printf("There are %d weeks in a year.\n", s);
        return 0;
    }
    ```

（5）假设下面的 4 个例子都是完整程序的一部分，它们都输出什么结果？
```c
a. printf("Baa Baa Black Sheep.");
   printf("Have you any wool?\n");
b. printf("Begone!\nO creature of lard!\n");
c. printf("What?\nNo/nfish?\n");
d. int num;
   num = 2;
   printf("%d + %d = %d", num, num, num + num);
```

??? note "答案"

    a. `Baa Baa Black Sheep.Have you any wool?`
    `Sheep.` 与 `Have` 之间没有空格
    b. 分两行输出 `Begone!` 与 `O creature of lard!`
    c. 分两行输出 `What?` 与 `No/nfish?`，`/` 是普通字符，原样打印
    d. `2 + 2 = 4`，`+` 可以在 `printf()` 的参数中计算

（6）在 `main`，`int`，`function`，`char`，`=` 中，哪些是 C 语言的关键字？

??? note "答案"

    `int` 与 `char`，`main` 是函数名，`function` 是普通单词，`=` 是运算符

（7）如何以下面的格式输出变量 `words` 和 `lines` 的值？
```c
There were 3020 words and 350 lines.
```

??? note "答案"

    `printf("There were %d words and %d lines.\n", words, lines);`

（8）考虑下面的程序，执行完第 7，第 8，第 9 行后，程序的状态分别是什么？
```c
#include <stdio.h>
int main(void)
{
     int a, b;
     a = 5;
     b = 2; /* 第7行 */
     b = a; /* 第8行 */
     a = b; /* 第9行 */
     printf("%d %d\n", b, a);
     return 0;
}
```

??? note "答案"

    第 7 行后 `a=5`，`b=2`
    第 8 行后 `a=5`，`b=5`
    第 9 行后 `a=5`，`b=5`，执行 `a = b;` 时 `b` 已是 5

（9）考虑下面的程序，执行完第 7，第 8，第 9 行后，程序的状态分别是什么？
```c
#include <stdio.h>
int main(void)
{
     int x, y;
     x = 10;
     y = 5;      /* 第7行 */
     y = x + y;  /*第8行*/
     x = x*y;    /*第9行*/
     printf("%d %d\n", x, y);
     return 0;
}
```

??? note "答案"

    第 7 行后 `x=10`，`y=5`
    第 8 行后 `x=10`，`y=15`
    第 9 行后 `x=150`，`y=15`

## 编程练习

!!! question "编程练习"

    1. 编写一个程序，调用一次 `printf()` 函数，把名和姓打印在一行
    再调用一次 `printf()` 函数，把名和姓分别打印在两行
    然后再调用两次 `printf()` 函数，把名和姓打印在一行
    输出应如下所示

        ```c
        Gustav Mahler      ←第1次打印的内容
        Gustav             ←第2次打印的内容
        Mahler             ←仍是第2次打印的内容
        Gustav Mahler      ←第3次和第4次打印的内容
        ```

    2. 编写一个程序，打印你的姓名和地址

    3. 编写一个程序把你的年龄转换成天数，并显示这两个值
    这里不用考虑闰年的问题

    4. 编写一个程序，生成以下输出

        ```c
        For he's a jolly good fellow!
        For he's a jolly good fellow!
        For he's a jolly good fellow!
        Which nobody can deny!
        ```

        除了 `main()` 函数以外，该程序还要调用两个自定义函数
        一个名为 `jolly()`，用于打印前 3 条消息，调用一次打印一条
        另一个名为 `deny()`，打印最后一条消息

    5. 编写一个程序，生成以下输出

        ```c
        Brazil, Russia, India, China
        India, China,
        Brazil, Russia
        ```

        除了 `main()` 以外，该程序还要调用两个自定义函数
        一个名为 `br()`，调用一次打印一次 `Brazil, Russia`
        另一个名为 `ic()`，调用一次打印一次 `India, China`
        其他内容在 `main()` 函数中完成

    6. 编写一个程序，创建一个整型变量 `toes`，并将 `toes` 设置为 10
    程序中还要计算 `toes` 的两倍和 `toes` 的平方
    该程序应打印 3 个值，并分别描述以示区分

    7. 编写一个程序，生成以下格式的输出

        ```c
        Smile!Smile!Smile!
        Smile!Smile!
        Smile!
        ```

        该程序要定义一个函数，该函数被调用一次打印一次 `Smile!`
        根据程序的需要使用该函数

    8. 编写一个程序，调用一个名为 `one_three()` 的函数
    该函数在一行打印单词 `one`，再调用第 2 个函数 `two()`
    然后在另一行打印单词 `three`
    `two()` 函数在一行显示单词 `two`
    `main()` 函数在调用 `one_three()` 前打印 `starting now:`
    并在调用完毕后显示 `done!`
    输出应如下所示

        ```c
        starting now:
        one
        two
        three
        done!
        ```
