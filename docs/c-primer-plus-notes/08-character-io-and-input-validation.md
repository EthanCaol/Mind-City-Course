# 第8章 字符输入/输出和输入验证

## getchar() 与 putchar()

!!! abstract "语法形式"

    ```c
    int getchar(void);
    int putchar(int c);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch;
        while ((ch = getchar()) != '#')
            putchar(ch);
        return 0;
    }
    ```

    输出：

    ```text
    Hello#
    Hello
    ```

!!! note "说明"

    - `getchar()` 从标准输入读取下一个字符，返回它的字符编码
    - `putchar()` 把一个字符写到标准输出，返回写出的字符，失败时返回 `EOF`
    - 两者在 `stdio.h` 中声明，多数实现同时提供宏版本
    - `'#'` 只作为结束标记，不进入循环体，所以不打印

    [C 标准把 `getchar` 与 `putchar` 规定为函数
    - 允许实现另用宏提供同名接口
    - 教材称两者"都不是真正的函数"不准确]

!!! warning "常见错误"

    - 用 `char` 型变量接收 `getchar()` 的返回值，无法区分 `EOF`
    - 把 `'#'` 写成 `"#"`，双引号表示字符串，`!=` 比较的是指针

## 缓冲输入

!!! note "说明"

    - 缓冲输入： 字符先存入缓冲区，按 Enter 后整行交给程序
    - 缓冲区是临时存储区，常见大小为 512 或 4096 字节
    - 无缓冲输入： 按键后字符立即交给程序，老式系统与部分编译器提供
    - ANSI C 规定标准输入为缓冲输入，未提供无缓冲的标准方式
    - 把多个字符作为一个块传输，比逐字符传输省时间，也允许用户修改输错的字符

    ![图8.1 缓冲输入和无缓冲输入](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00047.jpg)

    表8-1 缓冲输入的类型

    | 类型 | 刷新缓冲区的条件 | 典型场合 |
    | --- | --- | --- |
    | 行缓冲 | 读到换行符 | 键盘输入 |
    | 完全缓冲 | 缓冲区被填满 | 文件输入 |
    | 无缓冲 | 每个字符立即传送 | 交互式程序，非标准 |

!!! warning "常见错误"

    - 以为按键后程序立即读到字符，实际要按 Enter
    - 用 `conio.h` 的 `getch()` 与 `getche()` 写程序，这两个函数不属于 C 标准

## 标准流 stdin 与 stdout

!!! note "说明"

    - C 程序通过流处理输入输出，不直接操作设备
    - `stdin` 表示键盘输入，`stdout` 表示屏幕输出
    - 两个流在程序启动时自动打开，不需要显式建立
    - `getchar()` `putchar()` `printf()` `scanf()` 都作用于这两个流
    - 打开文件即把流与文件关联，文件读写由标准 I/O 包统一处理
    - 标准 I/O 包在不同系统的换行约定之间转换，程序只需判断 `'\n'`

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch = getchar();      /* 从 stdin 读一个字符 */
        putchar(ch);             /* 写到 stdout */
        return 0;
    }
    ```

## 文件结尾 EOF

!!! abstract "语法形式"

    ```c
    #define EOF (-1)            /* stdio.h 中的常见定义 */
    int ch;
    while ((ch = getchar()) != EOF)
        /* 处理 ch */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch;
        while ((ch = getchar()) != EOF)
            putchar(ch);
        return 0;
    }
    ```

    输出：

    ```text
    abc
    abc
    ```

    [第二行按 Ctrl+D (Linux) 或 Ctrl+Z 加回车 (Windows 控制台) 结束输入]

!!! note "说明"

    - `EOF` 是文件结尾标记，不是文件中能找到的符号
    - `EOF` 由 `stdio.h` 用 `#define` 定义，值为负的整数常量，常见 `-1`
    - 标准只要求它与任何字符编码都不同，不保证等于 `-1`
    - `getchar()` 检测到文件结尾或读取错误时返回 `EOF`
    - 键盘模拟文件结尾： 行首按 Ctrl+D (UNIX/Linux)，按 Ctrl+Z 后回车 (Windows)
    - `putchar()` 的参数类型是 `int`，`ch` 声明为 `int` 不影响打印
    - 声明为 `int` 的原因是 `EOF` 与扩展字符都能容纳

    ![图8.2 带文件结尾标记的文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00048.jpg)

    [`char` 是否有符号由实现决定，教材称 `char` 只能表示 `0` 到 `255` 不准确]

!!! warning "常见错误"

    - 输入 `EOF` 三个字母或 `-1` 来结束，程序把它们当作普通字符
    - 用 `char` 保存 `getchar()` 的返回值，无符号 `char` 上 `EOF` 变成 `255`
    - 写成 `while (ch != EOF)` 而 `ch` 从未赋值

## 输入重定向

!!! abstract "语法形式"

    ```c
    ./prog < file
    ```

!!! example "示例"

    ```c
    /* echo_eof.c: 复制输入到输出 */
    #include <stdio.h>
    int main(void)
    {
        int ch;
        while ((ch = getchar()) != EOF)
            putchar(ch);
        return 0;
    }
    ```

    输出：

    ```text
    $ ./echo_eof < words
    The world is too much with us
    ```

!!! note "说明"

    - `./prog < file` 把 `file` 与 `stdin` 关联，程序从文件读取
    - 重定向由命令行环境完成，与 C 语言无关
    - 程序不知道输入来自键盘还是文件，只看到字符流
    - 运算符两侧的空格在 UNIX，Linux，Windows 命令提示中都可省略
    - 输入文件必须是文本文件

!!! warning "常见错误"

    - 把程序名与文件名写反，写成 `./words < echo_eof`
    - 在 IDE 中直接运行，重定向符号被当作命令行参数传给程序

## 输出重定向

!!! abstract "语法形式"

    ```c
    ./prog > file
    ./prog >> file
    ```

!!! example "示例"

    ```c
    $ ./echo_eof > mywords
    a line
    [Ctrl+D]
    $ cat mywords
    a line
    ```

!!! note "说明"

    - `./prog > file` 把 `stdout` 关联到文件，屏幕不再显示输出
    - 文件不存在时创建，已存在时长度先截断为 `0`
    - `>>` 把输出追加到文件末尾，不截断原有内容
    - `printf()` 与 `putchar()` 的输出都写到 `stdout`，一并被重定向
    - 标准错误流 `stderr` 不参与重定向，仍然显示在屏幕上

!!! warning "常见错误"

    - 以为 `>` 只是打开文件，实际会清空原有内容
    - 把 `>>` 写成 `>>>` 或 `> >`

## 组合重定向

!!! abstract "语法形式"

    ```c
    ./prog < in.txt > out.txt
    ./prog > out.txt < in.txt
    ```

!!! example "示例"

    ```c
    $ ./echo_eof < mywords > savewords
    ```

!!! note "说明"

    - 两个运算符的顺序不影响结果，分别决定输入源与输出目标
    - 输入文件名与输出文件名不能相同
    - 输入输出各只能有一个，不能连接两个文件或两个程序

    表8-2 重定向运算符

    | 运算符 | 作用 |
    | --- | --- |
    | `<` | 把文件内容作为程序的标准输入 |
    | `>` | 把程序的标准输出写入文件，覆盖原有内容 |
    | `>>` | 把程序的标准输出追加到文件末尾 |

!!! warning "常见错误"

    - 写成 `./prog < mywords > mywords`，`>` 先把文件截断，输入随即为空
    - 写成 `./prog < a < b` 或 `./prog > a b`，违反一程序一文件的规则
    - 用重定向连接两个数据文件，如 `./fish > beets`

## 直接打开文件读取

!!! abstract "语法形式"

    ```c
    FILE *fp = fopen(文件名, "r");
    int ch = getc(fp);
    fclose(fp);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
        FILE *fp = fopen("words.txt", "r");
        int ch;
        if (fp == NULL)
            exit(1);
        while ((ch = getc(fp)) != EOF)
            putchar(ch);
        fclose(fp);
        return 0;
    }
    ```

!!! note "说明"

    - 无法使用重定向时的替代做法，显式打开文件
    - `getc(fp)` 从指定流读取字符，返回值与 `EOF` 规则同 `getchar()`
    - `fopen()` 失败返回空指针，需要判断后再使用
    - `exit()` 在 `stdlib.h` 中声明
    - 文件处理的完整内容见第 13 章

!!! warning "常见错误"

    - 打开失败直接调用 `getc()`，程序崩溃
    - 忘记 `fclose()`，输出缓冲区的内容可能没有写入文件

## 清除输入行剩余字符

!!! abstract "语法形式"

    ```c
    while (getchar() != '\n')
        continue;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        char response;
        int guess = 1;
        printf("Is it %d? ", guess);
        while ((response = getchar()) != 'y')
        {
            if (response == 'n')
                printf("Is it %d? ", ++guess);
            else
                printf("Only y or n: ");
            while (getchar() != '\n')
                continue;
        }
        printf("Done.\n");
        return 0;
    }
    ```

    输出：

    ```text
    Is it 1? no
    Is it 2? f
    Only y or n: y
    Done.
    ```

!!! note "说明"

    - 内层循环读掉本行余下的全部字符，包括换行符
    - 输入 `no` 或 `no way` 都按首字符 `n` 处理
    - 输入以 `y` 开头时退出循环，该行余下内容未清除
    - 交互式程序应预先考虑误输入，给出提示后重新读取

!!! warning "常见错误"

    - 省略内层循环，上一次输入的换行符被当作一次否定应答
    - 只丢弃一个字符，行内其余字符留到下一轮

## 混合字符与数值输入

!!! abstract "语法形式"

    ```c
    while ((ch = getchar()) != '\n')
    {
        if (scanf("%d %d", &rows, &cols) != 2)
            break;
        /* 处理 ch, rows, cols */
        while (getchar() != '\n')
            continue;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch, rows, cols;
        printf("Enter a character and two integers:\n");
        while ((ch = getchar()) != '\n')
        {
            if (scanf("%d %d", &rows, &cols) != 2)
                break;
            printf("%d %d\n", rows, cols);
            while (getchar() != '\n')
                continue;
        }
        printf("Bye.\n");
        return 0;
    }
    ```

    输出：

    ```text
    Enter a character and two integers:
    c 2 3
    2 3
    ! 3 6
    3 6
    Bye.
    ```

!!! note "说明"

    - `getchar()` 读取每个字符，包括空格与换行符
    - `scanf()` 读数值时跳过前导空白，读完把空格与换行留在输入队列
    - 下一轮 `getchar()` 先读到残留的换行符，循环条件立即成立
    - 每轮末清掉本行，才能读到下一行首字符
    - 在 `scanf()` 失败时用 `break` 结束，比让循环条件偶然成立更清楚

    [教材此处给出 `display(char(ch), rows, cols);` 消除警告
    - `char(ch)` 是 C++ 的函数式转换，C 中应写成 `(char) ch`]

!!! warning "常见错误"

    - 省略每轮末尾的清行循环，输入一组后就退出
    - 把 `scanf()` 的返回值与 `EOF` 比较，忘记它也可能返回 `0`

## 检查 scanf 的返回值

!!! abstract "语法形式"

    ```c
    while (scanf("%ld", &n) == 1 && n >= 0)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        long n;
        while (scanf("%ld", &n) == 1 && n >= 0)
            printf("%ld\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    3 7 -1
    3
    7
    ```

!!! note "说明"

    - `scanf()` 返回成功赋值的输入项个数
    - 转换失败时返回 `0`，遇到文件结尾或读取错误时返回 `EOF`
    - 转换失败时 `n` 的值不变，失败的字符留在输入队列中
    - 条件从左向右求值，前一项失败时不再判断 `n >= 0`
    - 完整条件读作"当输入是一个整数且该整数非负时"

!!! warning "常见错误"

    - 只检查 `n` 的值，不检查 `scanf()` 是否成功
    - 直接把 `scanf()` 当作布尔条件，返回 `EOF` 时也非零，被当作真

## 读整数直到成功

!!! abstract "语法形式"

    ```c
    long get_long(void)
    {
        long input;
        int ch;
        while (scanf("%ld", &input) != 1)
        {
            while ((ch = getchar()) != '\n')
                putchar(ch);
            /* 提示重新输入 */
        }
        return input;
    }
    ```

!!! example "输出"

    ```text
    low is not an integer. Try again: 3
    ```

    [`low` 是内层循环用 `putchar()` 回显的非法输入，提示语接在它后面输出]

!!! note "说明"

    - 外层循环重复到 `scanf()` 成功，此时返回值为 `1`
    - 内层循环逐字符回显并丢弃本行，直到换行符
    - 转换失败后 `scanf()` 不再前进，不清掉那一段输入就会反复失败
    - 输入行中的数字也一并丢弃，因为整行都按非法输入处理
    - 变量声明为 `long` 时转换说明用 `%ld`

!!! warning "常见错误"

    - 只清一个字符，非法输入的长单词导致提示重复出现
    - `int` 变量配 `%ld`，读写宽度不一致

## 数值范围校验

!!! abstract "语法形式"

    ```c
    bool bad_limits(long begin, long end, long low, long high);
    ```

!!! example "示例"

    ```c
    #include <stdbool.h>
    bool bad_limits(long begin, long end, long low, long high)
    {
        bool bad = false;
        if (begin > end)
            bad = true;
        if (begin < low || end < low)
            bad = true;
        if (begin > high || end > high)
            bad = true;
        return bad;
    }
    ```

!!! note "说明"

    - 三个条件独立判断，不提前返回，一次报告全部超限项
    - 函数返回 `true` 表示输入无效，与函数名前缀 `bad` 一致
    - `bool` `true` `false` 由 `stdbool.h` 提供
    - 调用方在返回值无效时提示重试，有效时调用计算函数

!!! warning "常见错误"

    - 写成链式 `else if`，只报告第一个问题
    - 忘记包含 `stdbool.h`，或在不支持 `_Bool` 的编译器上直接使用

## 菜单循环

!!! abstract "语法形式"

    ```c
    while ((choice = get_choice()) != 'q')
    {
        switch (choice)
        {
            case 'a': /* 动作 */
                      break;
            default:  /* 不应到达 */
                      break;
        }
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch;
        while ((ch = getchar()) != 'q')
        {
            switch (ch)
            {
                case 'a': printf("advice\n"); break;
                case 'b': putchar('\a'); break;
                default:  printf("?\n"); break;
            }
            while (getchar() != '\n')
                continue;
        }
        printf("Bye.\n");
        return 0;
    }
    ```

    输出：

    ```text
    a
    advice
    x
    ?
    q
    Bye.
    ```

!!! note "说明"

    - `while` 控制重复访问菜单，`switch` 按选项分派动作
    - 上例直接用 `getchar()` 取选项，完整版本改用 `get_choice()`
    - `get_choice()` 只返回菜单中的选项字符与终止字符 `'q'`
    - `default` 用于发现筛选函数漏掉的取值，正常运行时不应到达
    - 退出循环后统一打印结束语

!!! warning "常见错误"

    - `case` 分支漏写 `break`，执行落到下一个分支
    - 用 `switch` 外的 `if` 处理终止字符，与 `while` 条件重复

## 菜单选项的读取

!!! abstract "语法形式"

    ```c
    char get_choice(void)
    ```

!!! example "示例"

    ```c
    char get_choice(void)
    {
        int ch;
        printf("a. advice  b. bell\nc. count   q. quit\n");
        ch = get_first();
        while ((ch < 'a' || ch > 'c') && ch != 'q')
        {
            printf("Respond with a, b, c, or q: ");
            ch = get_first();
        }
        return ch;
    }
    ```

!!! note "说明"

    - 读取过程与 `getchar()` 相同，循环直到得到合法选项
    - 合法范围是 `'a'` 到 `'c'`，加上终止字符 `'q'`
    - 返回值约定与 `getchar()` 一致，便于放进 `while` 条件
    - 依赖 `get_first()` 清理本行，否则回车产生的换行符被当作非法选项

!!! warning "常见错误"

    - 条件写成 `ch < 'a' || ch > 'c' || ch != 'q'`，逻辑永真
    - 用 `getchar()` 代替 `get_first()`，输入 `act` 时把 `c` 当成选项

## 读取行首字符

!!! abstract "语法形式"

    ```c
    int get_first(void)
    {
        int ch = getchar();
        while (getchar() != '\n')
            continue;
        return ch;
    }
    ```

!!! note "说明"

    - 返回本行第一个字符，其余字符读掉
    - 输入 `act` 按 `a` 处理，不会把 `c` 当作下一次的选项
    - 本行只有回车时返回换行符，由调用方判断
    - 返回类型用 `int`，与 `getchar()` 保持一致

!!! warning "常见错误"

    - 声明返回 `char`，在需要与 `EOF` 比较时失效
    - 在 `scanf()` 之后立即调用，返回的是数字后面残留的换行符

## 菜单中混用数值输入

!!! abstract "语法形式"

    ```c
    n = get_int();
    /* 处理 n */
    while (getchar() != '\n')
        continue;
    ```

!!! example "示例"

    ```c
    void count(void)
    {
        int n, i;
        printf("Count how far? ");
        n = get_int();
        while (getchar() != '\n')
            continue;
        for (i = 1; i <= n; i++)
            printf("%d\n", i);
    }
    ```

    输出：

    ```text
    Count how far? two
    two is not an integer. Try again: 5
    1
    2
    3
    4
    5
    ```

!!! note "说明"

    - `scanf()` 读完数字把换行符留在队列，下一次读取会先拿到它
    - 两种处理： 在读数值的函数内清掉本行，或让 `get_first()` 跳过前导空白
    - 读数值的函数与 `get_long()` 结构相同，转换说明改为 `%d`，变量改为 `int`
    - 输入非法时函数内部循环提示，不返回菜单

!!! warning "常见错误"

    - 只在菜单处清行，数值输入后仍残留换行
    - 把清理循环写在 `for` 之前，循环输出尚未占用的行内还有残留

## 复习题

（1）`putchar(getchar())` 是一个有效表达式，它实现什么功能？
`getchar(putchar())` 是否也是有效表达式？

??? note "答案"

    前者读取下一个输入字符并打印
    `getchar()` 的返回值作为 `putchar()` 的参数
    后者无效，`getchar()` 不接受参数
    而 `putchar()` 需要参数

（2）下面的语句分别完成什么任务？
a. `putchar('H');`
b. `putchar('\007');`
c. `putchar('\n');`
d. `putchar('\b');`

??? note "答案"

    a 显示字符 `H`. b 在 ASCII 系统上发出一声警报。 c 把光标移到下一行开头。 d 光标退后一格

（3）假设有一个名为 `count` 的可执行程序，用于统计输入的字符数
设计一个使用 `count` 程序统计 `essay` 文件中字符数的命令行
并把统计结果保存在 `essayct` 文件中

??? note "答案"

    `count <essay >essayct` 或 `count >essayct <essay`

（4）给定复习题 3 中的程序和文件，下面哪一条是有效的命令？
a. `essayct <essay`
b. `count essay`
c. `essay >count`

??? note "答案"

    都不是有效命令

（5）`EOF` 是什么？

??? note "答案"

    `EOF` 是 `getchar()` 与 `scanf()` 检测到文件结尾时返回的特殊值

（6）对下面的输入与程序段，分别写出输出。 `ch` 是 `int` 类型，输入为缓冲输入
a. 输入
```c
If you quit, I will.
```
程序段
```c
while ((ch = getchar()) != 'i')
   putchar(ch);
```
b. 输入
```c
Harhar
```
程序段
```c
while ((ch = getchar()) != '\n')
{
   putchar(ch++);
   putchar(++ch);
}
```

??? note "答案"

    a 输出 `If you qu`
    字符 `I` 与 `i` 不同，检测到 `i` 后循环退出，`i` 不打印
    b 在 ASCII 系统上输出 `HJacrthjacrt`
    第一轮读入 `H`，先打印 `H` 再自增为 `I`
    第二个 `putchar()` 先自增为 `J` 再打印
    下一轮读入 `a`，重复同一过程

（7）C 如何处理不同计算机系统中的不同文件和换行约定？

??? note "答案"

    C 的标准 I/O 库把不同的文件映射为统一的流来处理

（8）在使用缓冲输入的系统中，把数值和字符混合输入会遇到什么潜在的问题？

??? note "答案"

    数值输入跳过空格与换行符，字符输入不跳过
    输入数字后按回车留下的换行符会成为下一次字符读取的值
    应在字符输入前清掉它

    ```c
    int score;
    char grade;
    printf("Enter the score.\n");
    scanf("%d", &score);
    printf("Enter the letter grade.\n");
    grade = getchar();          /* 读到的是残留换行符 */
    ```

    [附录答案此处写作 `scanf("%s", &score);`
    `%s` 与 `int` 变量不匹配，应为 `%d`，上例按此更正]

## 编程练习

!!! question "编程练习"

    1. 设计一个程序，统计在读到文件结尾之前读取的字符数

    2. 编写一个程序，在遇到 `EOF` 之前把输入作为字符流读取
       程序打印每个输入字符及其 ASCII 十进制值
       空格之前的字符都是非打印字符，需要特殊处理
       换行符打印 `\n`，制表符打印 `\t`
       其他非打印字符用控制字符表示法
       例如 ASCII 值为 1 的字符显示为 `^A`
       `A` 的 ASCII 值等于 Ctrl+A 的值加 64
       除遇到换行符时另起一行外，每行打印 10 对值

    3. 编写一个程序，在遇到 `EOF` 之前把输入作为字符流读取
       报告大写字母与小写字母的个数
       可以假定字母编码连续，或使用 `ctype.h` 的分类函数

    4. 编写一个程序，在遇到 `EOF` 之前把输入作为字符流读取
       报告平均每个单词的字母数
       空白不计为字母，标点符号可以暂不计较

    5. 修改猜数字程序，使用二分查找策略
       程序最初猜 `50`，询问用户猜大了，猜小了还是猜对了
       猜小时下一次取剩余区间的中值，猜大时同理

    6. 修改 `get_first()` 函数，使其返回读取的第一个非空白字符，并在一个简单程序中测试

    7. 修改第 7 章的编程练习 8，用字符代替数字标记菜单选项，用 `q` 代替 `5` 作为结束标记

    8. 编写一个程序，显示提供加法，减法，乘法，除法的菜单
       用户选择后提示输入两个数字，执行相应运算
       程序只接受菜单提供的选项
       用 `float` 变量储存输入的数字，输入失败时允许重新输入
       除法运算中第二个数为 `0` 时提示重新输入
