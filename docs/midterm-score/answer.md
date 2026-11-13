---
icon: material/file-document-outline
---

# 期中考试参考答案

## 一、单选题（每题 2.5 分，共 20 分）

### 1 · 合法的关键字

下列选项，______ 是 C 语言中合法的关键字。

- A. `integer`
- B. `sizeof`
- C. `main`
- D. `array`

??? note "答案"

    B

---

### 2 · `||` 与 `&&` 的短路求值

如下程序段的输出结果是 ______

```c
int a, b, c;
a = b = c = 1 / 2;
a++ || ++b && c++;
printf("%d, %d, %d\n", a, b, c);
```

- A. 1, 1, 1
- B. 1, 1, 0
- C. 1, 0, 0
- D. 1, 0, 1

??? note "答案"

    A

---

### 3 · `do-while` 的条件

执行如下循环时，说法正确的是 ______

```c
int x = -2;
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

---

### 4 · `strlen` 与 `sizeof`

若有定义 `char s[] = "abc\0def";`，则 `strlen(s)` 和 `sizeof(s)` 的值分别是

- A. 3 和 8
- B. 7 和 8
- C. 3 和 7
- D. 7 和 7

??? note "答案"

    A

---

### 5 · 一维数组的初始化

对一维数组 `int a[5];` 进行初始化，希望数组元素为 1, 2, 0, 0, 0，分别使用了如下方法

- (1) `int a[5] = {1, 2};`
- (2) `int a[5] = {1, 2, 0, 0, 0};`
- (3) `int a[5] = {1, 2, 0, 0, 0, 0};`
- (4) `int a[5] = {1, 2, , , };`

在上述初始化方法中正确的有 ______ 种

- A. 1
- B. 2
- C. 3
- D. 0

??? note "答案"

    B

---

### 6 · 结构化程序设计的三种基本结构

C 语言中用于结构化程序设计的 3 种基本结构是 ______

- A. 顺序结构, 选择结构, 循环结构
- B. `if`, `switch`, `break`
- C. `for`, `while`, `do-while`
- D. `if`, `for`, `continue`

??? note "答案"

    A

---

### 7 · `if` 条件的等价写法

在 `if(x)` 条件中的 x 与下面条件表达式等价的是

- A. `x!=0`
- B. `x==1`
- C. `x!=1`
- D. `x==0`

??? note "答案"

    A

---

### 8 · 二维数组的说明

以下对二维数组 a 的正确说明是（　）

- A. `int a[3][];`
- B. `float a[3, 4];`
- C. `double a[1][4];`
- D. `float a(3)(4);`

??? note "答案"

    C

---

## 二、程序阅读题（每题 5 分，共 20 分）

### 1 · 程序功能

以下程序的功能是 ______

```c
#include <stdio.h>

int main() {
    int i, s = 0;
    for (i = 1; i < 10; i += 2)
        s += i + 1;
    printf("%d\n", s);
    return 0;
}
```

??? note "答案"

    计算并输出 2+4+6+8+10 的和

---

### 2 · `switch` 穿透

以下程序运行所产生的输出是 ______

```c
#include <stdio.h>

int main() {
    int i, a = 0, b = 0, c = 0;
    for (i = 0; i < 10; i++) {
        switch (i % 4) {
        case 0: a++;
        case 1: b++;
        case 2: c++; break;
        case 3: a++; break;
        }
    }
    printf("%d,%d,%d\n", a, b, c);
    return 0;
}
```

??? note "答案"

    5,6,8

---

### 3 · `continue` 与 `break`

写出下面程序执行后的屏幕显示结果 ______

```c
#include <stdio.h>

int main() {
    int i, j = 0;
    for (i = 0; i < 20; i++) {
        if (i % 4 == 0) continue;
        if (i - 9) j++;
        else break;
    }
    printf("i=%d,j=%d\n", i, j);
    return 0;
}
```

??? note "答案"

    i=9,j=6

---

### 4 · `while` 条件中的自增

写出下面程序执行后的输出结果 ______

```c
#include <stdio.h>

int main() {
    int x = 0, y = 4, z = 2;
    while (z-- > 0 && ++x < 3)
        y = y - 1;
    printf("%d,%d,%d\n", x, y, z);
    return 0;
}
```

??? note "答案"

    2,2,-1

---

## 三、改错题（10 分）

注意：不得增行或删行，也不得更改程序结构。

### 1 · 正整数转换成数字字符序列

以下程序将输入的正整数转换成数字字符序列，输出转换结果

```c
/* 1 */  #include <stdio.h>
/* 2 */
/* 3 */  int main()
/* 4 */  {
/* 5 */      char s[10];
/* 6 */      int i = 0, n, t;
/* 7 */      scanf("%d", n);
/* 8 */      if (n = 0) s[i++] = '0';
/* 9 */      else {
/* 10 */         t = n;
/* 11 */         while (t > 0) { s[i++] = t % 10 + '0'; t /= 10; }
/* 12 */     }
/* 13 */     while (i > 0) putchar(s[--i]);
/* 14 */     printf("\n");
/* 15 */     return 0;
/* 16 */ }
```

??? note "答案"

    - 第 7 行改为 `scanf("%d", &n);`
    - 第 8 行改为 `if (n == 0) s[i++] = '0';`

---

### 2 · 累加数列

已知数列：S=1+1/(1×2)+1/(2×3)+1/(3×4)+...，以下程序输入一个阈值 eps，不断累加，直到当前项的值不大于 eps 时停止，输出累加和

```c
/* 17 */ #include <stdio.h>
/* 18 */ int main()
/* 19 */ {
/* 20 */     int i;
/* 21 */     double t, s = 0, eps;
/* 22 */     scanf("%f", &eps);
/* 23 */     i = 1;
/* 24 */     t = 1.0;
/* 25 */     while (t > eps)
/* 26 */     {
/* 27 */         s = s + t;
/* 28 */         i++;
/* 29 */         t = 1 / (i * (i + 1));
/* 30 */     }
/* 31 */     printf("sum = %lf\n", s);
/* 32 */     return 0;
/* 33 */ }
```

??? note "答案"

    - 第 22 行改为 `scanf("%lf", &eps);`
    - 第 23 行改为 `i = 0;`
    - 第 29 行改为 `t = 1.0 / (i * (i + 1.0));`

---

## 四、完全程序题（每空 3 分，共 21 分）

### 1 · 数组线性查找

以下是一个数组线性查找的程序：从数组的第一个位置开始，找到 key 的第二个出现时，记录位置

```c
#include <stdio.h>

int main() {
    int a[10] = {3, 7, 2, 7, 9, 7, 1, 7, 5, 7};
    int n = 10, key = 7, i, count = 0, pos = ______(1)______;
    for (i = 0; i < n; i++) {
        if (a[i] == key) {
            ______(2)______;
            if (______(3)______) {
                pos = i;
                ______(4)______;
            }
        }
    }
    if (pos != -1)
        printf("第二次出现的位置: %d\n", pos);
    else
        printf("key 出现次数不足两次\n");
    return 0;
}
```

??? note "答案"

    - (1) -1
    - (2) count++
    - (3) count == 2
    - (4) break

---

### 2 · 选择排序

使用选择排序算法将数组 a 中的数值按从小到大的顺序排序，然后输出排序后的数组

选择排序的基本思想：每一趟从待排序的元素中选出最小的元素，与待排序部分的第一个元素交换，直到全部排完

```c
#include <stdio.h>

int main() {
    int a[] = {4, 45, 65, 43, 32, 3, 72, 27};
    int n, i, j, minIndex, t;
    n = ______(5)______;
    for (i = 0; i < n - 1; i++) {
        ______(6)______;
        for (j = i + 1; j < n; j++)
            if (a[j] < ______(7)______)
                minIndex = j;
        if (minIndex != i) {
            t = a[i];
            a[i] = a[minIndex];
            a[minIndex] = t;
        }
    }
    return 0;
}
```

??? note "答案"

    - (5) sizeof(a) / sizeof(a[0])
    - (6) minIndex = i
    - (7) a[minIndex]

---

## 五、编程题（第 1 题 14 分，第 2 题 15 分，共 29 分）

### 1 · 矩阵上下翻转

输入一个 n 行 m 列（0<n,m<20）的矩阵 A，输出它上下翻转（第 1 行与最后一行交换，第 2 行与倒数第 2 行交换……）后的矩阵 B

输入：

```
3 2
1 2
3 4
5 6
```

输出：

```
5 6
3 4
1 2
```

参考代码：

```c
#include <stdio.h>

int main() {
    int n, m, i, j;
    int a[20][20];

    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &a[i][j]);

    for (i = n - 1; i >= 0; i--) {
        for (j = 0; j < m; j++) {
            if (j > 0)
                printf(" ");
            printf("%d", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

---

### 2 · 删除字符串中的字符

编写程序，输入两个字符串 str1 和 str2（长度均小于 120），删除 str1 中所有在 str2 出现的字符（大写和小写都要删除），输出处理后的 str1。要求：不能使用其他数组

例：

输入：

```
I love C Language.
love
```

输出：

```
I  C anguag.
```

参考代码：

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[120], str2[120];
    char c1, c2;
    int i, j, is_remove;

    fgets(str1, 120, stdin);
    fgets(str2, 120, stdin);
    str1[strcspn(str1, "\n")] = '\0';
    str2[strcspn(str2, "\n")] = '\0';

    for (i = 0; str1[i] != '\0'; i++) {
        is_remove = 0;
        for (j = 0; str2[j] != '\0'; j++) {
            c1 = str1[i];
            c2 = str2[j];
            if (c1 >= 'A' && c1 <= 'Z')
                c1 = c1 - 'A' + 'a';
            if (c2 >= 'A' && c2 <= 'Z')
                c2 = c2 - 'A' + 'a';
            if (c1 == c2) {
                is_remove = 1;
                break;
            }
        }
        if (!is_remove)
            putchar(str1[i]);
    }
    putchar('\n');

    return 0;
}
```

另一版（用 `tolower` 转换大小写）：

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str1[120], str2[120];
    int i, j, is_remove;

    fgets(str1, 120, stdin);
    fgets(str2, 120, stdin);
    str1[strcspn(str1, "\n")] = '\0';
    str2[strcspn(str2, "\n")] = '\0';

    for (i = 0; str1[i] != '\0'; i++) {
        is_remove = 0;
        for (j = 0; str2[j] != '\0'; j++) {
            if (tolower(str1[i]) == tolower(str2[j])) {
                is_remove = 1;
                break;
            }
        }
        if (!is_remove)
            putchar(str1[i]);
    }
    putchar('\n');

    return 0;
}
```
