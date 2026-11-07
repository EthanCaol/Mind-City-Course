---
icon: material/format-list-checks
---

# 期中复习习题 2

本页是课件《期中复习习题-2.pdf》的文字版

## 一、选择题

### 第1题

下列选项中，合法的 C 语言关键字是

- A. `VAR`
- B. `integer`
- C. `default`
- D. `public`

??? note "答案"

    C

### 第2题

以下选项中不属于 C 语言的数据类型是

- A. 整型
- B. 实型
- C. 双精度型
- D. 复数型

??? note "答案"

    D

### 第3题

在 C 语言中，不正确的 short 类型（假设存储单元数为 2 个 bytes）的常数是

- A. `123`
- B. `32768`
- C. `037`
- D. `0xAF`

??? note "答案"

    B

### 第4题

以下选项中合法的实型常数是

- A. `.58`
- B. `E-3`
- C. `.E2`
- D. `1.3E`

??? note "答案"

    A

### 第5题

下面哪种运算的优先级最高

- A. `!`
- B. `!=`
- C. `||`
- D. `&&`

??? note "答案"

    A

### 第6题

`7/9*9` 在 C 语言中的计算结果是

- A. `1`
- B. `0.08642`
- C. `0`
- D. 以上都不是

??? note "答案"

    C

### 第7题

C 语言程序的基本单位是

- A. 语句
- B. 程序行
- C. 函数
- D. 字符

??? note "答案"

    C

### 第8题

以下哪一个是 main() 的正确声明

- A. `int main()`
- B. `int main(int argc, char *argv[])`
- C. A 和 B 都是不正确的
- D. A 和 B 都是正确的

??? note "答案"

    D

### 第9题

以下叙述中正确的是

- A. 可以在一个函数中定义另一个函数
- B. main() 函数必须放在其它函数之前
- C. 所有被调用的函数一定要在调用之前进行定义
- D. 以上皆不正确

??? note "答案"

    D

### 第10题

表达式 `!(1&&1||1&&0)` 的值是

- A. 错误的表达式
- B. `True/1`
- C. `False/0`
- D. 不确定

??? note "答案"

    C

### 第11题

有数组定义 `int a[2][2]={{1},{2,3}};`，则 a[0][1] 的值为

- A. `0`
- B. `1`
- C. `2`
- D. `3`

??? note "答案"

    A

### 第12题

下列描述中不正确的是

- A. 字符型数组中可以存放字符串
- B. 可以对字符型数组进行整体输入、输出
- C. 可以对整型数组进行整体输入、输出
- D. 不能在赋值语句中通过赋值运算符“=”对字符型数组进行整体赋值

??? note "答案"

    C

### 第13题

这个循环语句 `for (int x=0; x=3; x++)` 会执行多少次

- A. 1 次都不
- B. 3 次
- C. 4 次
- D. 死循环

??? note "答案"

    D

### 第14题

设有如下定义 `int x=1, y=-1`，则语句 `printf("%d\n", (x--&++y));` 的输出结果是

- A. `1`
- B. `0`
- C. `-1`
- D. `2`

??? note "答案"

    B

### 第15题

十进制数 1384 转换成十六进制数为

- A. `567`
- B. `568`
- C. `D84`
- D. `D54`

??? note "答案"

    B

### 第16题

以下程序的输出结果是

```c
#include<stdio.h>
int main( )
{
    int i;
    for (i = 1; i < 6; i++) {
        if (i % 2) {
            printf("#");
            continue;
        }
        printf("*");
    }
    printf("\n");
}
```

- A. `#*#*#`
- B. `#####`
- C. `*****`
- D. `*#*#*`

??? note "答案"

    A

### 第17题

以下程序的输出结果是

```c
int main( )
{
    int i;
    for (i = 'A'; i < 'I'; i++，i++)
        printf("%c"，i+32);
    printf(" \n");
}
```

- A. 编译不通过，无输出
- B. `aceg`
- C. `acegi`
- D. `abcdefghi`

??? note "答案"

    A

??? note "解析"

    材料上 `i++` 后面和 `printf` 的参数之间用的是全角逗号，所以编译不通过。

### 第18题

以下程序的运行结果是

```c
#include<stdio.h>
int main( )
{
    char a[10] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 0}, *p;
    int i;
    i = 8;
    p = a + i;
    printf("%s\n", p-3);
}
```

- A. `6`
- B. `6789`
- C. `'6'`
- D. `789`

??? note "答案"

    B

### 第19题

以下程序的输出结果是

```c
int main(  )
{
    char s[] = "12134211";
    int v[4] = {0, 0, 0, 0}, k, i;
    for (k = 0; s[k]; k++) {
        switch (s[k]) {
        case '1': i = 0;
        case '2': i = 1;
        case '3': i = 2;
        case '4': i = 3;
        }
        v[i]++;
    }
    for (k = 0; k < 4; k++)
        printf("%d ", v[k]);
}
```

- A. `4 2 1 1`
- B. `0 0 0 8`
- C. `4 6 7 8`
- D. `8 8 8 8`

??? note "答案"

    B

### 第20题

运行以下程序将会出现

```c
int main(  )
{
    int x;
    while (x < 100) {
        printf("%d", x);
        x++;
    }
}
```

- A. 输出 0123..99
- B. 输出 0123...100
- C. 输出 0123...101
- D. 不确定

??? note "答案"

    D

## 二、填空题

### 第1题

`#include <filename.h>` 和 `#include "filename.h"` 有什么区别？

??? note "答案"

    前者编译器只会到系统指定目录下搜索头文件；后者编译器会先在工作目录下查找头文件，如果找不到，则到系统指定目录下搜索

### 第2题

下列程序的输出结果是什么？

```c
#include <stdio.h>
#include <string.h>
int main()
{
    char ch[] = "abc", x[3][4];
    int i;
    for (i = 0; i < 3; i++)
        strcpy(x[i], ch);
    for (i = 0; i < 3; i++)
        printf("%s", &x[i][i]);
    printf("\n");
}
```

??? note "答案"

    abcbcc

### 第3题

下列程序的输出结果是什么？

```c
#include<stdio.h>
int main()
{
    int a = 1, b;
    for (b = 1; b <= 10; b++) {    /* b=1, a=6; b=2, a=3; b=3, a=8; b=4 */
        if (a >= 8)
            break;
        if (a % 2 == 1) {
            a += 5;
            continue;
        }
        a -= 3;
    }
    printf("%d\n", b);
}
```

??? note "答案"

    4

## 三、程序改错题

```c
int binsearch(int x, int v[], int n)
{
    int low, high, mid;
    low = 1;
    high = n;
    mid = (high - low) / 2;
    while (low < high && x = v[mid]) {
        if (x < v[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    if (x == v[mid])
        return mid;     /* found match */
    else
        return -1;      /* no match */
}
```

??? note "答案"

    ```c
    int binsearch(int x, int v[], int n)
    {
        int low, high, mid;
        low = 0;
        high = n - 1;
        mid = (low + high) / 2;
        while (low <= high && x != v[mid]) {
            if (x < v[mid])
                high = mid - 1;
            else
                low = mid + 1;
            mid = (low + high) / 2;
        }
        if (x == v[mid])
            return mid;
        else
            return -1;
    }
    ```

## 三、综合题（略）

### 第1题 · 质因子分解

输入一个自然数 N（N>1），输出它的质因子分解式。如 n＝8，程序输出 8＝2*2*2。

??? note "思路"

    从 2 开始试除。n 能被 d 整除，就输出 d，并令 n = n / d；不能整除则 d 加 1。n 变成 1 时结束，因子之间补 `*`。

??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n, d;
        scanf("%d", &n);
        printf("%d=", n);
        d = 2;
        while (n > 1) {
            if (n % d == 0) {
                printf("%d", d);
                n /= d;
                if (n > 1)
                    printf("*");
            } else {
                d++;
            }
        }
        printf("\n");
        return 0;
    }
    ```

    运行示例：

    ```text
    8     ->  8=2*2*2
    30    ->  30=2*3*5
    1024  ->  1024=2*2*2*2*2*2*2*2*2*2
    97    ->  97=97
    ```

### 第2题 · 取棋子

有 n 个棋子，甲、乙两方轮流取棋子，每方至少取一个，最多取 m 个。谁最后取剩下的一个棋子谁就输。甲方先取，给出甲方必赢的算法（即无论乙怎么下，甲都能赢）。

??? note "思路"

    按剩余棋子数分类，从只剩 1 个的局面开始倒推：

    | 剩余棋子数 | 结论  | 依据                                                                                       |
    | ---------- | ----- | ------------------------------------------------------------------------------------------ |
    | 1          | 必败× | 只能取走最后一个，直接输                                                                   |
    | 2          | 必胜  | 取 1 个，给对方留 1 个                                                                     |
    | 3          | 必胜  | 取 2 个，给对方留 1 个                                                                     |
    | 4          | 必胜  | 取 3 个，给对方留 1 个                                                                     |
    | ……         | 必胜  | 剩 `n` 个就取 `n−1` 个，只要不超过 `m`                                                     |
    | `m+1`      | 必胜  | 取 `m` 个，给对方留 1 个                                                                   |
    | `m+2`      | 必败× | 无论取 `k` 个（`1 ≤ k ≤ m`），留给对方的都是 `m+2−k` 个，落在 2 到 `m+1`，是对方的必胜局面 |

    照此递推，必败局面依次是 1、`m+2`、`2(m+1)+1`，即 `n ≡ 1（mod m+1）`。

    ------

    必胜一方的走法：

    1. 先取 `(n−1) mod (m+1)` 个，把局面留成 `n ≡ 1（mod m+1）`
    2. 此后对方取 `k` 个，自己就取 `m+1−k` 个，每轮两方合计固定取走 `m+1` 个
    3. 重复第 2 步，最终就可以给对方只剩下 1 个

    若一开始就面对 `n ≡ 1（mod m+1）`，则没有必胜策略。

    ------

    以 `n = 8`、`m = 3` 为例，`(8−1) mod 4 = 3`，甲先取 3 个：

    | 轮次 | 取前棋子数 | 行动            | 取后剩余数 | 剩余数满足       |
    | ---- | ---------- | --------------- | ---------- | ---------------- |
    | 甲   | 8          | 取 3 个         | 5          | `5 ≡ 1（mod 4）` |
    | 乙   | 5          | 取 1 个         | 4          |                  |
    | 甲   | 4          | 取 3 个         | 1          | `1 ≡ 1（mod 4）` |
    | 乙   | 1          | 只能取最后 1 个 | 0，乙输    |                  |

    ------

    以 `n = 15`、`m = 3` 为例，`(15−1) mod 4 = 2`，甲先取 2 个：

    | 轮次 | 取前棋子数 | 行动            | 取后剩余数 | 剩余数满足        |
    | ---- | ---------- | --------------- | ---------- | ----------------- |
    | 甲   | 15         | 取 2 个         | 13         | `13 ≡ 1（mod 4）` |
    | 乙   | 13         | 取 3 个         | 10         |                   |
    | 甲   | 10         | 取 1 个         | 9          | `9 ≡ 1（mod 4）`  |
    | 乙   | 9          | 取 2 个         | 7          |                   |
    | 甲   | 7          | 取 2 个         | 5          | `5 ≡ 1（mod 4）`  |
    | 乙   | 5          | 取 1 个         | 4          |                   |
    | 甲   | 4          | 取 3 个         | 1          | `1 ≡ 1（mod 4）`  |
    | 乙   | 1          | 只能取最后 1 个 | 0，乙输    |                   |

    ------

    以 `n = 10`、`m = 4` 为例，`(10−1) mod 5 = 4`，甲先取 4 个：

    | 轮次 | 取前棋子数 | 行动            | 取后剩余数 | 剩余数满足       |
    | ---- | ---------- | --------------- | ---------- | ---------------- |
    | 甲   | 10         | 取 4 个         | 6          | `6 ≡ 1（mod 5）` |
    | 乙   | 6          | 取 2 个         | 4          |                  |
    | 甲   | 4          | 取 3 个         | 1          | `1 ≡ 1（mod 5）` |
    | 乙   | 1          | 只能取最后 1 个 | 0，乙输    |                  |

    ------

    以 `n = 6`、`m = 2` 为例，`(6−1) mod 3 = 2`，甲先取 2 个：

    | 轮次 | 取前棋子数 | 行动            | 取后剩余数 | 剩余数满足       |
    | ---- | ---------- | --------------- | ---------- | ---------------- |
    | 甲   | 6          | 取 2 个         | 4          | `4 ≡ 1（mod 3）` |
    | 乙   | 4          | 取 2 个         | 2          |                  |
    | 甲   | 2          | 取 1 个         | 1          | `1 ≡ 1（mod 3）` |
    | 乙   | 1          | 只能取最后 1 个 | 0，乙输    |                  |



??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        int n, m, stones, take, k;

        scanf("%d%d", &n, &m);
        if (n % (m + 1) == 1) {
            printf("甲没有必胜策略：先手面对 %d 个棋子必输\n", n);
            return 0;
        }
        stones = n;
        take = (stones - 1) % (m + 1);
        printf("甲取 %d 个，剩 %d 个\n", take, stones - take);
        stones -= take;
        while (stones > 1) {
            k = 1;                      /* 演示中乙每次只取 1 个 */
            if (k > m)
                k = m;
            printf("乙取 %d 个，剩 %d 个\n", k, stones - k);
            stones -= k;
            if (stones == 0) {
                printf("乙取走最后一个，乙输\n");
                return 0;
            }
            take = m + 1 - k;
            if (take > stones - 1)
                take = stones - 1;      /* 留 1 个给乙 */
            printf("甲取 %d 个，剩 %d 个\n", take, stones - take);
            stones -= take;
        }
        printf("乙只能取最后 1 个，乙输\n");
        return 0;
    }
    ```

    输入 `8 3`，输出：

    ```text
    甲取 3 个，剩 5 个
    乙取 1 个，剩 4 个
    甲取 3 个，剩 1 个
    乙只能取最后 1 个，乙输
    ```

    输入 `9 3`，`9 ≡ 1（mod 4）`，输出：

    ```text
    甲没有必胜策略：先手面对 9 个棋子必输
    ```

### 第3题 · 白黑石子移动

设有 N 个白石子和 N 个黑石子，开始时排成一行，中间有一个空位置。N＝3 时，三个白子和三个黑子排成 `WWW.BBB`，其中 W 为白、B 为黑，`.` 是空位。

目标是把这一行变成 N 个黑子在前、N 个白子在后，中间仍是一个空位置，即 `BBB.WWW`。

移动规则：

- 每次只能移动一个石子
- 石子朝自己的目标方向移动：走进相邻的空位置，或者跳过一颗不同颜色的石子，进入空位置

设计移动策略，并编写程序，输出每次移动后的状态。

??? note "思路"

    把局面写成一串字符，W 是白子，B 是黑子，`.` 是空位，初始 `WWW.BBB`，目标 `BBB.WWW`。

    一步合法的移动有两种：白子向右、黑子向左走进相邻的空位；或者按同一方向跳过一颗另一种颜色的石子，进入距它两格的空位。

    于是问题变成在状态图上找一条从初始局面到目标局面的路径。用广度优先搜索逐层扩展，得到的步数最少；用一个哈希表记录已经出现过的局面，避免重复。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <string.h>

    #define MAXN   10
    #define LEN    (2 * MAXN + 1)
    #define MAXS   600000
    #define HSIZE  (1 << 20)

    static char state[MAXS][LEN + 1];
    static int  parent[MAXS];
    static int  from[MAXS];          /* 这步移动的石子原来所在的格子 */
    static int  table[HSIZE];
    static int  head, tail, L;

    static unsigned long long hashStr(const char *s)
    {
        unsigned long long h = 1469598103934665603ULL;
        while (*s) {
            h ^= (unsigned char)*s++;
            h *= 1099511628211ULL;
        }
        return h;
    }

    static int lookup(const char *s)
    {
        unsigned i = (unsigned)(hashStr(s) % HSIZE);
        while (table[i]) {
            if (strcmp(state[table[i] - 1], s) == 0)
                return table[i] - 1;
            i = (i + 1) % HSIZE;
        }
        return -1;
    }

    static void put(const char *s, int id)
    {
        unsigned i = (unsigned)(hashStr(s) % HSIZE);
        while (table[i])
            i = (i + 1) % HSIZE;
        table[i] = id + 1;
    }

    static void expand(int id)
    {
        char s[LEN + 1], t[LEN + 1];
        int e = 0, i, d, mid;

        strcpy(s, state[id]);
        while (s[e] != '.')
            e++;
        for (i = 0; i < L; i++) {
            if (i == e)
                continue;
            d = e - i;
            if (s[i] == 'W' && d < 0)      /* 白子只向右走 */
                continue;
            if (s[i] == 'B' && d > 0)      /* 黑子只向左走 */
                continue;
            if (d == 1 || d == -1) {
                /* 邻格为空，直接移动 */
            } else if (d == 2 || d == -2) {
                mid = (i + e) / 2;
                if (s[mid] == '.' || s[mid] == s[i])
                    continue;              /* 只能跳过另一种颜色的石子 */
            } else {
                continue;
            }
            strcpy(t, s);
            t[e] = t[i];
            t[i] = '.';
            if (lookup(t) < 0) {
                strcpy(state[tail], t);
                parent[tail] = id;
                from[tail] = i;
                put(t, tail);
                tail++;
            }
        }
    }

    int main(void)
    {
        int n, i, id, goal = -1, path[MAXS], len = 0;
        char s[LEN + 1], g[LEN + 1];

        scanf("%d", &n);
        L = 2 * n + 1;
        for (i = 0; i < n; i++)
            s[i] = 'W';
        s[n] = '.';
        for (i = n + 1; i < L; i++)
            s[i] = 'B';
        s[L] = '\0';

        for (i = 0; i < n; i++)
            g[i] = 'B';
        g[n] = '.';
        for (i = n + 1; i < L; i++)
            g[i] = 'W';
        g[L] = '\0';

        strcpy(state[0], s);
        parent[0] = -1;
        put(s, 0);
        tail = 1;

        while (head < tail) {
            if (strcmp(state[head], g) == 0) {
                goal = head;
                break;
            }
            expand(head);
            head++;
        }
        if (goal < 0) {
            printf("无解\n");
            return 0;
        }
        for (id = goal; id != -1; id = parent[id])
            path[len++] = id;
        printf("%d 步\n", len - 1);
        for (i = len - 1; i >= 0; i--) {
            id = path[i];
            if (parent[id] < 0)
                printf("       %s\n", state[id]);
            else
                printf("%2d步  %s   移动第 %d 格的 %c\n",
                       len - 1 - i, state[id], from[id] + 1,
                       state[parent[id]][from[id]]);
        }
        return 0;
    }
    ```

    输入 `3`，输出：

    ```text
    15 步
           WWW.BBB
     1步  WW.WBBB   移动第 3 格的 W
     2步  WWBW.BB   移动第 5 格的 B
     3步  WWBWB.B   移动第 6 格的 B
     4步  WWB.BWB   移动第 4 格的 W
     5步  W.BWBWB   移动第 2 格的 W
     6步  .WBWBWB   移动第 1 格的 W
     7步  BW.WBWB   移动第 3 格的 B
     8步  BWBW.WB   移动第 5 格的 B
     9步  BWBWBW.   移动第 7 格的 B
    10步  BWBWB.W   移动第 6 格的 W
    11步  BWB.BWW   移动第 4 格的 W
    12步  B.BWBWW   移动第 2 格的 W
    13步  BB.WBWW   移动第 3 格的 B
    14步  BBBW.WW   移动第 5 格的 B
    15步  BBB.WWW   移动第 4 格的 W
    ```

    实测 N=3 时 15 步、N=4 时 24 步、N=5 时 35 步。
