# 第11章 字符串和字符串函数

## 字符串字面量

!!! abstract "语法形式"

    ```c
    "字符串内容"
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char greeting[50] = "Hello, and" " how are"
                            " you today!";
        printf("%s\n", greeting);
        printf("\"%s\"\n", "quoted");
        return 0;
    }
    ```

    输出：

    ```text
    Hello, and how are you today!
    "quoted"
    ```

!!! note "说明"

    - 用双引号括起的字符序列，编译器在末尾自动加入 `'\0'`
    - 相邻的字面量在编译时拼接，中间可以隔空白
    - 字面量存放在静态存储区，程序运行期间只存一份
    - 字面量视为指向首字符的指针，属于 `const` 数据

!!! warning "常见错误"

    - 用单引号写多字符常量，如 `'abc'`
    - 以为拼接字面量要用 `+`

## 字符串字面量的地址

!!! abstract "语法形式"

    ```c
    "字符串"    /* 表达式的值是指向首字符的指针 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        printf("%s, %p, %c\n",
               "We", "are", *"space farers");
        return 0;
    }
    ```

    输出：

    ```text
    We, 0x100000f61, s
    ```

!!! note "说明"

    - `%s` 按字符串输出，从首字符开始直到空字符
    - `%p` 输出字面量首字符的地址，具体值随系统变化
    - `*"space farers"` 取出首字符 `'s'`
    - 对字面量取下标，等价于对字符数组取下标

!!! warning "常见错误"

    - 以为 `*"abc"` 得到整个字符串
    - 用 `%s` 输出 `*"abc"`，类型不匹配

## 用字符串字面量初始化字符数组

!!! abstract "语法形式"

    ```c
    const char 数组名[容量] = "字符串";
    char 数组名[] = "字符串";
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        const char m1[40] = "Limit yourself.";
        char m2[] = "Hi";
        printf("%s\n", m1);
        printf("sizeof m2 = %zu\n", sizeof m2);
        m2[0] = 'h';
        puts(m2);
        return 0;
    }
    ```

    输出：

    ```text
    Limit yourself.
    sizeof m2 = 3
    hi
    ```

!!! note "说明"

    - 数组容量至少为字符串长度加 1，多出的位置存放 `'\0'`
    - 未使用的元素自动置 `0`
    - 省略容量时，编译器按字面量长度加 1 确定数组大小
    - 初始化把字面量的副本写入数组，数组内容可以修改
    - 数组大小只能由初始化列表确定，声明后不能再补

    ![图11.1 初始化数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00060.jpg)

!!! warning "常见错误"

    - 数组容量等于字符串长度，没有位置存放 `'\0'`
    - 声明为 `const` 后仍对数组元素赋值

## 字符数组名与首元素地址

!!! abstract "语法形式"

    ```c
    char 数组名[容量] = "字符串";
    数组名 == &数组名[0]
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char car[10] = "Tata";
        printf("%c %c\n", *car, *(car + 1));
        printf("%s\n", car + 1);
        return 0;
    }
    ```

    输出：

    ```text
    T a
    ata
    ```

!!! note "说明"

    - 数组名是首元素地址的别名，属于地址常量
    - `car + 1` 指向第 2 个元素，可以参与指针运算
    - 数组元素是变量，可以赋值，除非数组声明为 `const`
    - `++car` 与 `car = ...` 都不合法

!!! warning "常见错误"

    - 对数组名使用递增运算符
    - 把数组名当作可以改存的指针变量

## 指针指向字符串字面量

!!! abstract "语法形式"

    ```c
    const char *指针名 = "字符串";
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        const char *pt = "Something is pointing at me.";
        printf("%s\n", pt);
        printf("%c\n", *(pt + 4));
        pt += 10;
        puts(pt);
        return 0;
    }
    ```

    输出：

    ```text
    Something is pointing at me.
    t
    is pointing at me.
    ```

!!! note "说明"

    - 指针变量存放字面量首字符的地址
    - 指针本身可以修改，`pt++` 或 `pt += n` 合法
    - 指针指向的数据视为 `const`，不能通过指针改写
    - 初始化指针只复制地址，不复制字符

!!! warning "常见错误"

    - 声明为 `char *` 后改写字面量，行为未定义
    - 以为指针变量为字符串分配了独立的存储空间

## 数组与指针表示字符串的区别

!!! abstract "语法形式"

    ```c
    char 数组名[] = "字符串";        /* 内容是副本, 名字不可改 */
    const char *指针名 = "字符串";    /* 名字可改, 内容不可改 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char heart[] = "I love Tillie!";
        const char *head = "I love Millie!";
        head = heart;
        puts(head);
        heart[7] = 'M';
        puts(heart);
        return 0;
    }
    ```

    输出：

    ```text
    I love Tillie!
    I love Millie!
    ```

!!! note "说明"

    - 两者都可以用下标和指针加法访问字符
    - 只有指针可以递增，只有数组元素可以改写
    - `head = heart` 改变指针保存的地址，不复制字符串
    - 初始化数组时字符串有两份： 静态区一份，数组一份

!!! warning "常见错误"

    - 写 `heart = head`，数组名不是可修改的左值
    - 把 `head = heart` 当成字符串复制

## 字符串指针数组与二维字符数组

!!! abstract "语法形式"

    ```c
    const char *指针数组[行数] = {"字符串1", "字符串2", ...};
    char 二维数组[行数][列宽] = {"字符串1", "字符串2", ...};
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define LIM 3

    int main(void)
    {
        const char *pt[LIM] = {"Alpha", "Beta", "Gamma"};
        char ar[LIM][10] = {"Alpha", "Beta", "Gamma"};
        printf("%s %c\n", pt[1], pt[1][2]);
        printf("%s\n", ar[2]);
        printf("%zu %zu\n", sizeof pt, sizeof ar);
        return 0;
    }
    ```

    输出：

    ```text
    Beta t
    Gamma
    24 30
    ```

!!! note "说明"

    - 指针数组的每个元素是一个地址，字面量存放在静态区
    - 二维数组每行等宽，按最长字符串分配，空间利用率低
    - `pt[i]` 指向字面量，内容不能修改
    - `ar[i]` 是数组，内容可以修改
    - 上一行输出按 64 位系统计算，指针占 8 字节

    ![图11.2 矩形数组和不规则数组](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00061.jpg)

!!! warning "常见错误"

    - 列宽等于最长字符串长度，没有位置存放 `'\0'`
    - 用指针数组保存需要修改的输入字符串

## 指针赋值不复制字符串

!!! abstract "语法形式"

    ```c
    指针2 = 指针1;    /* 只复制地址 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        const char *mesg = "Don't be a fool!";
        const char *copy = mesg;
        printf("%p %p\n", (void *)mesg, (void *)copy);
        puts(copy);
        puts(mesg + 6);
        return 0;
    }
    ```

    输出：

    ```text
    0x100000f50 0x100000f50
    Don't be a fool!
    be a fool!
    ```

!!! note "说明"

    - 两个指针保存同一地址，指向同一个字符串
    - 指针的地址 `&mesg` 与指针保存的地址 `mesg` 不同
    - 需要独立副本时使用 `strcpy()` 或 `strncpy()`
    - 复制地址比复制整个数组快，但两者共享数据

!!! warning "常见错误"

    - 把 `copy = mesg` 当成字符串复制
    - 输出指针值时混用 `&mesg` 与 `mesg`

## 为字符串输入分配空间

!!! abstract "语法形式"

    ```c
    char 数组名[容量];
    scanf("%s", 数组名);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char name[81];
        printf("Enter a name: ");
        scanf("%80s", name);
        printf("Hello, %s\n", name);
        return 0;
    }
    ```

    输出：

    ```text
    Enter a name: Ada
    Hello, Ada
    ```

!!! note "说明"

    - 读入前必须先分配空间，数组声明给出容量
    - 数组名本身就是首元素地址，传入 `scanf()` 时不加 `&`
    - 未初始化的 `char *` 不能让 `scanf()` 写入
    - 字段宽度取容量减 1，留一个位置给 `'\0'`

!!! warning "常见错误"

    - `char *name; scanf("%s", name);` 写入未知地址
    - `scanf("%s", &name)` 类型不匹配

## gets() 函数

!!! abstract "语法形式"

    ```c
    char *gets(char *s);    /* C11 起从标准中移除 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char words[81];
        puts("Enter a string:");
        gets(words);
        printf("[%s]\n", words);
        return 0;
    }
    ```

    输出：

    ```text
    Enter a string:
    I want to learn
    [I want to learn]
    ```

!!! note "说明"

    - 读取整行输入，丢弃换行符，末尾补 `'\0'`
    - 只接收一个参数，无法知道数组容量
    - 输入过长时继续写入，造成缓冲区溢出
    - [C99 起标记为废弃，C11 起从标准中移除，部分编译器仍作为扩展支持]
    - 替代写法： `fgets(words, sizeof words, stdin)`，再删除末尾换行符

!!! warning "常见错误"

    - 在新标准下使用 `gets()`，编译失败或给出警告
    - 以为 `gets()` 会检查数组长度

## fgets() 与 fputs()

!!! abstract "语法形式"

    ```c
    char *fgets(char *s, int n, FILE *stream);
    int fputs(const char *s, FILE *stream);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define STLEN 14

    int main(void)
    {
        char words[STLEN];
        fgets(words, STLEN, stdin);
        puts(words);
        fputs(words, stdout);
        return 0;
    }
    ```

    输出：

    ```text
    apple pie

    apple pie
    ```

!!! note "说明"

    - 最多读入 `n-1` 个字符，或读到换行符为止
    - 换行符会存入字符串，这一点与 `gets()` 不同
    - 第 3 个参数为 `stdin` 时从键盘读取
    - `fputs()` 不在末尾追加换行符，与 `fgets()` 配对
    - 输入行比 `n-1` 短时，字符串末尾带着换行符

!!! warning "常见错误"

    - `fgets()` 之后用 `puts()` 输出，出现空行
    - 把字符串长度当作 `n` 传入

## fgets() 的返回值与读取循环

!!! abstract "语法形式"

    ```c
    while (fgets(s, n, stdin) != NULL)
        ...
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define STLEN 10

    int main(void)
    {
        char words[STLEN];
        while (fgets(words, STLEN, stdin) != NULL
               && words[0] != '\n')
            fputs(words, stdout);
        puts("Done.");
        return 0;
    }
    ```

    输出：

    ```text
    By the way
    Done.
    ```

!!! note "说明"

    - 成功时返回第 1 个参数，读到文件结尾或出错时返回 `NULL`
    - 返回值可以与 `NULL` 比较，用于结束循环
    - 过长输入分多次读入，逐段输出可以拼回整行
    - 空行用 `words[0] == '\n'` 判断
    - `NULL` 是空指针宏，定义在 `stdio.h` 等头文件中

!!! warning "常见错误"

    - 不检查返回值，对 `NULL` 解引用
    - 把 `NULL` 与数字 `0` 或字符 `'0'` 混淆

## 删除换行符与丢弃多余输入

!!! abstract "语法形式"

    ```c
    while (s[i] != '\n' && s[i] != '\0')
        i++;
    if (s[i] == '\n')
        s[i] = '\0';
    else
        while (getchar() != '\n')
            continue;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char line[10];
        int i = 0;
        fgets(line, 10, stdin);
        while (line[i] != '\n' && line[i] != '\0')
            i++;
        if (line[i] == '\n')
            line[i] = '\0';
        else
            while (getchar() != '\n')
                continue;
        puts(line);
        return 0;
    }
    ```

    输出：

    ```text
    program s
    ```

!!! note "说明"

    - 循环定位换行符或空字符
    - 找到换行符时替换成 `'\0'`，字符串末尾不再带换行
    - 先遇到空字符说明输入被截断，用 `getchar()` 丢弃本行余下字符
    - 丢弃余下字符后，下一次读取从新的一行开始

!!! warning "常见错误"

    - 只删除换行符，不处理被截断的剩余字符
    - 截断时不清空输入，余下字符被下一次读取当作输入

## gets_s() 函数

!!! abstract "语法形式"

    ```c
    #define __STDC_WANT_LIB_EXT1__ 1
    char *gets_s(char *s, rsize_t n);    /* C11 可选 */
    ```

!!! example "示例"

    ```c
    #define __STDC_WANT_LIB_EXT1__ 1
    #include <stdio.h>

    int main(void)
    {
        char words[10];
        if (gets_s(words, sizeof words) == NULL)
            puts("Input too long or read error.");
        else
            puts(words);
        return 0;
    }
    ```

    输出：

    ```text
    hello
    hello
    ```

!!! note "说明"

    - 只从标准输入读取，不需要文件参数
    - 读到换行符时丢弃，与 `gets()` 相同
    - 输入超出容量时把首字符置 `'\0'`，丢弃该行剩余输入，返回 `NULL`
    - [属于 C11 附录 K 的可选扩展，编译器不一定提供]
    - 输入过长时的处理方式不如 `fgets()` 灵活

!!! warning "常见错误"

    - 在不支持附录 K 的编译器上直接使用
    - 忽略 `NULL` 返回值，继续使用未读入的数组

## 自定义 s_gets() 函数

!!! abstract "语法形式"

    ```c
    char *s_gets(char *st, int n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    char *s_gets(char *st, int n)
    {
        char *ret = fgets(st, n, stdin);
        int i = 0;
        if (ret)
        {
            while (st[i] != '\n' && st[i] != '\0')
                i++;
            if (st[i] == '\n')
                st[i] = '\0';
            else
                while (getchar() != '\n')
                    continue;
        }
        return ret;
    }

    int main(void)
    {
        char line[10];
        if (s_gets(line, 10))
            puts(line);
        return 0;
    }
    ```

    输出：

    ```text
    hello
    hello
    ```

!!! note "说明"

    - 组合 `fgets()` 与清行处理，返回值与 `fgets()` 相同
    - 读到 `NULL` 时跳过处理，直接返回
    - 有换行符时替换为 `'\0'`，没有换行符时丢弃该行剩余字符
    - 后续程序反复使用这一模式读取整行

!!! warning "常见错误"

    - 在 `ret` 为 `NULL` 时继续读写 `st`
    - 清行部分放在 `if` 外，对未读入的缓冲区调用 `getchar()`

## scanf() 读取字符串与字段宽度

!!! abstract "语法形式"

    ```c
    scanf("%Ns", 数组名);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char name1[11], name2[11];
        int count;
        count = scanf("%5s %10s", name1, name2);
        printf("%d %s %s\n", count, name1, name2);
        return 0;
    }
    ```

    输出：

    ```text
    2 Porte nsia
    ```

!!! note "说明"

    - `%s` 从第 1 个非空白字符开始，到下一个空白字符结束
    - 字段宽度限制读入字符数，可以防止溢出
    - 返回成功读取的项数，读到文件结尾返回 `EOF`
    - 只能读单词，不能读含空白的整行
    - 第 2 次读取从上次停止的位置继续

    ![图11.3 字段宽度和 scanf()](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00062.gif)

!!! warning "常见错误"

    - 不加字段宽度，输入过长时溢出
    - 用 `scanf("%s")` 读取姓名或书名

## puts() 函数

!!! abstract "语法形式"

    ```c
    int puts(const char *s);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char str1[80] = "An array was initialized to me.";
        const char *str2 = "A pointer was initialized to me.";
        puts(&str1[5]);
        puts(str2 + 4);
        return 0;
    }
    ```

    输出：

    ```text
    ray was initialized to me.
    inter was initialized to me.
    ```

!!! note "说明"

    - 输出直到空字符为止，并追加一个换行符
    - 参数是字符串地址，数组名与字面量都可以
    - 从中间开始输出时，传入中间字符的地址
    - 字符串缺少 `'\0'` 时会继续输出后面的内存

!!! warning "常见错误"

    - 对缺少空字符的字符数组使用 `puts()`
    - 以为 `puts()` 会自动截断到数组长度

## fputs() 函数

!!! abstract "语法形式"

    ```c
    int fputs(const char *s, FILE *stream);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        fputs("no newline", stdout);
        fputs(" here\n", stdout);
        return 0;
    }
    ```

    输出：

    ```text
    no newline here
    ```

!!! note "说明"

    - 第 2 个参数指定输出文件，显示器用 `stdout`
    - 不在末尾追加换行符
    - 与 `fgets()` 配对，输出保留输入中的换行符
    - `gets()` 与 `puts()` 配对，`fgets()` 与 `fputs()` 配对

!!! warning "常见错误"

    - 用 `fputs()` 后忘记换行，多行输出挤在一行
    - 把 `stdout` 写成 `stdin`

## printf() 输出字符串

!!! abstract "语法形式"

    ```c
    printf("%s\n", 字符串地址);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char name[] = "Ada";
        printf("Well, %s, %s\n", name, "welcome");
        return 0;
    }
    ```

    输出：

    ```text
    Well, Ada, welcome
    ```

!!! note "说明"

    - `printf()` 不自动追加换行符，需要在格式串中写 `\n`
    - `printf("%s\n", s)` 与 `puts(s)` 效果相同
    - 可以在同一行组合多个字符串与其他类型
    - 执行开销略大于 `puts()`

!!! warning "常见错误"

    - 漏写 `\n`，后续输出接在同一行

## 自定义字符串输出函数

!!! abstract "语法形式"

    ```c
    void put1(const char *string);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    void put1(const char *string)
    {
        while (*string)
            putchar(*string++);
    }

    int main(void)
    {
        put1("pizza");
        putchar('\n');
        return 0;
    }
    ```

    输出：

    ```text
    pizza
    ```

!!! note "说明"

    - 以空字符作为结束标志，不需要长度参数
    - `*string++` 先取当前字符，再让指针后移
    - 后缀 `++` 的值是旧值，因此解引用的是当前字符
    - `while (*string)` 等价于 `while (*string != '\0')`
    - 参数用 `const char *`，表示函数不修改字符串

!!! warning "常见错误"

    - 写成 `while (string)`，条件恒为真，循环不终止
    - 忘记 `const`，使函数可以改写字面量

## 返回字符数的输出函数

!!! abstract "语法形式"

    ```c
    int put2(const char *string);    /* 返回输出字符数 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int put2(const char *string)
    {
        int count = 0;
        while (*string)
        {
            putchar(*string++);
            count++;
        }
        putchar('\n');
        return count;
    }

    int main(void)
    {
        printf("count = %d\n", put2("pizza"));
        return 0;
    }
    ```

    输出：

    ```text
    pizza
    count = 5
    ```

!!! note "说明"

    - 计数器在循环内递增，空字符不计入
    - 返回值可以在调用处参与表达式
    - 嵌套调用时先执行实参 `put2()`，再执行 `printf()`
    - 换行符不计入字符数

!!! warning "常见错误"

    - 把 `count` 声明在循环内，每次迭代都重置
    - 把末尾换行符也计入字符数

## strlen() 函数

!!! abstract "语法形式"

    ```c
    size_t strlen(const char *s);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        char mesg[] = "Things should be simple.";
        printf("%zu\n", strlen(mesg));
        mesg[6] = '\0';
        puts(mesg);
        return 0;
    }
    ```

    输出：

    ```text
    24
    Things
    ```

!!! note "说明"

    - 返回空字符之前的字符数，不包括 `'\0'`
    - 从头扫描到空字符确定长度，不检查数组边界
    - 截短字符串只需在目标位置写入 `'\0'`
    - 写入 `'\0'` 后的字符仍留在数组中
    - `size_t` 是无符号整数类型，输出用 `%zu`

    ![图11.4 puts() 函数和空字符](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00063.jpg)

!!! warning "常见错误"

    - 把返回值当作数组容量
    - 对缺少空字符的数组调用 `strlen()`

## strcat() 函数

!!! abstract "语法形式"

    ```c
    char *strcat(char *s1, const char *s2);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        char flower[80] = "Rose";
        char addon[] = "s smell like old shoes.";
        strcat(flower, addon);
        puts(flower);
        puts(addon);
        return 0;
    }
    ```

    输出：

    ```text
    Roses smell like old shoes.
    s smell like old shoes.
    ```

!!! note "说明"

    - 从 `s1` 的空字符处开始追加 `s2`，覆盖原有的 `'\0'`
    - 返回 `s1`
    - `s2` 保持不变
    - 不检查 `s1` 的剩余空间，可能溢出
    - 调用者负责确认 `s1` 能容纳两个字符串加空字符

!!! warning "常见错误"

    - 目标数组空间不足，追加后溢出
    - 以为 `strcat()` 会分配新空间

## strncat() 函数

!!! abstract "语法形式"

    ```c
    char *strncat(char *s1, const char *s2, size_t n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>
    #define BUGSIZE 13

    int main(void)
    {
        char bug[BUGSIZE] = "Aphid";
        char addon[] = "s smell like old shoes.";
        int available = BUGSIZE - strlen(bug) - 1;
        strncat(bug, addon, available);
        puts(bug);
        return 0;
    }
    ```

    输出：

    ```text
    Aphids smell
    ```

!!! note "说明"

    - 最多追加 `n` 个字符，或遇到 `s2` 的空字符时停止
    - 总会在追加内容末尾补一个 `'\0'`
    - `n` 是追加字符数上限，不是目标数组总容量
    - 剩余空间按目标容量减去原字符串长度与空字符计算

!!! warning "常见错误"

    - 把 `n` 当作目标数组容量
    - 忘记为空字符留一个位置

## strcmp() 函数

!!! abstract "语法形式"

    ```c
    int strcmp(const char *s1, const char *s2);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        printf("%d %d %d\n",
               strcmp("A", "A") == 0,
               strcmp("A", "B") < 0,
               strcmp("B", "A") > 0);
        if (strcmp("quit", "quit") == 0)
            puts("equal");
        return 0;
    }
    ```

    输出：

    ```text
    1 1 1
    equal
    ```

!!! note "说明"

    - 相等返回 `0`，`s1` 在前返回负数，`s1` 在后返回正数
    - 具体返回值由实现决定，只保证符号，不保证为 `±1`
    - 按字符编码逐一比较，到不同字符或空字符为止
    - 比较的是字符串内容，不是地址
    - 数组大小不影响比较，比较在空字符处结束

!!! warning "常见错误"

    - 写 `if (s1 == s2)` 比较地址
    - 写 `if (strcmp(s1, s2) == 1)` 依赖具体返回值

## strncmp() 函数

!!! abstract "语法形式"

    ```c
    int strncmp(const char *s1, const char *s2, size_t n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        const char *list[] = {"astronomy", "astounding",
                              "astrophysics", "ostracize"};
        int i;
        for (i = 0; i < 4; i++)
            if (strncmp(list[i], "astro", 5) == 0)
                puts(list[i]);
        return 0;
    }
    ```

    输出：

    ```text
    astronomy
    astrophysics
    ```

!!! note "说明"

    - 最多比较 `n` 个字符，到不同字符或空字符时停止
    - 适合比较前缀，例如查找以 `astro` 开头的字符串
    - 返回值规则与 `strcmp()` 相同
    - `n` 超过字符串长度时，比较到空字符为止

!!! warning "常见错误"

    - 用 `strcmp()` 比较前缀，后续字符不同导致判断错误
    - 把 `n` 设得过大而越过空字符

## strcpy() 函数

!!! abstract "语法形式"

    ```c
    char *strcpy(char *s1, const char *s2);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>
    #define SIZE 40

    int main(void)
    {
        char copy[SIZE] = "Be the best that you can be.";
        const char *orig = "beast";
        char *ps = strcpy(copy + 7, orig);
        puts(copy);
        puts(ps);
        return 0;
    }
    ```

    输出：

    ```text
    Be the beast
    beast
    ```

!!! note "说明"

    - 把 `s2` 连同空字符复制到 `s1`
    - 返回 `s1`
    - 第 1 个参数不必是数组开头，可以复制到中间位置
    - 不检查目标空间，目标数组必须足够大
    - 第 1 个参数是目标，第 2 个参数是源

    ![图11.5 使用指针strcpy](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00064.jpg)

!!! warning "常见错误"

    - 目标指针未初始化，如 `char *str; strcpy(str, "...");`
    - 目标数组小于源字符串长度加 1

## strncpy() 函数

!!! abstract "语法形式"

    ```c
    char *strncpy(char *s1, const char *s2, size_t n);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>
    #define TARGSIZE 7

    int main(void)
    {
        char word[TARGSIZE];
        strncpy(word, "quadratic", TARGSIZE - 1);
        word[TARGSIZE - 1] = '\0';
        puts(word);
        return 0;
    }
    ```

    输出：

    ```text
    quadra
    ```

!!! note "说明"

    - 最多复制 `n` 个字符
    - 源字符串长度小于 `n` 时，复制整个字符串并补空字符
    - 源字符串长度不小于 `n` 时不复制空字符，目标不一定以空字符结尾
    - 常见做法： `n` 取容量减 1，再手工补 `'\0'`

!!! warning "常见错误"

    - 复制后直接当字符串使用，没有补 `'\0'`
    - 把 `n` 设为数组容量，无法保证以空字符结尾

## sprintf() 函数

!!! abstract "语法形式"

    ```c
    int sprintf(char *s, const char *format, ...);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char formal[50];
        sprintf(formal, "%s, %-8s: $%6.2f\n",
                "von Wurstkasse", "Annie", 25000.0);
        fputs(formal, stdout);
        return 0;
    }
    ```

    输出：

    ```text
    von Wurstkasse, Annie   : $25000.00
    ```

!!! note "说明"

    - 把格式化结果写入字符串，不输出到屏幕
    - 第 1 个参数是目标字符串地址
    - 其余参数与 `printf()` 相同
    - 声明在 `stdio.h`，不在 `string.h`
    - 不检查目标空间，需要自行确认足够大

!!! warning "常见错误"

    - 目标数组小于格式化结果
    - 以为 `sprintf()` 自动分配空间

## strchr() 与其他查找函数

!!! abstract "语法形式"

    ```c
    char *strchr(const char *s, int c);
    ```

    表11-1 string.h 常用查找函数

    | 函数原型 | 返回值 |
    | --- | --- |
    | `char *strchr(const char *s, int c);` | 指向 `c` 首次出现的位置，未找到返回空指针 |
    | `char *strrchr(const char *s, int c);` | 指向 `c` 最后一次出现的位置，未找到返回空指针 |
    | `char *strstr(const char *s1, const char *s2);` | 指向 `s2` 首次出现的位置，未找到返回空指针 |
    | `char *strpbrk(const char *s1, const char *s2);` | 指向 `s1` 中任一 `s2` 字符首次出现的位置，未找到返回空指针 |

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        char line[80];
        char *find;
        fgets(line, 80, stdin);
        find = strchr(line, '\n');
        if (find)
            *find = '\0';
        puts(line);
        return 0;
    }
    ```

    输出：

    ```text
    hello
    hello
    ```

!!! note "说明"

    - 查找范围包括字符串末尾的空字符
    - 未找到时返回空指针，调用处必须检查
    - `strchr()` 的结果可直接用于替换字符
    - 用 `strchr()` 替换换行符，与 `s_gets()` 的循环等价

    [教材原文对 `strpbrk()` 写 "返回空字符"，本笔记写 "返回空指针"，
    - 依据： C 标准与 man-pages 中 `strpbrk()` 未找到匹配时返回 `NULL`]

## 字符串排序

!!! abstract "语法形式"

    ```c
    void stsrt(char *strings[], int num);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <string.h>
    #define N 4
    #define SIZE 20

    void stsrt(char *strings[], int num)
    {
        char *temp;
        int top, seek;
        for (top = 0; top < num - 1; top++)
            for (seek = top + 1; seek < num; seek++)
                if (strcmp(strings[top], strings[seek]) > 0)
                {
                    temp = strings[top];
                    strings[top] = strings[seek];
                    strings[seek] = temp;
                }
    }

    int main(void)
    {
        char input[N][SIZE] = {"pear", "apple", "fig", "banana"};
        char *pt[N];
        int i;
        for (i = 0; i < N; i++)
            pt[i] = input[i];
        stsrt(pt, N);
        for (i = 0; i < N; i++)
            puts(pt[i]);
        return 0;
    }
    ```

    输出：

    ```text
    apple
    banana
    fig
    pear
    ```

!!! note "说明"

    - 排序的是指针数组，不移动字符串本身
    - 交换两个指针比用 `strcpy()` 交换字符串内容简单
    - 选择排序： 外层确定位置，内层在剩余元素中找最小者
    - `input` 中的原始顺序保持不变
    - 字符串仍由 `strcmp()` 确定先后

    ![图11.6 排序字符串指针](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00065.jpg)

!!! warning "常见错误"

    - 交换字符串内容而不是指针，效率低且容易越界
    - 指针数组元素没有指向实际存储的字符串

## ctype.h 字符函数

!!! abstract "语法形式"

    ```c
    #include <ctype.h>
    int toupper(int c);
    int ispunct(int c);
    ```

    表11-2 ctype.h 常用字符函数

    | 函数 | 判断或转换 |
    | --- | --- |
    | `isalnum()` | 字母或数字 |
    | `isalpha()` | 字母 |
    | `isdigit()` | 十进制数字 |
    | `isspace()` | 空白字符 |
    | `ispunct()` | 标点符号 |
    | `isupper()` / `islower()` | 大写字母 / 小写字母 |
    | `toupper()` / `tolower()` | 转成大写 / 小写 |

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <ctype.h>

    int main(void)
    {
        char s[] = "Hello, World!";
        int i, punct = 0;
        for (i = 0; s[i] != '\0'; i++)
        {
            s[i] = toupper(s[i]);
            if (ispunct(s[i]))
                punct++;
        }
        printf("%s\n%d\n", s, punct);
        return 0;
    }
    ```

    输出：

    ```text
    HELLO, WORLD!
    2
    ```

!!! note "说明"

    - 函数参数与返回值都是 `int`，以便同时处理 `EOF`
    - 转换函数只对相应类别的字符生效，其他字符原样返回
    - 逐个字符处理，循环以空字符结束
    - 头文件 `ctype.h` 提供这一组函数的原型

!!! warning "常见错误"

    - 传入负值而不是 `unsigned char` 或 `EOF`，行为未定义
    - 以为 `toupper()` 能处理整个字符串

## 命令行参数

!!! abstract "语法形式"

    ```c
    int main(int argc, char *argv[]);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>

    int main(int argc, char *argv[])
    {
        int i;
        printf("argc = %d\n", argc);
        for (i = 0; i < argc; i++)
            printf("%d: %s\n", i, argv[i]);
        return 0;
    }
    ```

    输出：

    ```text
    argc = 4
    0: repeat
    1: Resistance
    2: is
    3: futile
    ```

!!! note "说明"

    - `argc` 是命令行字符串个数，包含程序名
    - `argv[0]` 指向程序名，`argv[1]` 起指向各个参数
    - `argv[0]` 的具体内容取决于调用方式，可能是程序名或完整路径
    - `argv` 也可声明为 `char **argv`
    - 双引号可把多个单词合成一个参数
    - 系统用空格分隔各个参数

    ![图11.7 命令行参数](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00066.jpg)

!!! warning "常见错误"

    - 直接访问 `argv[1]` 而不检查 `argc`
    - 把 `argc` 当作参数个数，忘记程序名

## atoi() 与 atof()，atol()

!!! abstract "语法形式"

    ```c
    int atoi(const char *s);
    long atol(const char *s);
    double atof(const char *s);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        int times, i;
        if (argc < 2 || (times = atoi(argv[1])) < 1)
            puts("Usage: program positive-number");
        else
            for (i = 0; i < times; i++)
                puts("Hello");
        return 0;
    }
    ```

    输出：

    ```text
    Hello
    Hello
    Hello
    ```

!!! note "说明"

    - 跳过前导空白，转换开头的数字部分
    - 无法转换时行为由实现决定，标准未定义，常见实现返回 `0`
    - 只报告结果，不报告停止位置，错误检测用 `strtol()`
    - `atof()` 返回 `double`，`atol()` 返回 `long`
    - 原型在 `stdlib.h`

!!! warning "常见错误"

    - 对非数字字符串调用 `atoi()` 并依赖返回值
    - 忘记检查 `argc` 就访问 `argv[1]`

## strtol() 函数

!!! abstract "语法形式"

    ```c
    long strtol(const char *nptr, char **endptr, int base);
    unsigned long strtoul(const char *nptr, char **endptr, int base);
    double strtod(const char *nptr, char **endptr);
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        char *end;
        long v;
        v = strtol("10atom", &end, 10);
        printf("%ld, stopped at %s (%d)\n", v, end, *end);
        v = strtol("10atom", &end, 16);
        printf("%ld, stopped at %s (%d)\n", v, end, *end);
        return 0;
    }
    ```

    输出：

    ```text
    10, stopped at atom (97)
    266, stopped at tom (116)
    ```

!!! note "说明"

    - `nptr` 是待转换字符串
    - `endptr` 是 `char *` 变量的地址，函数把停止位置的地址写入该变量
    - `base` 指定进制，支持 2 到 36，取 `0` 时自动识别
    - `endptr == nptr` 表示没有转换任何字符
    - `strtod()` 只按十进制转换，只需要两个参数

!!! warning "常见错误"

    - 把 `&end` 写成 `end`
    - 不检查 `endptr`，无法判断转换是否成功

## 复习题

（1）下面的字符串声明有什么问题？
```c
int main(void)
{
    char name[] = {'F', 'e', 's', 's' };
    ...
}
```

??? note "答案"

    初始化列表缺少 `'\0'`，得到的是字符数组而不是字符串，
    改为 `char name[] = "Fess";`，或在列表末尾补 `'\0'`

（2）下面的程序会打印什么？
```c
#include <stdio.h>
int main(void)
{
    char note[] = "See you at the snack bar.";
    char *ptr;
    ptr = note;
    puts(ptr);
    puts(++ptr);
    note[7] = '\0';
    puts(note);
    puts(++ptr);
    return 0;
}
```

??? note "答案"

    ```text
    See you at the snack bar.
    ee you at the snack bar.
    See you
    e you
    ```

（3）下面的程序会打印什么？
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char food [] = "Yummy";
    char *ptr;
    ptr = food + strlen(food);
    while (--ptr >= food)
        puts(ptr);
    return 0;
}
```

??? note "答案"

    ```text
    y
    my
    mmy
    ummy
    Yummy
    ```

（4）下面的程序会打印什么？
```c
#include <stdio.h>
#include <string.h>
int main(void)
{
    char goldwyn[40] = "art of it all ";
    char samuel[40] = "I read p";
    const char * quote = "the way through.";
    strcat(goldwyn, quote);
    strcat(samuel, goldwyn);
    puts(samuel);
    return 0;
}
```

??? note "答案"

    `I read part of it all the way through.`

（5）下面的练习涉及字符串，循环，指针和递增指针。 首先，假设定义了下面的函数：
```c
#include <stdio.h>
char *pr(char *str)
{
    char *pc;
    pc = str;
    while (*pc)
        putchar(*pc++);
    do {
        putchar(*--pc);
        } while (pc - str);
    return (pc);
}
```
考虑下面的函数调用：
```c
x = pr("Ho Ho Ho!");
```
a. 将打印什么？
b. `x` 是什么类型？
c. `x` 的值是什么？
d. 表达式 `*--pc` 是什么意思？ 与 `--*pc` 有何不同？
e. 如果用 `*pc--` 替换 `*--pc`，会打印什么？
f. 两个 `while` 循环用来测试什么？
g. 如果 `pr()` 函数的参数是空字符串，会怎样？
h. 必须在主调函数中做什么，才能让 `pr()` 函数正常运行？

??? note "答案"

    a. 输出 `Ho Ho Ho!!oH oH oH`
    b. `char *`，即指向 `char` 的指针
    c. 第 1 个 `H` 的地址
    d. `*--pc` 先把指针减 1，再取该位置的值； `--*pc` 先取 `pc` 指向的值，再把该值减 1
    e. 输出 `Ho Ho Ho!!oH oH o`; 两个 `!` 之间有一个空字符，通常不显示
    f. 第 1 个循环检查 `*pc` 是否为空字符，第 2 个循环检查 `pc - str` 是否为 0，
    即是否回到字符串开头
    g. `pc` 先指向空字符，再退到字符串首字符之前的位置，读取并输出该位置的内容，结束条件永不满足，
    循环不会停止
    h. 在主调函数中声明 `char *pr(char *);`

（6）假设有如下声明：
```c
char sign = '$';
```
`sign` 占用多少字节的内存？ `'$'` 占用多少字节的内存？ `"$"` 占用多少字节的内存？

??? note "答案"

    `sign` 占 1 字节，`'$'` 是字符常量，类型为 `int`，通常占 2 或 4 字节，
    `"$"` 占 2 字节，一个存 `'$'`，一个存 `'\0'`

（7）下面的程序会打印出什么？
```c
#include <stdio.h>
#include <string.h>
#define M1 "How are ya, sweetie? "
char M2[40] = "Beat the clock.";
char * M3 = "chat";
int main(void)
{
    char words[80];
    printf(M1);
    puts(M1);
    puts(M2);
    puts(M2 + 1);
    strcpy(words, M2);
    strcat(words, " Win a toy.");
    puts(words);
    words[4] = '\0';
    puts(words);
    while (*M3)
        puts(M3++);
    puts(--M3);
    puts(--M3);
    M3 = M1;
    puts(M3);
    return 0;
}
```

??? note "答案"

    ```text
    How are ya, sweetie? How are ya, sweetie?
    Beat the clock.
    eat the clock.
    Beat the clock. Win a toy.
    Beat
    chat
    hat
    at
    t
    t
    at
    How are ya, sweetie?
    ```

（8）下面的程序会打印出什么？
```c
#include <stdio.h>
int main(void)
{
    char str1 [] = "gawsie";
    char str2 [] = "bletonism";
    char *ps;
    int i = 0;
    for (ps = str1; *ps != '\0'; ps++) {
        if (*ps == 'a' || *ps == 'e')
            putchar(*ps);
        else
            (*ps)--;
        putchar(*ps);
        }
    putchar('\n');
    while (str2[i] != '\0') {
        printf("%c", i % 3 ? str2[i] : '*');
        ++i;
        }
    return 0;
}
```

??? note "答案"

    ```text
    faavrhee
    *le*on*sm
    ```

（9）本章定义的 `s_gets()` 函数，用指针表示法代替数组表示法便可减少一个变量 `i`. 请改写该函数

??? note "答案"

    ```c
    #include <stdio.h>
    char * s_gets(char * st, int n)
    {
        char * ret_val;

        ret_val = fgets(st, n, stdin);
        if (ret_val)
        {
            while (*st != '\n' && *st != '\0')
                st++;
            if (*st == '\n')
                *st = '\0';
            else
                while (getchar() != '\n')
                     continue;
        }
        return ret_val;
    }
    ```

（10）`strlen()` 函数接受一个指向字符串的指针作为参数，并返回该字符串的长度。 请编写一个这样的函数

??? note "答案"

    ```c
    int strlen(const char * s)
    {
        int ct = 0;
        while (*s++)
            ct++;
        return(ct);
    }
    ```

（11）本章定义的 `s_gets()` 函数，
可以用 `strchr()` 函数代替其中的 `while` 循环来查找换行符。 请改写该函数

??? note "答案"

    ```c
    #include <stdio.h>
    #include <string.h>
    char * s_gets(char * st, int n)
    {
        char * ret_val;
        char * find;
        ret_val = fgets(st, n, stdin);
        if (ret_val)
        {
            find = strchr(st, '\n');
            if (find)
                *find = '\0';
            else
                while (getchar() != '\n')
                     continue;
        }
        return ret_val;
    }
    ```

（12）设计一个函数，接受一个指向字符串的指针，返回指向该字符串第 1 个空格字符的指针，或如果未找到空格字符，
则返回空指针

??? note "答案"

    ```c
    #include <stdio.h>
    char * strblk(char * string)
    {
        while (*string != ' ' && *string != '\0')
            string++;
        if (*string == '\0')
            return NULL;
        else
            return string;
    }
    ```

（13）重写程序清单11.21，使用 `ctype.h` 头文件中的函数，以便无论用户选择大写还是小写，
该程序都能正确识别答案

??? note "答案"

    ```c
    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>
    #define ANSWER "GRANT"
    #define SIZE 40
    char * s_gets(char * st, int n);
    void ToUpper(char * str);

    int main(void)
    {
        char try[SIZE];
        puts("Who is buried in Grant's tomb?");
        s_gets(try, SIZE);
        ToUpper(try);
        while (strcmp(try, ANSWER) != 0)
        {
            puts("No, that's wrong. Try again.");
            s_gets(try, SIZE);
            ToUpper(try);
        }
        puts("That's right!");
        return 0;
    }

    void ToUpper(char * str)
    {
        while (*str != '\0')
        {
            *str = toupper(*str);
            str++;
        }
    }

    char * s_gets(char * st, int n)
    {
        char * ret_val;
        int i = 0;

        ret_val = fgets(st, n, stdin);
        if (ret_val)
        {
            while (st[i] != '\n' && st[i] != '\0')
                i++;
            if (st[i] == '\n')
                st[i] = '\0';
            else
                while (getchar() != '\n')
                     continue;
        }
        return ret_val;
    }
    ```

## 编程练习

!!! question "编程练习"

    1. 设计并测试一个函数，从输入中获取 `n` 个字符 (包括空白，制表符，换行符)，把结果储存在一个数组里，
       它的地址被传递作为一个参数

    2. 修改并编程练习 1 的函数，在 `n` 个字符后停止，或在读到第 1 个空白，制表符或换行符时停止，
       哪个先遇到哪个停止。 不能只使用 `scanf()`

    3. 设计并测试一个函数，从一行输入中把一个单词读入一个数组中，
       并丢弃输入行中的其余字符。 该函数应该跳过第 1 个非空白字符前面的所有空白。 将一个单词定义为没有空白，
       制表符或换行符的字符序列

    4. 设计并测试一个函数，它类似编程练习 3 的描述，只不过它接受第 2 个参数指明可读取的最大字符数

    5. 设计并测试一个函数，搜索第 1 个函数形参指定的字符串，
       在其中查找第 2 个函数形参指定的字符首次出现的位置。 如果成功，该函数返指向该字符的指针，
       如果在字符串中未找到指定字符，
       则返回空指针 (该函数的功能与 `strchr()` 函数相同). 在一个完整的程序中测试该函数，
       使用一个循环给函数提供输入值

    6. 编写一个名为 `is_within()` 的函数，
       接受一个字符和一个指向字符串的指针作为两个函数形参。 如果指定字符在字符串中，
       该函数返回一个非零值 (即为真). 否则，返回 `0` (即为假). 在一个完整的程序中测试该函数，
       使用一个循环给函数提供输入值

    7. `strncpy(s1, s2, n)` 函数把 `s2` 中的 `n` 个字符拷贝至 `s1` 中，
       截断 `s2`，或者有必要的话在末尾添加空字符。 如果 `s2` 的长度是 `n` 或多于 `n`,
       目标字符串不能以空字符结尾。 该函数返回 `s1`. 自己编写一个这样的函数，
       名为 `mystrncpy()`. 在一个完整的程序中测试该函数，使用一个循环给函数提供输入值

    8. 编写一个名为 `string_in()` 的函数，
       接受两个指向字符串的指针作为参数。 如果第 2 个字符串包含在第 1 个字符串中，
       该函数将返回第 1 个字符串开始的地址。 例如，
       `string_in("hats", "at")` 将返回 `hats` 中 `a` 的地址。 否则，
       该函数返回空指针。 在一个完整的程序中测试该函数，使用一个循环给函数提供输入值

    9. 编写一个函数，把字符串中的内容用其反序字符串代替。 在一个完整的程序中测试该函数，使用一个循环给函数提供输入值

    10. 编写一个函数接受一个字符串作为参数，并删除字符串中的空格。 在一个程序中测试该函数，使用循环读取输入行，
        直到用户输入一行空行。 该程序应该应用该函数读取每个输入的字符串，并显示处理后的结果

    11. 编写一个程序，
        读入 10 个字符串或者读到 `EOF` 时停止。 该程序为用户提供一个有 5 个选项的菜单： 打印源字符串列表，
        以 ASCII 中的顺序打印字符串，按长度递增顺序打印字符串，按字符串中第 1 个单词的长度打印字符串，
        退出。 菜单可以循环显示，除非用户选择退出选项。 当然，该程序要能真正完成菜单中各选项的功能

    12. 编写一个程序，读取输入，直至读到 `EOF`，报告读入的单词数，大写字母数，小写字母数，
        标点符号数和数字字符数。 使用 `ctype.h` 头文件中的函数

    13. 编写一个程序，反序显示命令行参数的单词。 例如，命令行参数是 `see you later`,
        该程序应打印 `later you see`

    14. 编写一个通过命令行运行的程序计算幂。 第 1 个命令行参数是 `double` 类型的数，作为幂的底数，
        第 2 个参数是整数，作为幂的指数

    15. 使用字符分类函数实现 `atoi()` 函数。 如果输入的字符串不是纯数字，该函数返回 `0`

    16. 编写一个程序读取输入，直至读到文件结尾，然后把字符串打印出来。 该程序识别和实现下面的命令行参数：

    ```c
    -p         按原样打印
    -u         把输入全部转换成大写
    -l         把输入全部转换成小写
    ```

    如果没有命令行参数，则让程序像是使用了 `-p` 参数那样运行
