# 第7章 C控制语句：分支和跳转

## if 语句

!!! abstract "语法形式"

    ```c
    if (表达式)
        语句
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int temperature = -3;
        if (temperature < 0)
            printf("below freezing\n");
        return 0;
    }
    ```

    输出：

    ```text
    below freezing
    ```

!!! note "说明"

    - 表达式求值为非 `0` 时执行语句，为 `0` 时跳过
    - 表达式可以是任意类型，通常是关系表达式
    - 语句可以是一条简单语句，也可以是用花括号括起的复合语句
    - 复合语句在语法上仍算一条语句
    - `if` 只测试并执行一次，`while` 可反复测试

!!! warning "常见错误"

    - 写成 `if (x = 5)`，赋值表达式的值非 `0`，条件恒为真，应写 `==`
    - 条件后多写分号，如 `if (x > 0);`，语句部分变成空语句
    - 需要执行多条语句时漏写花括号

## if else 语句

!!! abstract "语法形式"

    ```c
    if (表达式)
        语句1
    else
        语句2
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a = 3, b = 8, max;
        if (a > b)
            max = a;
        else
            max = b;
        printf("max = %d\n", max);
        return 0;
    }
    ```

    输出：

    ```text
    max = 8
    ```

!!! note "说明"

    - 表达式为真执行语句1，为假执行语句2，两条分支只执行一条
    - 两条分支都可以是简单语句或复合语句
    - 缩进不是语法要求，只影响阅读
    - `else if` 是 `else` 后紧跟另一条 `if`，由内层 `if else` 嵌套而成

!!! warning "常见错误"

    - 在 `if` 与 `else` 之间写两条语句
      编译器把第一条当作 `if` 的语句，第二条单独成句
      `else` 找不到所属的 `if`，编译报错

    ```c
    if (x > 0)
        printf("x > 0\n");
        x++;          // 不属于 if
    else              // 错误: else 没有匹配的 if
        printf("x <= 0\n");
    ```

    - 靠缩进判断 `else` 的归属，编译器会忽略缩进
    - 需要执行多条语句时漏写花括号

## else if 多重选择

!!! abstract "语法形式"

    ```c
    if (表达式1)
        语句1
    else if (表达式2)
        语句2
    else
        语句3
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int score = 85;
        if (score >= 90)      puts("A");
        else if (score >= 80) puts("B");
        else if (score >= 70) puts("C");
        else                  puts("D");
        return 0;
    }
    ```

    输出：

    ```text
    B
    ```

!!! note "说明"

    - 条件按书写顺序测试，执行第一个为真的分支后跳过其余分支
    - 前面的条件为假是进入后续分支的前提，后续条件不必重复下界
    - 该结构等价于在 `else` 部分再嵌套一条 `if else`
    - 整条 `if else` 算一条语句，嵌套时不必加花括号
    - C99 要求编译器至少支持 127 层嵌套

    [教材程序清单 7.4 的 `BASE3` 定义为 `BASE1 + BASE2 + ...`
    - 多计了一次 `BASE1`，超过 720 kWh 时电费偏高
    - 按分段累计的写法应为 `BASE2 + (RATE3 * (BREAK3 - BREAK2))`
    - 同节正文把第 2 个分界点写成 482 kWh，与 `#define BREAK2 468.0` 不符
    - 以 468 为准]

!!! warning "常见错误"

    - 把最宽的条件写在最前面，后面的分支永远执行不到
    - 在 `else if` 链末尾漏写 `else`，部分输入没有对应分支
    - 用 `switch` 可以表达的等值判断写成过长的 `else if` 链

## else 与 if 的配对

!!! abstract "语法形式"

    ```c
    if (表达式1)
        if (表达式2)
            语句1
        else
            语句2
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int number = 15;
        if (number > 6)
            if (number < 12)
                printf("close\n");
            else
                printf("lose a turn\n");
        return 0;
    }
    ```

    输出：

    ```text
    lose a turn
    ```

!!! note "说明"

    - 没有花括号时，`else` 与离它最近的未配对 `if` 匹配
    - 上例中 `else` 属于内层 `if`，对应 `number >= 12`
    - 最近的 `if` 已被花括号括起时，`else` 与外层 `if` 匹配
    - 要让 `else` 归属外层，用花括号把内层 `if` 包起来

    ```c
    if (number > 6)
    {
        if (number < 12)
            printf("close\n");
    }
    else
        printf("lose a turn\n");
    ```

!!! warning "常见错误"

    - 以为缩进决定配对关系
    - 内外层 `if` 都不加花括号，修改时 `else` 归属随之改变

## getchar() 与 putchar()

!!! abstract "语法形式"

    ```c
    ch = getchar();
    putchar(ch);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch;
        printf("Enter a line: ");
        while ((ch = getchar()) != '\n')
            putchar(ch + 1);
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    Enter a line: CALL
    DBMM
    ```

!!! note "说明"

    - `getchar()` 不带参数，从输入队列返回下一个字符，无输入时返回 `EOF`
    - `putchar()` 输出一个字符，只处理参数的最低一个字节
    - 这两个函数效果分别等同 `scanf("%c", &ch)` 与 `printf("%c", ch)`
    - 不需要转换说明，比通用的 `scanf()` 与 `printf()` 更快，更简洁
    - 通常定义在 `stdio.h` 中，多数实现把它们写成预处理宏
    - 返回值为 `int`，用 `char` 接收时无法区分 `EOF` 与普通字符

!!! warning "常见错误"

    - 把返回值存入 `char` 变量，读到文件末尾时无法识别 `EOF`，循环不结束
    - 以为 `putchar()` 会自动换行，换行符需要单独输出
    - 用带参数的写法 `getchar(ch)`

## 测试条件中的赋值表达式

!!! abstract "语法形式"

    ```c
    while ((变量 = 读取函数()) != 结束值)
        语句
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch, sum = 0;
        printf("Enter a line: ");
        while ((ch = getchar()) != '\n')
            sum += ch;
        printf("%d\n", sum);
        return 0;
    }
    ```

    输出：

    ```text
    Enter a line: AB
    131
    ```

!!! note "说明"

    - 赋值表达式的值等于赋给左侧对象的新值
    - 先调用读取函数，再把返回值赋给变量，最后与结束值比较
    - `ch = getchar()` 两侧的圆括号不能省略
      省略后 `!=` 先结合，赋给 `ch` 的是比较结果 `0` 或 `1`
    - 这种写法把读取与判断合并，循环体内不再读取
    - 每轮迭代只读取一个字符

!!! warning "常见错误"

    - 写成 `while (ch = getchar() != '\n')`，赋值对象错成比较结果
    - 圆括号只包住一个标识符，如 `while ((ch) = getchar() != '\n')`
    - 循环体内又调用一次 `getchar()`，每轮跳过两个字符

## ctype.h 字符函数

!!! abstract "语法形式"

    ```c
    #include <ctype.h>
    isalpha(ch);
    isdigit(ch);
    isspace(ch);
    toupper(ch);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <ctype.h>
    int main(void)
    {
        int ch;
        printf("Enter a line: ");
        while ((ch = getchar()) != '\n')
            putchar(isalpha(ch) ? toupper(ch) : ch);
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    Enter a line: Look! 42
    LOOK! 42
    ```

    表7-1 ctype.h 字符测试函数

    | 函数名 | 参数满足条件时返回真 |
    | --- | --- |
    | `isalnum()` | 字母或数字 |
    | `isalpha()` | 字母 |
    | `isblank()` | 空格或水平制表符 |
    | `iscntrl()` | 控制字符，如 `Ctrl+B` |
    | `isdigit()` | 数字 |
    | `isgraph()` | 除空格外的可打印字符 |
    | `islower()` | 小写字母 |
    | `isprint()` | 可打印字符，含空格 |
    | `ispunct()` | 标点符号，即除空格与字母数字外的可打印字符 |
    | `isspace()` | 空格，换行，换页，回车，垂直制表，水平制表 |
    | `isupper()` | 大写字母 |
    | `isxdigit()` | 十六进制数字字符 |

    表7-2 ctype.h 字符映射函数

    | 函数名 | 行为 |
    | --- | --- |
    | `tolower()` | 参数为大写字母时返回小写形式，否则返回原值 |
    | `toupper()` | 参数为小写字母时返回大写形式，否则返回原值 |

!!! note "说明"

    - 测试函数在参数属于该类时返回非 `0`，否则返回 `0`
    - 映射函数返回修改后的值，不修改实参
      写成 `tolower(ch);` 不改变 `ch`，应写 `ch = tolower(ch);`
    - 参数的值应能表示为 `unsigned char`，或等于 `EOF`，否则行为未定义
    - 与直接比较字符编码相比，这些函数不依赖具体编码

    [教材表 7.1 把换行符列入 `isblank()` 的判定范围
    - C 标准在默认区域设置下只把空格与水平制表符归为空白字符
    - 换行符属于 `isspace()` 的判定范围]

!!! warning "常见错误"

    - 调用映射函数后未赋值，以为原变量已被改写
    - 把函数名当变量，如 `if (isalpha)` 漏写参数
    - 用 `isalpha(ch)` 判断时 `ch` 为负值，触发未定义行为

## 逻辑运算符

!!! abstract "语法形式"

    ```c
    表达式1 && 表达式2
    表达式1 || 表达式2
    !表达式
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch, n = 0;
        printf("Enter text: ");
        while ((ch = getchar()) != '.')
            if (ch != '"' && ch != '\'')
                n++;
        printf("%d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    Enter text: ab"c'.
    3
    ```

    表7-3 逻辑运算符

    | 运算符 | 含义 | 运算对象个数 |
    | --- | --- | --- |
    | `&&` | 与 | 2 |
    | `\|\|` | 或 | 2 |
    | `!` | 非 | 1 |

!!! note "说明"

    - `exp1 && exp2` 当且仅当两者都为真时为真
    - `exp1 || exp2` 任一侧为真即为真
    - `!exp` 在 `exp` 为假时为真，反之亦然
    - 运算对象按真值处理，非 `0` 为真，`0` 为假
    - `5 > 2 && 4 > 7` 为假，`5 > 2 || 4 > 7` 为真
    - `!(4 > 7)` 等价于 `4 <= 7`
    - 逻辑运算符的优先级低于关系运算符，子表达式不必加圆括号

!!! warning "常见错误"

    - 写成 `if (ch != 'q' && != 'Q')`，第二个比较缺左侧表达式
    - 用 `||` 连接两个本应同时成立的条件
    - 把 `!` 的作用范围记错，`!a > b` 解释为 `(!a) > b`

## 逻辑运算符的优先级与求值顺序

!!! note "说明"

    - `!` 与前置 `++` 同属一元运算符，低于括号与后缀运算符
    - `&&` 的优先级高于 `||`
    - 两者都低于关系运算符，高于赋值运算符
    - `a > b && b > c || b > d` 等价于
      `((a > b) && (b > c)) || (b > d)`
    - `&&` 与 `||` 保证从左到右求值
    - 结果一旦确定就停止求值，右侧的副作用不再发生
    - 两个运算符都是序列点，左侧的副作用在右侧求值前完成

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int number = 0;
        if (number != 0 && 12 / number == 2)
            printf("5 or 6\n");
        else
            printf("guarded\n");
        return 0;
    }
    ```

    输出：

    ```text
    guarded
    ```

!!! note "说明"

    - 上例中第一个子表达式为假，右侧的除法不求值，避免了除数为 `0`

    ```c
    while ((c = getchar()) != ' ' && c != '\n')
        putchar(c);
    ```

    - 这行依赖从左到右求值： 先把读到的字符赋给 `c`，再比较 `c`

!!! warning "常见错误"

    - 在 `&&` 左侧写不具有副作用的比较，右侧却依赖某个赋值
    - 以为 `||` 会求值两侧，把必须执行的语句写在右侧
    - 把 `&&` 与 `||` 的优先级记反，以为 `||` 先结合

## 逻辑运算符测试范围

!!! abstract "语法形式"

    ```c
    if (下限 <= 变量 && 变量 <= 上限)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int range = 95;
        if (range >= 90 && range <= 100)
            printf("good\n");
        else
            printf("bad\n");
        return 0;
    }
    ```

    输出：

    ```text
    good
    ```

!!! note "说明"

    - 数学写法 `90 <= range <= 100` 在 C 中不能表达范围
    - 关系运算符从左到右结合，上式解释为 `(90 <= range) <= 100`
    - 子表达式的值为 `0` 或 `1`，两者都小于 `100`，整个表达式恒为真
    - 该错误属于语义错误，编译器通常只给警告
    - 字符范围 `ch >= 'a' && ch <= 'z'` 依赖编码中字母连续
    - 可移植的替代写法是 `islower(ch)`

!!! warning "常见错误"

    - 照数学写法写连续比较
    - 把范围条件之间的 `&&` 写成 `,` 或 `&`
    - 在 EBCDIC 等编码上使用字母范围比较

## iso646.h 备选拼写

!!! abstract "语法形式"

    ```c
    #include <iso646.h>
    a and b
    a or b
    not a
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <iso646.h>
    int main(void)
    {
        int ch = 'q';
        if (ch != 'q' and ch != 'k')
            printf("other\n");
        else
            printf("q or k\n");
        return 0;
    }
    ```

    输出：

    ```text
    q or k
    ```

    表7-4 逻辑运算符的备选拼写

    | 传统写法 | iso646.h |
    | --- | --- |
    | `&&` | `and` |
    | `\|\|` | `or` |
    | `!` | `not` |

!!! note "说明"

    - C99 引入，用于没有这些符号键的键盘
    - `and` `or` `not` 是宏，不是关键字
    - 必须包含 `iso646.h` 才能使用
    - 除了逻辑运算符，该头文件还定义了其他运算符的备选拼写

!!! warning "常见错误"

    - 不包含头文件直接使用 `and`，编译器当作未声明的标识符
    - 在 C++ 环境下测试后，误以为 C 中也不需头文件

## 条件运算符 ?:

!!! abstract "语法形式"

    ```c
    条件 ? 表达式1 : 表达式2
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int y = -7, x;
        x = (y < 0) ? -y : y;
        printf("%d\n", x);
        return 0;
    }
    ```

    输出：

    ```text
    7
    ```

!!! note "说明"

    - 条件为真时整个表达式的值取表达式1，否则取表达式2
    - 条件运算符是 C 中唯一的三元运算符
    - 常用形式 `max = (a > b) ? a : b;`
    - 第二与第三运算对象可以是字符串，如 `cans == 1 ? "can" : "cans"`
    - 与等价的 `if else` 相比，代码更简洁，可作表达式的一部分
    - 只能替代在两条分支中选值的情形，不能替代需要执行语句的分支

!!! warning "常见错误"

    - 分支中写赋值表达式时漏写圆括号，如 `y < 0 ? x = -y : x = y`
    - 嵌套使用时漏写圆括号，结合方向出错
    - 把 `?:` 用在需要执行多条语句的分支上

## continue 语句

!!! abstract "语法形式"

    ```c
    continue;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch, n = 0;
        printf("Enter a line: ");
        while ((ch = getchar()) != '\n')
        {
            if (ch == ' ') continue;
            n++;
        }
        printf("%d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    Enter a line: a b c
    3
    ```

    表7-5 continue 之后的下一步

    | 循环 | 下一步 |
    | --- | --- |
    | `while` | 求值循环测试表达式 |
    | `do while` | 求值出口条件 |
    | `for` | 先执行更新表达式，再求值测试表达式 |

!!! note "说明"

    - 跳过本次迭代的剩余部分，开始下一轮
    - 只影响包含它的最内层循环
    - 可用于 `while` `do while` `for` 三种循环
    - 单独用于 `switch` 不合法，但可出现在循环内的 `switch` 中
      此时直接开始下一轮循环，不再执行 `switch` 的其余部分
    - 循环体为空时可用 `continue;` 代替单独的分号，便于辨认
    - 简化代码时可以用反转 `if` 条件代替

!!! warning "常见错误"

    - 在 `while` 循环中把更新控制变量的语句放在 `continue` 之后，形成死循环
    - 以为 `continue` 会跳过 `for` 的更新表达式
    - 在嵌套循环中以为 `continue` 影响外层循环

## break 语句

!!! abstract "语法形式"

    ```c
    break;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch;
        printf("Enter a line: ");
        while ((ch = getchar()) != '\n')
        {
            if (ch == ' ') break;
            putchar(ch);
        }
        return 0;
    }
    ```

    输出：

    ```text
    Enter a line: ab cd
    ab
    ```

!!! note "说明"

    - 终止当前循环，转到循环后的第一条语句
    - 可用于循环与 `switch`
    - 在 `switch` 中转到 `switch` 之后，不再执行其余标签
    - 只跳出最内层循环，跳出多层需要逐层 `break` 或使用 `goto`
    - 在 `for` 循环中直接跳过更新表达式
    - 与 `continue` 的区别在于结束整个循环，而非只结束本次迭代

!!! warning "常见错误"

    - 嵌套循环中只写一个 `break`，以为能跳出两层
    - 在 `switch` 中漏写 `break`，继续执行后面的分支
    - 用 `break` 代替条件判断，让循环出口分散在多处

## switch 语句

!!! abstract "语法形式"

    ```c
    switch (整型表达式)
    {
    case 常量1:
        语句
        break;
    case 常量2:
        语句
        break;
    default:
        语句
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch = 'b';
        switch (ch)
        {
        case 'a': puts("argali"); break;
        case 'b': puts("babirusa"); break;
        default:  puts("unknown");
        }
        return 0;
    }
    ```

    输出：

    ```text
    babirusa
    ```

!!! note "说明"

    - 先求值括号中的表达式，再与各 `case` 标签比较
    - 匹配后从该标签开始顺序执行，直到遇到 `break` 或到达 `switch` 末尾
    - 没有标签匹配时转到 `default`，没有 `default` 时跳过整个 `switch`
    - 测试表达式必须是整型，包括 `char`，不能是浮点类型
    - `case` 标签必须是整型常量表达式，不能用变量
    - 各 `case` 的常量值不能重复
    - `default` 可放在任意位置，习惯放在末尾
    - `switch` 可以嵌套

!!! warning "常见错误"

    - 漏写 `break`，发生贯穿，继续执行后续分支的语句
    - 用 `case 1.5:` 或 `case n:` 作标签
    - 在 C99 与 C11 中，`case` 标签后不能直接写声明，标签必须跟一条语句
    - 把 `switch` 用于浮点数或字符串的比较

## switch 的多重标签

!!! abstract "语法形式"

    ```c
    case 常量1:
    case 常量2:
        语句
        break;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int ch = 'e', n = 0;
        switch (ch)
        {
        case 'a': case 'e': case 'i':
        case 'o': case 'u': n++; break;
        }
        printf("%d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    1
    ```

!!! note "说明"

    - 多个 `case` 标签可以共用同一条语句
    - 标签之间没有语句时，程序流继续落到下一个标签
    - 共用语句前的所有标签都指向同一条语句
    - 最后一组标签的 `break` 删去也不影响结果，保留可防止以后添加标签时遗漏
    - 大小写字母可用 `toupper()` 或 `tolower()` 先统一，减少标签数量
    - 也可把转换写在测试表达式中，如 `switch (toupper(ch))`

!!! warning "常见错误"

    - 在共用的标签之间误插语句，导致部分分支提前执行
    - 添加新标签后忘记补 `break`

## switch 与 if else 的选择

!!! note "说明"

    - `switch` 只能对整型表达式做等值比较，分支标签是整型常量
    - `if else` 可以比较浮点数，字符串，也可以测试范围
    - 用 `switch` 覆盖一个整数范围需要为每个值写一个标签，不实用
    - `switch` 通常生成更紧凑的代码，分支多时运行更快
    - 判断条件为等值且分支较多时用 `switch`
    - 判断条件为不等式，范围或浮点时用 `if else`

    表7-6 switch 与 if else 的适用范围

    | 判据 | switch | if else |
    | --- | --- | --- |
    | 整型等值 | 适用 | 适用 |
    | 浮点数或字符串 | 不适用 | 适用 |
    | 范围比较 | 不适用 | 适用 |
    | 代码紧凑度 | 通常更好 | 一般 |

## goto 语句

!!! abstract "语法形式"

    ```c
    goto 标签;
    ...
    标签: 语句
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int i, j;
        for (i = 0; i < 3; i++)
            for (j = 0; j < 3; j++)
                if (i * 10 + j == 12) goto found;
    found:
        printf("%d %d\n", i, j);
        return 0;
    }
    ```

    输出：

    ```text
    1 2
    ```

!!! note "说明"

    - 标签名遵循变量命名规则，后面跟一个冒号
    - 标签可以写在 `goto` 之前或之后，只在所在函数内有效
    - 跳出多层嵌套循环是常见用法，一条 `break` 只能跳出一层
    - 跳转到函数末尾统一清理资源也是常见用法
    - 不能跳过可变长度数组的声明进入其作用域
    - `break` 与 `continue` 可以看作受限的 `goto`，名称已说明用途

    [教材称原则上不必在 C 程序中使用 `goto`
    - 现行编码规范通常允许两类用法： 一次跳出多层循环，以及跳转到末尾统一释放资源
    - Linux 内核编码风格也采用第二种用法，并要求标签名写明清理动作]

!!! warning "常见错误"

    - 用 `goto` 代替 `if else` 或循环，破坏程序的结构
    - 跳到会跳过变量初始化的位置，变量处于未初始化状态
    - 标签重名，同一函数内标签不能重复

## 复习题

（1）判断下列表达式是 true 还是 false
a. `100 > 3 && 'a' > 'c'`
b. `100 > 3 || 'a' > 'c'`
c. `!(100 > 3)`

??? note "答案"

    a. `false`，b. `true`，c. `false`

（2）根据下列条件分别构造一个表达式
a. `number` 等于或大于 `90`，但小于 `100`
b. `ch` 不是字符 `q` 或 `k`
c. `number` 在 `1` 至 `9` 之间，包括两端，但不是 `5`
d. `number` 不在 `1` 至 `9` 之间

??? note "答案"

    a. `number >= 90 && number < 100`

    b. `ch != 'q' && ch != 'k'`

    c. `(number >= 1 && number <= 9) && number != 5`

    d. `number < 1 || number > 9`
    也可写成 `!(number >= 1 && number <= 9)`，但前者更易读

（3）下面的程序关系表达式过于复杂，而且还有些错误，请简化并改正
```c
#include <stdio.h>                                   /* 1 */
int main(void)                                       /* 2 */
{                                                    /* 3 */
    int weight, height;                              /* 4 */
    scanf("%d , weight, height);                     /* 5 */
    if (weight < 100 && height > 64)                 /* 6 */
        if (height >= 72)                            /* 7 */
            printf("You are very tall for your weight.\n");  /* 8 */
        else if (height < 72 && > 64)                /* 9 */
            printf("You are tall for your weight.\n");       /* 10 */
        else if (weight > 300 && !(weight <= 300)    /* 11 */
            && height < 48)                          /* 12 */
        if (!(height >= 48))                         /* 13 */
            printf(" You are quite short for your weight.\n"); /* 14 */
    else                                             /* 15 */
        printf("Your weight is ideal.\n");           /* 16 */
    return 0;
}
```

??? note "答案"

    第 `5` 行应为 `scanf("%d %d", &weight, &height);`，前面还应加提示输入

    第 `9` 行中，能到达该处的 `height` 必定小于 `72`，且第 `6` 行已保证
    `height > 64`，该行改为 `else`

    第 `11` 行的条件与第 `1` 个表达式重复
    更严重的是 `else if` 按最近配对规则与第 `9` 行配对
    而到达该处时 `weight` 不可能超过 `300`

    第 `7` 至 `10` 行应用花括号括起，使第 `11` 行与第 `6` 行的 `if` 匹配
    第 `9` 行改成简单 `else` 后，不必再加花括号

    第 `13` 行应删去，第 `12` 行已测试过同一条件

    ```c
    #include <stdio.h>
    int main(void)
    {
        int weight, height;

        printf("Enter your weight in pounds and ");
        printf("your height in inches.\n");
        scanf("%d %d", &weight, &height);
        if (weight < 100 && height > 64)
            if (height >= 72)
                printf("You are very tall for your weight.\n");
            else
                printf("You are tall for your weight.\n");
        else if (weight > 300 && height < 48)
            printf(" You are quite short for your weight.\n");
        else
            printf("Your weight is ideal.\n");

        return 0;
    }
    ```

（4）下列各表达式的值是多少
a. `5 > 2`
b. `3 + 4 > 2 && 3 < 2`
c. `x >= y || y > x`
d. `d = 5 + (6 > 2)`
e. `'X' > 'T' ? 10 : 5`
f. `x > y ? y > x : x > y`

??? note "答案"

    a. `1`，`5` 大于 `2`，表达式为真

    b. `0`，`3 + 4 > 2` 为真，但 `3 < 2` 为假，`&&` 的结果为假

    c. `1`，两个子表达式总有一个为真

    d. `6`，`6 > 2` 的值为 `1`，故 `5 + 1` 得 `6`

    e. `10`，条件为真

    f. `0`，条件为真时取 `y > x`，为假时取 `x > y`，两者都为假

（5）下面的程序将打印什么
```c
#include <stdio.h>
int main(void)
{
    int num;
    for (num = 1; num <= 11; num++)
    {
        if (num % 3 == 0)
            putchar('$');
        else
            putchar('*');
        putchar('#');
        putchar('%');
    }
    putchar('\n');
    return 0;
}
```

??? note "答案"

    ```text
    *#%*#%$#%*#%*#%$#%*#%*#%$#%*#%*#%
    ```

    每轮循环都会打印 `#`，缩进不能让 `putchar('#');` 成为 `if else` 的一部分

（6）下面的程序将打印什么
```c
#include <stdio.h>
int main(void)
{
    int i = 0;
    while (i < 3) {
        switch (i++) {
            case 0: printf("fat ");
            case 1: printf("hat ");
            case 2: printf("cat ");
            default: printf("Oh no!");
        }
        putchar('\n');
    }
    return 0;
}
```

??? note "答案"

    ```text
    fat hat cat Oh no!
    hat cat Oh no!
    cat Oh no!
    ```

    `switch` 中的 `case` 都没有 `break`，匹配后继续执行后续分支

（7）下面的程序有哪些错误
```c
#include <stdio.h>
int main(void)
{
    char ch;
    int lc = 0; /* 统计小写字母
    int uc = 0; /* 统计大写字母
    int oc = 0; /* 统计其他字母
    while ((ch = getchar()) != '#')
    {
        if ('a' <= ch >= 'z')
            lc++;
        else if (!(ch < 'A') || !(ch > 'Z')
            uc++;
        oc++;
    }
    printf(%d lowercase, %d uppercase, %d other, lc, uc, oc);
    return 0;
}
```

??? note "答案"

    第 `5` 至 `7` 行的注释缺少 `*/`，或把开头的 `/*` 换成 `//`

    `'a' <= ch >= 'z'` 应写作 `ch >= 'a' && ch <= 'z'`
    关系运算符从左到右结合，原式先求 `'a' <= ch` 得到 `0` 或 `1`
    再用该值比较 `>= 'z'`，结果恒为 `0`
    更简单的写法是 `islower(ch)`

    第 `2` 个条件中的 `||` 应为 `&&`，`'z'` 后缺少右括号
    `!(ch < 'A')` 可简化为 `ch >= 'A'`，或用 `isupper(ch)`

    `oc++;` 前缺少 `else`，否则每读一个字符它都递增

    `printf()` 的格式串缺少双引号

    ```c
    #include <stdio.h>
    #include <ctype.h>
    int main(void)
    {
        char ch;
        int lc = 0;  /* 统计小写字母 */
        int uc = 0;  /* 统计大写字母 */
        int oc = 0;  /* 统计其他字符 */

        while ((ch = getchar()) != '#')
        {
            if (islower(ch))
                lc++;
            else if (isupper(ch))
                uc++;
            else
                oc++;
        }
        printf("%d lowercase, %d uppercase, %d other",
               lc, uc, oc);
        return 0;
    }
    ```

（8）下面的程序将打印什么
```c
/* retire.c */
#include <stdio.h>
int main(void)
{
    int age = 20;
    while (age++ <= 65)
    {
        if ((age % 20) == 0)
            printf("You are %d. Here is a raise.\n", age);
        if (age = 65)
            printf("You are %d. Here is your gold watch.\n", age);
    }
    return 0;
}
```

??? note "答案"

    程序不停地重复打印下面一行

    ```text
    You are 65. Here is your gold watch.
    ```

    问题在 `if (age = 65)`，它把 `65` 赋给 `age`，赋值表达式的值非 `0`
    每次迭代的测试条件都为真，循环无法结束

（9）给定下面的输入时，以下程序将打印什么
```
q
c
h
b
```
```c
#include <stdio.h>
int main(void)
{
    char ch;
    while ((ch = getchar()) != '#')
    {
        if (ch == '\n')
            continue;
        printf("Step 1\n");
        if (ch == 'c')
            continue;
        else if (ch == 'b')
            break;
        else if (ch == 'h')
            goto laststep;
        printf("Step 2\n");
    laststep: printf("Step 3\n");
    }
    printf("Done\n");
    return 0;
}
```

??? note "答案"

    ```text
    q
    Step 1
    Step 2
    Step 3
    c
    Step 1
    h
    Step 1
    Step 3
    b
    Step 1
    Done
    ```

    `b` 与 `#` 都能结束循环
    输入 `b` 时先打印 `Step 1`，输入 `#` 时不会

（10）重写复习题 9，但不能使用 `continue` 和 `goto` 语句

??? note "答案"

    ```c
    #include <stdio.h>
    int main(void)
    {
        char ch;
        while ((ch = getchar()) != '#')
        {
            if (ch != '\n')
            {
                printf("Step 1\n");
                if (ch == 'b')
                    break;
                else if (ch != 'c')
                {
                    if (ch != 'h')
                        printf("Step 2\n");
                    printf("Step 3\n");
                }
            }
        }
        printf("Done\n");
        return 0;
    }
    ```

## 编程练习

!!! question "编程练习"

    1. 编写一个程序读取输入，读到 `#` 字符停止
    然后报告读取的空格数，换行符数和所有其他字符的数量

    2. 编写一个程序读取输入，读到 `#` 字符停止
    程序打印每个输入的字符以及对应的 ASCII 码，用十进制表示
    每行打印 8 个字符与 ASCII 码的组合
    提示： 用字符计数与求模运算符 `%` 在每 8 个循环周期打印一个换行符

    3. 编写一个程序，读取整数直到用户输入 `0`
    输入结束后报告输入的偶数个数，这些偶数的平均值
    以及输入的奇数个数与奇数平均值，偶数不包括 `0`

    4. 使用 `if else` 语句编写一个程序读取输入，读到 `#` 停止
    用感叹号替换句号，用两个感叹号替换原来的感叹号
    最后报告进行了多少次替换

    5. 使用 `switch` 重写练习 4

    6. 编写程序读取输入，读到 `#` 停止，报告 `ei` 出现的次数
    程序要记录前一个字符与当前字符
    可用 `Receive your eieio award` 这样的输入测试

    7. 编写一个程序，提示用户输入一周工作的小时数
    然后打印工资总额，税金和净收入，假设如下

    a. 基本工资为 `10.00` 美元/小时

    b. 超过 `40` 小时的部分按 `1.5` 倍计算

    c. 前 `300` 美元按 `15%` 计税，续 `150` 美元按 `20%` 计税
       余下部分按 `25%` 计税

    用 `#define` 定义符号常量，不必考虑现行税法

    8. 修改练习 7 的假设 a，让程序给出可选择的工资等级菜单，用 `switch` 选择

    ```text
    *****************************************************************
    Enter the number corresponding to the desired pay rate or action:
    1) $8.75/hr                     2) $9.33/hr
    3) $10.00/hr                    4) $11.20/hr
    5) quit
    *****************************************************************
    ```

    选择 `1` 至 `4` 时程序询问工作小时数
    程序循环运行，直到用户输入 `5`
    输入 `1` 至 `5` 以外的数字时提示重新输入，再显示菜单
    用 `#define` 定义各工资等级与税率

    9. 编写一个程序，只接受正整数输入，然后显示所有小于或等于该数的素数

    10. 1988 年美国联邦税收计划分为 4 个类别，每个类别有两个等级
    下列金额为应征税的收入

    - 单身： `17850` 美元按 `15%` 计，超出部分按 `28%` 计
    - 户主： `23900` 美元按 `15%` 计，超出部分按 `28%` 计
    - 已婚共有： `29750` 美元按 `15%` 计，超出部分按 `28%` 计
    - 已婚离异： `14875` 美元按 `15%` 计，超出部分按 `28%` 计

    例如，应税收入为 `20000` 美元的单身纳税人
    税额为 `0.15×17850+0.28×(20000-17850)`
    编写程序，让用户指定类别与应税收入，然后计算税额
    程序通过循环让用户可以多次输入

    11. ABC 邮购杂货店出售洋蓟 `2.05` 美元/磅，甜菜 `1.15` 美元/磅
    胡萝卜 `1.09` 美元/磅
    订单在加运费之前，满 `100` 美元打 `5%` 折扣
    不超过 `5` 磅的订单收 `6.5` 美元运费与包装费
    `5` 至 `20` 磅收 `14` 美元
    超过 `20` 磅在 `14` 美元基础上每续重 `1` 磅加 `0.5` 美元
    编写程序，在循环中用 `switch` 实现不同字母输入的不同响应
    输入 `a` 时询问洋蓟磅数，`b` 为甜菜，`c` 为胡萝卜，`q` 退出订购
    程序要累计各类商品的重量
    例如先输入 `4` 磅甜菜，再输入 `5` 磅甜菜，应报告甜菜共 `9` 磅
    随后计算货物总价，折扣，运费与包装费
    最后显示各项售价，订购重量，蔬菜费用，订单总费用
    折扣，运费与包装费以及费用总额
