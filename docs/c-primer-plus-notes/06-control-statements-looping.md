# 第6章 C控制语句：循环

## while 语句

!!! abstract "语法形式"

    ```c
    while (expression)
        statement
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int n = 1;
        while (n <= 3)          // 条件非零时执行循环体
        {
            printf("n = %d\n", n);
            n++;
        }
        printf("done\n");
        return 0;
    }
    ```

    输出：

    ```text
    n = 1
    n = 2
    n = 3
    done
    ```

!!! note "说明"

    - `expression` 求值非零时执行一次 `statement`，然后重新求值
    - `statement` 可以是分号结尾的简单语句，也可以是花括号复合语句
    - 每次重复执行称为一次迭代
    - 循环体内必须改变测试表达式的值，否则表达式始终为真，循环不终止
    - 任意表达式都可作测试条件，不必是关系表达式

!!! warning "常见错误"

    - 循环体内不更新测试的变量，形成无限循环
    - 缩进写了多行，却只用一条语句作循环体，其余语句只执行一次
    - 在测试条件后多写一个分号，循环体变成空语句

## C 风格读取循环

!!! abstract "语法形式"

    ```c
    while (scanf("%d", &num) == 1)
        statement
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int num, sum = 0;
        printf("enter integers, q to quit: ");
        while (scanf("%d", &num) == 1)
            sum += num;
        printf("sum = %d\n", sum);
        return 0;
    }
    ```

    输出：

    ```text
    enter integers, q to quit: 3 4 5 q
    sum = 12
    ```

!!! note "说明"

    - `scanf()` 返回成功读取的项数，读取失败返回 `0`
    - 转换前遇到文件结尾或硬件错误，返回 `EOF`，其值通常为 `-1`
    - 把函数调用直接写在测试条件中，每次迭代都读取新值并判断
    - 用户输入非数字字符时循环结束，非数字字符留在输入队列中
    - 先读值再判断的写法需要两次 `scanf()`，一次在循环前，一次在循环末

!!! warning "常见错误"

    - 把 `scanf()` 的返回值当作读到的数值使用
    - 循环体内忘记再次调用 `scanf()`，重复处理同一个值

## 循环体的边界与空语句

!!! abstract "语法形式"

    ```c
    while (n++ < 3)
        ;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int n = 0;
        while (n++ < 3)
            ;                   // 空语句, 循环体不做任何事
        printf("n = %d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    n = 4
    ```

!!! note "说明"

    - 循环体只有紧跟在测试条件后的第一条语句
    - 单独一个分号是一条语句，称为空语句，不执行任何操作
    - 所有工作在测试条件中完成时，可以有意使用空语句
    - 空语句单独占一行，让读代码的人看出它是有意写的

!!! warning "常见错误"

    - 写成 `while (n < 3) printf(...); n++;`，`n++` 不在循环内，条件不变
    - 测试条件后误加分号，循环空转，循环体只执行一次
    - 把空语句与测试条件写在同一行，误读为循环体

## 入口条件循环

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int index = 10;
        while (index < 5)
            printf("never\n");
        printf("index = %d\n", index);
        return 0;
    }
    ```

    输出：

    ```text
    index = 10
    ```

!!! note "说明"

    - `while` 与 `for` 都是入口条件循环
    - 每次迭代之前检查测试条件，条件一开始为假时循环体一次也不执行
    - 有条件指的是循环体的执行取决于测试表达式描述的条件

## 关系运算符

!!! abstract "语法形式"

    ```c
    a < b
    a <= b
    a == b
    a >= b
    a > b
    a != b
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int a = 3, b = 5;
        printf("%d %d %d\n", a < b, a == b, a != b);
        printf("%d %d\n", 'a' < 'b', 'z' <= 'a');
        return 0;
    }
    ```

    输出：

    ```text
    1 0 1
    1 0
    ```

    表6-1 关系运算符

    | 运算符 | 含义 |
    | --- | --- |
    | `<` | 小于 |
    | `<=` | 小于或等于 |
    | `==` | 等于 |
    | `>=` | 大于或等于 |
    | `>` | 大于 |
    | `!=` | 不等于 |

!!! note "说明"

    - 关系运算符比较左右两个值，构成关系表达式
    - 字符按机器字符码比较，通常为 ASCII
    - 字符串不能用关系运算符比较
    - 浮点数比较见下一张卡片，尽量只用 `<` 与 `>`

!!! warning "常见错误"

    - 把相等运算符 `==` 写成赋值运算符 `=`
    - 用 `==` 比较两个字符串，实际比较的是地址

## 关系表达式的真值

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int n = 3;
        while (n)
            printf("%d ", n--);
        printf("| %d\n", n);
        return 0;
    }
    ```

    输出：

    ```text
    3 2 1 | 0
    ```

!!! note "说明"

    - 关系为真时表达式的值为 `1`，为假时为 `0`
    - 任何非零值都视为真，只有 `0` 视为假
    - `while (goats)` 与 `while (goats != 0)` 等价，C 程序员常用前者
    - `while (1)` 的测试条件恒为真，需要内部语句结束循环

!!! warning "常见错误"

    - 认为真值只能是 `1`，把其他非零值当作假
    - 误用 `=` 使测试条件变成赋值表达式的值
      例如 `while (status = 1)` 的值恒为 `1`，循环永不退出

## 浮点数的相等比较

!!! abstract "语法形式"

    ```c
    while (fabs(x - target) > epsilon)
    ```

!!! example "示例"

    ```c
    #include <math.h>
    #include <stdio.h>
    int main(void)
    {
        double x = 0.1 + 0.2;
        printf("%d\n", x == 0.3);
        printf("%d\n", fabs(x - 0.3) < 1e-9);
        return 0;
    }
    ```

    输出：

    ```text
    0
    1
    ```

!!! note "说明"

    - 浮点数的舍入误差会使逻辑上相等的两个数不相等
    - `fabs()` 声明在 `math.h` 中，返回浮点值的绝对值
    - 比较两数之差是否小于给定容差，而不是直接比较相等
    - 用 gcc 链接时在命令行加 `-lm`

!!! warning "常见错误"

    - 用 `==` 判断两个浮点计算结果相等
    - 容差取得过小，小于该类型能分辨的精度

## 关系运算符的优先级

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int x = 5, y = 3, z;
        printf("%d\n", x > y + 2);
        z = x > y;
        printf("%d\n", z);
        printf("%d\n", (2 != 3) == 1);
        return 0;
    }
    ```

    输出：

    ```text
    0
    1
    1
    ```

    表6-2 运算符优先级 (从高到低)

    | 运算符 | 结合律 |
    | --- | --- |
    | `()` | 从左往右 |
    | `- + ++ -- sizeof` | 从右往左 |
    | `* / %` | 从左往右 |
    | `+ -` | 从左往右 |
    | `< <= > >=` | 从左往右 |
    | `== !=` | 从左往右 |
    | `=` | 从右往左 |

!!! note "说明"

    - 关系运算符的优先级低于算术运算符，高于赋值运算符
    - `x > y + 2` 与 `x > (y + 2)` 相同
    - `x = y > 2` 与 `x = (y > 2)` 相同，赋给 `x` 的是比较结果
    - `< <= > >=` 的优先级高于 `== !=`
    - 关系运算符从左往右结合，`ex != wye == zee` 即 `(ex != wye) == zee`
    - 把常量写在左侧可让编译器查出误写的 `=`，例如 `5 == canoes`

!!! warning "常见错误"

    - 以为 `x = y > 2` 会把 `y` 赋给 `x`
    - 依赖 `==` 与 `<` 的优先级而不加括号，读代码时难以判断

## _Bool 类型

!!! abstract "语法形式"

    ```c
    _Bool 变量名;
    bool 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdbool.h>
    #include <stdio.h>
    int main(void)
    {
        _Bool a = 5;
        bool b = false;
        printf("%d %d\n", a, b);
        printf("%d\n", 1 == true);
        return 0;
    }
    ```

    输出：

    ```text
    1 0
    1
    ```

!!! note "说明"

    - `_Bool` 是 C99 新增的布尔类型，只能储存 `1` 或 `0`
    - 赋入其他非零值时，变量被置为 `1`
    - 包含 `stdbool.h` 后，`bool` 是 `_Bool` 的别名
    - 该头文件把 `true` 与 `false` 定义为 `1` 与 `0` 的符号常量
    - 布尔变量名通常写成陈述句，例如 `input_is_good`
    - 系统不支持 `_Bool` 时，可以改用 `int`

!!! warning "常见错误"

    - 用 `printf("%d", b)` 以外的格式输出布尔值
    - 认为 `_Bool` 能储存 `2` 等非零值，实际只会得到 `1`

## 不确定循环与计数循环

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        const int NUMBER = 3;
        int count = 1;
        while (count <= NUMBER)
        {
            printf("loop %d\n", count);
            count++;
        }
        return 0;
    }
    ```

    输出：

    ```text
    loop 1
    loop 2
    loop 3
    ```

!!! note "说明"

    - 不确定循环： 循环次数事先未知，由测试条件决定何时结束
    - 计数循环： 循环次数在进入循环前已经确定
    - 计数循环涉及三个行为： 初始化计数器，计数器与限值比较，递增计数器
    - `for` 把这三个行为写在循环头的一行中，比 `while` 更不容易遗漏

!!! warning "常见错误"

    - 计数器在循环外初始化，忘记初始化
    - 递增语句写在循环末尾却被花括号排除在循环外

## for 语句

!!! abstract "语法形式"

    ```c
    for (initialize; test; update)
        statement
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int num;
        for (num = 1; num <= 3; num++)
            printf("%d %d\n", num, num * num * num);
        return 0;
    }
    ```

    输出：

    ```text
    1 1
    2 8
    3 27
    ```

!!! note "说明"

    - 三个表达式用两个分号隔开，都是完整表达式
    - `initialize` 在循环开始前只执行一次
    - `test` 在每次迭代之前求值，为假时结束循环
    - `update` 在每次迭代结束时求值
    - `for` 是入口条件循环，循环体可能一次也不执行
    - 循环结束后计数器的值通常比最后打印的值大 `1`

!!! warning "常见错误"

    - 三个表达式之间用逗号代替分号
    - 在 `for` 的圆括号后加分号，循环体变成空语句
    - 以为循环结束时计数器停在最后一个使用值上

## for 循环头的灵活性

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int secs;
        double debt;
        for (secs = 3; secs > 0; secs--)
            printf("%d ", secs);
        for (debt = 100.0; debt < 150.0; debt *= 1.1)
            printf("%.2f ", debt);
        printf("\n");
        return 0;
    }
    ```

    输出：

    ```text
    3 2 1 100.00 110.00 121.00 133.10 146.41
    ```

!!! note "说明"

    - 计数器可以递减，也可以每次加 `2`，加 `13` 等
    - 可以用字符计数，字符在内部按整数储存
    - 更新表达式可以乘一个固定因子，使计数几何增长
    - 三个表达式可以涉及不同的变量
    - 可以省略一个或多个表达式，但分号不能省
    - 省略第二个表达式视为真，`for (; ; )` 是无限循环
    - 第一个表达式可以是 `printf()` 等函数调用
    - 循环体可以改变循环头中表达式的值

!!! warning "常见错误"

    - 省略表达式时把分号一起省掉
    - 在循环体内把更新量改成 `0`，循环不终止

## 组合赋值运算符

!!! abstract "语法形式"

    ```c
    变量 op= 表达式
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int scores = 10;
        scores += 20;
        scores *= 2;
        printf("%d\n", scores);
        return 0;
    }
    ```

    输出：

    ```text
    60
    ```

    表6-3 组合赋值运算符

    | 运算符 | 等价写法 |
    | --- | --- |
    | `+=` | `x = x + y` |
    | `-=` | `x = x - y` |
    | `*=` | `x = x * y` |
    | `/=` | `x = x / y` |
    | `%=` | `x = x % y` |

!!! note "说明"

    - 左侧是变量名，右侧是表达式，新值由右侧的值调整得到
    - `x *= 3 * y + 12` 与 `x = x * (3 * y + 12)` 相同
    - 组合赋值运算符与 `=` 的优先级相同，低于算术运算符
    - 组合形式比一般形式生成的机器代码更高效，写 `for` 循环头时也更紧凑

!!! warning "常见错误"

    - 把 `x *= 3 + 12` 读成 `(x * 3) + 12`
    - 在运算符中间加空格，写成 `x + = 1`

## 逗号运算符

!!! abstract "语法形式"

    ```c
    表达式1, 表达式2
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int x, y = 3, z;
        x = (y = 3, (z = ++y + 2) + 5);  // 整个表达式的值取右侧
        printf("%d %d %d\n", x, y, z);
        return 0;
    }
    ```

    输出：

    ```text
    11 4 6
    ```

!!! note "说明"

    - 逗号运算符把两个表达式连接成一个表达式
    - 逗号是序列点，左侧子表达式的副作用在右侧求值之前完成
    - 整个逗号表达式的值是最右侧子表达式的值
    - 在 `for` 循环头中可以初始化或更新多个变量
    - 逗号也用作分隔符，例如声明多个变量，分隔函数实参
      此时的逗号不是运算符
    - `houseprice = 249,500;` 是逗号表达式
      先把 `249` 赋给变量，整个表达式的值为 `500`

!!! warning "常见错误"

    - 想写 `249500` 却写成 `249,500`，赋值仍执行但值不对
    - 在 `for` 的初始化部分用分号分隔多个初始化，应为逗号
    - 把声明中的逗号当作逗号运算符

## do while 语句

!!! abstract "语法形式"

    ```c
    do
        statement
    while (expression);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int code = 0;
        do
        {
            printf("code: ");
            scanf("%d", &code);
        } while (code != 13);
        printf("done\n");
        return 0;
    }
    ```

    输出：

    ```text
    code: 12
    code: 14
    code: 13
    done
    ```

!!! note "说明"

    - `do while` 是出口条件循环，执行完循环体后才检查测试条件
    - 循环体至少执行一次
    - 以分号结尾，分号属于语法的一部分
    - 适用于至少需要迭代一次的任务，例如先读取输入再判断
    - 需要先询问再决定是否执行其余工作时，不用这种结构，因为其余工作会先执行一次

!!! warning "常见错误"

    - 漏写 `while (expression)` 后的分号
    - 把需要先判断的循环写成 `do while`，导致多执行一次

## 三种循环的选择

!!! abstract "语法形式"

    表6-4 三种循环的比较

    | 循环 | 检查位置 | 最少执行次数 | 典型用途 |
    | --- | --- | --- | --- |
    | `while` | 循环体之前 | 0 | 次数未知，由条件决定 |
    | `for` | 循环体之前 | 0 | 计数循环，有初始化与更新 |
    | `do while` | 循环体之后 | 1 | 至少执行一次，如读取输入 |

!!! note "说明"

    - 先决定用入口条件循环还是出口条件循环，多数场合用入口条件循环
    - 入口条件循环把测试放在开头，可读性更高，条件一开始不满足时整段跳过
    - `for (; test; )` 与 `while (test)` 等价
    - 测试条件不含初始化与更新时，用 `while` 更自然，例如 `while (scanf(...) == 1)`
    - 涉及索引计数时用 `for`，三个行为集中在循环头

## 嵌套循环

!!! abstract "语法形式"

    ```c
    for (外层初始化; 外层条件; 外层更新)
    {
        for (内层初始化; 内层条件; 内层更新)
            内层语句;
        外层语句;
    }
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int row;
        char ch;
        for (row = 0; row < 3; row++)
        {
            for (ch = 'A' + row; ch <= 'D'; ch++)
                printf("%c", ch);
            printf("\n");       // 内层循环结束后换行
        }
        return 0;
    }
    ```

    输出：

    ```text
    ABCD
    BCD
    CD
    ```

!!! note "说明"

    - 外层循环每迭代一次，内层循环完整执行一遍
    - 常用外层循环处理行，内层循环处理列
    - 内层循环的初值可以依赖外层循环的计数器，每行内容随之不同
    - 内层循环结束后，外层循环继续执行换行等收尾语句

!!! warning "常见错误"

    - 内层计数器的初值不随外层循环重置，每行内容相同
    - 把换行语句放进内层循环，每打印一个字符就换行

## 数组简介

!!! abstract "语法形式"

    ```c
    类型 数组名[元素个数];
    数组名[下标]
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int arr[5] = {10, 20, 30, 40, 50};
        printf("%d %d\n", arr[0], arr[4]);
        printf("%zu\n", sizeof arr / sizeof arr[0]);
        return 0;
    }
    ```

    输出：

    ```text
    10 50
    5
    ```

!!! note "说明"

    - 数组按顺序储存一系列类型相同的值，整个数组有一个名称
    - 下标从 `0` 开始，最后一个元素的下标是元素个数减 `1`
    - 数组元素可以像同类型变量一样赋值与读入
    - 下标必须是整数，也称索引或偏移量
    - 元素依次存放在内存中相邻的位置
    - `char` 数组末尾存放空字符 `\0` 时，数组内容构成字符串
    - 编译器不检查下标是否越界，越界写入会改写相邻数据

    ![图6.6 字符数组和字符串](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00041.jpg)

    ![图6.7 内存中的 char 与 int 数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00042.jpg)

!!! warning "常见错误"

    - 用 `arr[5]` 访问 5 个元素的最后一个元素，越界
    - 用 1 到元素个数作循环下标

## 在 for 循环中使用数组

!!! example "示例"

    ```c
    #include <stdio.h>
    #define SIZE 5
    int main(void)
    {
        int score[SIZE] = {99, 95, 109, 105, 100};
        int index, sum = 0;
        for (index = 0; index < SIZE; index++)
            sum += score[index];
        printf("sum = %d, average = %.2f\n",
               sum, (float) sum / SIZE);
        return 0;
    }
    ```

    输出：

    ```text
    sum = 508, average = 101.60
    ```

!!! note "说明"

    - 处理大小为 `SIZE` 的数组
      循环写作 `for (index = 0; index < SIZE; index++)`
    - 循环边界用明示常量，修改数组大小时只改 `#define` 一处
    - `index < SIZE` 使最后一个下标为 `SIZE - 1`
    - 读入元素写作 `scanf("%d", &score[index])`，与普通变量一样取地址
    - 把读入，统计，输出分成独立的循环，每个循环只完成一项任务

!!! warning "常见错误"

    - 循环条件写成 `index <= SIZE`，多访问一个越界元素
    - 对数组元素漏写 `&`

## 带返回值的函数作循环条件

!!! abstract "语法形式"

    ```c
    返回类型 函数名(参数列表);
    return 表达式;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    double power(double n, int p);
    int main(void)
    {
        int exp = 1;
        double v;
        while ((v = power(2.0, exp)) < 100)
        {
            printf("%.0f\n", v);
            exp++;
        }
        return 0;
    }
    double power(double n, int p)
    {
        double pow = 1;
        int i;
        for (i = 1; i <= p; i++)
            pow *= n;
        return pow;
    }
    ```

    输出：

    ```text
    2
    4
    8
    16
    32
    64
    ```

!!! note "说明"

    - 函数名前的类型是返回类型，`return` 后面的值交给主调函数
    - 函数调用可以写在测试条件中，返回的值直接参与比较
    - 返回值先赋给 `v` 再与 `100` 比较，循环体内可以重复使用 `v`
    - `return` 可以返回变量，也可以返回表达式的值
    - 返回值可以赋给变量，参与表达式，作实参，或者忽略
    - 函数原型末尾有分号，函数定义末尾没有
    - 使用函数前需要原型声明，编译器据此知道返回值的字节数与解释方式
    - 把 `scanf()` 的返回值与 `2` 比较，可以控制读取两个值的循环
    - `stdio.h` 中已包含 `scanf()` 的原型，因此不必另行声明

!!! warning "常见错误"

    - 函数定义末尾加分号
    - 在 `main()` 之后定义函数却没有前置声明
    - 返回类型与原型不一致，调用处按错误类型解释返回值

## 复习题

（1）写出执行完下列各行后 `quack` 的值
后 5 行使用前一行生成的 `quack` 的值
```c
int quack = 2;
quack += 5;
quack *= 10;
quack -= 6;
quack /= 8;
quack %= 3;
```

??? note "答案"

    `2`，`7`，`70`，`64`，`8`，`2`

（2）假设 `value` 是 `int` 类型，下面循环的输出是什么
```c
for (value = 36; value > 0; value /= 2)
    printf("%3d", value);
```
如果 `value` 是 `double` 类型，会出现什么问题

??? note "答案"

    ```text
    36 18 9 4 2 1
    ```

    `double` 类型的 `value` 小于 `1` 时测试条件仍为真
    循环直到下溢为 `0` 才结束，另外 `%3d` 也不适用于 `double`

（3）用代码表示以下测试条件
a. `x` 大于 `5`
b. `scanf()` 读取一个名为 `x` 的 `double` 类型值且失败
c. `x` 的值等于 `5`

??? note "答案"

    a. `x > 5`

    b. `scanf("%lf", &x) != 1`

    c. `x == 5`

（4）用代码表示以下测试条件
a. `scanf()` 成功读入一个整数
b. `x` 不等于 `5`
c. `x` 大于或等于 `20`

??? note "答案"

    a. `scanf("%d", &x) == 1`

    b. `x != 5`

    c. `x >= 20`

（5）下面的程序有点问题，请找出问题所在
```c
#include <stdio.h>
int main(void)
{                                       /* 第3行 */
    int i, j, list(10);                 /* 第4行 */
    for (i = 1, i <= 10, i++)           /* 第6行 */
    {                                   /* 第7行 */
        list[i] = 2*i + 3;              /* 第8行 */
        for (j = 1, j > = i, j++)       /* 第9行 */
             printf(" %d", list[j]);    /* 第10行 */
        printf("\n");                   /* 第11行 */
}                                       /* 第12行 */
```

??? note "答案"

    第 `4` 行应为 `int i, j, list[10];`

    第 `6` 行的逗号改为分号，`i` 的范围应为 `0` 到 `9`，不是 `1` 到 `10`

    第 `9` 行的逗号改为分号，`>=` 改为 `<=`，否则 `i` 等于 `1` 时成为无限循环

    第 `10` 行与第 `11` 行之间少一个右花括号
    它与第 `7` 行的左花括号配对，构成循环块

    最后一个右花括号前少一行 `return 0;`

    ```c
    #include <stdio.h>
    int main(void)
    {
        int i, j, list[10];

        for (i = 0; i < 10; i++)
        {
            list[i] = 2*i + 3;
            for (j = 1; j <= i; j++)
                printf(" %d", list[j]);
            printf("\n");
        }
        return 0;
    }
    ```

    [教材给出的正确版本仍写作 `for (i = 0, i < 10, i++)`
    与同一答案中逗号改为分号的说法矛盾，本笔记按后者改写]

（6）编写一个程序打印下面的图案，要求使用嵌套循环
```
$$$$$$$$
$$$$$$$$
$$$$$$$$
$$$$$$$$
```

??? note "答案"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int col, row;

        for (row = 1; row <= 4; row++)
        {
            for (col = 1; col <= 8; col++)
                printf("$");
            printf("\n");
        }
        return 0;
    }
    ```

（7）下面的程序各打印什么内容
a.
```c
#include <stdio.h>
int main(void)
{
    int i = 0;
    while (++i < 4)
        printf("Hi! ");
    do
        printf("Bye! ");
    while (i++ < 8);
    return 0;
}
```
b.
```c
#include <stdio.h>
int main(void)
{
    int i;
    char ch;
    for (i = 0, ch = 'A'; i < 4; i++, ch += 2 * i)
           printf("%c", ch);
    return 0;
}
```

??? note "答案"

    a. `Hi! Hi! Hi! Bye! Bye! Bye! Bye! Bye!`

    b. `ACGM`

（8）假设用户输入的是 `Go west, young man!`
下面各程序的输出是什么
(在 ASCII 码中，`!` 紧跟在空格字符后面)
a.
```c
#include <stdio.h>
int main(void)
{
    char ch;
    scanf("%c", &ch);
    while (ch != 'g')
    {
        printf("%c", ch);
        scanf("%c", &ch);
    }
    return 0;
}
```
b.
```c
#include <stdio.h>
int main(void)
{
    char ch;
    scanf("%c", &ch);
    while (ch != 'g')
    {
        printf("%c", ++ch);
        scanf("%c", &ch);
    }
    return 0;
}
```
c.
```c
#include <stdio.h>
int main(void)
{
    char ch;
    do {
        scanf("%c", &ch);
        printf("%c", ch);
    } while (ch != 'g');
    return 0;
}
```
d.
```c
#include <stdio.h>
int main(void)
{
    char ch;
    scanf("%c", &ch);
    for (ch = '$'; ch != 'g'; scanf("%c", &ch))
        printf("%c", ch);
    return 0;
}
```

??? note "答案"

    a. `Go west, youn`

    b. `Hp!xftu-!zpvo`

    c. `Go west, young`

    d. `$o west, youn`

（9）下面的程序打印什么内容
```c
#include <stdio.h>
int main(void)
{
    int n, m;
    n = 30;
    while (++n <= 33)
        printf("%d|", n);
    n = 30;
    do
        printf("%d|", n);
    while (++n <= 33);
    printf("\n***\n");
    for (n = 1; n*n < 200; n += 4)
        printf("%d\n", n);
    printf("\n***\n");
    for (n = 2, m = 6; n < m; n *= 2, m += 2)
        printf("%d %d\n", n, m);
    printf("\n***\n");
    for (n = 5; n > 0; n--)
    {
        for (m = 0; m <= n; m++)
             printf("=");
        printf("\n");
    }
    return 0;
}
```

??? note "答案"

    ```text
    31|32|33|30|31|32|33|
    ***
    1
    5
    9
    13

    ***
    2 6
    4 8
    8 10

    ***
    ======
    =====
    ====
    ===
    ==
    ```

（10）考虑下面的声明
```c
double mint[10];
```
a. 数组名是什么
b. 该数组有多少个元素
c. 每个元素可以储存什么类型的值
d. 下面的哪一个 `scanf()` 的用法正确
i. `scanf("%lf", mint[2])`
ii. `scanf("%lf", &mint[2])`
iii. `scanf("%lf", &mint)`

??? note "答案"

    a. `mint`

    b. `10` 个元素

    c. `double` 类型的值

    d. 第 ii 行正确，`mint[2]` 是 `double` 类型的值
    `&mint[2]` 是它在内存中的地址

（11）Noah 先生喜欢以 2 计数，编写了下面的程序
创建一个储存 2、4、6、8 等数字的数组
这个程序是否有错误之处，如果有，请指出
```c
#include <stdio.h>
#define SIZE 8
int main(void)
{
    int by_twos[SIZE];
    int index;
    for (index = 1; index <= SIZE; index++)
         by_twos[index] = 2 * index;
    for (index = 1; index <= SIZE; index++)
         printf("%d ", by_twos);
    printf("\n");
    return 0;
}
```

??? note "答案"

    第 `1` 个元素的下标是 `0`
    循环范围应为 `0` 到 `SIZE - 1`，不是 `1` 到 `SIZE`

    只改范围会使第 `1` 个元素被赋为 `0`，赋值语句应改为

    ```c
    for (index = 0; index < SIZE; index++)
        by_twos[index] = 2 * (index + 1);
    ```

    打印循环同样要把范围改为 `0` 到 `SIZE - 1`，并在数组名后写下标

    ```c
    for (index = 0; index < SIZE; index++)
        printf("%d ", by_twos[index]);
    ```

（12）假设要编写一个返回 `long` 类型值的函数，函数定义中应包含什么

??? note "答案"

    返回类型写作 `long`，并包含返回 `long` 类型值的 `return` 语句

（13）定义一个函数，接受一个 `int` 类型的参数
并以 `long` 类型返回参数的平方值

??? note "答案"

    先把参数强制转换为 `long` 再相乘
    否则在 `int` 为 `16` 位的系统中，乘积会先被截断为 `int`

    ```c
    long square(int num)
    {
        return ((long) num) * num;
    }
    ```

（14）下面的程序打印什么内容
```c
#include <stdio.h>
int main(void)
{
    int k;
    for (k = 1, printf("%d: Hi!\n", k);
         printf("k = %d\n", k), k*k < 26;
         k += 2, printf("Now k is %d\n", k))
             printf("k is %d in the loop\n", k);
    return 0;
}
```

??? note "答案"

    ```text
    1: Hi!
    k = 1
    k is 1 in the loop
    Now k is 3
    k = 3
    k is 3 in the loop
    Now k is 5
    k = 5
    k is 5 in the loop
    Now k is 7
    k = 7
    ```

## 编程练习

!!! question "编程练习"

    1. 编写一个程序，创建一个包含 26 个元素的数组
    并在其中储存 26 个小写字母，然后打印数组的所有内容

    2. 使用嵌套循环，按下面的格式打印字符

    ```text
    $
    $$
    $$$
    $$$$
    $$$$$
    ```

    3. 使用嵌套循环，按下面的格式打印字母

    ```text
    F
    FE
    FED
    FEDC
    FEDCB
    FEDCBA
    ```

    注意： 如果系统不使用 ASCII 或其他以数字顺序编码的代码
    可以把字符数组初始化为字母表中的字母

    ```c
    char lets[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    ```

    然后用数组下标选择单独的字母，例如 `lets[0]` 是 `'A'`

    4. 使用嵌套循环，按下面的格式打印字母

    ```text
    A
    BC
    DEF
    GHIJ
    KLMNO
    PQRSTU
    ```

    如果系统不使用以数字顺序编码的代码，参照练习 3 的方案解决

    5. 编写一个程序，提示用户输入大写字母
    使用嵌套循环以下面金字塔型的格式打印字母

    ```text
        A
       ABA
      ABCBA
     ABCDCBA
    ABCDEDCBA
    ```

    根据用户输入的字母决定打印的图形，上面的图形是输入 `E` 后的结果
    提示： 外层循环处理行，每行用 3 个内层循环
    分别处理空格，以升序打印字母，以降序打印字母
    如果系统不使用 ASCII 或其他以数字顺序编码的代码，参照练习 3 的方案

    6. 编写一个程序打印一个表格
    每一行打印一个整数，该数的平方，该数的立方
    要求用户输入表格的上下限，使用一个 `for` 循环

    7. 编写一个程序把一个单词读入一个字符数组中
    然后倒序打印这个单词
    提示： `strlen()` 函数可用于计算数组最后一个字符的下标

    8. 编写一个程序，要求用户输入两个浮点数
    并打印两数之差除以两数乘积的结果
    在用户输入非数字之前，程序应循环处理用户输入的每对值

    9. 修改练习 8，使用一个函数返回计算的结果

    10. 编写一个程序，要求用户输入一个上限整数和一个下限整数
    计算从下限到上限范围内所有整数的平方和，并显示计算结果
    然后程序继续提示用户输入上下限，直到上限整数等于或小于下限整数为止
    程序的运行示例如下

    ```text
    Enter lower and upper integer limits: 5 9

    The sums of the squares from 25 to 81 is 255
    Enter next set of limits: 3 25

    The sums of the squares from 9 to 625 is 5520
    Enter next set of limits: 5 5

    Done
    ```

    [教材原文写作从上限到下限，与运行示例中先输入下限的写法矛盾
    本笔记按示例写为从下限到上限]

    11. 编写一个程序，在数组中读入 8 个整数
    然后按倒序打印这 8 个整数

    12. 考虑下面两个无限序列

    ```text
    1.0 + 1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ...
    1.0 - 1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ...
    ```

    编写一个程序计算这两个无限序列的总和，直到到达某次数
    提示： 奇数个 `-1` 相乘得 `-1`，偶数个 `-1` 相乘得 `1`
    让用户交互地输入指定的次数，当用户输入 `0` 或负值时结束输入
    查看运行 100 项，1000 项，10000 项后的总和，是否发现每个序列都收敛于某值

    13. 编写一个程序，创建一个包含 8 个元素的 `int` 类型数组
    分别把数组元素设置为 2 的前 8 次幂
    使用 `for` 循环设置数组元素的值，使用 `do while` 循环显示数组元素的值

    14. 编写一个程序，创建两个包含 8 个元素的 `double` 类型数组
    使用循环提示用户为第一个数组输入 8 个值
    第二个数组元素的值设置为第一个数组对应元素的累积之和
    例如，第二个数组的第 4 个元素是第一个数组前 4 个元素之和
    第二个数组的第 5 个元素是第一个数组前 5 个元素之和
    利用第二个数组的第 5 个元素等于第 4 个元素与第一个数组第 5 个元素之和
    只用一个循环就能完成，不需要嵌套循环
    最后用循环显示两个数组的内容，第一个数组显示成一行
    第二个数组显示在第一个数组的下一行，每个元素与第一个数组各元素对齐

    15. 编写一个程序，读取一行输入，然后把输入的内容倒序打印出来
    可以把输入储存在 `char` 类型的数组中，假设每行字符不超过 255
    `%c` 转换说明使 `scanf()` 一次只能读取一个字符
    用户按下 Enter 键时 `scanf()` 会生成一个换行字符 `\n`

    16. Daphne 以 10% 的单利息投资了 100 美元
    即每年获利相当于原始投资的 10%
    Deirdre 以 5% 的复合利息投资了 100 美元
    即利息是当前余额的 5%，包含之前的利息
    编写一个程序，计算多少年后 Deirdre 的投资额会超过 Daphne
    并显示那时两人的投资额

    17. Chuckie Lucky 赢得了 100 万美元 (税后)
    他把奖金存入年利率 8% 的账户
    在每年的最后一天，Chuckie 取出 10 万美元
    编写一个程序，计算多少年后 Chuckie 会取完账户的钱

    18. Rabnud 博士加入了一个社交圈，起初他有 5 个朋友
    他注意到朋友数量以下面的方式增长
    第 1 周少了 1 个朋友，剩下的朋友数量翻倍
    第 2 周少了 2 个朋友，剩下的朋友数量翻倍
    一般而言，第 N 周少了 N 个朋友，剩下的朋友数量翻倍
    编写一个程序，计算并显示 Rabnud 博士每周的朋友数量
    程序一直运行，直到超过邓巴数
    邓巴数是粗略估算一个人在社交圈中有稳定关系的成员的最大值
    该值大约是 150
