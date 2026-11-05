---
icon: material/format-list-checks
---

# 期中复习习题 4

本页是课件《期中复习习题-4》的文字版，8 页。答案按材料上的标注给出。

## 一、单选题

### 1

请选出可以作为 C 语言标识符的一组标识符（D）。

- A. 2num, f1, total
- B. main, case, _sum
- C. print, int$, number_1
- D. _data, sum1, Average

### 2

设有 `int i=3.0/2.0; double d=3/2;`，则 i 和 d 的值分别为（A）。

- A. 1, 1.0
- B. 2, 1.0
- C. 1, 1.5
- D. 2, 1.5

### 3

若定义 `char a[][3]={'1','2','3','4'};`，则 sizeof(a) 的返回值为（B）。

- A. 4
- B. 6
- C. 8
- D. 12

### 4

设有 `int x, y;`，循环语句 `while (!x && !y)` 中的循环条件表达式等价于（C）。

- A. `!(x == 0 && y == 0)`
- B. `!(x == 0 || y == 0)`
- C. `!(x != 0 || y != 0)`
- D. `x = 0 && y = 0`

### 5

程序语句 `printf("%d", strlen("hello\078world!"));` 的输出结果是（A）。

- A. 13
- B. 12
- C. 6
- D. 5

### 6

如下程序 scanf 输入 `1<B>.234<CR>`（其中 `<B>` 表示空格，`<CR>` 表示回车），输出（D）。

```c
#include<stdio.h>
int main()
{
    double x;
    scanf("%f", &x);
    printf("%.2f", x);
    return 0;
}
```

- A. 1.234
- B. 1.23
- C. 1.00
- D. 以上答案均不是

### 7

如果定义了以下变量和数组，那么以下可以通过编译的合法表达式或者语句是（A）。

```c
int a[3], b[3], i = 3, j;
```

- A. `j = a == b;`
- B. `b = a;`
- C. `&(i + j);`
- D. `a++;`

### 8

若以下程序执行后，输出为（D）。

```c
int i = 3, j;
j = (++i) + (i++);
```

- A. i = 4, j = 8
- B. i = 5, j = 9
- C. i = 5, j = 10
- D. 结果未定义

## 二、程序阅读题

### 1

请写出以下程序运行所产生的输出：3,6,6。

```c
#include <stdio.h>
int main()
{
    int i = 0, v1 = 0, v2 = 1, v3 = 2;
    for (i = 1; i < 10; i++) {
        switch (i % 4) {
        case 1: v1++;
        case 2: v2++; break;
        default: v3++;
        }
    }
    printf("%d,%d,%d\n", v1, v2, v3);
    return 0;
}
```

### 2

请写出以下程序运行所产生的输出。

```c
#include<stdio.h>
int main()
{
    int y, x = 3;
    do {
        y = x--;
        if (!y) {
            printf("*");
            break;
        }
        printf("#");
    } while (1 <= x <= 2);
    printf("\nx=%d,y=%d", x, y);
}
```

材料上：

```text
###*
x=-1,y=0
```

### 3

写出下面程序的功能和执行后的显示结果。

```c
#include <stdio.h>
int main()
{
    int a[5] = {2, 4, 6, 8, 10};
    int i, sum = 0;
    for (i = 0; i < 5; i++) {
        if (a[i] % 4 == 0)
            continue;
        sum += a[i];
    }
    printf("sum = %d\n", sum);
    return 0;
}
```

材料上：程序功能是将数组 a 中所有不能被 4 整除的元素累加求和，程序输出 `sum = 18`。

## 三、改错题

现有一个统计学生成绩的程序（如下），请找出出错的行，并改正。

| 行 | 代码 |
| --- | --- |
| 2 | `#include <stdio.h>` |
| 3 | `int main() {` |
| 4 | `int n, i;` |
| 5 | `float sum = 0;` |
| 6 | `int scores[5];` |
| 7 | 空行 |
| 8 | `printf("请输入5个学生的成绩（以空格分隔）：");` |
| 9 | `scanf("%f %f %f %f %f", scores);` |
| 10 | `for (i = 0; i <= 5; i++) {` |
| 11 | `sum += scores[i];` |
| 12 | `}` |
| 13 | 空行 |
| 14 | `float avg = sum / 5;` |
| 15 | `if (avg = 60.0)` |
| 16 | `printf("平均分刚好为60分！\n", avg);` |
| 17 | `else if (avg > 60.0)` |
| 18 | `printf("平均分为%.2f，及格！\n", avg);` |
| 19 | `else` |
| 20 | `printf("平均分为%.2f，不及格！\n", avg);` |
| 21 | 空行 |
| 22 | `return 0;` |
| 23 | `}` |

材料上只给出题目，未标出错误行和改正后的代码。
