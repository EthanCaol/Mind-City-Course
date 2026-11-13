# 第14章 结构和其他数据形式

## 结构声明

!!! abstract "语法形式"

    ```c
    struct 标记 {
        类型 成员名;
        ...
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct point {
        int x;
        int y;
    };                    /* 分号不能省略 */

    int main(void)
    {
        printf("%zu\n", sizeof(struct point));
        return 0;
    }
    ```

    输出：

    ```text
    8
    ```

!!! note "说明"

    - `struct` 后跟可选的标记，花括号内是成员列表
    - 每个成员用一条完整的声明语句描述
    - 声明只描述布局，不为数据分配空间
    - 成员可以是任意类型，也可以是另一个结构
    - 声明放在函数内时，标记只在该函数内可见
    - 声明放在所有函数外时，其后的函数都可以使用该标记

!!! warning "常见错误"

    - 把关键字写成 `structure`
    - 漏掉成员声明末尾的分号
    - 漏掉右花括号后的分号
    - 以为结构声明已经创建了变量

## 声明结构变量

!!! abstract "语法形式"

    ```c
    struct 标记 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        char author[31];
        float value;
    };

    int main(void)
    {
        struct book library;    /* 分配一块结构大小的空间 */
        library.value = 1.95f;
        printf("%.2f %zu\n", library.value, sizeof library);
        return 0;
    }
    ```

    输出：

    ```text
    1.95 76
    ```

!!! note "说明"

    - 编译器按结构布局为变量分配空间
    - 各成员按声明顺序排列，名称统一绑定到变量名
    - 结构大小可能因对齐大于各成员大小之和
    - 结构变量名不是地址，取地址要写 `&library`
    - `struct book` 在声明中的作用相当于 `int` 或 `float`
    - 可以同时声明多个变量与指针： `struct book a, b, *p;`

    ![图14.1 一个结构的内存分配](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00071.jpg)

!!! warning "常见错误"

    - 用 `book library;` 声明，漏掉 `struct`
    - 把结构变量当作指针直接传给函数

## 声明与定义合并

!!! abstract "语法形式"

    ```c
    struct 标记 {
        ...
    } 变量名;

    struct {
        ...
    } 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct point {
        int x;
        int y;
    } origin = {0, 0};      /* 声明布局并定义变量 */

    struct {
        int x;
        int y;
    } temp;                 /* 无标记, 只能使用这一次 */

    int main(void)
    {
        temp.x = 3;
        printf("%d %d\n", origin.x, temp.x);
        return 0;
    }
    ```

    输出：

    ```text
    0 3
    ```

!!! note "说明"

    - 结构声明与变量定义可以合并为一个步骤
    - 合并后可以不写标记
    - 无标记的结构无法在别处再用 `struct` 加标记引用
    - 需要多次使用时，应保留标记或使用 `typedef`

!!! warning "常见错误"

    - 声明无标记结构后，再写 `struct temp t;`
    - 把合并声明当成类型定义，直接写 `point p;`

## 初始化结构变量

!!! abstract "语法形式"

    ```c
    struct 标记 变量名 = {值1, 值2, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        char author[31];
        float value;
    };

    int main(void)
    {
        struct book library = {
            "The Pious Pirate",
            "Renee Vivotte",
            1.95
        };
        printf("%s, %.2f\n", library.title, library.value);
        return 0;
    }
    ```

    输出：

    ```text
    The Pious Pirate, 1.95
    ```

!!! note "说明"

    - 初始化项按成员在声明中的顺序对应
    - 每个初始化项独占一行只为便于阅读
    - 项数少于成员数时，其余成员置 `0`
    - 自动存储期的结构可以用非常量表达式初始化
    - 静态存储期的结构只能用常量表达式初始化
    - 成员是字符数组时，用字符串字面量初始化

!!! warning "常见错误"

    - 先声明变量，再用花括号整体赋值
    - 初始化项顺序与成员顺序不一致
    - 对静态结构使用运行时变量初始化

## 访问结构成员

!!! abstract "语法形式"

    ```c
    变量名.成员名
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        float value;
    };

    int main(void)
    {
        struct book library = {"C Primer Plus", 59.99};
        library.value = 49.99;      /* 修改成员 */
        printf("%s %.2f\n", library.title, library.value);
        return 0;
    }
    ```

    输出：

    ```text
    C Primer Plus 49.99
    ```

!!! note "说明"

    - `.` 左侧是结构变量，右侧是成员名
    - `library.value` 的类型就是成员的类型
    - 该表达式可以像同类型普通变量一样使用
    - 取成员地址写 `&library.value`
    - `.` 的优先级高于 `&` 和 `*`
    - 成员是数组时，数组名可直接作字符串参数

!!! warning "常见错误"

    - `scanf("%f", library.value)` 漏掉 `&`
    - 用 `library[0]` 这样的下标访问成员
    - 把 `.` 当作运行时下标，以为成员名可以拼接

## 指定初始化器

!!! abstract "语法形式"

    ```c
    struct 标记 变量名 = {.成员名 = 值, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        char author[31];
        float value;
    };

    int main(void)
    {
        struct book a = {.value = 10.99};
        struct book b = {.value = 18.90,
                         .author = "Philionna Pestle",
                         0.25};
        printf("%.2f %s %.2f\n", a.value, b.author, b.value);
        return 0;
    }
    ```

    输出：

    ```text
    10.99 Philionna Pestle 0.25
    ```

!!! note "说明"

    - 用 `.成员名 = 值` 指定初始化目标，顺序任意
    - 未指定的成员置 `0`
    - 指定项之后的普通项按成员顺序继续赋值
    - 同一成员被多次赋值时，最后一次生效
    - 上例的 `0.25` 跟在 `.author` 之后，赋给 `value`
    - 数组的指定初始化器写成 `[下标] = 值`

!!! warning "常见错误"

    - 以为指定初始化器可以只写值不写成员名
    - 忽略后面普通初始化的落点，造成成员被覆盖

## 声明结构数组

!!! abstract "语法形式"

    ```c
    struct 标记 数组名[元素个数];
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    #define MAXBKS 100

    struct book {
        char title[41];
        float value;
    };

    int main(void)
    {
        struct book library[MAXBKS] = {
            {"C Primer Plus", 59.99},
            {"The C Programming Language", 45.00}
        };
        printf("%s %.2f\n", library[1].title, library[1].value);
        return 0;
    }
    ```

    输出：

    ```text
    The C Programming Language 45.00
    ```

!!! note "说明"

    - 数组的每个元素都是一个结构变量
    - 数组名是数组的地址，不是结构名
    - 未显式初始化的元素按存储类别规则处理
    - 大型结构数组放在栈上可能超出栈的容量
    - 可以改为静态数组，外部数组或减小数组长度

    ![图14.2 一个结构数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00072.jpg)

!!! warning "常见错误"

    - 写成 `library.value[2]`，下标放错位置
    - 以为数组名可以当结构名使用
    - 在栈上声明过大的结构数组导致栈溢出

## 访问结构数组的成员

!!! abstract "语法形式"

    ```c
    数组名[下标].成员名
    数组名[下标].数组成员[下标]
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        float value;
    };

    int main(void)
    {
        struct book library[3] = {
            {"Alpha", 1.0}, {"Bravo", 2.0}, {"Charlie", 3.0}
        };
        printf("%c %c\n",
               library[2].title[4], library[1].title[0]);
        return 0;
    }
    ```

    输出：

    ```text
    l B
    ```

!!! note "说明"

    - 左侧下标选择数组元素，右侧下标选择成员内的字符
    - `library[2]` 是结构变量，可以再取成员
    - `library[2].title` 是字符数组
    - `library[2].title[4]` 是该数组中的一个字符
    - 一层一层由外向内读表达式

!!! warning "常见错误"

    - `library.title[2]` 把数组下标用到整个数组上
    - `library[2].title[4]` 写成 `library[2].title.[4]`
    - 把 `library[2]` 当作成员而不是结构

## 嵌套结构

!!! abstract "语法形式"

    ```c
    struct 外层 {
        struct 内层 成员名;
        ...
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    #define LEN 20

    struct names {
        char first[LEN];
        char last[LEN];
    };

    struct guy {
        struct names handle;    /* 嵌套结构成员 */
        char job[LEN];
        float income;
    };

    int main(void)
    {
        struct guy fellow = {
            {"Ewen", "Villard"},
            "personality coach",
            68112.00
        };
        printf("%s %s %s\n", fellow.handle.first,
               fellow.handle.last, fellow.job);
        return 0;
    }
    ```

    输出：

    ```text
    Ewen Villard personality coach
    ```

!!! note "说明"

    - 先声明内层结构，再声明外层结构
    - 外层结构中的成员声明与普通变量声明写法相同
    - 访问内层成员要连续使用两次点运算符
    - `fellow.handle` 本身是一个结构变量
    - `(fellow.handle).first` 与 `fellow.handle.first` 相同

!!! warning "常见错误"

    - 写 `fellow.first`，漏掉中间的结构成员名
    - 在未声明 `struct names` 时使用它

## 声明结构指针

!!! abstract "语法形式"

    ```c
    struct 标记 *指针名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct guy {
        int income;
    };

    int main(void)
    {
        struct guy barney = {100};
        struct guy * him = &barney;    /* 指向已有结构 */
        him->income += 50;
        printf("%d\n", barney.income);
        return 0;
    }
    ```

    输出：

    ```text
    150
    ```

!!! note "说明"

    - 指针声明只分配指针本身的空间，不创建结构
    - 结构变量名不是地址，赋值时要写 `&barney`
    - 指针加 `1` 跨过一个完整结构
    - 结构大小可能因对齐大于成员大小之和
    - 同一指针可以改指向另一个同类型结构

!!! warning "常见错误"

    - 写 `him = barney`，漏掉 `&`
    - 以为声明指针就创建了可用的结构
    - 用未初始化的指针访问成员

## 用指针访问成员

!!! abstract "语法形式"

    ```c
    指针名->成员名
    (*指针名).成员名
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct guy {
        int income;
    };

    int main(void)
    {
        struct guy barney = {100};
        struct guy * him = &barney;
        printf("%d %d\n", him->income, (*him).income);
        return 0;
    }
    ```

    输出：

    ```text
    100 100
    ```

!!! note "说明"

    - `->` 由减号与大于号组成，中间没有空格
    - `him->income` 等价于 `(*him).income`
    - 圆括号不能省略，`.` 的优先级高于 `*`
    - `*him` 是结构变量，可以继续用 `.` 取成员
    - `him.income` 不合法，因为 `him` 不是结构

!!! warning "常见错误"

    - 写 `*him.income`，实际被解析为 `*(him.income)`
    - 写 `him.income`
    - `->` 写成 `>-` 或中间加空格

## 传递结构成员

!!! abstract "语法形式"

    ```c
    函数名(结构变量.成员名)
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct funds {
        double bankfund;
        double savefund;
    };

    double sum(double x, double y)
    {
        return x + y;
    }

    int main(void)
    {
        struct funds stan = {4032.27, 8543.94};
        printf("%.2f\n", sum(stan.bankfund, stan.savefund));
        return 0;
    }
    ```

    输出：

    ```text
    12576.21
    ```

!!! note "说明"

    - 成员类型是单值时可作为普通实参传递
    - 函数不知道也不关心实参来自结构
    - 成员类型必须与形参类型匹配
    - 需要在函数内修改原成员时，传递成员地址
    - 只使用少数成员时，只传这些成员最直接

!!! warning "常见错误"

    - 把整个结构传给只接受 `double` 的函数
    - 以为传递成员会连带传递其他成员

## 传递结构地址

!!! abstract "语法形式"

    ```c
    返回类型 函数名(const struct 标记 *形参);
    函数名(&结构变量);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct funds {
        double bankfund;
        double savefund;
    };

    double sum(const struct funds * money)
    {
        return money->bankfund + money->savefund;
    }

    int main(void)
    {
        struct funds stan = {4032.27, 8543.94};
        printf("%.2f\n", sum(&stan));
        return 0;
    }
    ```

    输出：

    ```text
    12576.21
    ```

!!! note "说明"

    - 实参写 `&stan`，形参声明为指向结构的指针
    - 函数内用 `->` 访问成员
    - `const` 限定符阻止函数修改原结构
    - 只传递一个地址，开销与结构大小无关
    - 传结构数组时可直接用数组名代替首元素地址

!!! warning "常见错误"

    - 传 `stan` 而不是 `&stan`
    - 形参写成结构变量，却在函数内用 `->`
    - 漏写 `const` 后意外修改原数据

## 传递结构本身

!!! abstract "语法形式"

    ```c
    返回类型 函数名(struct 标记 形参);
    函数名(结构变量);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct funds {
        double bankfund;
        double savefund;
    };

    double sum(struct funds moolah)
    {
        moolah.bankfund = 0;    /* 只修改副本 */
        return moolah.savefund;
    }

    int main(void)
    {
        struct funds stan = {4032.27, 8543.94};
        printf("%.2f %.2f\n", sum(stan), stan.bankfund);
        return 0;
    }
    ```

    输出：

    ```text
    8543.94 4032.27
    ```

!!! note "说明"

    - 按值传递，形参是原结构的副本
    - 函数内修改形参不影响原结构
    - 形参是结构变量，用 `.` 访问成员
    - 大型结构按值传递占用时间和空间
    - 有指针成员时只复制地址，不复制指向的数据
    - 小型结构按值传递较常用，可保护原数据

!!! warning "常见错误"

    - 以为在函数内修改形参会改到原结构
    - 对大型结构按值传递，造成不必要的复制

## 结构赋值与比较

!!! abstract "语法形式"

    ```c
    目标结构 = 源结构;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct point {
        int x;
        int y;
    };

    int main(void)
    {
        struct point a = {1, 2};
        struct point b;
        b = a;              /* 逐成员复制 */
        b.x = 10;
        printf("%d %d %d\n", a.x, b.x, b.y);
        return 0;
    }
    ```

    输出：

    ```text
    1 10 2
    ```

!!! note "说明"

    - 同类型结构可以整体赋值
    - 赋值逐成员复制，数组成员也一并复制
    - 赋值的两个结构必须类型兼容
    - 结构不能用 `==` 或 `!=` 直接比较
    - 比较应逐成员进行，或写专门的比较函数
    - 有指针成员时整体赋值只复制地址，属于浅拷贝

    [C 标准没有定义结构的相等比较，`a == b` 是编译错误
    - 用 `memcmp()` 比较还会读到填充字节和字符串结尾后的内容，结果不可靠]

!!! warning "常见错误"

    - 写 `if (a == b)` 判断两个结构相等
    - 以为结构赋值会深拷贝指针成员指向的数据
    - 用 `memcmp()` 比较含填充字节的结构

## 结构作返回值

!!! abstract "语法形式"

    ```c
    struct 标记 函数名(形参列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct point {
        int x;
        int y;
    };

    struct point move(struct point p, int dx, int dy)
    {
        p.x += dx;
        p.y += dy;
        return p;           /* 返回结构的值 */
    }

    int main(void)
    {
        struct point a = {1, 2};
        a = move(a, 3, 4);
        printf("%d %d\n", a.x, a.y);
        return 0;
    }
    ```

    输出：

    ```text
    4 6
    ```

!!! note "说明"

    - 函数返回类型写成结构类型
    - 返回的是结构值的副本
    - 调用方用同类型结构接住返回值
    - 一次返回可以把多个成员一起传回
    - 返回结构与传结构地址都能完成双向通信
    - 不能返回局部结构变量的地址

!!! warning "常见错误"

    - 返回指向函数内局部结构的指针
    - 调用后不接返回值，以为原结构已被修改
    - 函数声明与定义的返回类型不一致

## 结构中的字符数组与字符指针

!!! abstract "语法形式"

    ```c
    struct 标记 {
        char 数组名[长度];    /* 储存字符串本身 */
        char *指针名;         /* 储存字符串的地址 */
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    #define LEN 20

    struct names {
        char first[LEN];
        char last[LEN];
    };

    struct pnames {
        char * first;
        char * last;
    };

    int main(void)
    {
        struct names veep = {"Talia", "Summers"};
        struct pnames treas = {"Brad", "Fallingjaw"};
        printf("%s %s\n", veep.first, treas.first);
        return 0;
    }
    ```

    输出：

    ```text
    Talia Brad
    ```

!!! note "说明"

    - 字符数组成员在结构内分配空间，字符串属于结构
    - 字符指针成员只存地址，字符串在别处
    - 指针成员可以指向字符串常量或已分配的内存
    - 用指针成员读入字符串前，必须先让它指向可用空间
    - 字符串常量不可修改，不要通过指针成员改写
    - 只储存字符串时，用字符数组更简单

!!! warning "常见错误"

    - 对未初始化的指针成员调用 `scanf("%s", s.last)`
    - 以为结构会为指针成员指向的字符串分配空间
    - 把字符串常量地址赋给指针成员后又修改内容

## 结构指针与 malloc

!!! abstract "语法形式"

    ```c
    结构指针->成员 = malloc(字节数);
    free(结构指针->成员);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    struct namect {
        char * fname;
        char * lname;
        int letters;
    };

    int main(void)
    {
        struct namect p;
        char temp[] = "Floresiensis";

        p.fname = malloc(strlen(temp) + 1);
        strcpy(p.fname, temp);
        p.lname = malloc(5);
        strcpy(p.lname, "Mann");
        p.letters = strlen(p.fname) + strlen(p.lname);

        printf("%s %s %d\n", p.fname, p.lname, p.letters);
        free(p.fname);
        free(p.lname);
        return 0;
    }
    ```

    输出：

    ```text
    Floresiensis Mann 16
    ```

!!! note "说明"

    - 结构只存地址，字符串存在 `malloc()` 分配的内存中
    - `strlen` 返回值加 `1` 才包含空字符
    - 每个 `malloc()` 都要有对应的 `free()`
    - 字符串不在结构内，其他字符串函数仍可使用
    - 结构整体赋值只复制地址，两个结构共享同一块内存
    - 需要独立副本时，应分别分配并复制字符串

    [结构赋值对指针成员只做浅拷贝。 复制后的两个结构指向同一块内存，修改或释放其中一个会影响另一个]

!!! warning "常见错误"

    - 忘记 `free()`，造成内存泄漏
    - 复制结构后对两个副本各 `free()` 一次，造成重复释放
    - 分配 `strlen(temp)` 字节，漏掉空字符的位置

## 复合字面量

!!! abstract "语法形式"

    ```c
    (类型名){初始化列表}
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct book {
        char title[41];
        float value;
    };

    int main(void)
    {
        struct book readfirst;
        readfirst = (struct book) {"Crime and Punishment", 11.25};
        printf("%s %.2f\n", readfirst.title, readfirst.value);
        return 0;
    }
    ```

    输出：

    ```text
    Crime and Punishment 11.25
    ```

!!! note "说明"

    - 类型名放在圆括号中，后面紧跟初始化列表
    - 可以赋给同类型结构，也可以直接作实参
    - 需要传地址时写 `&(struct book){"...", 1.0}`
    - 块内的复合字面量具有自动存储期
    - 所有函数外的复合字面量具有静态存储期
    - 初始化规则与普通初始化列表相同，可用指定初始化器

!!! warning "常见错误"

    - 漏掉类型名外的圆括号
    - 保存复合字面量的地址后在所属块外使用
    - 以为复合字面量可以重复赋值并保留上次内容

## 伸缩型数组成员

!!! abstract "语法形式"

    ```c
    struct 标记 {
        ...
        类型 数组名[];
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct flex {
        size_t count;
        double average;
        double scores[];    /* 伸缩型数组成员 */
    };

    int main(void)
    {
        struct flex * pf;
        int i, n = 5, tot = 0;

        pf = malloc(sizeof(struct flex) + n * sizeof(double));
        pf->count = n;
        for (i = 0; i < n; i++)
        {
            pf->scores[i] = 20.0 - i;
            tot += pf->scores[i];
        }
        pf->average = tot / n;
        printf("%zu %.0f\n", pf->count, pf->average);
        free(pf);
        return 0;
    }
    ```

    输出：

    ```text
    5 18
    ```

!!! note "说明"

    - 伸缩型数组成员必须是结构的最后一个成员
    - 方括号为空，结构中必须至少还有一个成员
    - `sizeof(struct flex)` 不包含伸缩数组的空间
    - 用 `malloc(sizeof(struct flex) + n * sizeof(double))` 分配
    - 分配后可以像普通数组一样使用 `scores[i]`
    - 不能为伸缩数组部分提供初始化项
    - 整体赋值或按值传递只复制固定成员，不要这样用
    - 不能作数组元素，也不能作其他结构的成员
    - 需要复制全部内容时用 `memcpy()`

!!! warning "常见错误"

    - 声明 `struct flex f;` 后直接访问 `f.scores`
    - 只分配 `sizeof(struct flex)`，却写入 `scores`
    - 用 `*pf2 = *pf1` 复制，只复制了数组以外的成员

## 匿名结构

!!! abstract "语法形式"

    ```c
    struct 外层 {
        类型 成员;
        struct {
            类型 内层成员;
        };
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct person {
        int id;
        struct {
            char first[20];
            char last[20];
        };                  /* 匿名结构成员 */
    };

    int main(void)
    {
        struct person ted = {8483, {"Ted", "Grass"}};
        printf("%s %s %d\n", ted.first, ted.last, ted.id);
        return 0;
    }
    ```

    输出：

    ```text
    Ted Grass 8483
    ```

!!! note "说明"

    - 匿名成员是没有成员名的结构成员
    - 其内层成员被当作外层结构的成员直接访问
    - 访问时不需要中间成员名
    - 初始化仍按嵌套层次使用花括号
    - 匿名结构是 C11 特性
    - 匿名特性在嵌套联合中更常用

!!! warning "常见错误"

    - 写 `ted.name.first`，匿名成员没有名字
    - 在 C99 模式下使用，编译报错
    - 初始化时漏掉内层花括号

## 结构数组作函数参数

!!! abstract "语法形式"

    ```c
    返回类型 函数名(const struct 标记 数组名[], int n);
    函数名(结构数组, 元素个数);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    #define N 2

    struct funds {
        double bankfund;
        double savefund;
    };

    double sum(const struct funds money[], int n)
    {
        double total = 0;
        int i;
        for (i = 0; i < n; i++)
            total += money[i].bankfund + money[i].savefund;
        return total;
    }

    int main(void)
    {
        struct funds jones[N] = {
            {4032.27, 8543.94},
            {3620.88, 3802.91}
        };
        printf("%.2f\n", sum(jones, N));
        return 0;
    }
    ```

    输出：

    ```text
    20000.00
    ```

!!! note "说明"

    - 数组名是该数组首元素的地址，可直接传递
    - 形参写成 `const struct funds money[]`
    - 形参也可以写成 `const struct funds *money`
    - 函数内用 `money[i].成员` 访问各元素
    - 传 `&jones[0]` 与传 `jones` 效果相同
    - 函数需要另外知道元素个数
    - `sizeof money` 在函数内只得到指针的大小

!!! warning "常见错误"

    - 在函数内用 `sizeof money` 求数组长度
    - 忘记传元素个数，造成越界访问
    - 形参写成结构数组，却用 `->` 访问元素成员

## 结构读写文件

!!! abstract "语法形式"

    ```c
    fwrite(&结构变量, sizeof(结构变量), 1, 文件指针);
    fread(&结构变量, sizeof(结构变量), 1, 文件指针);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct book {
        char title[41];
        float value;
    };

    int main(void)
    {
        struct book b = {"The Third Jar", 22.99};
        struct book r;
        FILE * fp = fopen("book.dat", "wb");

        if (fp == NULL)
            exit(1);
        fwrite(&b, sizeof b, 1, fp);    /* 写整块结构 */
        fclose(fp);

        fp = fopen("book.dat", "rb");
        fread(&r, sizeof r, 1, fp);     /* 读整块结构 */
        printf("%s %.2f\n", r.title, r.value);
        fclose(fp);
        remove("book.dat");
        return 0;
    }
    ```

    输出：

    ```text
    The Third Jar 22.99
    ```

!!! note "说明"

    - `fwrite()` 与 `fread()` 按二进制表示读写
    - 第二个参数是块大小，第三个参数是块数
    - 一次读写一个完整记录，不必逐字段处理
    - 追加写入用 `"a+b"` 模式打开
    - 读取前用 `rewind()` 把文件指针移回开头
    - 二进制布局依赖系统与编译器，文件不保证可移植
    - 结构中的填充字节也会被写入，占用额外空间

!!! warning "常见错误"

    - 用文本模式打开文件后读写结构
    - 写入与读取使用不同的结构类型或大小
    - 追加模式下读取前忘记 `rewind()`

## 自引用结构与链式结构

!!! abstract "语法形式"

    ```c
    struct 标记 {
        类型 数据;
        struct 标记 *指针名;
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct node {
        int value;
        struct node * left;     /* 指向同类型结构 */
        struct node * right;
    };

    int main(void)
    {
        struct node root = {2, NULL, NULL};
        struct node leaf = {1, NULL, NULL};

        root.left = &leaf;      /* 链接两个节点 */
        printf("%d %d\n", root.value, root.left->value);
        return 0;
    }
    ```

    输出：

    ```text
    2 1
    ```

!!! note "说明"

    - 成员可以是指向自身类型的指针
    - 不能是自身类型的结构变量，此时类型尚未完整
    - 指针把节点连成链表，二叉树等形式
    - 遍历时沿指针逐级访问
    - 每个节点通常单独用 `malloc()` 分配
    - 删除节点后要释放其内存

    ![图14.3 一个二叉树结构](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00073.jpg)

!!! warning "常见错误"

    - 写成 `struct node child;`，结构类型不完整
    - 声明指针后不初始化，遍历时访问野指针
    - 释放节点后仍保留指向它的指针

## 联合

!!! abstract "语法形式"

    ```c
    union 标记 {
        类型 成员名;
        ...
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    union hold {
        int digit;
        double bigfl;
        char letter;
    };

    int main(void)
    {
        printf("%zu %zu\n", sizeof(union hold), sizeof(double));
        return 0;
    }
    ```

    输出：

    ```text
    8 8
    ```

!!! note "说明"

    - 联合的成员共享同一块存储空间
    - 联合的大小由最大的成员决定，可能还要考虑对齐
    - 一次只能保存一个成员的值
    - 联合的声明语法与结构相同
    - 可以声明联合变量，联合数组与联合指针
    - 常见用途是表示几种互斥的数据形式

!!! warning "常见错误"

    - 以为联合能同时保存多个成员
    - 以为联合大小等于各成员大小之和
    - 对联合使用结构的初始化方式，填入多个值

## 初始化联合

!!! abstract "语法形式"

    ```c
    union 标记 变量名 = {值};
    union 标记 变量名 = {.成员名 = 值};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    union hold {
        int digit;
        double bigfl;
        char letter;
    };

    int main(void)
    {
        union hold a = {88};             /* 初始化第一个成员 */
        union hold b = {.bigfl = 118.2}; /* 指定初始化器 */
        union hold c = b;                /* 用同类型联合初始化 */
        printf("%d %.1f %.1f\n", a.digit, b.bigfl, c.bigfl);
        return 0;
    }
    ```

    输出：

    ```text
    88 118.2 118.2
    ```

!!! note "说明"

    - 花括号中只应有一个初始化项
    - 普通初始化项对应联合的第一个成员
    - 可用另一个同类型联合初始化
    - C99 指定初始化器可选择任意成员
    - 未指定的字节保持不确定的值
    - 联合变量也可以先声明，再给当前成员赋值

!!! warning "常见错误"

    - 写 `union hold u = {1, 2.0};`，联合不能同时初始化多个成员
    - 以为 `{88}` 会初始化指定的成员而不是第一个成员

## 使用联合

!!! abstract "语法形式"

    ```c
    联合变量.成员名
    联合指针->成员名
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    union hold {
        int digit;
        char letter;
    };

    int main(void)
    {
        union hold fit;
        fit.digit = 23;         /* 当前成员是 digit */
        printf("%d\n", fit.digit);
        fit.letter = 'h';       /* 改写后当前成员是 letter */
        printf("%c\n", fit.letter);
        return 0;
    }
    ```

    输出：

    ```text
    23
    h
    ```

!!! note "说明"

    - 点运算符表示当前使用的成员
    - 写入一个成员会覆盖其他成员的内容
    - 读取的成员应与最后写入的成员一致
    - 用指针访问联合时使用 `->`
    - 常与一个状态成员配合，由状态决定当前有效成员
    - 结构中放联合可表示互斥的几类信息

    [C 允许写入一个成员后按另一个成员读取，结果由实现定义
    - 通常称为 type punning. C++ 中这类访问是未定义行为，不要依赖]

!!! warning "常见错误"

    - 写入 `letter` 后按 `bigfl` 使用
    - 忘记用状态成员记录当前有效的成员
    - 用 `->` 访问联合变量而不是联合指针

## 匿名联合

!!! abstract "语法形式"

    ```c
    struct 外层 {
        类型 成员;
        union {
            类型 成员1;
            类型 成员2;
        };
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct owner {
        char socsecurity[12];
    };

    struct leasecompany {
        char name[40];
    };

    struct car_data {
        char make[15];
        int status;             /* 0 私有, 1 租赁 */
        union {
            struct owner owncar;
            struct leasecompany leasecar;
        };                      /* 匿名联合成员 */
    };

    int main(void)
    {
        struct car_data flits = {
            .make = "Ford", .status = 1,
            .leasecar = {"Hertz"}
        };
        printf("%s %s %d\n",
               flits.make, flits.leasecar.name, flits.status);
        return 0;
    }
    ```

    输出：

    ```text
    Ford Hertz 1
    ```

!!! note "说明"

    - 匿名联合是没有名字的联合成员
    - 其成员被当作外层结构的成员直接访问
    - 不需要写中间成员名
    - 初始化可用嵌套花括号或指定初始化器
    - 适合表示同一字段的几种互斥形式
    - 匿名联合是 C11 特性

!!! warning "常见错误"

    - 写 `flits.ownerinfo.leasecar.name`，匿名成员没有名字
    - 在 C99 模式下使用
    - 同时给两个互斥成员赋值

## 枚举声明

!!! abstract "语法形式"

    ```c
    enum 标记 {枚举符1, 枚举符2, ...};
    enum 标记 变量名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    enum spectrum { red, orange, yellow, green, blue, violet };

    int main(void)
    {
        enum spectrum color = blue;
        printf("%d %d\n", color, violet);
        return 0;
    }
    ```

    输出：

    ```text
    4 5
    ```

!!! note "说明"

    - 枚举符是具名的整型常量
    - 默认从 `0` 开始，依次加 `1`
    - 枚举变量声明为 `enum 标记`
    - 标记可以省略，但那样只能使用这一次定义
    - 枚举变量可赋值列表中未出现的整数
    - 枚举符可用于数组大小与 `case` 标签

!!! warning "常见错误"

    - 以为枚举会检查取值只能落在列表内
    - 用 `%s` 打印枚举变量
    - 把枚举符当作字符串

## 枚举常量与用法

!!! abstract "语法形式"

    ```c
    enum 标记 {名称 = 整数值, ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    enum kids { nippy, slats, skippy, nina, liz };
    enum levels { low = 100, medium = 500, high = 2000 };
    enum feline { cat, lynx = 10, puma, tiger };

    int main(void)
    {
        printf("%d %d %d %d\n", nina, low, puma, tiger);
        return 0;
    }
    ```

    输出：

    ```text
    3 100 11 12
    ```

!!! note "说明"

    - 未赋值的枚举符等于前一项加 `1`
    - 只给部分枚举符赋值，后续项继续递增
    - 枚举符是 `int` 类型的常量
    - 枚举变量可参与整数运算，用在 `switch` 中很方便
    - 输入时只能读数字，或先读字符串再转换
    - 枚举只影响书写方式，不增加运行时检查

!!! warning "常见错误"

    - 以为 `enum feline` 中 `tiger` 的值还是 `10`
    - 在 `switch` 的 `case` 中用字符串
    - 用 `scanf("%s")` 直接读入枚举符

## 标记的名称空间

!!! abstract "语法形式"

    ```c
    struct 标记 { ... };
    int 标记;          /* 与结构标记不冲突 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    struct rect {
        double x;
        double y;
    };

    int rect = 7;           /* 与标记 rect 不冲突 */

    int main(void)
    {
        struct rect r = {1.0, 2.0};
        printf("%d %.1f\n", rect, r.x);
        return 0;
    }
    ```

    输出：

    ```text
    7 1.0
    ```

!!! note "说明"

    - 结构，联合，枚举的标记共享一个名称空间
    - 标记与普通变量名属于不同名称空间
    - 同一作用域不能有两个同名标记
    - 同一作用域也不能有两个同名变量
    - 同类标识符混用会造成阅读困难
    - C++ 把标记放进普通名称空间，上述代码在 C++ 中不合法

    [C 允许结构标记与变量同名，C++ 不允许。 需要同时兼容两者时不要这样写]

!!! warning "常见错误"

    - 以为标记可以像变量一样直接使用
    - 在同一作用域重复声明同名结构标记
    - 把 C 的写法直接搬进 C++ 项目

## typedef 定义类型名

!!! abstract "语法形式"

    ```c
    typedef 已有类型 新名称;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    typedef unsigned char BYTE;
    typedef char * STRING;

    int main(void)
    {
        BYTE x = 255;
        STRING name = "C";
        printf("%d %s\n", x, name);
        return 0;
    }
    ```

    输出：

    ```text
    255 C
    ```

!!! note "说明"

    - `typedef` 为已有类型增加一个名称
    - 新名称是类型名，不是变量
    - 名称遵循变量的命名规则
    - 定义在函数内时具有局部作用域
    - 定义在函数外时具有文件作用域
    - 不创建新类型，只提供别名
    - 常用来简化结构，联合，指针与函数指针的声明

!!! warning "常见错误"

    - 把 `typedef` 当变量定义并赋初值
    - 漏掉末尾的分号
    - 以为新名称与原名是不同的类型

## typedef 与 #define 的差别

!!! abstract "语法形式"

    ```c
    typedef 类型 名称;
    #define 名称 替换文本
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    typedef char * STRING;
    #define STRING2 char *

    int main(void)
    {
        STRING a, b;            /* 两个都是 char * */
        STRING2 c, d;           /* d 是 char, 不是指针 */
        char x = 'x', y = 'y';

        a = &x; b = &y; c = &x; d = y;
        printf("%c %c %c %c\n", *a, *b, *c, d);
        return 0;
    }
    ```

    输出：

    ```text
    x y x y
    ```

!!! note "说明"

    - `typedef` 由编译器解释，`#define` 由预处理器替换
    - `typedef` 定义类型名，不能用于值
    - `#define` 只做文本替换，不检查类型
    - 指针别名在多重声明中的差别最明显
    - `typedef` 受作用域限制，`#define` 从定义处生效到文件末尾
    - `#define` 可用 `#undef` 取消

    - `#define STRING2 char *` 展开后，`STRING2 c, d;` 变成 `char * c, d;`
    - 只有 `c` 是指针

!!! warning "常见错误"

    - 用 `#define` 定义指针类型后一次声明多个变量
    - 认为 `typedef` 也会做文本替换
    - 在 `typedef` 后加初值

## typedef 与结构

!!! abstract "语法形式"

    ```c
    typedef struct 标记 {
        ...
    } 别名;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    typedef struct {
        double x;
        double y;
    } rect;

    typedef struct complex {
        float real;
        float imag;
    } COMPLEX;

    int main(void)
    {
        rect r1 = {3.0, 6.0};
        rect r2 = r1;
        COMPLEX c = {1.0f, -2.0f};
        printf("%.1f %.1f\n", r2.x, c.imag);
        return 0;
    }
    ```

    输出：

    ```text
    3.0 -2.0
    ```

!!! note "说明"

    - 可以同时给出结构标记与类型别名
    - 只需要别名时可以省略标记
    - 别名声明变量时不必再写 `struct`
    - 别名声明的是同一个类型，因此 `r1` 可以赋给 `r2`
    - 两个分别写出的无标记结构即使成员相同，也是不同类型
    - 别名不改变类型的兼容规则

    [教材称成员相同的两个无标记结构类型相同，这一点不成立
    - C 规定每写出一次 struct 声明都引入一个新类型
    - 只有复用同一个标记或 typedef，两个变量才类型兼容]

!!! warning "常见错误"

    - 以为 `typedef` 创建了独立的新类型
    - 省略标记后仍写 `struct rect r;`
    - 把别名与变量名混用

## 复杂声明的阅读规则

!!! abstract "语法形式"

    ```c
    声明符
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int * risks[10];        /* 10 个指向 int 的指针 */
        int (* rusks)[10];      /* 指向含 10 个 int 的数组 */
        int (* uof[3])[4];      /* 3 个指针, 各指向含 4 个 int 的数组 */

        printf("%zu %zu\n",
               sizeof risks / sizeof risks[0],
               sizeof uof / sizeof uof[0]);
        return 0;
    }
    ```

    输出：

    ```text
    10 3
    ```

!!! note "说明"

    - `[]` 与 `()` 的优先级高于 `*`
    - `[]` 与 `()` 优先级相同，从左向右结合
    - 先看标识符与谁结合，再由内向外读
    - `int * risks[10]` 是数组，元素是指针
    - `int (* rusks)[10]` 是指针，指向数组
    - `int (* uof[3])[4]` 是数组，元素是指向数组的指针
    - 圆括号改变 `*` 的结合对象

    表14-1 声明时可使用的符号

    | 符号 | 含义 |
    | --- | --- |
    | `*` | 表示一个指针 |
    | `()` | 表示一个函数 |
    | `[]` | 表示一个数组 |

!!! warning "常见错误"

    - 漏写 `(*指针名)` 外的圆括号
    - 把 `int *a[3]` 与 `int (*a)[3]` 当作同一种声明
    - 从右向左读而不先判断结合对象

## 声明函数指针

!!! abstract "语法形式"

    ```c
    返回类型 (*指针名)(形参类型列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    void ToUpper(char * s);
    void (*pf)(char *);     /* 指向该类型函数的指针 */

    int main(void)
    {
        char mis[] = "Nina";
        pf = ToUpper;       /* 函数名表示地址 */
        pf(mis);
        printf("%s\n", mis);
        return 0;
    }

    void ToUpper(char * s)
    {
        while (*s)
        {
            if (*s >= 'a' && *s <= 'z')
                *s -= 'a' - 'A';
            s++;
        }
    }
    ```

    输出：

    ```text
    NINA
    ```

!!! note "说明"

    - 先写函数原型，再把函数名换成 `(*pf)`
    - 第一对圆括号不能省略
    - `void *pf(char *)` 是返回指针的函数，不是函数指针
    - 函数指针的类型由返回类型与形参类型共同决定
    - 赋值时函数名与 `&函数名` 都表示地址
    - 只有类型完全匹配的函数才能赋给该指针

!!! warning "常见错误"

    - 写成 `void *pf(char *)`，含义完全不同
    - 写成 `pf = ToUpper()`，把调用结果赋给指针
    - 把参数类型不同的函数赋给指针

## 用函数指针调用函数

!!! abstract "语法形式"

    ```c
    (*指针名)(实参列表);
    指针名(实参列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    void ToLower(char * s);

    int main(void)
    {
        char a[] = "ABC", b[] = "ABC";
        void (*pf)(char *) = ToLower;

        (*pf)(a);      /* 语法 1 */
        pf(b);         /* 语法 2 */
        printf("%s %s\n", a, b);
        return 0;
    }

    void ToLower(char * s)
    {
        while (*s)
        {
            if (*s >= 'A' && *s <= 'Z')
                *s += 'a' - 'A';
            s++;
        }
    }
    ```

    输出：

    ```text
    abc abc
    ```

!!! note "说明"

    - `(*pf)(实参)` 与 `pf(实参)` 等价
    - ANSI C 及后续标准都接受这两种写法
    - `*pf` 与函数名等价，因为函数名表示地址
    - 指针和函数名在调用处可以互换
    - 两种写法调用的是同一个函数

!!! warning "常见错误"

    - 写 `*pf(实参)`，实际被解析为 `*(pf(实参))`
    - 以为 `pf(实参)` 只能用于函数名
    - 在函数指针未赋值时调用

## 函数指针作参数

!!! abstract "语法形式"

    ```c
    void 函数名(返回类型 (*形参)(参数类型), ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    void show(void (* fp)(char *), char * str)
    {
        (*fp)(str);         /* 调用传入的函数 */
        puts(str);
    }

    void Upper(char * s)
    {
        while (*s)
        {
            if (*s >= 'a' && *s <= 'z')
                *s -= 'a' - 'A';
            s++;
        }
    }

    int main(void)
    {
        char s[] = "hello";
        show(Upper, s);     /* 传函数名 */
        return 0;
    }
    ```

    输出：

    ```text
    HELLO
    ```

!!! note "说明"

    - 形参声明为函数指针，实参可写函数名
    - 函数名表示地址，`Upper` 与 `&Upper` 都可用
    - 函数内用 `(*fp)(实参)` 或 `fp(实参)` 调用
    - 同一接口可以接收不同处理函数
    - 可用 `typedef` 简化函数指针形参
    - `function(sqrt)` 传函数地址，`function(sqrt(4.0))` 传返回值

    ![图14.4 函数名的用法](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00074.jpg)

!!! warning "常见错误"

    - 传 `Upper()` 而不是 `Upper`
    - 形参与实参的函数类型不匹配
    - 在函数内对函数指针取地址写成 `&fp`

## 函数指针数组

!!! abstract "语法形式"

    ```c
    返回类型 (*数组名[元素个数])(形参类型列表);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    double sum(double a, double b) { return a + b; }
    double diff(double a, double b) { return a - b; }

    int main(void)
    {
        double (*pf[2])(double, double) = {sum, diff};
        printf("%.1f %.1f\n",
               pf[0](10.0, 2.5), (*pf[1])(10.0, 2.5));
        return 0;
    }
    ```

    输出：

    ```text
    12.5 7.5
    ```

!!! note "说明"

    - 数组的每个元素都是函数指针
    - 所有元素的函数类型必须相同
    - 用下标选择函数，可实现菜单分派
    - 可用 `typedef` 简化： `typedef double (*FUN)(double, double);`
    - 不存在函数数组，但可以有函数指针数组
    - 初始化列表直接写函数名

!!! warning "常见错误"

    - 声明写成 `double *pf[2](double, double)`
    - 初始化列表混入类型不匹配的函数
    - 数组下标越界后仍调用

## 复习题

（1）下面的结构模板有什么问题
```c
structure {
    char itable;
    int num[20];
    char * togs
}
```

??? note "答案"

    关键字应为 `struct`，不是 `structure`
    结构需要在左花括号前有标记，或在右花括号后跟变量名
    `togs` 后面与模板结尾处都少一个分号

（2）下面是程序的一部分，输出是什么
```c
#include <stdio.h>
struct house {
    float sqft;
    int rooms;
    int stories;
    char address[40];
};
int main(void)
{
    struct house fruzt = {1560.0, 6, 1, "22 Spiffo Road"};
    struct house *sign;
    sign = &fruzt;
    printf("%d %d\n", fruzt.rooms, sign->stories);
    printf("%s \n", fruzt.address);
    printf("%c %c\n", sign->address[3], fruzt.address[4]);
    return 0;
}
```

??? note "答案"

    输出为

    ```text
    6 1
    22 Spiffo Road
    S p
    ```

（3）设计一个结构模板储存一个月份名，该月份名的 3 个字母缩写，该月的天数以及月份号

??? note "答案"

    ```c
    struct month {
        char name[10];
        char abbrev[4];
        int days;
        int monumb;
    };
    ```

（4）定义一个数组，内含 12 个结构 (第 3 题的结构类型) 并初始化为一个年份 (非闰年)

??? note "答案"

    ```c
    struct month months[12] =
    {
        { "January", "jan", 31, 1 },
        { "February", "feb", 28, 2 },
        { "March", "mar", 31, 3 },
        { "April", "apr", 30, 4 },
        { "May", "may", 31, 5 },
        { "June", "jun", 30, 6 },
        { "July", "jul", 31, 7 },
        { "August", "aug", 31, 8 },
        { "September", "sep", 30, 9 },
        { "October", "oct", 31, 10 },
        { "November", "nov", 30, 11 },
        { "December", "dec", 31, 12 }
    };
    ```

（5）编写一个函数，用户提供月份号
该函数返回一年中到该月为止 (包括该月) 的总天数
假设在所有函数的外部声明了第 3 题的结构模板
和一个该类型结构的数组

??? note "答案"

    ```c
    extern struct month months[];
    int days(int month)
    {
        int index, total;
        if (month < 1 || month > 12)
            return(-1);         /* 错误信号 */
        else
        {
            for (index = 0, total = 0; index < month; index++)
                total += months[index].days;
            return(total);
        }
    }
    ```

    `index` 比月数小 `1`，因为数组下标从 `0` 开始，循环条件用 `index < month`

（6）a. 假设有下面的 `typedef`，声明一个内含 10 个指定结构的数组
然后单独给成员赋值，使第 3 个元素表示
焦距长度 500mm，孔径 f/2.0 的 Remarkata 镜头
```c
typedef struct lens {
    float foclen;
    float fstop;
    char brand[30];
} LENS;
```
b. 重写 a，在声明中使用指定初始化器的初始化列表，而不是对每个成员单独赋值

??? note "答案"

    a.

    ```c
    #include <string.h>

    LENS bigEye[10];
    bigEye[2].foclen = 500;
    bigEye[2].fstop = 2.0;
    strcpy(bigEye[2].brand, "Remarkatar");
    ```

    b.

    ```c
    LENS bigEye[10] = { [2] = {500, 2, "Remarkatar"} };
    ```

（7）考虑下面的程序片段
```c
struct name {
    char first[20];
    char last[20];
};
struct bem {
    int limbs;
    struct name title;
    char type[30];
};
struct bem * pb;
struct bem deb = {
    6,
    { "Berbnazel", "Gwolkapwolk" },
    "Arcturan"
};
pb = &deb;
```
a. 下面的语句分别打印什么
```c
printf("%d\n", deb.limbs);
printf("%s\n", pb->type);
printf("%s\n", pb->type + 2);
```
b. 如何用结构表示法 (两种方法) 表示 `"Gwolkapwolk"`
c. 编写一个函数，以 bem 结构的地址作为参数，输出结构的内容

??? note "答案"

    a. 输出为

    ```text
    6
    Arcturan
    cturan
    ```

    b. `deb.title.last` 与 `pb->title.last`

    c.

    ```c
    #include <stdio.h>
    #include "starfolk.h"

    void prbem(const struct bem * pbem)
    {
        printf("%s %s is a %d-limbed %s.\n",
               pbem->title.first, pbem->title.last,
               pbem->limbs, pbem->type);
    }
    ```

（8）考虑下面的声明
```c
struct fullname {
    char fname[20];
    char lname[20];
};
struct bard {
    struct fullname name;
    int born;
    int died;
};
struct bard willie;
struct bard *pt = &willie;
```
a. 用 `willie` 标识 `born` 成员
b. 用 `pt` 标识 `born` 成员
c. 用 `scanf()` 读入 `willie` 的 `born` 成员
d. 用 `scanf()` 读入 `pt` 指向结构的 `born` 成员
e. 用 `scanf()` 读入 `willie` 的 `name` 成员中的 `lname`
f. 用 `scanf()` 读入 `pt` 指向结构的 `name` 成员中的 `lname`
g. 构造标识符，标识姓名中名的第 3 个字母 (英文的名在前)
h. 构造表达式，表示名和姓中的字母总数

??? note "答案"

    a. `willie.born`

    b. `pt->born`

    c. `scanf("%d", &willie.born);`

    d. `scanf("%d", &pt->born);`

    e. `scanf("%s", willie.name.lname);`

    f. `scanf("%s", pt->name.lname);`

    g. `willie.name.fname[2]`

    h. `strlen(willie.name.fname) + strlen(willie.name.lname)`

（9）定义一个结构模板以储存汽车名，马力
EPA 城市交通 MPG 评级，轴距和出厂年份
使用 `car` 作为标记

??? note "答案"

    ```c
    struct car {
        char name[20];
        float hp;
        float epampg;
        float wbase;
        int year;
    };
    ```

（10）假设有下面的结构
```c
struct gas {
    float distance;
    float gals;
    float mpg;
};
```
a. 设计一个函数，接受 `struct gas` 类型的参数，计算 `mpg` 并返回该结构
b. 设计一个函数，接受 `struct gas` 类型的参数，计算 `mpg` 并赋给相应成员

??? note "答案"

    ```c
    struct gas mpgs(struct gas trip)
    {
        if (trip.gals > 0)
            trip.mpg = trip.distance / trip.gals;
        else
            trip.mpg = -1.0;
        return trip;
    }

    void set_mpgs(struct gas * ptrip)
    {
        if (ptrip->gals > 0)
            ptrip->mpg = ptrip->distance / ptrip->gals;
        else
            ptrip->mpg = -1.0;
    }
    ```

    第一个函数不能直接修改主调程序中的值，必须用返回值传递信息

    ```c
    struct gas idaho = {430.0, 14.8};
    idaho = mpgs(idaho);
    ```

    第二个函数直接访问原结构

    ```c
    struct gas ohio = {583, 17.6};
    set_mpgs(&ohio);
    ```

（11）声明一个标记为 `choices` 的枚举
把枚举常量 `no`，`yes` 和 `maybe` 分别设置为 `0`，`1`，`2`

??? note "答案"

    `enum choices {no, yes, maybe};`

（12）声明一个指向函数的指针
该函数返回指向 `char` 的指针
接受一个指向 `char` 的指针和一个 `char` 类型的值

??? note "答案"

    `char * (*pfun)(char *, char);`

（13）声明 4 个函数，并初始化一个指向这些函数的指针数组
每个函数接受两个 `double` 类型的参数，返回 `double` 类型的值
用两种方法使用该数组调用带 `10.0` 和 `2.5` 实参的第 2 个函数

??? note "答案"

    ```c
    double sum(double, double);
    double diff(double, double);
    double times(double, double);
    double divide(double, double);
    double (*pf1[4])(double, double) = {sum, diff, times, divide};
    ```

    也可用 `typedef` 简化

    ```c
    typedef double (*ptype)(double, double);
    ptype pfl[4] = {sum, diff, times, divide};
    ```

    调用第 2 个函数

    ```c
    pf1[1](10.0, 2.5);        /* 第 1 种写法 */
    (*pf1[1])(10.0, 2.5);     /* 等价写法 */
    ```

## 编程练习

!!! question "编程练习"

    1. 重新编写复习题 5，用月份名的拼写代替月份号，使用 `strcmp()`. 在一个简单的程序中测试该函数

    2. 编写一个函数，提示用户输入日，月和年
    月份可以是月份号，月份名或月份名缩写
    程序应返回一年中到用户指定日子 (包括这一天) 的总天数

    3. 修改程序清单 14.2 的图书目录程序
    使其按照输入图书的顺序输出图书信息
    然后按照标题字母的顺序输出
    最后按照价格的升序输出

    4. 编写一个程序，创建一个有两个成员的结构模板

    a. 第 1 个成员是社会保险号
    第 2 个成员是一个有 3 个成员的结构，分别代表名，中间名和姓
    创建并初始化一个内含 5 个该类型结构的数组
    以下面的格式打印数据

    ```c
    Dribble, Flossie M. -- 302039823
    ```

    有中间名时只打印第 1 个字母并加一个点，没有中间名时不打印点。 把结构数组传递给打印函数

    b. 修改 a 部分，传递结构的值而不是结构的地址

    5. 编写一个程序满足下面的要求

    a. 外部定义一个有两个成员的结构模板 `name`: 一个字符串储存名，一个字符串储存姓

    b. 外部定义一个有 3 个成员的结构模板 `student`
    成员分别是 `name` 类型的结构
    `grade` 数组储存 3 个浮点分数，一个变量储存 3 个分数的平均数

    c. 在 `main()` 中声明一个内含 `CSIZE` (`CSIZE = 4`) 个
    `student` 结构的数组，并初始化这些结构的名字部分

    d. 以交互方式获取每个学生的成绩，提示用户输入学生的姓名和分数，把分数储存到 `grade` 数组的相应结构中

    e. 计算每个结构的平均分，并把结果赋给相应的成员

    f. 打印每个结构的信息

    g. 打印班级的平均分，即所有结构数值成员的平均值

    6. 一个文本文件保存着一个垒球队的信息，每行数据排列如下

    ```c
    4 Jessie Joybat 5 2 1 1
    ```

    第 1 项是球员号，范围 0 到 18
    第 2 项是名，第 3 项是姓，名和姓都是单词
    第 4 项是上场次数，接着 3 项是击中数，走垒数和打点
    文件可能包含多场比赛的数据，同一位球员可能有多行数据
    且可能与其他球员的数据交错
    编写一个程序，把数据储存到结构数组中
    结构成员分别表示名，姓，上场次数，击中数，走垒数
    打点和安打率。 用球员号作数组索引，读到文件结尾
    统计每位球员的各项累计总和

    最简单的做法是把结构内容初始化为零
    把文件数据读入临时变量，再加入相应结构
    读完文件后计算每位球员的安打率
    用累计击中数除以累计上场次数
    最后一行显示一位球员的累计数据

    7. 修改程序清单 14.14，从文件中读取每条记录并显示
    允许用户删除记录或修改记录内容
    删除记录时把空出的空间留给下一个读入的记录
    修改现有内容要用 `"r+b"` 模式而不是 `"a+b"` 模式
    并注意定位文件指针，防止新记录覆盖现有记录
    最简单的方法是改动内存中的所有数据，最后再写入文件
    可在 `book` 结构中增加一个成员表示该项是否被删除

    8. 巨人航空公司的机群由 12 个座位的飞机组成，每天飞行一个航班。 编写一个座位预订程序

    a. 使用一个内含 12 个结构的数组，每个结构包括座位编号，是否已被预订，预订人的名和姓

    b. 程序显示下面的菜单

    ```c
    To choose a function, enter its letter label:
    a) Show number of empty seats
    b) Show list of empty seats
    c) Show alphabetical list of seats
    d) Assign a customer to a seat assignment
    e) Delete a seat assignment
    f) Quit
    ```

    c. 程序能执行上面的菜单。 选择 d 和 e 时提示用户进行额外输入，每个选项都能让用户中止输入

    d. 执行特定操作后再次显示菜单，除非用户选择 f

    9. 巨人航空公司需要另一架飞机 (容量相同)
    每天飞 4 班 (航班 102、311、444 和 519)
    把程序扩展为可以处理 4 个航班
    用一个顶层菜单提供航班选择和退出
    选择特定航班后出现与第 8 题类似的菜单
    但增加一个确认座位分配的选项，菜单中的退出改为返回顶层菜单
    每次显示都要指明当前航班号，座位分配显示要标明确认状态

    10. 编写一个程序，通过一个函数指针数组实现菜单。 例如，选择菜单中的 a，激活该数组第 1 个元素指向的函数

    11. 编写一个名为 `transform()` 的函数，接受 4 个参数
    内含 `double` 数据的源数组名
    内含 `double` 数据的目标数组名
    表示数组元素个数的 `int` 参数
    函数名 (或等价的函数指针)
    函数把指定函数应用于源数组的每个元素
    把返回值储存到目标数组中。 例如

    ```c
    transform(source, target, 100, sin);
    ```

    该调用把 `target[0]` 设为 `sin(source[0])`，共处理 100 个元素
    在一个程序中调用 `transform()` 4 次
    分别使用 `math.h` 中的两个函数和自定义的两个函数作为参数
