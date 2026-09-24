---
icon: material/notebook-outline
---

# 第八章 · 数据文件处理技术

《C语言程序设计（第3版）》第 8 章课后习题，共 10 题。

### 1 · 统计文件中英文字母个数

输入正文文件，统计文件中英文字母的个数，并输出。

??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char fname[256];
        FILE *fp;
        int ch, count = 0;

        printf("请输入文件名: ");
        if (scanf("%255s", fname) != 1)
            return 0;

        if ((fp = fopen(fname, "r")) == NULL) {
            printf("无法打开文件 %s\n", fname);
            return 1;
        }

        while ((ch = fgetc(fp)) != EOF)
            if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z'))
                count++;

        fclose(fp);
        printf("英文字母个数: %d\n", count);
        return 0;
    }
    ```

??? note "解析"

    思路：以只读方式打开用户给定的正文文件，逐字符读进来，遇到 `A`～`Z` 或 `a`～`z` 就把计数器加一，读到文件尾为止。

    关键点：

    1. `fgetc` 的返回值必须存进 `int`。`EOF` 是负值（本机是 -1），存进 `char` 时可能和某个合法字符的编码撞上，循环就停不下来。
    2. `fopen` 之后必须判空。文件不存在时 `"r"` 模式返回 `NULL`，不判空后面 `fgetc(NULL)` 直接崩。本题的失败分支是打印一句提示再 `return 1`。
    3. 判断字母用 `(ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')` 这种最直白的写法，大小写两个区间都要写。数字、标点、空格一个都不能算进去。
    4. 读文件的循环用 `while` 配 `fgetc`，不要用 `do...while`——空文件时 `do...while` 会先读一次再判断，那个 `EOF` 会被当成一个字符。
    5. `fclose` 不能省。虽然本题只读不写，关掉文件是文件操作的收尾动作。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`letters.txt` 的内容是 `Hello, World!`、`C programming 2024.`、`ABC abc` 三行，运行后输出 `英文字母个数: 28`，与手工数出来的 5+5+1+11+3+3 一致（`Hello` 5 个、`World` 5 个、`C` 1 个、`programming` 11 个、`ABC` 3 个、`abc` 3 个）。把文件名换成不存在的 `no_such.txt`，程序走 `无法打开文件 no_such.txt` 那一支，退出码 1。

    > 易错：① `int ch` 写成 `char ch`，文件里出现编码为 `0xFF` 的字节时循环不终止；② 忘了 `fclose`；③ 只统计大写字母或只统计小写字母。

---

### 2 · 键盘读入正文复制到文件

编写从键盘读入正文，复制到指定文件的程序。要求文件名由用户指定，并在文件的字符串之前能按用户要求或插入行号，或不插入行号。

??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char fname[256], line[1024];
        FILE *fp;
        int with_no, lineno = 1;

        printf("请输入目标文件名: ");
        if (scanf("%255s", fname) != 1)
            return 0;
        printf("是否插入行号（1 插入，0 不插入）: ");
        if (scanf("%d", &with_no) != 1)
            return 0;
        getchar();                       /* 吃掉上一个 scanf 留下的换行符 */

        if ((fp = fopen(fname, "w")) == NULL) {
            printf("无法创建文件 %s\n", fname);
            return 1;
        }

        printf("请输入正文，输入结束后按 Ctrl+D 结束:\n");
        while (fgets(line, sizeof line, stdin) != NULL) {
            if (with_no)
                fprintf(fp, "%d: %s", lineno++, line);
            else
                fputs(line, fp);
        }

        fclose(fp);
        return 0;
    }
    ```

??? note "解析"

    思路：先问两件事——目标文件名、要不要插行号；然后逐行从键盘读正文，边读边往目标文件写。插行号时把行号写在该行前面，不插就原样写出去。

    关键点：

    1. 输入数组按 `char fname[256]` 开，`scanf` 就写 `"%255s"`：宽度比数组长度小一，最多存 255 个字符加一个 `'\0'`，不会越界。
    2. 两次 `scanf` 读完之后，输入缓冲区里还留着一个换行符。接着用 `fgets` 读正文，先 `getchar()` 把这个换行吃掉，否则第一行正文会读成一个空行。
    3. 插行号用 `fprintf(fp, "%d: %s", lineno++, line)`：`fgets` 读进来的 `line` 本身带着行尾换行符，格式串末尾就不要再加 `\n`，加了每行之间会多出一个空行。`lineno++` 是先取原值再自增，行号从 1 开始递增。
    4. 不插行号时直接 `fputs(line, fp)`，内容和键盘上敲的逐字节相同。
    5. 写文件用 `"w"` 模式：文件不存在就新建，已存在就清空重写。复制场景要的就是这个语义，用 `"a"` 会把新内容追到旧内容后面。
    6. 正文读到什么时候为止？题目没有给结束标记，这里按"读到输入结束"处理：在终端里手工输入时按下结束输入的按键（Ctrl+D），用管道喂输入时就是读到输入尾。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：喂入 `out_no.txt`、`1` 和正文 `line one`、`line two` 两行，生成的 `out_no.txt` 是 `1: line one`、`2: line two` 两行；把第二个输入改成 `0`，生成的 `out_plain.txt` 与键盘输入的正文逐字节相同。

    > 易错：① 写成 `fprintf(fp, "%d: %s\n", ...)`，`line` 自带的换行加上格式串里的 `\n`，结果每行之间空一行；② 忘了 `getchar()`，第一行正文变成空行；③ `fopen` 不判空，目标文件建不出来时后面全是空指针操作；④ 忘了 `fclose`，缓冲区没落盘，文件可能是空的或短一截。

---

### 3 · 按指定行长复制文件

编写复制文件的程序。要求源文件名和目标文件名由用户指定，新文件各行的字符个数也可由用户指定。

??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char src[256], dst[256];
        FILE *in, *out;
        int n, ch, cnt = 0;

        printf("请输入源文件名: ");
        if (scanf("%255s", src) != 1)
            return 0;
        printf("请输入目标文件名: ");
        if (scanf("%255s", dst) != 1)
            return 0;
        printf("请输入新文件每行的字符个数: ");
        if (scanf("%d", &n) != 1 || n <= 0) {
            printf("每行字符个数必须是正整数\n");
            return 1;
        }

        if ((in = fopen(src, "r")) == NULL) {
            printf("无法打开源文件 %s\n", src);
            return 1;
        }
        if ((out = fopen(dst, "w")) == NULL) {
            printf("无法创建目标文件 %s\n", dst);
            fclose(in);
            return 1;
        }

        while ((ch = fgetc(in)) != EOF) {
            if (ch == '\n')          /* 新文件的行长由用户指定，源文件的换行不再保留 */
                continue;
            fputc(ch, out);
            cnt++;
            if (cnt % n == 0)
                fputc('\n', out);
        }
        if (cnt % n != 0)            /* 末行不足 n 个字符也要收尾 */
            fputc('\n', out);

        fclose(in);
        fclose(out);
        return 0;
    }
    ```

??? note "解析"

    思路：题面只说"新文件各行的字符个数也可由用户指定"，此处按"新文件每行恰好放 `n` 个字符"理解：把源文件的字符按顺序读出来，每凑够 `n` 个就往新文件里写一个换行符。

    源文件里原有的换行不再保留。这一点是上面这个理解的必然结果：如果连源文件的换行也照抄，新文件的行长仍然是源文件原来的行长，就谈不上"新文件各行的字符个数由用户指定"了。

    关键点：

    1. 换行符要单独判掉（`if (ch == '\n') continue;`），否则它会占掉一个字符位，新文件的行长就不整齐。
    2. `cnt % n == 0` 时补一个换行，正好每写满 `n` 个字符换一行。计数用累计的 `cnt`，不需要每次清零。
    3. 循环结束后如果 `cnt % n != 0`，说明末行不满 `n` 个字符，也要补一个换行把最后一行收掉，不然它会和上一行粘在一起。
    4. 输入的 `n` 要挡一下非正数，否则 `cnt % n` 就是除零。
    5. 新文件用 `"w"` 模式打开，已存在时先清空——复制出来的是本次运行的结果。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：源文件 `src.txt` 是 `abcdefghij`、`klmnopqrst`、`uvwxyz` 三行，去掉换行后共 26 个字符；指定每行 5 个字符，生成的 `out_reflow.txt` 是 `abcde`、`fghij`、`klmno`、`pqrst`、`uvwxy`、`z` 六行，一共 26 个字符，一个不多一个不少。

    > 易错：① 忘了跳过源文件的换行符，新文件的行长时多时少；② 末行不满 `n` 个字符时不补换行；③ 目标文件用了 `"a"` 模式，第二次运行的结果追加在旧内容后面；④ `n` 不判正负，输入 0 时程序直接崩。

---

### 4 · 合并两个有序整数文件

编写将两个有序整数文件合并复制一个有序整数文件的程序，假定整数文件中的整数是从小到大排列的。要求新文件中的整数也从小到大排列，并且互不相同。

??? note "答案"

    ```c
    #include <stdio.h>

    int main(void)
    {
        char n1[256], n2[256], n3[256];
        FILE *f1, *f2, *f3;
        int a, b, x, last = 0, has_last = 0, has_a, has_b;

        printf("请输入第 1 个整数文件名: ");
        if (scanf("%255s", n1) != 1)
            return 0;
        printf("请输入第 2 个整数文件名: ");
        if (scanf("%255s", n2) != 1)
            return 0;
        printf("请输入合并后的文件名: ");
        if (scanf("%255s", n3) != 1)
            return 0;

        if ((f1 = fopen(n1, "r")) == NULL) {
            printf("无法打开文件 %s\n", n1);
            return 1;
        }
        if ((f2 = fopen(n2, "r")) == NULL) {
            printf("无法打开文件 %s\n", n2);
            fclose(f1);
            return 1;
        }
        if ((f3 = fopen(n3, "w")) == NULL) {
            printf("无法创建文件 %s\n", n3);
            fclose(f1);
            fclose(f2);
            return 1;
        }

        has_a = (fscanf(f1, "%d", &a) == 1);
        has_b = (fscanf(f2, "%d", &b) == 1);

        while (has_a || has_b) {
            if (has_a && has_b)
                x = (a <= b) ? a : b;
            else
                x = has_a ? a : b;

            /* 取走刚用掉的那个元素 */
            if (has_a && x == a)
                has_a = (fscanf(f1, "%d", &a) == 1);
            if (has_b && x == b)
                has_b = (fscanf(f2, "%d", &b) == 1);

            /* 两个文件各自有序，相等的整数一定相邻出现，跳过重复的即可 */
            if (!has_last || x != last) {
                fprintf(f3, "%d\n", x);
                last = x;
                has_last = 1;
            }
        }

        fclose(f1);
        fclose(f2);
        fclose(f3);
        return 0;
    }
    ```

??? note "解析"

    思路：两个文件各读一个整数放在 `a`、`b` 里，每轮挑小的那个写进新文件，然后把用掉的那一边再往前读一个。两边相等时各读一个，这一步正好顺带完成了去重。

    关键点：

    1. 循环条件是 `has_a || has_b`，两边都读完了才停。写成 `has_a && has_b` 的话，某个文件先读完时循环整个退出，另一个文件剩下的整数全部丢掉。
    2. 用 `has_a`、`has_b` 记录"这一边还读没读到数"，不要拿某个特殊值（比如 -1）当结束标记——整数文件里任何一个数都可能是合法数据。
    3. 去重靠"跳过和上一次写出去的值相同的数"。两个文件各自从小到大有序，归并出来的序列必然有序，相等的整数一定相邻出现，所以只要和 `last` 比一次就够，不需要额外的查找结构。
    4. 推进指针时判断 `x == a` / `x == b`：`x` 是从哪一边取来的，就推进哪一边；两边相等时两个都推进。
    5. 三个文件都要判空。新文件用 `"w"` 打开，已存在时先清空。
    6. 写出的格式是每行一个整数，这样生成的文件本身还是一个"整数文件"，可以再拿去和别的文件合并。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`nums1.txt` 为 `1 3 5 7 9`、`nums2.txt` 为 `2 3 4 9 10`，合并出的 `merged.txt` 是 `1 2 3 4 5 7 9 10`，`3` 和 `9` 各只出现一次；把第一个文件换成空文件，结果就是 `nums2.txt` 的内容原样；把两个文件分别换成 `1 1 2 2 2` 和 `2 3 3`（文件内部也有重复），结果是 `1 2 3`。文件名不存在时走 `无法打开文件` 那一支，退出码 1。

    !!! note "跳过重复用的是相邻比较，不是先把所有数读进内存"
        这种做法只用到两个文件各自有序这一个性质，内存里始终只有两个整数，文件多大都跑得动。它同时管住了两种重复：同一个文件内部的重复（`1 1 2 2 2`）和两个文件之间的重复（两个文件里都有 `3`）。

    > 易错：① 循环条件写成 `has_a && has_b`，一个文件读完就整个退出；② 只处理了两个文件之间的重复，漏了同一文件内部的重复；③ 推进指针时只看值不看来源，两边相等时只推进了一边（不丢数据，但要多绕几轮）。

---

### 5 · 三个单词文件的共同单词

设有 3 个按词典编辑顺序组织的单词文件，编写从这 3 个文件中找出第 1 个在这 3 个文件中都出现的单词。要求程序采用的算法是最快的。然后修改程序，使程序能找出在这 3 个文件中都出现的全部单词。

??? note "答案"

    程序一：找第 1 个共同单词。

    ```c
    #include <stdio.h>
    #include <string.h>

    #define NWORD 3
    #define MAXW  64

    int main(void)
    {
        const char *names[NWORD] = {"w1.txt", "w2.txt", "w3.txt"};
        FILE *fp[NWORD];
        char w[NWORD][MAXW];
        int ok[NWORD];
        int i, found = 0;

        for (i = 0; i < NWORD; i++) {
            if ((fp[i] = fopen(names[i], "r")) == NULL) {
                printf("无法打开文件 %s\n", names[i]);
                while (--i >= 0)
                    fclose(fp[i]);
                return 1;
            }
            ok[i] = (fscanf(fp[i], "%63s", w[i]) == 1);
        }

        /* 三路归并：每次把三者中最小的那个往前推 */
        while (ok[0] && ok[1] && ok[2]) {
            if (strcmp(w[0], w[1]) == 0 && strcmp(w[1], w[2]) == 0) {
                printf("第 1 个在 3 个文件中都出现的单词: %s\n", w[0]);
                found = 1;
                break;
            }

            if (strcmp(w[0], w[1]) <= 0 && strcmp(w[0], w[2]) <= 0)
                ok[0] = (fscanf(fp[0], "%63s", w[0]) == 1);
            else if (strcmp(w[1], w[2]) <= 0)
                ok[1] = (fscanf(fp[1], "%63s", w[1]) == 1);
            else
                ok[2] = (fscanf(fp[2], "%63s", w[2]) == 1);
        }

        if (!found)
            printf("3 个文件中没有共同单词\n");

        for (i = 0; i < NWORD; i++)
            fclose(fp[i]);
        return 0;
    }
    ```

    程序二：找出全部共同单词。与程序一只有一处不同——命中之后不退出，而是三个文件同时往前推一个。

    ```c
    #include <stdio.h>
    #include <string.h>

    #define NWORD 3
    #define MAXW  64

    int main(void)
    {
        const char *names[NWORD] = {"w1.txt", "w2.txt", "w3.txt"};
        FILE *fp[NWORD];
        char w[NWORD][MAXW];
        int ok[NWORD];
        int i;

        for (i = 0; i < NWORD; i++) {
            if ((fp[i] = fopen(names[i], "r")) == NULL) {
                printf("无法打开文件 %s\n", names[i]);
                while (--i >= 0)
                    fclose(fp[i]);
                return 1;
            }
            ok[i] = (fscanf(fp[i], "%63s", w[i]) == 1);
        }

        while (ok[0] && ok[1] && ok[2]) {
            if (strcmp(w[0], w[1]) == 0 && strcmp(w[1], w[2]) == 0) {
                printf("%s\n", w[0]);
                for (i = 0; i < NWORD; i++)
                    ok[i] = (fscanf(fp[i], "%63s", w[i]) == 1);
                continue;
            }

            if (strcmp(w[0], w[1]) <= 0 && strcmp(w[0], w[2]) <= 0)
                ok[0] = (fscanf(fp[0], "%63s", w[0]) == 1);
            else if (strcmp(w[1], w[2]) <= 0)
                ok[1] = (fscanf(fp[1], "%63s", w[1]) == 1);
            else
                ok[2] = (fscanf(fp[2], "%63s", w[2]) == 1);
        }

        for (i = 0; i < NWORD; i++)
            fclose(fp[i]);
        return 0;
    }
    ```

??? note "解析"

    思路：题面要求"算法最快"，指的就是三路归并——三个文件各读一个单词放在当前词上，每轮比较这三个词：三个相同就是找到了，否则把其中最小的那个对应的文件往前推一个。三个文件各扫一遍，复杂度是三个文件单词总数的一次线性扫描。

    对照一下不这么写的做法：把所有单词读进内存再逐个查找，最坏是平方级；给每个文件建一张哈希表，也要额外的内存。这些都比三路归并慢。

    关键点：

    1. 判决用 `strcmp`，不能写 `w[0] == w[1]`——那样比的是两个数组的地址，永远不相等。
    2. 每轮推的是"最小的那个"。`w[0] <= w[1] && w[0] <= w[2]` 说明 `w[0]` 是最小值之一，推它；否则 `w[0]` 一定比 `w[1]` 或 `w[2]` 大，再在 `w[1]` 和 `w[2]` 里挑小的推。写成 `if / else if / else` 每轮只推一个，是安全的。
    3. 循环条件是三个文件都还没读完。任何一个文件读到尾，就不可能再有共同单词了——这部分单词已经不在它的词表里。
    4. 程序二与程序一的差别只有命中之后那三行：不 `break`，而是三个文件同时往前推一个再 `continue`。三边同推保证了同一个单词只输出一次，也不会卡在原地反复命中。
    5. `fscanf(fp, "%63s", w[i])` 里的 `63` 是宽度限制：数组是 `char[64]`，最多存 63 个字符加一个 `'\0'`。
    6. 三个文件里只要有任何一个打不开就退出，退出前把已经打开的那些关掉。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`w1.txt` 为 apple、banana、cherry、grape、lemon、peach，`w2.txt` 为 avocado、cherry、fig、grape、mango、peach，`w3.txt` 为 cherry、grape、kiwi、peach、quince。程序一输出 `第 1 个在 3 个文件中都出现的单词: cherry`；程序二输出 `cherry`、`grape`、`peach` 三行。换成三个互不相交的单词文件，程序一输出 `3 个文件中没有共同单词`，程序二没有任何输出。

    > 易错：① 用 `==` 比较字符串；② 程序二命中之后不推指针，程序死循环；③ 循环条件写成"三个文件都读完了才继续"，指针停在文件尾还在做比较；④ 三个单词文件按题面是"按词典编辑顺序组织"的，程序依赖这个前提；文件没排序的话三路归并不成立。

---

### 6 · 随机数写文件与读回统计

编写一个程序，利用随机数产生若干个整数存入文件，然后从文件中读出整数，显示在屏幕上，并统计文件中有多少个整数，找出其中最大的整数和最小的整数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    #define N 20

    int main(void)
    {
        const char *fname = "rand.txt";
        FILE *fp;
        int i, x, count = 0, max = 0, min = 0;

        srand((unsigned)time(NULL));          /* 用当前时间做种子 */

        if ((fp = fopen(fname, "w")) == NULL) {
            printf("无法创建文件 %s\n", fname);
            return 1;
        }
        for (i = 0; i < N; i++)
            fprintf(fp, "%d\n", rand() % 100);   /* 产生 0～99 的整数 */
        fclose(fp);

        if ((fp = fopen(fname, "r")) == NULL) {
            printf("无法打开文件 %s\n", fname);
            return 1;
        }

        printf("文件中的整数: ");
        while (fscanf(fp, "%d", &x) == 1) {
            printf("%d ", x);
            if (count == 0) {
                max = min = x;
            } else {
                if (x > max) max = x;
                if (x < min) min = x;
            }
            count++;
        }
        printf("\n");
        fclose(fp);

        if (count == 0) {
            printf("文件里没有整数\n");
            return 0;
        }
        printf("整数个数: %d\n", count);
        printf("最大整数: %d\n", max);
        printf("最小整数: %d\n", min);
        return 0;
    }
    ```

??? note "解析"

    思路：分两趟做。第一趟以写方式打开文件，循环 `N` 次，每次把 `rand() % 100` 产生的一个 0～99 的整数写进去；第二趟重新以读方式打开同一个文件，边读边显示，同时统计个数、用打擂台法求最大最小。

    关键点：

    1. `srand((unsigned)time(NULL))` 用当前时间做种子，每次运行产生不同的序列。不调 `srand` 的话 `rand` 的默认种子是 1，每次运行出来的数一模一样，看着就不像随机了。
    2. 写完必须 `fclose`，再重新 `fopen(..., "r")`。同一个流又写又读需要插定位函数，分两次开最省事，也最不容易错。
    3. 读回时用 `while (fscanf(fp, "%d", &x) == 1)`：返回 1 表示成功读到一个整数，读到文件尾返回 `EOF`。
    4. 求最大最小用打擂台，但初值不能随手写 0。如果产生的随机数全是负数，初值 0 会让"最大值"变成 0。这里的写法是第一个读到的数同时当最大和最小的初值（`if (count == 0) max = min = x;`），任何数据都不会错。
    5. 个数由计数器 `count` 数出来，不是直接打 `N`。虽然这里写进去几个就读回几个，但"统计文件中有多少个整数"问的是文件里实际有多少个，数出来的才作数。
    6. 产生的范围 `rand() % 100` 是 0～99。想换范围就改这个除数，但取模的取值范围不能超过 `rand()` 能产生的最大值——上限由 `RAND_MAX` 决定（本机是 2147483647）。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：某一次运行写出的文件内容是 `4 63 40 70 38 72 15 24 71 39 14 95 58 70 19 68 60 97 38 65`，屏幕输出 `整数个数: 20`、`最大整数: 97`、`最小整数: 4`；隔 1 秒再跑一次，文件内容换成 `88 50 95 98 50 45 51 6 43 20 46 4 47 33 43 21 8 77 57 42`，输出 `整数个数: 20`、`最大整数: 98`、`最小整数: 4`。两次的个数都是 20，最大最小都和文件里的内容对得上。

    !!! note "同一秒内连跑两次会得到同一串数"
        种子是 `time(NULL)`，单位是秒。同一秒内启动的两次运行拿到的是同一个种子，`rand` 从头开始的序列当然一模一样。这不是错误，是"秒级种子"的固有粒度；换成毫秒级种子或者把上一次的结果存下来做种子，都能避开。

    > 易错：① 忘了 `srand`（或者把 `srand` 写进循环里），每次运行都出同一串数；② 最大最小的初值写 0，数据全是负数时结果就错了；③ 写完不 `fclose` 就换个流去读，缓冲区还没落盘，读到的可能是空文件；④ 个数直接打印写文件时用的 `N`，而不是从文件里数出来。

---

### 7 · 统计各不同整数的出现次数

编写程序检索指定的整数文件，统计文件中各个不同整数在文件中的出现次数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    #define MAXN 1000

    int cmp(const void *p, const void *q)
    {
        int a = *(const int *)p;
        int b = *(const int *)q;

        return (a > b) - (a < b);
    }

    int main(void)
    {
        char fname[256];
        FILE *fp;
        int a[MAXN], n = 0, i;

        printf("请输入整数文件名: ");
        if (scanf("%255s", fname) != 1)
            return 0;

        if ((fp = fopen(fname, "r")) == NULL) {
            printf("无法打开文件 %s\n", fname);
            return 1;
        }
        while (n < MAXN && fscanf(fp, "%d", &a[n]) == 1)
            n++;
        fclose(fp);

        qsort(a, n, sizeof a[0], cmp);        /* 排序后相同的整数必定相邻 */

        for (i = 0; i < n; ) {
            int j = i;
            while (j < n && a[j] == a[i])
                j++;
            printf("%d 出现 %d 次\n", a[i], j - i);
            i = j;
        }
        return 0;
    }
    ```

??? note "解析"

    思路：一次读不完就统计不了——读到某个整数时还不知道后面有没有同样的值。所以先把文件里的整数全部读进数组，用 `qsort` 排好序，再从头扫一遍：相同的整数排序后必定挨在一起，把连续相同的一段数出来，这段的长度就是这个整数的出现次数。

    关键点：

    1. `qsort` 的比较函数返回 `(a > b) - (a < b)`：两个关系表达式各取 0 或 1，相减得 -1、0、1，正好对应小于、等于、大于。直接写 `return a - b;` 在多数情况下也能用，但两个数相差超过 `int` 的范围时相减会溢出。
    2. 计数循环里 `i` 只在外层步进：内层用 `j` 一直探到第一个不等于 `a[i]` 的位置，`j - i` 就是出现次数，然后 `i = j` 从下一段继续。忘了 `i = j` 的话同一个值会被数好几遍。
    3. 数组开了 `MAXN` 上限。循环条件里 `n < MAXN` 写在前面——先判上限再读，不会写越界。文件里的整数多于 `MAXN` 时后面的读不进来，需要更大容量就把 `MAXN` 改大。
    4. 输出按值从小到大排列，这是排序带来的副产品。
    5. 空文件时 `n` 为 0，循环一次都不执行，程序正常结束、不输出任何行。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`ints.txt` 的内容是 `3 1 4 1 5 9 2 6 5 3 5`，共 11 个整数；程序输出 7 行，依次是 `1 出现 2 次`、`2 出现 1 次`、`3 出现 2 次`、`4 出现 1 次`、`5 出现 3 次`、`6 出现 1 次`、`9 出现 1 次`，与手工数出来的一致。换成空文件，输出为空。

    > 易错：① 比较函数写成 `return a - b;`；② 数完一段忘了把 `i` 跳到 `j`，同一个值被输出多次；③ 边读边统计——同一个整数的计数会被后来的文件内容推翻，必须先把数据全部读进来。

---

### 8 · 有序链表统计整数出现次数

试按以下要求编写程序：

从整数文件中读入整数，构造一个由小到大顺序链接的整数链表，并统计各整数在文件中出现的次数，然后按由小到大的顺序输出各整数及其出现次数。

为实现问题的要求，链表的表元类型应包含 3 个元素：值、计数器和后继表元指针。主函数读入文件的名字，打开文件；循环从文件读入整数，调用函数 `insert()`；最后调用函数 `write()`，输出链表各表元中的值和次数。函数 `insert()` 首先在链表中检查新读入的整数是否已在链表中，如已在链表中，则增加其计数即可，否则要为它建立一个新表元，并插入。函数 `write()` 输出链表各表元的值和次数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    typedef struct Node {
        int value;              /* 值 */
        int count;              /* 计数器 */
        struct Node *next;      /* 后继表元指针 */
    } Node;

    /* 把 x 插入有序链表：已在链表中就加计数，否则新建表元插到应在的位置 */
    Node *insert(Node *head, int x)
    {
        Node *p = head, *prev = NULL, *q;

        while (p != NULL && p->value < x) {
            prev = p;
            p = p->next;
        }

        if (p != NULL && p->value == x) {
            p->count++;
            return head;
        }

        q = malloc(sizeof *q);
        if (q == NULL) {
            printf("内存分配失败\n");
            exit(1);
        }
        q->value = x;
        q->count = 1;
        q->next = p;

        if (prev == NULL)
            return q;           /* 插在表头，新的表头要交回给主函数 */
        prev->next = q;
        return head;
    }

    /* 输出链表各表元中的值和次数 */
    void write(const Node *head)
    {
        const Node *p;

        for (p = head; p != NULL; p = p->next)
            printf("%d 出现 %d 次\n", p->value, p->count);
    }

    int main(void)
    {
        char fname[256];
        FILE *fp;
        Node *head = NULL, *p;
        int x;

        printf("请输入文件名: ");
        if (scanf("%255s", fname) != 1)
            return 0;

        if ((fp = fopen(fname, "r")) == NULL) {
            printf("无法打开文件 %s\n", fname);
            return 1;
        }
        while (fscanf(fp, "%d", &x) == 1)
            head = insert(head, x);
        fclose(fp);

        write(head);

        while (head != NULL) {
            p = head;
            head = head->next;
            free(p);
        }
        return 0;
    }
    ```

??? note "解析"

    思路：每从文件里读到一个整数就交给 `insert()`。`insert()` 从表头开始找第一个"值不小于 `x`"的表元：如果这个表元的值正好等于 `x`，说明链表中已经有这个整数，把它的计数器加一就行；否则新建一个表元插在这个位置。链表从头到尾始终保持升序，所以最后 `write()` 顺着指针走一遍，输出的就是从小到大排列的各个整数及其出现次数。

    关键点：

    1. 表元类型按题面要求写三个成员：值 `value`、计数器 `count`、后继指针 `next`。
    2. `insert()` 返回链表头指针。新表元可能插在表头（链表原来是空的，或者 `x` 比所有已有值都小），这时新表元成了新的表头，主函数必须用返回值把它接住——主函数里写的是 `head = insert(head, x);`。若把 `insert` 定义成 `void`，表头的变化就丢在函数里了，只能改用二级指针传参。
    3. 表头指针的初值必须是 `NULL`，表示空链表。`while (p != NULL && p->value < x)` 里两个条件都不能省：先保证没走到链表尾，再取值比较。
    4. 相等时把计数加一之后直接 `return`，不要再往下走建新表元——这是"同一个整数只占一个表元"的关键。
    5. `malloc` 之后要判 `NULL`。内存分配失败就没法建新表元了，这里打印一句提示后退出。
    6. 链表表元是 `malloc` 出来的，程序结束前逐个 `free` 掉。
    7. 用有序链表的好处是读完之后不用再排序，`write()` 直接输出就是升序；数组写法要额外排一次序（见题 7）。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：拿和题 7 相同的 `ints.txt`（`3 1 4 1 5 9 2 6 5 3 5`）跑，输出 7 行，从 `1 出现 2 次` 到 `9 出现 1 次`，与题 7 的数组解法逐行完全相同——一个用排序后的数组、一个用有序链表，两条路互相印证。换成空文件，`write()` 没有任何输出。

    !!! note "为什么从表头往后找插入位置"
        链表是有序的，从表头顺着 `next` 扫过去，第一个值不小于 `x` 的位置就是它该待的地方，一趟就够；`prev` 一路跟着，要插在中间时直接改两个指针。单链表不能往回走，"从后往前找"这条路走不通。

    > 易错：① `insert` 写成 `void`，表头变化丢掉；② 值相等时忘了直接返回，结果同一个整数建了多个表元；③ `malloc` 之后不判空就直接解引用；④ 忘了把 `head` 初值置 `NULL`，链表从一个野指针开始；⑤ 插入时没有维护 `prev`，新表元接不上前一个。

---

### 9 · 按行求和输出到另一个文件

设有一个整数文件，每行有若干个整数，要求编写程序，求文件中各行整数之和并输出到另一个文件。假定整数文件中每行的整数个数不定，每行最后一个整数之后可以有多余的空格符，也可能直接以换行符结束。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    #define MAXLINE 4096

    int main(void)
    {
        char src[256], dst[256], line[MAXLINE];
        FILE *in, *out;
        int lineno = 0;

        printf("请输入源文件名: ");
        if (scanf("%255s", src) != 1)
            return 0;
        printf("请输入目标文件名: ");
        if (scanf("%255s", dst) != 1)
            return 0;

        if ((in = fopen(src, "r")) == NULL) {
            printf("无法打开文件 %s\n", src);
            return 1;
        }
        if ((out = fopen(dst, "w")) == NULL) {
            printf("无法创建文件 %s\n", dst);
            fclose(in);
            return 1;
        }

        while (fgets(line, sizeof line, in) != NULL) {
            char *p = line;
            long sum = 0;

            for (;;) {
                char *end;
                long v = strtol(p, &end, 10);
                if (end == p)       /* 这一行再没有整数了 */
                    break;
                sum += v;
                p = end;
            }

            fprintf(out, "第 %d 行整数之和: %ld\n", ++lineno, sum);
        }

        fclose(in);
        fclose(out);
        return 0;
    }
    ```

??? note "解析"

    思路：用 `fgets` 一行一行地读，每读完一行就在这一行里反复取整数累加，再把这一行的和写进目标文件。按行切分交给 `fgets`，行内取数交给 `strtol`，两层各管一件事。

    关键点：

    1. `fgets` 把整行（连同行尾的换行符）读进缓冲区，"每行整数个数不定"这件事天然就被处理掉了：读进来的这一行里有几个整数就算几个。
    2. 题面提到的两种情况都不用特殊处理：行尾有多余空格时，`fgets` 读进来的字符串以空格加换行结尾；直接以换行符结束时，就以换行结尾。下面取数的循环遇到两种情况都会自然停下。
    3. `strtol(p, &end, 10)` 从 `p` 开始跳过空白、读出一个十进制整数，并把"读到的位置"写到 `end` 里；`end == p` 表示这一段再没有整数了，循环退出。把 `p` 更新成 `end` 再读下一个——这是"在一行里连续取数"的标准写法。
    4. `strtol` 返回 `long`，累加变量 `sum` 就用 `long`，输出配 `%ld`。换成 `int` 在整数多、数值大的行上会溢出。
    5. 空白行（一个整数都没有）的和是 0，照样输出一行，不跳过——这样输出文件的行号和源文件的行号能一一对上。
    6. 输出格式自己定，`第 N 行整数之和: S` 把行号和结果都写清楚，比只写一个数更好核对。
    7. 两个文件都要判空，输出文件用 `"w"` 模式，已存在时先清空。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`sum.txt` 共 5 行，第 1 行 `1 2 3`，第 2 行 `10   20    30`（行尾还有 3 个多余的空格），第 3 行是空白行，第 4 行 `5`，第 5 行 `7 8`。程序写出的 `sum_out.txt` 是 `第 1 行整数之和: 6`、`第 2 行整数之和: 60`、`第 3 行整数之和: 0`、`第 4 行整数之和: 5`、`第 5 行整数之和: 15` 五行，与手工算的一致。源文件名不存在时走 `无法打开文件` 那一支，退出码 1。

    > 易错：① 用 `fscanf(fp, "%d", &x)` 直接逐个读，读完之后分不清这个整数属于哪一行；② 用 `fgets` 之后手工数空格、找数字起点——跳过空白和完成转换这两件事 `strtol` 一起做了；③ 忘了 `fclose` 输出文件，目标文件可能是空的或短一截；④ 空白行被跳过不输出，输出文件的行号和源文件对不上。

---

### 10 · 考生成绩评定与统计

编写对一系列考生进行考试成绩评定与统计的程序。假设试卷共有 10 道试题，每个考生选答其中 5 道。规定每道试题满分 20 分，试卷满分 100 分。规定每个考生的考号及依次选择的 10 道试题的得分组成一行信息。其中，未解答的试题以得分为负数标识；选答试题多于 5 道的，只按前 5 道得分评定成绩；有不合理得分或其他错误，该行信息作废。要求程序对实考人数、各等级得分人数及各道试题解答人数与平均得分进行统计和输出。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    #define NQ   10              /* 试题数 */
    #define FULL 20              /* 每题满分 */
    #define PASS 5               /* 每人选答的试题数 */

    int main(void)
    {
        char fname[256], line[512];
        FILE *fp;
        int solve[NQ] = {0};             /* 各道试题的解答人数 */
        long sum_of[NQ] = {0};           /* 各道试题的得分总和 */
        int level[5] = {0};              /* 优、良、中、及格、不及格 */
        int total = 0;
        int i;

        printf("请输入成绩文件名: ");
        if (scanf("%255s", fname) != 1)
            return 0;

        if ((fp = fopen(fname, "r")) == NULL) {
            printf("无法打开文件 %s\n", fname);
            return 1;
        }

        while (fgets(line, sizeof line, fp) != NULL) {
            int id, s[NQ], ok = 1, answered = 0, picked = 0, sum = 0;

            /* 一行 = 考号 + 10 个得分 */
            if (sscanf(line, "%d%d%d%d%d%d%d%d%d%d%d",
                       &id, &s[0], &s[1], &s[2], &s[3], &s[4],
                       &s[5], &s[6], &s[7], &s[8], &s[9]) != 1 + NQ)
                continue;                /* 数据不完整，该行作废 */

            for (i = 0; i < NQ; i++) {
                if (s[i] < 0)
                    continue;            /* 负数表示未解答 */
                if (s[i] > FULL)
                    ok = 0;              /* 不合理得分 */
                answered++;
            }
            if (!ok || answered < PASS)
                continue;                /* 不合理或有错、选答不足 5 道的行作废 */

            /* 只按前 5 道选答题的得分评定成绩 */
            for (i = 0; i < NQ && picked < PASS; i++) {
                if (s[i] < 0)
                    continue;
                sum += s[i];
                picked++;
            }

            total++;
            if (sum >= 90)      level[0]++;
            else if (sum >= 80) level[1]++;
            else if (sum >= 70) level[2]++;
            else if (sum >= 60) level[3]++;
            else                level[4]++;

            for (i = 0; i < NQ; i++)
                if (s[i] >= 0) {
                    solve[i]++;
                    sum_of[i] += s[i];
                }
        }
        fclose(fp);

        printf("实考人数: %d\n", total);
        printf("优（90～100 分）: %d 人\n", level[0]);
        printf("良（80～89 分）: %d 人\n", level[1]);
        printf("中（70～79 分）: %d 人\n", level[2]);
        printf("及格（60～69 分）: %d 人\n", level[3]);
        printf("不及格（60 分以下）: %d 人\n", level[4]);

        printf("各道试题的解答人数与平均得分:\n");
        printf("题号  解答人数  平均得分\n");
        for (i = 0; i < NQ; i++)
            printf("%3d   %6d   %8.2f\n", i + 1, solve[i],
                   solve[i] ? (double)sum_of[i] / solve[i] : 0.0);
        return 0;
    }
    ```

??? note "解析"

    思路：一行一个考生。先用 `sscanf` 把考号加 10 个得分一起抠出来，数据不齐的直接跳过。然后逐项判定：得分是负数的表示未解答；非负的先查是不是超过每题满分，再数一共答了几道。答过的题不足 5 道、或出现超满分的得分，这一行作废。合格的考生把前 5 道答过的题的得分相加当总成绩，据此归入五个等级；同时把每道题（只要答过）的解答人数加一、得分累加，供最后统计平均分。

    关键点：

    1. 题面说"考号及依次选择的 10 道试题的得分组成一行信息"，所以一行是 11 个数：第 1 个是考号，后面 10 个依次是第 1～10 题的得分。`sscanf` 的返回值应该等于 11，不等于就说明这一行数据不齐，按"其他错误"作废。
    2. "未解答的试题以得分为负数标识"——负数不是错误，是标记。所以负数不参与"得分是否合理"的检查，只表示这道题没答。这样也正好：真实得分不可能为负。
    3. "不合理得分"在这里就是超过每题满分 20 分的得分。判据是 `s[i] > FULL`。
    4. "选答试题多于 5 道的，只按前 5 道得分评定成绩"：取的是前 5 道答过的题，不是第 1～5 题。所以第 1 题没答、第 7 题答了的情况下，第 7 题也要算进这 5 道里。程序里的 `for (i = 0; i < NQ && picked < PASS; i++)` 加 `if (s[i] < 0) continue;` 就是这个意思。
    5. "各道试题解答人数与平均得分"统计的是全体有效考生在每道题上的情况，不套用"只取前 5 道"的限制：第 6 道及以后的题只要有人答过，照样计入解答人数和平均分。
    6. 平均分要防分母为 0：某道题一个人都没答时 `solve[i]` 是 0，用三元表达式给出 `0.00`，不能直接相除。
    7. 等级按满分 100 分划五档：90～100 优、80～89 良、70～79 中、60～69 及格、60 以下不及格。五档人数加起来正好等于实考人数，可以拿这条自查。
    8. 作废的行不参与任何统计——既不进实考人数，也不进各题的人数与总分。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：`score.txt` 共 10 行，其中 4 行作废（1001 和 1005 只答了 4 道，1004 有一个 21 分的超满分得分，1006 只有 3 个得分）。程序输出 `实考人数: 6`，等级人数依次是 1、1、1、1、2；各题解答人数与平均得分是第 1～5 题各 6 人、平均 13.83、13.33、13.00、12.50、12.00，第 6 题 1 人、平均 20.00，第 7～10 题 0 人、0.00——因为只有 1003 答了第 6 题。这与逐行手工推导的结果完全一致。

    !!! note "作废和解答不足是两回事，结果都是这行不要"
        题面把"选答试题多于 5 道"和"有不合理得分或其他错误"分开写，程序里也分开判：`s[i] > FULL` 或数据不齐归到"不合理得分或其他错误"，答过的题不够 5 道归到"选答不足"。两者的处置相同——整行作废。

    > 易错：① 把"前 5 道"理解成"第 1～5 题"；② 负数得分也被判成不合理，结果所有考生全部作废；③ 统计各题平均分时也只用前 5 道，漏掉第 6 题以后的数据；④ 某道题没人答时直接除以 0；⑤ 作废的行仍被计进实考人数，导致等级人数之和和实考人数对不上。
