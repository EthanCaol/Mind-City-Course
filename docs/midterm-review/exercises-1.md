---
icon: material/format-list-checks
---

# 期中复习习题 1

本页是课件《期中复习习题-1.pdf》的文字版。

## 一、选择题

### 第1题

结构化程序设计所规定的三种基本结构是

- A. 主程序、子程序、函数
- B. 树形、网形、环形
- C. 顺序、选择、循环
- D. 输入、处理、输出

??? note "答案"

    C

### 第2题

下列关于 C 语言的叙述错误的是

- A. 对大小写不敏感
- B. 不同类型的变量可以在一个表达式中
- C. main 函数可以写在程序文件的任何位置
- D. 同一个运算符号在不同的场合可以有不同的含义

??? note "答案"

    A

### 第3题

以下合法的实型常数是

- A. `.E4`
- B. `2.5E`
- C. `3.`
- D. `E7`

??? note "答案"

    C

### 第4题

(多选)能正确表示关系 `x>y≥z` 的 C 语言表达式是

- A. `x>y>=z`
- B. `(x>y)&(y>=z)`
- C. `(y<x)&&(y>=z)`
- D. `(x>y)and(y>=z)`

??? note "答案"

    B，C

### 第5题

有语句 `scanf("%d,%d", &a, &b)`，要使变量 a、b 分别得 23、45，则正确的输入形式为

- A. `23 45`
- B. `23,45`
- C. `23;45`
- D. `2345`

??? note "答案"

    B

### 第6题

已知 `int i=10;` 表达式 `20-0<=i<=9` 的值是

- A. `0`
- B. `1`
- C. `19`
- D. `20`

??? note "答案"

    B

### 第7题

已知 `int a=15`，执行语句 `a=a<<2` 以后，变量 a 的值是

- A. `20`
- B. `40`
- C. `60`
- D. `80`

??? note "答案"

    C

### 第8题

对二维数组的正确说明是

- A. `int a[][]={1,2,3,4,5,6}`
- B. `int a[2][]={1,2,3,4,5,6}`
- C. `int a[][3]={1,2,3,4,5,6}`
- D. `int a[2,3]={1,2,3,4,5,6}`

??? note "答案"

    C

### 第9题

若以下选项中的变量已正确定义，则正确的赋值语句是

- A. `x1=26.8%3`
- B. `1+2=x2`
- C. `x3=0x12`
- D. `x4=1+2=3`

??? note "答案"

    C

### 第10题

(多选)设有以下定义：

```c
#define d 2
int a = 0;
double b = 1.25;
char c = 'A';
```

则下面语句中错误的是

- A. `a++;`
- B. `b++`
- C. `c++;`
- D. `d++;`

??? note "答案"

    B，D

### 第11题

表达式 `5 % 3 + 5 / 3` 的值为

- A. `3`
- B. `4`
- C. `.666667`
- D. `4.666667`

??? note "答案"

    A

### 第12题

下面 C 程序的输出是

```c
int main()
{
    int m = 5;
    if (++m > 5)
        printf("%d\n", m);
    else
        printf("%d\n", --m);
}
```

- A. `4`
- B. `5`
- C. `6`
- D. `7`

??? note "答案"

    C

### 第13题

有以下程序：

```c
int main()
{
    char a, b, c, d;
    scanf("%c,%c,%d,%d", &a, &b, &c, &d);
    printf("%c,%c,%c,%c\n", a, b, c, d);
}
```

若运行时从键盘上输入 `6,5,65,66<回车>`，则输出结果是

- A. `6,5,A,B`
- B. `6,5,65,66`
- C. `6,5,6,5`
- D. `6,5,6,6`

??? note "答案"

    A

### 第14题

若变量已正确定义，要求程序段完成求 5! 的计算，不能完成此操作的程序段是

- A. `for(i=1,p=1;i<=5;i++) p*=i;`
- B. `for(i=1;i<=5;i++){ p=1; p*=i;}`
- C. `i=1;p=1;while(i<=5){p*=i; i++;}`
- D. `i=1;p=1;do{p*=i; i++; }while(i<=5);`

??? note "答案"

    B

### 第15题

有以下程序：

```c
int main()
{
    int i = 0, x = 0, s = 0;
    for (;;) {
        if (i == 3 || i == 5)
            continue;
        if (i == 6)
            break;
        i++;
        s += i;
    }
    printf("%d\n", s);
}
```

程序运行后的输出结果是

- A. `10`
- B. `13`
- C. `21`
- D. 程序进入死循环

??? note "答案"

    D

### 第16题

C 语言中的变量名只能由字母、数字和下划线三种字符组成，且第一个字符

- A. 必须为字母
- B. 必须为下划线
- C. 必须为字母或下划线
- D. 可以是字母、数字或下划线中的任意一种

??? note "答案"

    C

### 第17题

以下选项中可作为 C 语言合法常量的是

- A. `1.0u`
- B. `087`
- C. `-8e1.0`
- D. `0X15L`

??? note "答案"

    D

### 第18题

设有整型变量 a 的值为 2，则执行下列语句后，浮点型变量 b 的值不为 0.5 的是

- A. `b=1.0/a;`
- B. `b=(float)(1/a);`
- C. `b=1/(float)a;`
- D. `b=1/(a*1.0)`

??? note "答案"

    B

### 第19题

执行如下循环时，说法正确的是

```c
int x = -1;
do {
    x = x * x;
} while (x = 1);
```

- A. 循环体将执行一次
- B. 循环体将执行无限次
- C. 循环体不执行
- D. 系统将提示有语法错误

??? note "答案"

    B

### 第20题

以下能正确定义数组的选项是

- A. `char str[5] = {a, b, c, d, e};`
- B. `char str[5] = "abcde";`
- C. `char str[5] = {'a', 'b', 'c', 'd', 'e'};`
- D. 以上都不可以

??? note "答案"

    C

## 二、填空题

### 第1题

设有定义 `int a=-1, b=0, c=3;`，则表达式 `++a || b++ && ++c` 运算后 c 的值为

??? note "答案"

    3

### 第2题

写出描述“x 和 y 中有且仅有一个大于 z”的 C 表达式

??? note "答案"

    x>z!=y>z

### 第3题

设有定义 `int x=8, y=4, z=1;`，执行语句 `z+=x>y>z;` 之后变量 z 的值为

??? note "答案"

    1

### 第4题

设有定义 `char a[] = { '1', '2', '\n', '\0', '5', '6','\0' }; int s=0;`，执行语句 `s=strlen(a);` 之后变量 s 的值为

??? note "答案"

    3

### 第5题

以下程序运行所产生的输出是

```c
#include <stdio.h>
int main()
{
    int i = 0, v1 = 0, v2 = 1, v3 = 2;
    for (i = 1; i < 10; i++) {
        switch (i % 4) {    /* 1, 2, 3, 0, 1, 2, 3, 0, 1 */
        case 1: v1++;
        case 2: v2++; break;
        default: v3++;
        }
    }
    printf("%d,%d,%d\n", v1, v2, v3);
    return 0;
}
```

??? note "答案"

    3, 6, 6

## 三、问答题

### 第1题

有以下程序：

```c
int main( )
{
    char k;
    int i;
    for (i = 1; i < 3; i++) {
        scanf("%c", &k);
        switch (k) {
        case '0': printf("another\n");
        case '1': printf("number\n");
        }
    }
}
```

程序运行时，从键盘输入 `01<回车>`，程序执行后的输出结果是

??? note "答案"

    ```text
    another
    number
    number
    ```

### 第2题

以下程序的功能是什么？

```c
int main( )
{
    int i, s = 0;
    for (i = 1; i < 10; i += 2)
        s += i+1;
    printf("%d\n", s);
}
```

??? note "答案"

    小于等于 10 的偶数之和

### 第3题

以下程序的功能是什么？

```c
#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    printf("a=%d,b=%d\n", a, b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("a=%d,b=%d\n", a, b);
}
```

??? note "答案"

    交换两个整数

### 第4题

以下程序段的输出结果是

```c
int a = 10, b = 50, c = 30;
if (a > b)
    a = b;
b = c;
c = a;
printf("a=%d b=%d c=%d\n", a, b, c);
```

??? note "答案"

    a=10 b=30 c=10

### 第5题

以下程序运行所产生的输出是

```c
#include <stdio.h>
int factorial(int n)
{
    int ret;
    printf("ENTER: %d\n", n);
    if (n == 0 || n == 1)
        ret = 1;
    else
        ret = n * factorial(n-1);
    printf("EXIT: %d\n", n);
    return ret;
}
int main()
{
    printf("fac(%d)=%d\n", 4, factorial(4));
    return 0;
}
```

??? note "答案"

    ```text
    Enter: 4
    Enter: 3
    Enter: 2
    Enter: 1
    Exit: 1
    Exit: 2
    Exit: 3
    Exit: 4
    fac(4)=24
    ```

### 第6题

若 c 已经正确定义，`while(( c = getchar()) != '\n');` 语句的功能是

??? note "答案"

    从键盘输入字符，直到输入为回车时停止

### 第7题

输入 `3<回车>` 后，下列程序的输出结果是

```c
#include <stdio.h>
int main()
{
    int i, j, n, temp, a[6][6];
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            a[i][j] = j + i * n;
    for (i = 0; i < n; i++)
        for (j = 0; j < n / 2; j++) {
            temp = a[n - j - 1][i];
            a[n - j - 1][i] = a[i][j];
            a[i][j] = temp;
        }
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%2d", a[i][j]);
        printf("#");
    }
    return 0;
}
```

??? note "答案"

    6 1 2# 7 4 5# 8 3 0#

## 四、改错题

### 第1题

以下程序将输入的数字字符序列转换成十进制整数，输出转换结果。注意：不得增行或删行，也不得更改程序结构。

```c
/* 1 */ #include <stdio.h>
/* 2 */ #define N 10;
/* 3 */ int main()
/* 4 */ {
/* 5 */     char s[N], c;
/* 6 */     int i, n;
/* 7 */     scanf("%s", &s);
/* 8 */     for (i = 0; s[i] >= 0 && s[i] <= 9; i++)
/* 9 */         n = n * 10 + s[i];
/* 10 */    printf("%d\n", n);
/* 11 */    return 0;
/* 12 */ }
```

??? note "答案"

    ```c
    /* 1 */ #include <stdio.h>
    /* 2 */ #define N 10
    /* 3 */ int main()
    /* 4 */ {
    /* 5 */     char s[N], c;
    /* 6 */     int i, n = 0;
    /* 7 */     scanf("%s", s);
    /* 8 */     for (i = 0; s[i] >= '0' && s[i] <= '9'; i++)
    /* 9 */         n = n * 10 + s[i] - '0';
    /* 10 */    printf("%d\n", n);
    /* 11 */    return 0;
    /* 12 */ }
    ```

### 第2题

S=1-1/2+1/3-1/4+1/5-1/6+…，以下程序输入正整数 n，计算并输出 s 前 n 项的和。

```c
/* 13 */ #include <stdio.h>
/* 14 */ int main( )
/* 15 */ {
/* 16 */     int i, j, n;
/* 17 */     double t, s;
/* 18 */     scanf("%d", &n);
/* 19 */     for (i = j = 1; i <= n; i++)
/* 20 */     {
/* 21 */         t = j/i;
/* 22 */         s = s + t;
/* 23 */         j = -j;
/* 24 */     }
/* 25 */     printf("sum = %lf\n", s);
/* 26 */     return 0;
/* 27 */ }
```

??? note "答案"

    ```c
    /* 13 */ #include <stdio.h>
    /* 14 */ int main( )
    /* 15 */ {
    /* 16 */     int i, j, n;
    /* 17 */     double t, s = 0;
    /* 18 */     scanf("%d", &n);
    /* 19 */     for (i = j = 1; i <= n; i++)
    /* 20 */     {
    /* 21 */         t = (double) j/i;
    /* 22 */         s = s + t;
    /* 23 */         j = -j;
    /* 24 */     }
    /* 25 */     printf("sum = %lf\n", s);
    /* 26 */     return 0;
    /* 27 */ }
    ```

## 五、补全题

### 第1题

给定十进制正整数 n（n>=2），函数 maxZeros 返回整数 k（k>=2），当 n 在 k 进制表示时有最多的 0，如果有多个答案，输出最小的 k。例如：十进制正整数 31 的三进制表示有一个 0，三十一进制表示也有一个 0，则函数返回 3。函数定义如下：

```c
int maxZeros(int n)
{
    int m, value, answer = 0, max = 0;
    for (int k = 2; k <= n; k++) {
        m = 0;
        (1)
        ;
        while (value) {
            if (value % k == 0)
                m++;
            (2)
            ;
        }
        if (
            (3)
        ) {
            max = m;
            answer = k;
        }
    }
    return answer;
}
```

??? note "答案"

    ```c
    int maxZeros(int n)
    {
        int m, value, answer = 0, max = 0;
        for (int k = 2; k <= n; k++) {
            m = 0;
            value = n;
            while (value) {
                if (value % k == 0)
                    m++;
                value /= k;
            }
            if (m > max) {
                max = m;
                answer = k;
            }
        }
        return answer;
    }
    ```

### 第2题

假设整数数组 a[N] 的元素已按从小到大顺序排序，用二分法查找 key 的程序段如下。若找到 key，返回 key 在数组中的下标，否则返回 -1。

```c
int low = 0, high = N - 1, k;
while (
    (4)
) {
    k = (low + high) / 2;
    if (
        (5)
    )
        return k;
    else if (
        (6)
    )
        high = k-1;
    else
        low = k+1;
}
(7)
;
```

??? note "答案"

    ```c
    int low = 0, high = N - 1, k;
    while (low <= high) {
        k = (low + high) / 2;
        if (a[k] == key)
            return k;
        else if (key < a[k])
            high = k-1;
        else
            low = k+1;
    }
    return -1;
    ```

### 第3题

读入一个字符串，将该字符串中的所有字符按 ASCII 码降序排序后输出，使用冒泡法排序。例如：若输入 dafhc，则输出 hfdca。

```c
#include<stdio.h>
#include<string.h>
#define N 100
int main()
{
    int i, j, n;
    char s[N], c;
    gets(s);
    n = strlen(s);
    for (i = 1;
         (8)
         ; i++)
        for (j = 0;
             (9)
             ; j++)
            if (
                (10)
            ) {
                c = s[j];
                s[j] = s[j+1];
                s[j+1] = c;
            }
    puts(s);
    return 0;
}
```

??? note "答案"

    ```c
    #include<stdio.h>
    #include<string.h>
    #define N 100
    int main()
    {
        int i, j, n;
        char s[N], c;
        gets(s);
        n = strlen(s);
        for (i = 1; i < n; i++)
            for (j = 0; j < n-i; j++)
                if (s[j] < s[j+1]) {
                    c = s[j];
                    s[j] = s[j+1];
                    s[j+1] = c;
                }
        puts(s);
        return 0;
    }
    ```

## 六、编程题

### 第1题

读取两个字符串，并将它们连接起来而不用到 strcat 函数（假设两个字符串 str1、str2 分别存储在两个长度为 100 的字符数组里，且 str1 的数组足够容纳 str2 的内容）。

??? note "答案"

    ```c
    #include <stdio.h>
    void main()
    {
        int i = 0, j = 0;
        char str1[100], str2[100];
        gets(str1);
        gets(str2);
        // move to the end character '\0' of str1
        for (; str1[i] != '\0'; i++)
            ;
        // copy characters in str2 to str1 until '\0'
        while (str2[j] != '\0') {
            str1[i++] = str2[j++];
        }
        // end str1 with '\0'
        str1[i] = '\0';
        printf("%s\n", str1);
    }
    ```

### 第2题

实现直接插入排序算法。

算法思想：将序列中的数据一个个插入。当插入第 i（i≥1）个对象时，前面的 V[0]，V[1]，…，V[i-1] 个数据已经排好序，这时，用 V[i] 与 V[i-1]，V[i-2]，…顺序进行比较，找到插入位置即将 V[i] 插入，原来位置上的对象向后顺移。

??? note "答案"

    ```c
    void InsertionSort(int a[], int size)
    {
        for (int i = 1; i < size; i++) {
            int temp = a[i];
            int j = i - 1;
            while (j >= 0 && temp < a[j]) {
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = temp;
        }
    }
    void main()
    {
        int array[5] = {8, 9, 28, 11, 23};
        InsertionSort(array, 5);
        for (int i = 0; i < 5; i++) {
            printf("%d ", array[i]);
        }
        printf("\n");
    }
    ```

### 第3题

编写程序，输入一个正整数 n，输出所有只改变一位数字而获得的更大整数。例：

```text
输入：10
输出：11  12  13  14  15  16  17  18  19  20  30  40  50  60  70  80  90
```

??? note "答案"

    ```c
    #include <stdio.h>
    #define N 10
    int main()
    {
        int i, j;
        int n, m, a[N] = {0}, len;
        scanf("%d", &n);
        i = 0;
        while (n) {     // 把 n 的每位数值取出保存在数组中
            a[i++] = n % 10;
            n /= 10;
        }
        len = i;
        // n 的位数
        for (i = 0; i < len; ++i) {
            // 修改每个位数, 获得更大的数
            m = a[i];
            // 保存当前位数的值
            for (++a[i]; a[i] < 10; ++a[i]) {
                // 改变当前位数值
                n = 0;
                for (j = len-1; j >= 0; --j)
                    // 生成每个更大的数
                    n = n*10 + a[j];
                printf("%d\t", n);
            }
            a[i] = m;
            // 恢复原来的位数值
            printf("\n");
        }
        return 0;
    }
    ```

### 第4题

编写程序，输入两个字符串 str1 和 str2，删除 str1 中所有在 str2 出现的字符，输出处理后的 str1。要求：不能使用工作数组。例：

```text
输入:
I love C Language.
love
输出：
I C Languag.
```

??? note "答案"

    ```c
    #include <stdio.h>
    #define N 1024
    int main()
    {
        char str1[N], str2[N];
        int i, j, m;
        gets(str1);
        gets(str2);
        for (i = 0; str2[i]; ++i)
            for (j = 0; str1[j]; )
                if (str2[i] == str1[j])
                    for (m = j; str1[m]; ++m)
                        str1[m] = str1[m+1];    // 删除 str1[j]
                else
                    ++j;
        puts(str1);
        return 0;
    }
    ```
