# 第4章 字符串和格式化输入/输出

## 字符串

!!! abstract "语法形式"

    ```c
    "Zing went the strings of my heart!"
    ```

!!! note "说明"

    - 字符串是一个或多个字符的序列
    - 双引号不属于字符串，只用于界定字符串的起止
    - C 没有专门的字符串类型，字符串存放在 `char` 数组中
    - 字符串末尾有一个空字符 `'\0'`，由编译器或输入函数添加

## 字符数组与空字符

!!! abstract "语法形式"

    ```c
    char name[40];
    ```

    ![图4.1 数组中的字符串](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00020.jpg)

    ![图4.2 变量与数组的声明差别](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00021.jpg)

!!! note "说明"

    - 数组是同类型元素的有序序列，元素存放在连续的存储单元中
    - 方括号中的 `40` 是元素个数，每个 `char` 元素占 1 字节
    - 40 个字节最多存 39 个字符，最后一个字节留给 `'\0'`
    - `'\0'` 是空字符，ASCII 值为 0，不是字符 `'0'`
    - C 字符串一定以空字符结束，所以数组容量要比字符数多 1

!!! warning "常见错误"

    - 数组元素个数等于字符数，没有位置存放空字符

## 字符串常量的存储

!!! abstract "语法形式"

    ```c
    char ch = 'x';

    printf("%zu %zu\n", sizeof ch, sizeof "x");
    ```

!!! example "输出"

    ```text
    1 2
    ```

!!! note "说明"

    - `'x'` 是字符常量，`"x"` 是字符串常量
    - `"x"` 由字符 `'x'` 和空字符 `'\0'` 两个字符组成
    - `sizeof "x"` 统计的是数组占用的字节数，因此为 2

    ![图4.3 字符常量与字符串常量](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00022.jpg)

    [教材称 `'x'` 的类型是 `char`，与 C 标准不符
    - 整型字符常量 `'x'` 的类型是 `int`，本机 `sizeof 'x'` 为 4
    - 赋给 `char` 变量后才占 1 字节]

## `strlen()` 函数

!!! abstract "语法形式"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        char name[40];

        scanf("%s", name);
        printf("%zu %zu\n", strlen(name), sizeof name);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    Serendipity
    11 40
    ```

!!! note "说明"

    - `strlen()` 返回字符串中的字符数，不计末尾的空字符
    - `sizeof` 返回数组占用的总字节数，包含空字符
    - `strlen()` 从首字符开始数，遇到 `'\0'` 停止
    - 原型声明在 `string.h` 中，使用时需要包含该头文件
    - 两个函数的返回类型都是 `size_t`，用 `%zu` 输出

    ![图4.4 `strlen()` 何时停止](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00023.jpg)

    [教材例中用 `%zd` 输出 `size_t`，标准写法是 `%zu`
    - `z` 修饰符要配合无符号转换字符才与 `size_t` 对应
    - `%zd` 表示对应的有符号类型]

## `sizeof` 的写法

!!! abstract "语法形式"

    ```c
    sizeof(char)     // 运算对象是类型, 圆括号必需
    sizeof name      // 运算对象是变量, 圆括号可省
    sizeof(6.28)     // 运算对象是常量, 建议加圆括号
    ```

!!! note "说明"

    - 运算对象是类型时必须加圆括号
    - 运算对象是变量或常量时圆括号可以省略
    - 书写时统一加圆括号，可以减少混淆

## `#define` 定义明示常量

!!! abstract "语法形式"

    ```c
    #define 名称 值
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define TAXRATE 0.015

    int main(void)
    {
        double owed = 100.0;

        printf("%.3f\n", owed * TAXRATE);

        return 0;
    }
    ```

    输出：

    ```text
    1.500
    ```

!!! note "说明"

    - 编译前预处理器把程序中所有 `TAXRATE` 替换成 `0.015`
    - 这一过程称为编译时替换，运行时替换已经完成
    - 名称与值之间用空格分隔，不用等号
    - 行末不加分号，它由预处理器处理，不是 C 语句
    - 名称习惯用大写，便于与变量区分

    ![图4.5 输入内容与编译后内容](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00024.jpg)

!!! warning "常见错误"

    ```c
    #define TOES = 20
    ```

    - 替换的是 `= 20`，而不是 `20`

    ```c
    digits = fingers + TOES;
    ```

    - 预处理后变成 `digits = fingers + = 20;`，编译报错

## `#define` 定义字符与字符串

!!! abstract "语法形式"

    ```c
    #define BEEP '\a'
    #define TEE 'T'
    #define ESC '\033'
    #define OOPS "Now you have done it!"
    ```

!!! note "说明"

    - 字符常量用单引号，字符串常量用双引号
    - 替换的是包含引号在内的整段内容
    - `'\033'` 是八进制转义序列，表示 ASCII 码 27 的字符

## `const` 限定符

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        const int MONTHS = 12;

        printf("%d\n", MONTHS);
        // MONTHS = 13;   // 编译错误

        return 0;
    }
    ```

!!! example "输出"

    ```text
    12
    ```

!!! note "说明"

    - `const` 声明的变量为只读，初始化后不能赋值
    - 可以参与计算，也可以打印
    - C 中 `const` 声明的是变量，不是常量表达式
    - 因此不能当作编译期常量使用

## `limits.h` 与 `float.h`

!!! abstract "语法形式"

    ```c
    #include <stdio.h>
    #include <limits.h>
    #include <float.h>

    int main(void)
    {
        printf("%d %d\n", INT_MAX, CHAR_BIT);
        printf("%d %e\n", FLT_DIG, FLT_EPSILON);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    2147483647 8
    6 1.192093e-07
    ```

!!! note "说明"

    - 两个头文件用 `#define` 给出整型与浮点型的实现限制
    - `INT_MAX` 与 `INT_MIN` 是 `int` 可表示的最大值与最小值
    - `CHAR_BIT` 是 1 字节的位数
    - `FLT_DIG` 是 `float` 保证的十进制有效数字位数
    - `FLT_EPSILON` 是 1.0 与下一个 `float` 值之差
    - 把 `float.h` 中的 `FLT` 换成 `DBL` 或 `LDBL`
    - 可得到 `double` 或 `long double` 的对应常量

## `printf()` 的转换说明

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("%d %u %o %x\n", 76, 76, 76, 76);
        printf("%c %s\n", 76, "text");
        printf("%f %e %g\n", 76.0, 76.0, 76.0);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    76 76 114 4c
    L text
    76.000000 7.600000e+01 76
    ```

!!! note "说明"

    - 转换说明以 `%` 开始，由修饰符和转换字符组成
    - 转换说明决定待打印值按什么形式显示

    | 转换说明 | 输出 |
    | --- | --- |
    | `%d` `%i` | 有符号十进制整数 |
    | `%u` | 无符号十进制整数 |
    | `%o` | 无符号八进制整数 |
    | `%x` `%X` | 无符号十六进制整数 |
    | `%c` | 单个字符 |
    | `%s` | 字符串 |
    | `%f` | 十进制小数形式的浮点数 |
    | `%e` `%E` | 指数形式的浮点数 |
    | `%g` `%G` | 自动选择 `%f` 或 `%e` |
    | `%a` `%A` | 十六进制指数形式的浮点数 |
    | `%p` | 指针 |
    | `%%` | 一个百分号 |

## `printf()` 的基本用法

!!! abstract "语法形式"

    ```c
    #include <stdio.h>
    #define PI 3.141593

    int main(void)
    {
        int number = 7;
        double pies = 12.75;

        printf("The %d contestants ate %f berry pies.\n",
               number, pies);
        printf("The value of pi is %f.\n", PI);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    The 7 contestants ate 12.750000 berry pies.
    The value of pi is 3.141593.
    ```

!!! note "说明"

    - 第一个参数是格式字符串，后面是待打印项
    - 待打印项可以是变量，常量或表达式
    - 转换说明按顺序与待打印项一一对应
    - 数量或类型不匹配时，输出没有意义

## 打印百分号

!!! abstract "语法形式"

    ```c
    printf("Only %d%% of them were edible.\n", 12);
    ```

!!! example "输出"

    ```text
    Only 12% of them were edible.
    ```

!!! note "说明"

    - `%%` 输出一个百分号
    - 单个 `%` 会被当成转换说明的开头

## 字段宽度

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("*%d*\n", 959);
        printf("*%2d*\n", 959);
        printf("*%10d*\n", 959);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    *959*
    *959*
    *       959*
    ```

!!! note "说明"

    - 数字表示最小字段宽度
    - 内容宽度小于字段时补空格，默认右对齐
    - 内容宽度大于字段时按实际宽度输出，不截断
    - `%2d` 不能把 3 位的 `959` 压成 2 位

## 左对齐

!!! abstract "语法形式"

    ```c
    printf("*%-10d*\n", 959);
    ```

!!! example "输出"

    ```text
    *959       *
    ```

!!! note "说明"

    - `-` 标记使内容在字段内左对齐
    - 与宽度一起使用才有可见效果
    - 省略宽度时，`-` 没有实际作用

## 浮点精度

!!! abstract "语法形式"

    ```c
    printf("*%4.2f*\n", 3852.99);
    printf("*%3.1f*\n", 3852.99);
    printf("*%10.3f*\n", 3852.99);
    ```

!!! example "输出"

    ```text
    *3852.99*
    *3853.0*
    *  3852.990*
    ```

!!! note "说明"

    - `.2` 表示小数点后保留两位，末位四舍五入
    - 宽度包含小数点与符号，是最小宽度
    - `%f` `%e` 的精度指小数点后的位数
    - `%g` 的精度指有效数字的位数
    - `%s` 的精度指最多打印的字符数
    - 整型转换的精度指最少数字位数，不足时补前导 0

## 指数形式

!!! abstract "语法形式"

    ```c
    printf("*%e*\n", 3852.99);
    printf("*%10.3E*\n", 3852.99);
    ```

!!! example "输出"

    ```text
    *3.852990e+03*
    * 3.853E+03*
    ```

!!! note "说明"

    - `%e` 默认小数点后 6 位，指数至少两位
    - `E` 使指数符号与字母大写
    - `printf()` 的 float 实参自动提升为 double
    - 所以浮点转换说明对应的是 double 或 long double

## `+` 标记

!!! abstract "语法形式"

    ```c
    printf("*%+4.2f*\n", 3852.99);
    printf("*%+4.2f*\n", -3852.99);
    ```

!!! example "输出"

    ```text
    *+3852.99*
    *-3852.99*
    ```

!!! note "说明"

    - 正数前显示 `+`，负数前显示 `-`
    - 字段宽度不足时自动扩大
    - `+` 与空格标记同时出现时，`+` 生效

## 空格标记

!!! abstract "语法形式"

    ```c
    printf("**%d**% d**% d**\n", 42, 42, -42);
    ```

!!! example "输出"

    ```text
    **42** 42**-42**
    ```

!!! note "说明"

    - 正数前留一个空格，负数前显示负号
    - 作用是让正数与负数的有效数字位数对齐
    - 该标记只对数值转换有意义

## `0` 标记

!!! abstract "语法形式"

    ```c
    printf("*%010.2f*\n", 3852.99);
    printf("**%05d**\n", 6);
    printf("**%05.3d**\n", 6);
    ```

!!! example "输出"

    ```text
    *0003852.99*
    **00006**
    **  006**
    ```

!!! note "说明"

    - 用前导 `0` 填满字段宽度
    - 整型格式中同时指定精度时，`0` 标记被忽略
    - `-` 标记与 `0` 标记同时出现时，`0` 标记被忽略

## `#` 标记

!!! abstract "语法形式"

    ```c
    printf("%x %#x %#o\n", 31, 31, 31);
    printf("%#.0f\n", 3.0);
    ```

!!! example "输出"

    ```text
    1f 0x1f 037
    3.
    ```

!!! note "说明"

    - `%#x` 加 `0x` 前缀，`%#X` 加 `0X` 前缀
    - `%#o` 加前导 `0`
    - 浮点格式保证输出中有小数点，即使小数部分为 0

## 字符串的宽度与精度

!!! abstract "语法形式"

    ```c
    #include <stdio.h>
    #define BLURB "Authentic imitation!"

    int main(void)
    {
        printf("[%2s]\n", BLURB);
        printf("[%24s]\n", BLURB);
        printf("[%24.5s]\n", BLURB);
        printf("[%-24.5s]\n", BLURB);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    [Authentic imitation!]
    [    Authentic imitation!]
    [                   Authe]
    [Authe                   ]
    ```

!!! note "说明"

    - 字符串宽度不足时，字段自动扩大以容纳全部字符
    - `.5` 只打印前 5 个字符
    - `-` 标记使字符串在字段内左对齐

## 转换说明的作用

!!! abstract "语法形式"

    ```c
    printf("%d %x %c\n", 76, 76, 76);
    ```

!!! example "输出"

    ```text
    76 4c L
    ```

!!! note "说明"

    - 76 在内存中的二进制形式为 `01001100`
    - `%d` 把同一比特串翻译成十进制文本 `76`
    - `%x` 翻译成十六进制文本 `4c`
    - `%c` 翻译成字符 `L`
    - 转换说明只决定显示形式，不改变存储的值

## 整型转换不匹配

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        short num = 336;
        short mnum = -336;

        printf("%hd %hu\n", mnum, mnum);
        printf("%d %c\n", num, num);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    -336 65200
    336 P
    ```

!!! note "说明"

    - `%hu` 把同一比特串按无符号数解释
    - 16 位 `short` 中 -336 存为 65200，即 65536 - 336
    - `%c` 只取最低 1 字节，相当于对 256 取模
    - 336 mod 256 = 80，ASCII 码 80 对应字符 `P`

    ![图4.8 把整数转换成字符](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00027.jpg)

!!! warning "常见错误"

    - 认为 `%u` 会去掉负号
    - 实际改变的是解释方式，比特串不变

## 浮点与整型转换不匹配

!!! abstract "语法形式"

    ```c
    long n = 2000000000;

    printf("%ld\n", n);
    printf("%e\n", n);
    ```

!!! example "输出"

    ```text
    2000000000
    [第二行随系统变化, 无意义]
    ```

!!! note "说明"

    - `%e` 要求 `printf()` 按 `double` 读取 8 字节
    - `long` 实参只占 4 字节，会连同相邻内存一起读取
    - 比特串按浮点格式解释后得到无意义的值
    - 转换说明必须与实参的实际类型匹配

## `printf()` 的返回值

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int rv;

        rv = printf("Hello\n");
        printf("%d\n", rv);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    Hello
    6
    ```

!!! note "说明"

    - 返回打印的字符数，包含空格与换行符
    - 输出出错时返回负值
    - 返回值可以赋给变量，也可以参与计算

## 长字符串的断行

!!! abstract "语法形式"

    ```c
    printf("Here's one way to print a ");
    printf("long string.\n");
    printf("Here's another way to print a \
    long string.\n");
    printf("Here's the newest way to print a "
           "long string.\n");
    ```

!!! example "输出"

    ```text
    Here's one way to print a long string.
    Here's another way to print a long string.
    Here's the newest way to print a long string.
    ```

!!! note "说明"

    - 方法一，用多个 `printf()` 依次输出，前一个不加换行
    - 方法二，用反斜杠加回车续行，字符串中不产生换行符
    - 方法三，相邻的字符串常量由编译器连接成一个
    - 反斜杠续行时下一行不要缩进，缩进的空格会进入字符串
    - 不能在引号内的字符串中间直接按回车

!!! warning "常见错误"

    ```c
    printf("Hello, young" "lovers");
    ```

    - 得到的是 `Hello, younglovers`
    - 两个字符串之间的空白被忽略，空格要写在引号内

## `scanf()` 的基本用法

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int age;
        float assets;
        char pet[30];

        scanf("%d %f", &age, &assets);
        scanf("%s", pet);
        printf("%d $%.2f %s\n", age, assets, pet);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    38 92360.88 llama
    38 $92360.88 llama
    ```

!!! note "说明"

    - `scanf()` 用格式字符串说明输入项的类型
    - 读取基本类型变量时，变量名前加 `&`
    - 读入字符数组时，不加 `&`
    - 参数列表传的是变量的地址

## `scanf()` 的 `%s`

!!! abstract "语法形式"

    ```c
    char name[40];

    scanf("%s", name);
    printf("[%s]\n", name);
    ```

!!! example "输出"

    ```text
    [Angela]
    ```

!!! note "说明"

    - 输入 `Angela Plains` 时只读到空格前的内容
    - `%s` 跳过前导空白，读到下一个空白字符为止
    - 只读取一个单词，剩余字符留在输入缓冲区
    - 读入数组时自动在末尾加 `'\0'`
    - 读取含空格的整行要用 `fgets()`

## `%c` 与空白

!!! abstract "语法形式"

    ```c
    char ch;

    scanf("%c", &ch);    // 读取下一个字符, 包括空白
    scanf(" %c", &ch);   // 跳过前导空白后读取
    ```

!!! note "说明"

    - 除 `%c` 外，各转换说明自动跳过前导空白
    - 所以 `%d%d` 与 `%d %d` 的行为相同
    - 格式字符串中 `%c` 前的空格表示跳过任意数量的空白
    - 包括零个空白

## `scanf()` 格式字符串中的普通字符

!!! abstract "语法形式"

    ```c
    int n, m;

    scanf("%d,%d", &n, &m);
    ```

!!! note "说明"

    - 格式字符串中的普通字符必须与输入严格匹配
    - `%d` 后的逗号要求输入中也有逗号
    - `scanf()` 会跳过整数前的空白，所以 `88, 121` 也可接受
    - 输入可以分行，在 `88,` 后换行再输入 `121`
    - 格式字符串中的空白匹配任意数量的空白，包括零个

## `scanf()` 的返回值

!!! abstract "语法形式"

    ```c
    int n;
    int rv;

    rv = scanf("%d", &n);
    printf("%d\n", rv);
    ```

!!! example "输出"

    ```text
    0
    ```

!!! note "说明"

    - 输入为 `abc` 时，返回成功读取并赋值的项数 0
    - 需要数字却读到非数字时返回 0
    - 遇到文件结尾返回 `EOF`，通常定义为 -1
    - 输入不匹配时，错误字符留在缓冲区

## `printf()` 的 `*` 修饰符

!!! abstract "语法形式"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int width, precision;
        double weight = 242.5;

        scanf("%d %d", &width, &precision);
        printf("Weight = %*.*f\n", width, precision, weight);

        return 0;
    }
    ```

!!! example "输出"

    ```text
    Weight =  242.500
    ```

!!! note "说明"

    - 输入 `8 3` 时，宽度为 8，精度为 3
    - `*` 表示宽度或精度由参数给出
    - 参数顺序与 `*` 出现的顺序相同
    - 这些参数位于待打印值之前
    - `%*d` 只用参数给出宽度，精度仍取默认值

## `scanf()` 的 `*` 修饰符

!!! abstract "语法形式"

    ```c
    int n;

    scanf("%*d %*d %d", &n);
    printf("%d\n", n);
    ```

!!! example "输出"

    ```text
    2015
    ```

!!! note "说明"

    - 输入 `2013 2014 2015` 时，前两项读取后丢弃
    - `*` 表示抑制赋值，不写入任何变量
    - 跳过的项不计入返回值
    - 适合读取文件中固定列的数据

## 复习题

（1）再次运行程序清单 4.1，要求输入名时输入名和姓 (中间有一个空格)，会发生什么？ 为什么？

??? note "答案"

    程序不能正常运行
    第一个 `scanf()` 只读取名，姓留在输入缓冲区
    下一条 `scanf()` 读取重量时，从缓冲区中先读到姓
    `scanf()` 把姓当作体重，读取失败
    如果输入 `Lasha 144`，程序会把 144 当作体重

（2）假设下列示例都是完整程序的一部分，它们打印的结果分别是什么？
a. `printf("He sold the painting for $%2.2f.\n", 2.345e2);`

??? note "答案"

    `He sold the painting for $234.50.`

    b. `printf("%c%c%c\n", 'H', 105, '\41');`

    `Hi!`

    第 1 个字符是字符常量，第 2 个由十进制整数转换，第 3 个是八进制字符常量

    c.

    ```c
    #define Q "His Hamlet was funny without being vulgar."
    printf("%s\nhas %d characters.\n", Q, strlen(Q));
    ```

    ```text
    His Hamlet was funny without being vulgar.
    has 42 characters.
    ```

    d. `printf("Is %2.2e the same as %2.2f?\n", 1201.0, 1201.0);`

    `Is 1.20e+003 the same as 1201.00?`

（3）在第 2 题的 c 中，要输出包含双引号的字符串 Q，应如何修改？

??? note "答案"

    在格式字符串中使用 `\"`

    ```c
    printf("\"%s\"\nhas %d characters.\n", Q, strlen(Q));
    ```

（4）找出下面程序中的错误
```c
define B booboo
define X 10
main(int)
{
    int age;
    char name;
    printf("Please enter your first name.");
    scanf("%s", name);
    printf("All right, %c, what's your age?\n", name);
    scanf("%f", age);
    xp = age + X;
    printf("That's a %s! You must be at least %d.\n", B, xp);
    rerun 0;
}
```

??? note "答案"

    需要加入头文件，补上 `#` 和引号，声明所有变量，改正格式字符串与参数

    ```c
    #include <stdio.h>
    #define B "booboo"
    #define X 10
    int main(void)
    {
        int age;
        int xp;
        char name[40];

        printf("Please enter your first name.\n");
        scanf("%s", name);
        printf("All right, %s, what's your age?\n", name);
        scanf("%d", &age);
        xp = age + X;
        printf("That's a %s! You must be at least %d.\n", B, xp);
        return 0;
    }
    ```

（5）用 `BOOK`，`cost` 和 `percent` 构造 `printf()` 语句，打印指定内容
```c
printf("This copy of \"%s\" sells for $%0.2f.\n", BOOK, cost);
printf("That is %0.0f%% of list.\n", percent);
```

（6）打印下列各项内容要分别使用什么转换说明？
a. 一个字段宽度与位数相同的十进制整数

??? note "答案"

    `%d`

    b. 一个形如 `8A`，字段宽度为 4 的十六进制整数

    `%4X`

    c. 一个形如 `232.346`，字段宽度为 10 的浮点数

    `%10.3f`

    d. 一个形如 `2.33e+002`，字段宽度为 12 的浮点数

    `%12.2e`

    e. 一个字段宽度为 30，左对齐的字符串

    `%-30s`

（7）打印下面各项内容要分别使用什么转换说明？
a. 字段宽度为 15 的 `unsigned long` 类型整数

??? note "答案"

    `%15lu`

    b. 一个形如 `0x8a`，字段宽度为 4 的十六进制整数

    `%#4x`

    c. 一个形如 `2.33E+02`，字段宽度为 12，左对齐的浮点数

    `%-12.2E`

    d. 一个形如 `+232.346`，字段宽度为 10 的浮点数

    `%+10.3f`

    e. 一个字段宽度为 8 的字符串的前 8 个字符

    `%8.8s`

（8）打印下面各项内容要分别使用什么转换说明？
a. 一个字段宽度为 6，最少有 4 位数字的十进制整数

??? note "答案"

    `%6.4d`

    b. 一个在参数列表中给定字段宽度的八进制整数

    `%*o`

    c. 一个字段宽度为 2 的字符

    `%2c`

    d. 一个形如 `+3.13`，字段宽度等于数字中字符数的浮点数

    `%+0.2f`

    e. 一个字段宽度为 7，左对齐字符串中的前 5 个字符

    `%-7.5s`

（9）分别写出读取下列各输入行的 `scanf()` 语句，并声明语句中用到变量和数组
a. `101`

??? note "答案"

    ```c
    int dalmations;
    scanf("%d", &dalmations);
    ```

    b. `22.32 8.34E-09`

    ```c
    float kgs, share;
    scanf("%f%f", &kgs, &share);
    ```

    转换字符可以用 `e`，`f` 或 `g`
    除 `%c` 外，在 `%` 与转换字符之间加空格不影响结果

    c. `linguini`

    ```c
    char pasta[20];
    scanf("%s", pasta);
    ```

    d. `catch 22`

    ```c
    char action[20];
    int value;
    scanf("%s %d", action, &value);
    ```

    e. `catch 22`，但跳过 `catch`

    ```c
    int value;
    scanf("%*s %d", &value);
    ```

（10）什么是空白？

??? note "答案"

    空白包括空格，制表符和换行符
    C 用空白分隔记号
    `scanf()` 用空白分隔连续的输入项

（11）下面的语句有什么问题？ 如何修正？
```c
printf("The double type is %z bytes..\n", sizeof(double));
```

??? note "答案"

    `z` 是修饰符，不是转换字符
    修饰符后面还要加一个转换字符
    打印十进制数用 `%zu`
    打印十六进制数用 `%zx`

（12）假设要在程序中用圆括号代替花括号，以下方法是否可行？
```c
#define ( {
#define ) }
```

??? note "答案"

    不可行
    预处理器不能区分哪些圆括号应替换成花括号
    哪些圆括号不能替换

    ```c
    int main(void)
    (
        printf("Hello, O Great One!\n");
    )
    ```

    会被替换成

    ```c
    int main{void}
    {
        printf{"Hello, O Great One!\n"};
    }
    ```

## 编程练习

!!! question "编程练习"

    1. 编写一个程序，提示用户输入名和姓，然后以 `名,姓` 的格式打印

    2. 编写一个程序，提示用户输入名字，并执行以下操作

    a. 打印名字，包括双引号
    b. 在宽度为 20 的字段右端打印名字，包括双引号
    c. 在宽度为 20 的字段左端打印名字，包括双引号
    d. 在比姓名宽度宽 3 的字段中打印名字

    3. 编写一个程序，读取一个浮点数，先以小数点记数法打印，再以指数记数法打印

    a. 输出形如 `The input is 21.3 or 2.1e+001.`
    b. 输出形如 `The input is +21.290 or 2.129E+001.`

    4. 编写一个程序，提示用户输入身高 (单位： 英寸) 和姓名，按指定格式显示

    ```text
    Dabney, you are 6.208 feet tall
    ```

    使用 `float` 类型，用 `/` 作为除号
    也可以要求以厘米为单位输入，以米为单位显示

    5. 编写一个程序，提示用户输入下载速度 (Mb/s) 和文件大小 (MB)
    计算下载时间，1 字节等于 8 位
    使用 `float` 类型，用 `/` 作为除号
    按指定格式打印 3 个变量，小数点后保留两位

    ```text
    At 18.12 megabits per second, a file of 2.20 megabytes
    downloads in 0.97 seconds.
    ```

    6. 编写一个程序，先提示输入名，再提示输入姓
    在一行打印名和姓，下一行打印各自的字母数
    字母数分别与名和姓的结尾对齐

    ```text
    Melissa Honeybee
          7        8
    ```

    再打印一份，字母数与名和姓的开头对齐

    ```text
    Melissa Honeybee
    7       8
    ```

    7. 编写一个程序，把 `double` 变量设为 `1.0/3.0`，`float` 变量设为 `1.0/3.0`
    分别显示两次计算的结果各 3 次
    一次显示小数点后 6 位，一次 12 位，一次 16 位
    包含 `float.h`，显示 `FLT_DIG` 和 `DBL_DIG` 的值
    比较 `1.0/3.0` 的值与这些值是否一致

    8. 编写一个程序，提示用户输入旅行的里程和消耗的汽油量
    计算并显示每加仑汽油行驶的英里数，小数点后一位
    用 1 加仑约 3.785 升，1 英里约 1.609 千米
    把英里/加仑换算成升/100 公里，小数点后一位
    用 `#define` 或 `const` 定义两个转换系数
