---
icon: material/notebook-outline
---

# 第七章 · 结构和链表

《C语言程序设计（第3版）》第 7 章课后习题，共 15 题。

### 1 · 通信录条目的结构与输入输出

自己设计一个通信录条目的结构，并分别编写输入和输出一条通信录条目的函数。

??? note "答案"

    ```c
    #include <stdio.h>

    #define NAME_MAX 20
    #define INFO_MAX 40

    /* 一条通信录条目：姓名、电话、邮箱、通信地址 */
    struct Contact {
        char name[NAME_MAX];
        char phone[INFO_MAX];                  /* 电话可能带区号或短横线，用字符串存 */
        char email[INFO_MAX];
        char addr[INFO_MAX * 2];
    };

    /* 输入一条通信录条目 */
    void inputContact(struct Contact *p)
    {
        printf("姓名: ");
        if (scanf("%19s", p->name) != 1)
            return;                            /* 读不到就退出，别拿没读到的内容当数据 */
        printf("电话: ");
        if (scanf("%39s", p->phone) != 1)
            return;
        printf("邮箱: ");
        if (scanf("%39s", p->email) != 1)
            return;
        printf("地址: ");
        if (scanf("%79s", p->addr) != 1)
            return;
    }

    /* 输出一条通信录条目 */
    void printContact(const struct Contact *p)
    {
        printf("%s | %s | %s | %s\n", p->name, p->phone, p->email, p->addr);
    }

    int main(void)
    {
        struct Contact book[2];
        int i;

        for (i = 0; i < 2; i++) {
            printf("--- 第 %d 条 ---\n", i + 1);
            inputContact(&book[i]);
        }

        printf("--- 通信录 ---\n");
        for (i = 0; i < 2; i++)
            printContact(&book[i]);
        return 0;
    }
    ```

??? note "解析"

    思路：结构把一条通信录的几项信息捆成一个整体，输入、输出各写一个函数，形参用指向结构的指针。`main` 里定义结构数组当通信录，逐个调用这两个函数。

    关键点：

    1. 成员用字符数组而不是 `char *`。结构里放指针只是存了个地址，字符串本身还要另外找地方放、另外管释放；姓名、电话这种定长信息用数组最省事，也不用管内存。
    2. 电话用字符数组而不是 `int`：区号、分机号、中间的短横线都不是数字。
    3. 形参写 `struct Contact *p`，函数里用 `p->name` 访问成员；输出函数的形参加 `const`，表示只读。
    4. `scanf` 的 `%19s` 限长 19（数组 20 字节，留 1 个给结尾的 `\0`），比裸 `%s` 安全。`%s` 读不进空白，姓名里要带空格就得换 `fgets`。
    5. 数组名本身就是地址，`scanf("%19s", p->name)` 不写 `&`。写成 `&p->name` 类型也能对上，但没必要。

    !!! note "教材年代不管 `scanf` 的返回值，今天的 `-Wall` 会报警告"
        教材的写法是 `scanf("%19s", p->name);` 直接调用。glibc 如今把 `scanf` 标成 `warn_unused_result`，在 gcc 15.2.0 的 `-Wall` 下不查返回值会给出 `-Wunused-result` 警告，所以答案里逐个查了返回值，读不到就直接返回。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：喂进张三、李四两条记录，输出两行，字段与输入一一对应；程序编译无警告。

    > 易错：① 成员写成 `char *name` 却没给它分配空间，`scanf` 直接往里写就是野指针；② 用裸 `%s` 不限长，输入一长就冲掉后面的成员；③ 实参忘了取地址写成 `inputContact(book[i])`（形参要的是指针，编译期就报类型不匹配）。

---

### 2 · 学生信息结构的定义

试定义一个表示学生信息的结构，要求包含学生的一些常见的固定信息和尽可能完全的学习成绩信息。

??? note "答案"

    ```c
    #include <stdio.h>

    #define COURSE_MAX 10

    /* 一门课的成绩 */
    struct Course {
        char  name[24];
        float credit;
        float score;                           /* 百分制成绩 */
    };

    /* 学生信息：前半是固定信息，后半是成绩信息 */
    struct Student {
        char  id[12];                          /* 学号 */
        char  name[20];                        /* 姓名 */
        char  sex;                             /* 'M' / 'F' */
        int   birth[3];                        /* 年、月、日 */
        char  major[32];                       /* 专业 */
        char  class_no[12];                    /* 班级 */
        char  phone[20];
        char  addr[60];

        struct Course scores[COURSE_MAX];      /* 成绩：一门课一条记录 */
        int   course_count;                    /* 已录入的门数 */
        float total;                           /* 总分 */
        float average;                         /* 平均分 */
    };

    int main(void)
    {
        struct Student s = {
            "2024001", "张三", 'M', {2006, 5, 20},
            "计算机科学与技术", "计科2401", "13800000000", "某市某区某路 1 号",
            {{"数学", 5.0f, 92.0f}, {"英语", 4.0f, 85.5f}, {"C语言", 4.0f, 96.0f}},
            3, 0.0f, 0.0f
        };
        int i;

        for (i = 0; i < s.course_count; i++)
            s.total += s.scores[i].score;
        s.average = s.total / s.course_count;

        printf("学号 %s 姓名 %s 性别 %c 生日 %d-%d-%d\n",
               s.id, s.name, s.sex, s.birth[0], s.birth[1], s.birth[2]);
        printf("专业 %s 班级 %s 电话 %s\n", s.major, s.class_no, s.phone);
        printf("地址 %s\n", s.addr);
        for (i = 0; i < s.course_count; i++)
            printf("  %s 学分 %.1f 成绩 %.1f\n",
                   s.scores[i].name, s.scores[i].credit, s.scores[i].score);
        printf("总分 %.1f 平均分 %.2f\n", s.total, s.average);
        printf("sizeof(struct Student) = %zu，其中成绩数组占 %zu 字节\n",
               sizeof(struct Student), sizeof(s.scores));
        return 0;
    }
    ```

??? note "解析"

    思路：把固定信息和成绩信息分成两块。固定信息一项一个成员；成绩的门数不固定、每门课还要带学分，所以用结构数组加一个门数计数器，总分、平均分留成汇总字段。

    关键点：

    1. 成绩不能摊成 `float math, english, c;` 这样一行一个成员，课程一改就全乱；也不能用几个并列的数组（课程名一个、学分一个、成绩一个）靠下标对齐，任何一个数组漏填，这一项就对不上号。
    2. 门数用 `course_count` 记着，遍历只走前 `course_count` 条。数组开 `COURSE_MAX` 是上限，不代表已经有这么多门课。
    3. 固定信息也要留足字节：`%s` 打印的是以 `\0` 结尾的字符串，数组长度必须比最长内容多 1 个字节。
    4. 学号、电话、邮编用字符数组而不是整型：学号可能有前导 0，电话可能带区号。
    5. 性别这种只有两个取值的成员，用 `char` 存 `'M'`/`'F'` 或者用枚举都行，别用 `int` 去存一个字符串。
    6. 总分、平均分是从成绩算出来的派生数据，录入或改动成绩后要重算，不能让它们和 `scores` 里的事实打架。

    !!! note "字符串塞不下结尾的 `\0`，`%s` 会串到下一个成员"
        "计算机科学与技术" 在 UTF-8 下是 24 字节，`char major[24]` 正好装下这 24 个字节，但结尾的 `\0` 没地方放了（C 允许这么初始化，不算错），`printf("%s")` 就会顺着内存往下读，把后面的班级一起打出来。答案里 `major` 开成 32 字节。中文字符一个字占 3 字节，"数组长度够不够"要按字节数算。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：用初始化列表填一条记录打印，总分 273.5、平均分 91.17 都对；`sizeof(struct Student)` 是 504 字节，其中 10 条成绩记录占 320 字节（一条 32 字节）。

    > 易错：① 结构成员写 `char *name = "张三";`（这么写只是初始化，别的记录就没法改了）；② 成绩用几个并列数组靠下标对齐；③ 把 `COURSE_MAX` 当成实际门数，遍历时读了没录入的空记录。

---

### 3 · 地址类型的定义

试定义地址类型，要求该类型能考虑一般的地址格式。

??? note "答案"

    ```c
    #include <stdio.h>

    /* 一般地址：行政区划由大到小，再接门牌和邮编 */
    struct Address {
        char country[20];                      /* 国家 */
        char province[20];                     /* 省 / 直辖市 */
        char city[30];                         /* 市 */
        char district[30];                     /* 区 / 县 */
        char street[40];                       /* 街道 / 乡镇 */
        char community[30];                    /* 小区 / 村 */
        int  building;                         /* 栋 */
        int  unit;                             /* 单元 */
        char room[16];                         /* 门牌，可能是 "12-3"、"A座" */
        char postcode[8];                      /* 邮编 */

        char receiver[20];                     /* 收件人 */
        char phone[20];
    };

    int main(void)
    {
        struct Address a = {
            "中国", "江苏省", "南京市", "栖霞区", "仙林大道", "文苑小区",
            7, 2, "12-3", "210046", "张三", "13800000000"
        };

        printf("%s%s%s%s%s%s%d栋%d单元%s\n", a.country, a.province, a.city,
               a.district, a.street, a.community, a.building, a.unit, a.room);
        printf("%s 收，邮编 %s，电话 %s\n", a.receiver, a.postcode, a.phone);
        printf("sizeof(struct Address) = %zu\n", sizeof(struct Address));
        return 0;
    }
    ```

??? note "解析"

    思路：一个通用的地址，从大到小排下来是国家、省、市、区、街道（乡镇）、小区（村），再接栋、单元、门牌，另外配上邮编和收件信息。

    关键点：

    1. 行政区划一级一个成员，而不是拼成一个长字符串。这样能按省或市统计、能排序，也能只取"省 + 市 + 街道"这一级打印。
    2. 门牌用字符数组存：`12-3`、`A座`、`101` 混在一起，纯整数的 `int` 表示不了。
    3. 栋、单元这种就是整数的成员，用 `int`；为了统一全写成字符串，用的时候还要再转回来，没必要。
    4. 邮编是定长数字而且可能有前导 0，用字符数组。
    5. 收件人和电话也放进结构：寄件时缺了这两项，地址再全也没用。若这个类型的用途只是"描述位置"，这两项可以拆出去。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：初始化一条记录后打印，拼出 `中国江苏省南京市栖霞区仙林大道文苑小区7栋2单元12-3` 和 `张三 收，邮编 210046，电话 13800000000`；`sizeof(struct Address)` 是 244 字节。

    > 易错：① 整条地址存成一个 `char addr[100]`，之后就再也分不出省市区；② 门牌用 `int`，`12-3` 这种写不进去；③ 邮编写 `int`，前导 0 丢了。

---

### 4 · 成绩录入与排序函数

编写输入学生某门课程成绩的函数，利用该函数输入学生的全部成绩。再编写按某门成绩或总成绩排序的函数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <string.h>

    #define COURSE_MAX 8
    #define STU_MAX 4

    struct Course {
        char  name[24];
        float score;
    };

    struct Student {
        char  id[12];
        char  name[20];
        int   n;                               /* 本学期门数 */
        struct Course c[COURSE_MAX];
        float total;
    };

    /* 输入某个学生第 k 门课的成绩（k 从 0 起） */
    void inputCourseScore(struct Student *p, int k)
    {
        printf("第 %d 门课名称: ", k + 1);
        if (scanf("%23s", p->c[k].name) != 1)
            return;
        printf("成绩: ");
        if (scanf("%f", &p->c[k].score) != 1)
            return;
    }

    /* 用上面的函数输入一个学生的全部成绩，并累加总分 */
    void inputAllScores(struct Student *p)
    {
        int k;

        p->total = 0;
        for (k = 0; k < p->n; k++) {
            inputCourseScore(p, k);
            p->total += p->c[k].score;
        }
    }

    float scoreOf(const struct Student *p, const char *course)
    {
        int k;

        for (k = 0; k < p->n; k++)
            if (strcmp(p->c[k].name, course) == 0)
                return p->c[k].score;
        return -1.0f;                          /* 没修这门课 */
    }

    /* 按某门课成绩由高到低排序；课不存在返回 -1 */
    int sortByCourse(struct Student a[], int num, const char *course)
    {
        int i, j;

        if (num > 0 && scoreOf(&a[0], course) < 0)
            return -1;
        for (i = 0; i < num - 1; i++) {
            int max = i;
            for (j = i + 1; j < num; j++)
                if (scoreOf(&a[j], course) > scoreOf(&a[max], course))
                    max = j;
            if (max != i) {
                struct Student t = a[i];       /* 结构变量可以整体赋值 */
                a[i] = a[max];
                a[max] = t;
            }
        }
        return 0;
    }

    /* 按总成绩由高到低排序 */
    void sortByTotal(struct Student a[], int num)
    {
        int i, j;

        for (i = 0; i < num - 1; i++) {
            int max = i;
            for (j = i + 1; j < num; j++)
                if (a[j].total > a[max].total)
                    max = j;
            if (max != i) {
                struct Student t = a[i];
                a[i] = a[max];
                a[max] = t;
            }
        }
    }

    void printStudents(const struct Student a[], int num)
    {
        int i, k;

        for (i = 0; i < num; i++) {
            printf("%-8s %-6s", a[i].id, a[i].name);
            for (k = 0; k < a[i].n; k++)
                printf(" %s=%.1f", a[i].c[k].name, a[i].c[k].score);
            printf(" 总分=%.1f\n", a[i].total);
        }
    }

    int main(void)
    {
        struct Student a[STU_MAX];
        int i;

        for (i = 0; i < 3; i++) {
            printf("--- 第 %d 个学生 ---\n", i + 1);
            printf("学号 姓名 门数: ");
            if (scanf("%11s%19s%d", a[i].id, a[i].name, &a[i].n) != 3)
                return 0;
            inputAllScores(&a[i]);
        }

        printf("\n原始顺序:\n");
        printStudents(a, 3);

        if (sortByCourse(a, 3, "数学") == 0) {
            printf("\n按 数学 由高到低:\n");
            printStudents(a, 3);
        }
        if (sortByCourse(a, 3, "物理") != 0)
            printf("\n按 物理 排序: 没有这门课，不排\n");

        sortByTotal(a, 3);
        printf("\n按总分由高到低:\n");
        printStudents(a, 3);
        return 0;
    }
    ```

??? note "解析"

    思路：先写最小的那一步——输入"某门课"的成绩；再由它拼出输入全部成绩的函数；排序写两个，比较的键分别是一门课的成绩和总分。

    关键点：

    1. `inputCourseScore(p, k)` 只负责第 k 门课，`inputAllScores(p)` 循环调用它，顺手把总分累加起来。一个函数只干一件事，后面管理系统的录入功能可以整个拿过去用。
    2. 课程用名字标识，所以查成绩退化成"按名字找下标"（`scoreOf`），找不到返回 -1，和 0 分区分得开。
    3. 排序用简单选择排序：每轮找出键最大的那个，和当前位置整体交换。结构变量可以整体赋值，`t = a[i]; a[i] = a[max]; a[max] = t;` 三行就够，不用逐个成员搬。
    4. 按某门课排序之前先确认这门课存在，不存在就直接返回 -1，不然所有键都是 -1，排完顺序看着莫名其妙。
    5. 降序改升序只差比较方向，把 `>` 换成 `<` 就行。
    6. `n` 是实际门数、`COURSE_MAX` 是数组上限，遍历用 `n`。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：三个学生各录三门课（王五第三门填的是"物理"），按数学排得 张三(92) → 王五(85) → 李四(78)，按总分排得 273.5 → 260.0 → 257.5；查没人修过的"物理"时函数返回 -1，程序打印"没有这门课，不排"。

    > 易错：① 排序时只交换了成绩，学号姓名没跟着走，数据错位；② 比较写成 `=`（把数据写坏了）或者写成 `>=` 导致相等时反复交换；③ 把 `n` 写成 `COURSE_MAX`，把没录入的空记录也拿去排。

---

### 5 · 班级信息管理系统

利用前面的结果，编写一个小型的班级同学信息的管理系统。要求至少设有以下实用功能：录入学生信息，求某一门课程的总分、平均分，按姓名或学号查找学生的信息并显示，顺序浏览学生信息，按指定的若干门课程或按总分由高到低显示学生信息等。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <string.h>

    #define STU_MAX 50
    #define COURSE_COUNT 3

    static const char *course_name[COURSE_COUNT] = {"数学", "英语", "C语言"};

    struct Student {
        char  id[12];
        char  name[20];
        float score[COURSE_COUNT];
        float total;
    };

    static struct Student stu[STU_MAX];
    static int stu_count = 0;

    /* 1 录入学生信息 */
    static void addStudent(void)
    {
        struct Student s;
        int k;

        if (stu_count >= STU_MAX) {
            printf("名单已满\n");
            return;
        }
        printf("学号 姓名: ");
        if (scanf("%11s%19s", s.id, s.name) != 2)
            return;
        s.total = 0;
        for (k = 0; k < COURSE_COUNT; k++) {
            printf("%s 成绩: ", course_name[k]);
            if (scanf("%f", &s.score[k]) != 1)
                return;
            s.total += s.score[k];
        }
        stu[stu_count++] = s;                  /* 结构整体赋值，存进名单 */
        printf("已录入，当前共 %d 人\n", stu_count);
    }

    static void printStudent(const struct Student *p)
    {
        int k;

        printf("%-10s %-8s", p->id, p->name);
        for (k = 0; k < COURSE_COUNT; k++)
            printf(" %8.1f", p->score[k]);
        printf("   总分 %6.1f  平均 %5.2f\n", p->total, p->total / COURSE_COUNT);
    }

    /* 2 求某门课程的总分与平均分 */
    static void courseStat(void)
    {
        int k, i;
        float sum = 0;

        if (stu_count == 0) {
            printf("还没有学生\n");
            return;
        }
        printf("课程号 1~%d: ", COURSE_COUNT);
        if (scanf("%d", &k) != 1)
            return;
        if (k < 1 || k > COURSE_COUNT) {
            printf("课程号不合法\n");
            return;
        }
        for (i = 0; i < stu_count; i++)
            sum += stu[i].score[k - 1];
        printf("%s: 总分 %.1f，平均分 %.2f\n",
               course_name[k - 1], sum, sum / stu_count);
    }

    /* 3 按姓名或学号查找并显示 */
    static void findStudent(void)
    {
        int type, i;
        char key[20];

        printf("1=姓名 2=学号: ");
        if (scanf("%d", &type) != 1)
            return;
        printf("关键字: ");
        if (scanf("%19s", key) != 1)
            return;
        for (i = 0; i < stu_count; i++) {
            const char *field = (type == 1) ? stu[i].name : stu[i].id;

            if (strcmp(field, key) == 0) {
                printStudent(&stu[i]);
                return;
            }
        }
        printf("没有找到 %s\n", key);
    }

    /* 5 按指定的若干门课的成绩之和（一门也不指定就是总分）由高到低显示 */
    static void rankBy(const int course[], int cnt)
    {
        const struct Student *idx[STU_MAX];    /* 只排下标的指针数组，不动名单顺序 */
        float key[STU_MAX];
        int i, j, k;

        if (stu_count == 0) {
            printf("还没有学生\n");
            return;
        }
        for (i = 0; i < stu_count; i++) {
            idx[i] = &stu[i];
            if (cnt == 0) {
                key[i] = stu[i].total;
            } else {
                key[i] = 0;
                for (k = 0; k < cnt; k++)
                    key[i] += stu[i].score[course[k]];
            }
        }
        for (i = 0; i < stu_count - 1; i++) {  /* 简单选择排序，降序 */
            int max = i;

            for (j = i + 1; j < stu_count; j++)
                if (key[j] > key[max])
                    max = j;
            if (max != i) {
                const struct Student *tp = idx[i];
                float tk = key[i];

                idx[i] = idx[max];
                idx[max] = tp;
                key[i] = key[max];
                key[max] = tk;
            }
        }
        for (i = 0; i < stu_count; i++)
            printStudent(idx[i]);
    }

    int main(void)
    {
        int choice, k, course[COURSE_COUNT], cnt;

        do {
            printf("\n1 录入  2 某门课总分/平均分  3 查找  4 浏览  "
                   "5 排序显示  0 退出\n请选择: ");
            if (scanf("%d", &choice) != 1)
                break;
            switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                courseStat();
                break;
            case 3:
                findStudent();
                break;
            case 4:
                if (stu_count == 0)
                    printf("还没有学生\n");
                for (k = 0; k < stu_count; k++)
                    printStudent(&stu[k]);
                break;
            case 5:
                printf("课程号 1~%d，多个用空格隔开，0 结束（直接 0 就是按总分）: ",
                       COURSE_COUNT);
                cnt = 0;
                for (;;) {
                    if (scanf("%d", &k) != 1)
                        break;
                    if (k == 0)
                        break;
                    if (k >= 1 && k <= COURSE_COUNT && cnt < COURSE_COUNT)
                        course[cnt++] = k - 1;
                    else
                        printf("忽略不合法课程号 %d\n", k);
                }
                rankBy(course, cnt);
                break;
            case 0:
                printf("退出\n");
                break;
            default:
                printf("没有这个选项\n");
                break;
            }
        } while (choice != 0);
        return 0;
    }
    ```

??? note "解析"

    思路：以题 2、题 4 的结构为基础，学生放在定长数组里，用一个菜单循环（`switch`）把五项功能串起来：录入、某门课总分与平均分、按姓名或学号查找、顺序浏览、按指定的若干门课或总分排序显示。

    关键点：

    1. 数据只有一份：`stu[]` 加 `stu_count`。各功能都在这一份数据上读写，不要每个功能各自存一份。
    2. 录入：读齐一条填进数组，`stu[stu_count++] = s;` 一句结构整体赋值就完成入库。
    3. 求总分、平均分：循环累加一列再除以人数，人数为 0 时先挡住。
    4. 查找：姓名和学号都是字符串，用 `strcmp` 比较，相等返回 0。用一个 `field` 指针把"按姓名还是按学号"两个分支收成一句。
    5. 排序显示：题干要"按指定的若干门课程或按总分"，这里合成一个 `rankBy(course[], cnt)`——一门课也不指定（`cnt == 0`）就按总分，指定了就按这几门课成绩之和。排的是指向记录的指针数组，名单本身的录入顺序不动，浏览时仍是录入顺序。
    6. 排序用选择排序，比较的键提前算进 `key[]`，交换时键和指针一起换，省得每次比较都重新求和。
    7. 菜单用 `do { ... } while (choice != 0)`；每个 `scanf` 都查返回值，输入结束（EOF）就结束循环。
    8. 规模按一个班 50 人、3 门课定死。要更大就把数组换成链表动态申请（见题 7 到题 11）。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：菜单脚本跑一遍——录 3 人后，选"某门课总分/平均分"看 C语言，得总分 230.0、平均分 76.67；按姓名查"张三"打出一行完整记录；浏览打出 3 行；按"数学 + 英语"两门课排序显示的次序是 S01（170）、S02（155）、S03（150），与按总分排的次序一致。

    > 易错：① 每个功能各自维护一份数组，改了一处另一处还是旧值；② 排序直接对名单本身做，把"顺序浏览"的顺序也改掉了；③ 求平均分时除以课程门数而不是人数；④ 菜单里的 `scanf` 不查返回值，输入结束时会死循环刷屏。

---

### 6 · 扑克牌的洗牌、发牌与比大小

一张扑克牌可用结构类型描述，一副扑克牌的 52 张牌则是一个结构数组，另引入表示牌面值的字符串指针数组和表示牌花色的字符串指针数组。试编写洗牌函数和供 4 人玩牌的发牌函数、两张牌的大小比较函数等。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    #define SUIT_COUNT   4
    #define RANK_COUNT   13
    #define PLAYER_COUNT 4
    #define DECK_SIZE    (SUIT_COUNT * RANK_COUNT)

    struct Card {
        int suit;                              /* 0~3：黑桃、红桃、方块、梅花 */
        int rank;                              /* 1~13：A、2、…、K */
    };

    static const char *suit_name[SUIT_COUNT] = {"黑桃", "红桃", "方块", "梅花"};
    static const char *rank_name[RANK_COUNT] = {"A", "2", "3", "4", "5", "6", "7",
                                                "8", "9", "10", "J", "Q", "K"};

    /* 建立一副按花色、面值排好的牌 */
    void initDeck(struct Card deck[])
    {
        int s, r, k = 0;

        for (s = 0; s < SUIT_COUNT; s++)
            for (r = 1; r <= RANK_COUNT; r++) {
                deck[k].suit = s;
                deck[k].rank = r;
                k++;
            }
    }

    /* 洗牌：从头到尾走一遍，让第 i 张和它前面（含自己）随机的一张互换 */
    void shuffle(struct Card deck[], int n)
    {
        int i;

        for (i = 0; i < n; i++) {
            int j = rand() % (i + 1);
            struct Card t = deck[i];

            deck[i] = deck[j];
            deck[j] = t;
        }
    }

    /* 发牌：轮流发，每人 13 张；发完各自按面值从小到大理牌 */
    void deal(const struct Card deck[], struct Card hand[PLAYER_COUNT][RANK_COUNT])
    {
        int i, p, k;

        for (i = 0; i < DECK_SIZE; i++)
            hand[i % PLAYER_COUNT][i / PLAYER_COUNT] = deck[i];

        for (p = 0; p < PLAYER_COUNT; p++)     /* 插入排序理牌 */
            for (i = 1; i < RANK_COUNT; i++) {
                struct Card t = hand[p][i];

                for (k = i; k > 0 && hand[p][k - 1].rank > t.rank; k--)
                    hand[p][k] = hand[p][k - 1];
                hand[p][k] = t;
            }
    }

    /* 比大小：面值大的牌大；面值相同再比花色（黑桃 > 红桃 > 方块 > 梅花） */
    int compareCard(struct Card a, struct Card b)
    {
        if (a.rank != b.rank)
            return a.rank > b.rank ? 1 : -1;
        if (a.suit != b.suit)
            return a.suit < b.suit ? 1 : -1;   /* suit 小的算大 */
        return 0;
    }

    void printCard(struct Card c)
    {
        printf("%s%s", suit_name[c.suit], rank_name[c.rank - 1]);
    }

    int main(void)
    {
        struct Card deck[DECK_SIZE], hand[PLAYER_COUNT][RANK_COUNT];
        int seen[DECK_SIZE] = {0};
        int i, p, same = 1;

        srand((unsigned)time(NULL));
        initDeck(deck);
        shuffle(deck, DECK_SIZE);

        for (i = 0; i < DECK_SIZE; i++) {      /* 洗牌只换位置，52 张牌应当互不相同 */
            int idx = deck[i].suit * RANK_COUNT + deck[i].rank - 1;

            if (seen[idx]++)
                same = 0;
        }
        printf("洗牌后 52 张牌互不相同: %s\n", same ? "是" : "否");

        deal(deck, hand);
        for (p = 0; p < PLAYER_COUNT; p++) {
            printf("第 %d 家:", p + 1);
            for (i = 0; i < RANK_COUNT; i++) {
                printf(" ");
                printCard(hand[p][i]);
            }
            printf("\n");
        }

        printf("黑桃A 对 红桃K: %d\n", compareCard((struct Card){0, 1}, (struct Card){1, 13}));
        printf("黑桃A 对 黑桃A: %d\n", compareCard((struct Card){0, 1}, (struct Card){0, 1}));
        printf("梅花5 对 方块5: %d\n", compareCard((struct Card){3, 5}, (struct Card){2, 5}));
        return 0;
    }
    ```

??? note "解析"

    思路：牌用 `struct Card`（花色 + 面值两个 `int`）表示，一副 52 张就是结构数组；牌面的文字放两个字符串指针数组，按 0 起的下标去取。洗牌、发牌、比大小各写一个函数。

    关键点：

    1. `suit_name`、`rank_name` 就是题干说的"字符串指针数组"：一个存"黑桃"到"梅花"，一个存 `A` 到 `K`，用下标取名字，牌面文字只写一遍。
    2. 洗牌用 Fisher–Yates：从头到尾走一遍，让第 i 张和随机选出的第 j 张（`0 <= j <= i`）互换。每张牌都恰好被抽到一次，52 张牌不多不少。
    3. 随机数用 `rand()`，用之前先 `srand()` 播种。不播种每次运行都是同一副牌；用 `time(NULL)` 播种，每次运行都不同。`rand()` 的具体序列由实现决定，标准只保证返回值落在 `0` 到 `RAND_MAX` 之间。
    4. 发牌就是轮流发：第 i 张发给第 `i % 4` 家，四家各 13 张。发完各自按面值理一次牌（插入排序），方便看牌。
    5. 比大小先比面值，面值一样再比花色。花色之间的大小题面没说，是要自己定的约定（这里定黑桃 > 红桃 > 方块 > 梅花），约定一改只需改 `compareCard` 里那两行。
    6. 程序里加了个自检：洗完牌后按"花色 × 13 + 面值"打表统计一遍，确认 52 张牌两两不同，也就是洗牌确实只是换了位置。
    7. 结构可以整体赋值，所以交换两张牌写 `t = deck[i]; deck[i] = deck[j]; deck[j] = t;` 即可。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：把种子写成 `srand(1)` 跑一遍，自检打印"洗牌后 52 张牌互不相同: 是"，四家各 13 张、合起来正好一副；比大小三组分别得 `-1`（黑桃A 对 红桃K）、`0`（黑桃A 对 黑桃A）、`-1`（梅花5 对 方块5，同点按花色）。种子换回 `time(NULL)` 后隔一秒连跑两次，两次发牌顺序不同。

    > 易错：① 洗牌写成"随机取两个下标换若干轮"，换的次数全靠猜，每张牌被换到的概率还不均匀；② 忘了 `srand`，每次运行都是同一副牌；③ 发牌按下标分段（第 1 到 13 张给第一家）而不是轮流发；④ 用 `rand() % 52` 反复重试来洗牌，理论上可能一直不结束。

---

### 7 · 两个有序链表的合并

编写实现将两个已知的有序链表合并成一个有序链表的函数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct Node {
        int data;
        struct Node *next;
    };

    /* 把数组里的数按顺序尾插到 head 后面，head 是辅助表元 */
    void buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        while (tail->next != NULL)
            tail = tail->next;
        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            tail->next = p;
            tail = p;
        }
    }

    void printList(const char *name, const struct Node *head)
    {
        const struct Node *p;

        printf("%s:", name);
        for (p = head->next; p != NULL; p = p->next)
            printf(" %d", p->data);
        printf("\n");
    }

    void freeList(struct Node *head)
    {
        struct Node *p = head->next;

        while (p != NULL) {
            struct Node *t = p;

            p = p->next;
            free(t);
        }
        head->next = NULL;
    }

    /* 把 h2 归并进 h1（两条链都带辅助表元），返回合并后的表头 */
    struct Node *mergeList(struct Node *h1, struct Node *h2)
    {
        struct Node *p1 = h1, *p2 = h2, *t;

        while (p1->next != NULL && p2->next != NULL) {
            if (p1->next->data <= p2->next->data) {
                p1 = p1->next;                 /* h1 的当前结点已就位，推进 */
            } else {
                t = p2->next;                  /* 摘下 h2 的当前结点 */
                p2->next = t->next;
                t->next = p1->next;            /* 插到 p1 之后 */
                p1->next = t;
                p1 = t;
            }
        }
        if (p1->next == NULL)
            p1->next = p2->next;               /* h1 走完，h2 剩下的整段接上 */
        p2->next = NULL;
        return h1;
    }

    int main(void)
    {
        struct Node d1 = {0, NULL}, d2 = {0, NULL};
        const int a[] = {1, 3, 5, 8}, b[] = {2, 3, 6, 7, 9};

        buildList(&d1, a, 4);
        buildList(&d2, b, 5);
        printList("链表1", &d1);
        printList("链表2", &d2);

        mergeList(&d1, &d2);
        printList("合并后", &d1);
        printList("链表2", &d2);               /* 结点被摘走，剩下空表 */

        freeList(&d1);
        freeList(&d2);
        return 0;
    }
    ```

??? note "解析"

    思路：两个指针各沿一条链走，谁的表元小就留下、推进另一条；`h2` 的表元小就把它从 `h2` 上摘下来，插到 `h1` 已经排好的那一段后面。走完一条链就停，另一条剩下的整段直接接上。

    关键点：

    1. 题干没说链表带不带辅助表元，这里按本章的统一口径用带辅助表元的链表（表头结点不存数据，见题 14 的明文要求）。有了它，"往空链表里插第一个表元"和"往中间插"是同一段代码。
    2. 每一轮比的是 `p1->next` 和 `p2->next`，`p1` 始终停在"已排好的最后一段"上。插的时候先摘后接，两句的顺序是 `t->next = p1->next;` 再 `p1->next = t;`。
    3. 搬完一个表元必须让 `p1 = t` 跟上，否则下一轮还在拿旧位置比，顺序会乱。
    4. 循环只要一条链走完就能停：`if (p1->next == NULL) p1->next = p2->next;` 一句把另一条整段挂上，不用逐个搬。归并类算法都有这个简化。
    5. 值相等时取 `h1` 的表元（用 `<=`），`h1` 原有的相对次序保持不变。
    6. 整个归并只改指针、不申请新表元，合并后表元总数等于两条链之和。时间 O(n+m)、额外空间 O(1)。
    7. 函数返回的 `h1` 就是传进去的那个辅助表元，调用方拿到的表头不变。

    !!! note "教材年代的 `malloc` 写法，今天的 C 里两处都变了"
        教材的写法是 `p = (struct Node *)malloc(sizeof(struct Node));`——既加类型强转，又常常不写 `#include <stdlib.h>`（C89 允许隐式声明，只给一条警告）。C23 删掉了隐式声明，缺 `<stdlib.h>` 直接报 `error: implicit declaration of function 'malloc' [-Wimplicit-function-declaration]`，加不加那个强转报的都是同一条错。C 里 `void *` 能自动转成任何对象指针，所以答案里不写强转，只保留 `#include <stdlib.h>`。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：链表 1 是 1 3 5 8、链表 2 是 2 3 6 7 9，合并后得 1 2 3 3 5 6 7 8 9，共 9 个表元，正好等于两条链之和；链表 2 的结点全被摘走，打印出来是空表。

    > 易错：① 插入的两句顺序写反，`h1` 原来的后半段就丢了；② 搬完忘了 `p1 = t`；③ 只写了循环、忘了最后"整段接上"，合并后少一截；④ 顺手把 `h2` 的表元 `free` 掉（结点还要用，只能 `free` 辅助表元那种真不要的）。

---

### 8 · 链表的三种复制

编写 3 个链表复制函数。第 1 个是复制出相同链接顺序的链表；第 2 个是复制出链接顺序相反的链表；第 3 个是复制出有序链表。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct Node {
        int data;
        struct Node *next;
    };

    void buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        while (tail->next != NULL)
            tail = tail->next;
        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            tail->next = p;
            tail = p;
        }
    }

    void printList(const char *name, const struct Node *head)
    {
        const struct Node *p;

        printf("%s:", name);
        for (p = head->next; p != NULL; p = p->next)
            printf(" %d", p->data);
        printf("\n");
    }

    void freeList(struct Node *head)
    {
        struct Node *p = head->next;

        while (p != NULL) {
            struct Node *t = p;

            p = p->next;
            free(t);
        }
        head->next = NULL;
    }

    static struct Node *newHead(void)
    {
        struct Node *h = malloc(sizeof(struct Node));

        h->data = 0;
        h->next = NULL;
        return h;
    }

    /* 复制出链接顺序相同的链表：尾插 */
    struct Node *copySame(const struct Node *src)
    {
        struct Node *dst = newHead(), *tail = dst;
        const struct Node *p;

        for (p = src->next; p != NULL; p = p->next) {
            struct Node *t = malloc(sizeof(struct Node));

            t->data = p->data;
            t->next = NULL;
            tail->next = t;
            tail = t;
        }
        return dst;
    }

    /* 复制出链接顺序相反的链表：头插 */
    struct Node *copyReverse(const struct Node *src)
    {
        struct Node *dst = newHead();
        const struct Node *p;

        for (p = src->next; p != NULL; p = p->next) {
            struct Node *t = malloc(sizeof(struct Node));

            t->data = p->data;
            t->next = dst->next;
            dst->next = t;
        }
        return dst;
    }

    /* 复制出有序链表：每个新结点插到升序位置上 */
    struct Node *copySorted(const struct Node *src)
    {
        struct Node *dst = newHead();
        const struct Node *p;

        for (p = src->next; p != NULL; p = p->next) {
            struct Node *pre = dst, *t = malloc(sizeof(struct Node));

            while (pre->next != NULL && pre->next->data < p->data)
                pre = pre->next;
            t->data = p->data;
            t->next = pre->next;
            pre->next = t;
        }
        return dst;
    }

    int main(void)
    {
        struct Node d = {0, NULL};
        const int a[] = {5, 3, 8, 1, 9, 2};
        struct Node *c1, *c2, *c3;

        buildList(&d, a, 6);
        printList("源链表  ", &d);

        c1 = copySame(&d);
        c2 = copyReverse(&d);
        c3 = copySorted(&d);
        printList("顺序相同", c1);
        printList("顺序相反", c2);
        printList("有序    ", c3);
        printList("源链表  ", &d);             /* 复制不动源链表 */

        freeList(c1);
        freeList(c2);
        freeList(c3);
        freeList(&d);
        free(c1);                              /* 辅助表元也是 malloc 出来的 */
        free(c2);
        free(c3);
        return 0;
    }
    ```

??? note "解析"

    思路：三个函数共用同一套遍历，区别只在"新表元往哪儿放"——相同顺序用尾插，相反顺序用头插，有序就在插入时按升序找位置。

    关键点：

    1. 复制就是给每一个表元 `malloc` 一份、把 `data` 抄过去，源链表一个字节都不动。这和题 7 那种"复用表元"的合并不一样，复制一定会多出一份内存。
    2. 每个复制函数先造一个辅助表元（`newHead()`），最后返回它，新链表与本章其他链表表示法保持一致。
    3. 头插（`t->next = dst->next; dst->next = t;`）会把后读到的表元排到最前面，所以一趟遍历就得到逆序链表，不必先复制成顺序的再原地反转。
    4. 有序复制用的是插入排序：对每个新表元，从表头往后找到"第一个比它大的表元"，插在它的前驱后面，也就是 `while (pre->next != NULL && pre->next->data < p->data) pre = pre->next;` 然后两句插入。
    5. 复杂度：相同顺序和相反顺序都是 O(n) 时间；有序复制每个表元都要从表头找位置，最坏 O(n²)。空间都是 O(n) 个新表元。
    6. 新链表用完要逐个 `free`，包括那个 `malloc` 出来的辅助表元本身，不能只释放数据表元。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：源链表 5 3 8 1 9 2，三个复制结果分别是 5 3 8 1 9 2（顺序相同）、2 9 1 8 3 5（顺序相反）、1 2 3 5 8 9（有序）；复制前后各打印一次源链表，两次都是 5 3 8 1 9 2，复制没动过它。

    > 易错：① `malloc` 之后只填了 `data`，忘了 `next = NULL`（尾插时问题不大，头插时就接上了垃圾）；② 逆序复制写成"先按顺序复制、再原地反转"，结果对但多一段容易写错的指针操作；③ 有序复制用 `<=` 比较，值相同的表元次序被倒过来；④ 只 `free` 了数据表元，辅助表元漏了。

---

### 9 · 三个有序链表的第 1 个公共整数

编写从 3 个有序整数链表中找出第 1 个只有整数的函数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct Node {
        int data;
        struct Node *next;
    };

    void buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        while (tail->next != NULL)
            tail = tail->next;
        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            tail->next = p;
            tail = p;
        }
    }

    void freeList(struct Node *head)
    {
        struct Node *p = head->next;

        while (p != NULL) {
            struct Node *t = p;

            p = p->next;
            free(t);
        }
        head->next = NULL;
    }

    /* 3 个有序链表（都带辅助表元）中第 1 个公共整数，找到返回 1 并写入 *out */
    int firstCommon(const struct Node *h1, const struct Node *h2,
                    const struct Node *h3, int *out)
    {
        const struct Node *p1 = h1->next, *p2 = h2->next, *p3 = h3->next;

        while (p1 != NULL && p2 != NULL && p3 != NULL) {
            if (p1->data < p2->data)
                p1 = p1->next;                 /* 最小的一条往前走 */
            else if (p2->data < p3->data)
                p2 = p2->next;
            else if (p3->data < p1->data)
                p3 = p3->next;
            else {
                *out = p1->data;               /* 三个都相等，就是它 */
                return 1;
            }
        }
        return 0;
    }

    int main(void)
    {
        struct Node d1 = {0, NULL}, d2 = {0, NULL}, d3 = {0, NULL};
        const int a[] = {1, 3, 5, 7, 9}, b[] = {2, 3, 6, 9}, c[] = {3, 4, 9};
        const int x[] = {1, 4}, y[] = {2, 5}, z[] = {3, 6};
        int v;

        buildList(&d1, a, 5);
        buildList(&d2, b, 4);
        buildList(&d3, c, 3);
        if (firstCommon(&d1, &d2, &d3, &v))
            printf("{1,3,5,7,9} / {2,3,6,9} / {3,4,9} 的第 1 个公共整数: %d\n", v);
        else
            printf("没有公共整数\n");

        freeList(&d1);
        freeList(&d2);
        freeList(&d3);
        buildList(&d1, x, 2);
        buildList(&d2, y, 2);
        buildList(&d3, z, 2);
        if (firstCommon(&d1, &d2, &d3, &v))
            printf("第 2 组: %d\n", v);
        else
            printf("{1,4} / {2,5} / {3,6} 没有公共整数\n");

        freeList(&d1);
        freeList(&d2);
        freeList(&d3);
        buildList(&d1, (const int[]){9}, 1);
        buildList(&d2, (const int[]){9}, 1);
        buildList(&d3, (const int[]){9}, 1);
        if (firstCommon(&d1, &d2, &d3, &v))
            printf("{9} / {9} / {9} 的第 1 个公共整数: %d\n", v);
        return 0;
    }
    ```

??? note "解析"

    题干转写为"第 1 个只有整数的"，此处按"三个链表中都出现的第 1 个整数"理解，也就是求三条有序整数链表的第 1 个公共整数。三个链表的成员都是整数，同一个值在三条链里都出现，就是"都出现"。

    思路：三个指针各指一条链，每轮把"当前值最小的那一条"往前推一格。最小值不可能是公共整数——另外两条链剩下的值都不比它小，而被跳过的值又都严格小于它，所以这个值在别的链里肯定不存在。当三个指针指的值相等时，就是第 1 个公共整数。

    关键点：

    1. 三个指针 `p1`、`p2`、`p3` 各沿一条链走，每轮只推一格，只推"值最小"的那一条。
    2. 判等用三条链的比较串起来：`p1` 最小推 `p1`，`p2` 最小推 `p2`，`p3` 最小推 `p3`，三个条件都不成立就说明三值相等。
    3. 三条链都是升序，所以第一次遇到的公共整数就是最小的那个公共整数，正是题干要的"第 1 个"。
    4. 只要有一条链走完就不可能再有公共整数，函数返回 0。
    5. 接口用"返回 1/0 + `int *out` 带出结果"，这样调用方能区分"没找到"和"找到的值正好是 0"。
    6. 时间 O(n₁+n₂+n₃)、额外空间 O(1)。链表有序是前提，无序链表套不了这个算法。
    7. 题干没说带不带辅助表元，这里仍按本章统一口径用带辅助表元。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：{1,3,5,7,9}、{2,3,6,9}、{3,4,9} 的第 1 个公共整数是 `3`；{1,4}、{2,5}、{3,6} 没有公共整数，函数返回 0；{9}、{9}、{9} 得 `9`。

    > 易错：① 三条链一起往前推，公共整数就这么被推过去了；② 比较写成 `if (p1->data == p2->data)` 之后只推 `p1`、`p2`，`p3` 没跟上；③ 链表无序也照套（前提是有序）；④ 用 0 当"没找到"的返回值，而 0 本身可能是公共整数。

---

### 10 · 表元带两个指针成分

令整数链表的表元包含两个指针成分，一个用于指出从小到大的链接顺序；另一个用于输入的先后顺序。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    /* 表元带两个指针：order 串出从小到大，seq 串出输入先后 */
    struct Node {
        int data;
        struct Node *order;
        struct Node *seq;
    };

    /* 两条链各用一个辅助表元 */
    struct Head {
        struct Node order;
        struct Node seq;
    };

    void initHead(struct Head *h)
    {
        h->order.data = h->seq.data = 0;
        h->order.order = h->order.seq = NULL;
        h->seq.order = h->seq.seq = NULL;
    }

    /* 插入一个值：order 链按升序插，seq 链接在末尾 */
    void insert(struct Head *h, int v)
    {
        struct Node *t = malloc(sizeof(struct Node));
        struct Node *pre = &h->order, *last = &h->seq;

        t->data = v;
        while (pre->order != NULL && pre->order->data < v)
            pre = pre->order;
        t->order = pre->order;
        pre->order = t;

        while (last->seq != NULL)
            last = last->seq;
        t->seq = NULL;
        last->seq = t;
    }

    /* 值为 v 的表元从两条链上同时摘掉、释放；没找到返回 0 */
    int removeValue(struct Head *h, int v)
    {
        struct Node *pre = &h->order, *q = &h->seq, *t;

        while (pre->order != NULL && pre->order->data < v)
            pre = pre->order;
        if (pre->order == NULL || pre->order->data != v)
            return 0;
        t = pre->order;
        pre->order = t->order;                 /* 先在 order 链上摘 */

        while (q->seq != t)
            q = q->seq;
        q->seq = t->seq;                       /* 再从 seq 链上摘 */
        free(t);                               /* 一个结点只释放一次 */
        return 1;
    }

    void printOrder(const struct Head *h)
    {
        const struct Node *p;

        printf("按值从小到大:");
        for (p = h->order.order; p != NULL; p = p->order)
            printf(" %d", p->data);
        printf("\n");
    }

    void printSeq(const struct Head *h)
    {
        const struct Node *p;

        printf("按输入先后  :");
        for (p = h->seq.seq; p != NULL; p = p->seq)
            printf(" %d", p->data);
        printf("\n");
    }

    int main(void)
    {
        struct Head h;
        const int a[] = {5, 3, 8, 1, 9, 2};
        int i;

        initHead(&h);
        for (i = 0; i < 6; i++)
            insert(&h, a[i]);
        printOrder(&h);
        printSeq(&h);

        printf("删除 8 %s\n", removeValue(&h, 8) ? "成功" : "没找到");
        printOrder(&h);
        printSeq(&h);

        printf("删除 4 %s\n", removeValue(&h, 4) ? "成功" : "没找到");
        printOrder(&h);
        printSeq(&h);
        return 0;
    }
    ```

??? note "解析"

    题干只规定了表元要包含哪两个指针成分，没有写要完成的动作，此处按"定义这样的表元，并写出建立链表（同时维护两条链）与按两种顺序输出、删除表元的函数"理解。

    思路：同一批表元挂两条链——`order` 把它们按值从小到大串起来，`seq` 按输入先后串起来。数据只有一份，两条链只是指针不同。

    关键点：

    1. 两个指针成分各管一条链，两条链共用同一批表元：插入时只 `malloc` 一次，两个指针各指一次，`data` 只存一份。
    2. 两条链各自要一个辅助表元（`struct Head` 里的两个成员），这样空链表也能插，头一个表元和中间表元走同一段代码。
    3. 插入分两步：先在 `order` 链上找升序位置插进去，再把同一个表元接到 `seq` 链末尾。两步互不干扰。
    4. 删除必须两边都摘：先从 `order` 链上摘（这时得到表元地址），再到 `seq` 链上找它的前驱、摘掉，最后 `free` 一次。漏摘一条链，那条链就指着已经释放的内存。
    5. 按 `order` 链遍历就是升序输出，按 `seq` 链遍历就是输入顺序输出，两个输出函数只差遍历时用哪个指针。
    6. 代价是一个表元多 8 个字节、插入与删除要维护两条链；换来的是同一批数据可以按两种顺序直接走，不用排序也不用复制。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：依次插入 5 3 8 1 9 2 后，`order` 链是 1 2 3 5 8 9、`seq` 链是 5 3 8 1 9 2；删除 8 后两条链同时变成 1 2 3 5 9 和 5 3 1 9 2；删除不存在的 4 返回"没找到"，两条链都不变。

    > 易错：① 只维护了一条链（`order` 排好了，`seq` 没接上）；② 删除时只摘了 `order` 链就 `free`，`seq` 链成了悬空指针；③ 给两条链各 `malloc` 一份表元，数据存了两份，改一份另一份不跟着变。

---

### 11 · 无序链表中找最小表元并删除

编写从无序的整数链表中找出最小表元，并将它从链表中删除的函数。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    struct Node {
        int data;
        struct Node *next;
    };

    void buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        while (tail->next != NULL)
            tail = tail->next;
        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            tail->next = p;
            tail = p;
        }
    }

    void printList(const struct Node *head)
    {
        const struct Node *p;

        for (p = head->next; p != NULL; p = p->next)
            printf(" %d", p->data);
        printf("\n");
    }

    /* 带辅助表元；找出最小表元、从链表上摘掉并释放，值写入 *out。空链表返回 0 */
    int removeMin(struct Node *head, int *out)
    {
        struct Node *pre = head, *p = head->next;
        struct Node *minPre, *minP;

        if (p == NULL)
            return 0;
        minPre = pre;
        minP = p;
        while (p != NULL) {
            if (p->data < minP->data) {
                minPre = pre;
                minP = p;
            }
            pre = p;
            p = p->next;
        }
        minPre->next = minP->next;             /* 摘掉最小表元 */
        *out = minP->data;
        free(minP);
        return 1;
    }

    int main(void)
    {
        struct Node d = {0, NULL};
        const int a[] = {5, 3, 8, 1, 9, 2};
        int v, i;

        buildList(&d, a, 6);
        printf("原链表:");
        printList(&d);
        for (i = 0; i < 3; i++) {
            if (removeMin(&d, &v)) {
                printf("第 %d 次删掉最小值 %d，剩下:", i + 1, v);
                printList(&d);
            }
        }

        while (removeMin(&d, &v))
            ;                                  /* 把剩下的表元都删掉，链表清空 */
        printf("空链表上再删: %s\n", removeMin(&d, &v) ? "成功" : "没有表元可删");
        return 0;
    }
    ```

??? note "解析"

    思路：走一趟链表，同时记下"最小的表元"和"它的前驱"——要摘掉一个表元，非改它前驱的 `next` 不可，所以前驱必须跟着一起记。扫完摘掉最小表元、`free` 掉，值通过 `*out` 带回去。

    关键点：

    1. 链表无序，只能挨个比一遍，时间 O(n)、额外空间 O(1)。
    2. `minPre` 和 `minP` 成对更新，缺一个就没法删除。
    3. 擂主初值取第 1 个表元（`minPre = head; minP = head->next;`），别用"某个很大的数"或 0 当初始最小值，数据里有负数或 0 就比不过。
    4. 辅助表元在这里的作用很直接：链表里只有 1 个表元、或者最小表元就是第 1 个时，它的前驱是辅助表元，摘除动作和中间表元完全一样，不用为首表元写特判。
    5. 空链表要先挡住，`head->next == NULL` 时直接返回 0。
    6. 接口和题 9 一致：返回 1/0 表示成功与否，值从 `int *out` 带出。
    7. 反复调用这个函数就等于选择排序：每次取出当前最小值，取出来的是一个升序序列。程序最后用 `while (removeMin(...))` 把链表清空，也可以拿它当"链表版清空"用。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：链表 5 3 8 1 9 2 连删三次，依次删掉 1、2、3，剩下 5 8 9；剩下的也删完后链表为空，再删返回"没有表元可删"。

    > 易错：① 只记最小表元、不记前驱，找到之后改不了链；② 初值取 0 或某个"很大的数"当擂主；③ 空链表不判，直接解引用空指针；④ `free` 之后还去读 `minP->data`（先取值、再释放）。

---

### 12 · 法雷序列的链表构造

n 级法雷（Forder）序列 Fₙ 是将分母小于等于 n 的不可约真分数按递增次序排列，并让分数 0/1 作为序列的第 1 个元素，分数 1/1 作为序列的最后一个元素。例如，F₅ 为：0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1。

要求编写程序，输入正整数 n，输出 n 级法雷（Forder）序列 Fₙ，另外，要求程序用链表存储法雷序列。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    /* 法雷序列里的一个分数：分子、分母 + 指向下一个分数的指针 */
    struct Frac {
        int num;
        int den;
        struct Frac *next;
    };

    void insertAfter(struct Frac *p, int num, int den)
    {
        struct Frac *t = malloc(sizeof(struct Frac));

        t->num = num;
        t->den = den;
        t->next = p->next;
        p->next = t;
    }

    /* 在辅助表元 head 后面建出 n 级法雷序列 */
    void buildFarey(struct Frac *head, int n)
    {
        struct Frac *p;

        head->next = NULL;
        insertAfter(head, 0, 1);               /* 第 1 个元素 0/1 */
        insertAfter(head->next, 1, 1);         /* 最后 1 个元素 1/1 */

        for (p = head->next; p != NULL && p->next != NULL; ) {
            if (p->den + p->next->den <= n) {
                /* 相邻两个分数 a/b、c/d：分母之和不超过 n 就把中分数插进去 */
                insertAfter(p, p->num + p->next->num, p->den + p->next->den);
                /* 插完 p 不动：让新建的分数接着和它右边的邻居比下去 */
            } else {
                p = p->next;
            }
        }
    }

    int gcd(int a, int b)
    {
        while (b != 0) {
            int t = a % b;

            a = b;
            b = t;
        }
        return a;
    }

    void printFarey(const struct Frac *head)
    {
        const struct Frac *p;

        for (p = head->next; p != NULL; p = p->next)
            printf(p == head->next ? "%d/%d" : ", %d/%d", p->num, p->den);
        printf("\n");
    }

    void freeFarey(struct Frac *head)
    {
        struct Frac *p = head->next;

        while (p != NULL) {
            struct Frac *t = p;

            p = p->next;
            free(t);
        }
        head->next = NULL;
    }

    int main(void)
    {
        struct Frac head;
        int n, count, growing = 1, irreducible = 1;
        struct Frac *p;

        printf("输入正整数 n: ");
        if (scanf("%d", &n) != 1 || n < 1)
            return 0;

        buildFarey(&head, n);
        printf("F%d = ", n);
        printFarey(&head);

        count = 0;
        for (p = head.next; p != NULL; p = p->next) {
            count++;
            if (gcd(p->num, p->den) != 1)
                irreducible = 0;
            if (p->next != NULL &&
                p->num * p->next->den >= p->next->num * p->den)
                growing = 0;                   /* 交叉相乘比较两个分数 */
        }
        printf("共 %d 项，严格递增: %s，全部不可约: %s\n",
               count, growing ? "是" : "否", irreducible ? "是" : "否");
        freeFarey(&head);
        return 0;
    }
    ```

??? note "解析"

    思路：法雷序列有个好用的性质：相邻两个分数 a/b 和 c/d，只要 b + d 不超过 n，就把中分数 (a+c)/(b+d) 插在它们中间；这么插下去，直到每一对相邻分数的分母之和都大于 n，序列就长成了。链表从 0/1 和 1/1 两个端点开始，按这个规则往里插。

    关键点：

    1. 骨架先摆好：辅助表元后面第 1 个是 0/1、最后 1 个是 1/1。
    2. 造序列就是一趟扫描：`p` 在链上走，看 `p` 和右邻居的分母之和；不超过 n 就把中分数插在 `p` 后面。
    3. 插入之后 `p` 不要前进，让刚插进去的分数接着和右边的邻居比。这样只要一趟扫描就够——每一对相邻分数都被比到"分母之和超过 n"为止，"所有相邻对分母之和都大于 n"正是法雷序列的终止条件。若插完就前进，左半边还得反复扫描才能补上。
    4. 插进去的分数自动不可约、自动落在正确位置：相邻的 a/b 与 c/d 满足 b·c − a·d = 1，中分数 (a+c)/(b+d) 的分子分母互质。程序里对结果做了自检：相邻项交叉相乘验严格递增、逐项验 gcd 为 1，都通过。
    5. 用分子分母交叉相乘（`a*d < c*b`）比较两个分数，不用浮点除法——浮点存不下 1/3 这类分数，位数一多顺序就可能错。
    6. 项数是 1 + Σφ(k)（k 从 1 到 n，φ 是欧拉函数）：n = 5 时 11 项，n = 8 时 23 项，与程序输出的项数吻合。n = 1 时只剩 0/1 和 1/1。
    7. 输入用 `scanf` 读，读不进来或 n 小于 1 就直接返回。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：n = 5 时输出 `0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1`，与题干给的 F₅ 逐项相同，自检打印"共 11 项，严格递增: 是，全部不可约: 是"；n = 8 得 23 项、n = 1 得 `0/1, 1/1`，自检同样通过。

    > 易错：① 插完就把 `p` 往前推，左半边该插的分数漏掉；② 用浮点数比较分数大小，位数一多顺序就错；③ 拿浮点值去重（该判的是不可约分数本身是否相等）；④ 终止条件写错，一直插下去（分母只增不减，写对了自然收敛）。

---

### 13 · 环上的加密函数

试编写按以下加密规则对指定的加密钥匙 key 和原文字符串的加密函数。设原文字符串有 n 个字符，生成的密文字符串也是 n 个字符。将密文字符串的 n 个字符位置按顺时针连成一个环。加密时，从环的起始位置起顺时针方向计数，每当数到第 key 个字符位置时，从原文字符串的第 1 个字符开始，依次将原文中的当前字符放入该密文字符位置中，已填入字符的密文字符位置以后不再在环上计数。重复上述过程，直至原文的 n 个字符全部放入密文环中。由此产生的密文环上的字符序列即为原文的密文。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define MAX_LEN 40

    /* 密文环上的一个字符位置 */
    struct Pos {
        int index;                             /* 是密文里的第几个字符 */
        struct Pos *next;
    };

    /* 原文 plain（n 个字符）按钥匙 key 加密，密文写入 cipher */
    void encrypt(const char *plain, int n, int key, char *cipher)
    {
        struct Pos *first = NULL, *last = NULL, *cur, *prev;
        int i, k;

        for (i = 0; i < n; i++) {              /* 把 n 个位置连成一个环 */
            struct Pos *p = malloc(sizeof(struct Pos));

            p->index = i;
            if (first == NULL)
                first = p;
            else
                last->next = p;
            last = p;
        }
        if (n > 0)
            last->next = first;

        prev = last;
        cur = first;
        for (i = 0; i < n; i++) {
            for (k = 1; k < key; k++) {        /* 从当前位置起数到第 key 个 */
                prev = cur;
                cur = cur->next;
            }
            cipher[cur->index] = plain[i];     /* 原文第 i 个字符放进这个位置 */
            prev->next = cur->next;            /* 这个位置退出环，后面不再数到 */
            free(cur);
            cur = prev->next;
        }
        cipher[n] = '\0';
    }

    int main(void)
    {
        char plain[MAX_LEN + 1], cipher[MAX_LEN + 1];
        int key, n;

        printf("加密钥匙 key: ");
        if (scanf("%d", &key) != 1 || key < 1)
            return 0;
        printf("原文: ");
        if (scanf("%40s", plain) != 1)
            return 0;

        n = (int)strlen(plain);
        encrypt(plain, n, key, cipher);
        printf("原文有 %d 个字符: %s\n", n, plain);
        printf("key = %d 时密文: %s\n", key, cipher);
        return 0;
    }
    ```

??? note "解析"

    思路：这就是约瑟夫环的变形。先把密文的 n 个位置连成一个环，然后按 key 报数：每数到第 key 个位置，就把原文的下一个字符放进这个位置，再把它从环上摘掉。摘除的先后顺序，就是"密文第几个位置放原文第几个字符"的对应表。

    关键点：

    1. 环用单链表加一个前驱指针实现：报数时 `prev` 和 `cur` 一起往前，摘除时 `prev->next = cur->next`。没有前驱指针就找不到"上一家"，删不掉。
    2. 题干说"从环的起始位置起顺时针方向计数"，所以起始位置本身算第 1 个，内层循环走 `key - 1` 步而不是 `key` 步。
    3. 放字符时先读 `cur->index` 再摘结点：密文的下标记下来了，`free` 之后再取就晚了。
    4. key 等于 1 时每次都数到当前位置本身，密文和原文一模一样——这是最好验证的一个特例。key 大于 n 时会绕着环多转几圈，代码不用为它特判。
    5. 摘下的结点立刻 `free`，`cur` 换成 `prev->next` 继续报数。环上只剩一个位置时它的前驱就是自己，这套写法定得住。
    6. 原文用 `scanf("%40s")` 读，遇到空白就停；要加密带空格的句子得改用 `fgets`，再把行尾换行剥掉。字符数用 `strlen` 量。
    7. 复杂度 O(n·key)：每摘一个位置平均要走 key 步。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：key = 3、原文 `abcdefg`（7 个字符）得密文 `fcagebd`；key = 1 得 `abcdefg`；key = 5 得 `fcbdage`；原文只有一个字符 `a` 时得 `a`。

    > 易错：① 报数从"起始位置的下一家"算起 1（题干那句"从环的起始位置起"就丢了）；② 内层循环写成 `k <= key`，相当于把钥匙当 key+1 用；③ 摘结点前忘了先记下标，`free` 之后才去读；④ 环上只剩一个位置时前驱指针处理不当，绕不出来。

---

### 14 · 带辅助表元：集合的并、差、交（结果在 S₁）

用带辅助表元的有序整数链表表示整数集合，分别编写已知两个集合求集合和（S₁=S₁∪S₂）、集合差（S₁=S₁-S₂）、集合交（S₁=S₁∩S₂）的函数。运算结果在链表 S₁。

设 S₁={2,3,5,6}，S₂={3,4,6,8}，则有，集合和 S₁∪S₂={2,3,4,5,6,8}，集合差 S₁-S₂={2,5}，集合交 S₁∩S₂={3,6}。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    /* 有序整数链表的表元 */
    struct Node {
        int data;
        struct Node *next;
    };

    /* 尾插建表，head 是辅助表元 */
    void buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        while (tail->next != NULL)
            tail = tail->next;
        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            tail->next = p;
            tail = p;
        }
    }

    void freeList(struct Node *head)
    {
        struct Node *p = head->next;

        while (p != NULL) {
            struct Node *t = p;

            p = p->next;
            free(t);
        }
        head->next = NULL;
    }

    void printSet(const char *name, const struct Node *head)
    {
        const struct Node *p;

        printf("%s = {", name);
        for (p = head->next; p != NULL; p = p->next)
            printf(p == head->next ? "%d" : ",%d", p->data);
        printf("}\n");
    }

    /* S1 = S1 ∪ S2，S2 用到的表元摘进 S1，用完 S2 变空表 */
    void setUnion(struct Node *s1, struct Node *s2)
    {
        struct Node *p1 = s1, *p2 = s2;

        while (p1->next != NULL && p2->next != NULL) {
            if (p1->next->data < p2->next->data) {
                p1 = p1->next;                 /* S1 这个值更小，留下 */
            } else if (p1->next->data > p2->next->data) {
                struct Node *t = p2->next;     /* 把 S2 的表元摘到 S1 里 */

                p2->next = t->next;
                t->next = p1->next;
                p1->next = t;
                p1 = t;
            } else {
                struct Node *t = p2->next;     /* 两个集合都有，S2 这一份多余 */

                p2->next = t->next;
                free(t);
            }
        }
        if (p1->next == NULL)
            p1->next = p2->next;               /* S1 走完，S2 剩下的整段接上 */
        p2->next = NULL;
    }

    /* S1 = S1 - S2 */
    void setDifference(struct Node *s1, const struct Node *s2)
    {
        struct Node *p1 = s1;
        const struct Node *p2 = s2->next;

        while (p1->next != NULL && p2 != NULL) {
            if (p1->next->data < p2->data) {
                p1 = p1->next;                 /* S2 里没有这个值，留下 */
            } else if (p1->next->data > p2->data) {
                p2 = p2->next;                 /* S2 的值更小，往前赶 */
            } else {
                struct Node *t = p1->next;     /* 相等：从 S1 里删掉 */

                p1->next = t->next;
                free(t);
                p2 = p2->next;
            }
        }
    }

    /* S1 = S1 ∩ S2 */
    void setIntersection(struct Node *s1, const struct Node *s2)
    {
        struct Node *p1 = s1;
        const struct Node *p2 = s2->next;

        while (p1->next != NULL) {
            if (p2 == NULL || p1->next->data < p2->data) {
                struct Node *t = p1->next;     /* S2 里没有这个值，删掉 */

                p1->next = t->next;
                free(t);
            } else if (p1->next->data > p2->data) {
                p2 = p2->next;
            } else {
                p1 = p1->next;                 /* 两边都有，留下 */
                p2 = p2->next;
            }
        }
    }

    int main(void)
    {
        struct Node d1 = {0, NULL}, d2 = {0, NULL};
        const int a[] = {2, 3, 5, 6}, b[] = {3, 4, 6, 8};

        buildList(&d1, a, 4);
        buildList(&d2, b, 4);
        setUnion(&d1, &d2);
        printSet("S1 ∪ S2", &d1);
        printSet("S2", &d2);                   /* 表元被摘走，S2 空了 */

        freeList(&d1);
        buildList(&d1, a, 4);
        buildList(&d2, b, 4);
        setDifference(&d1, &d2);
        printSet("S1 - S2", &d1);
        printSet("S2", &d2);                   /* 求差不动 S2 */

        freeList(&d1);
        buildList(&d1, a, 4);
        setIntersection(&d1, &d2);
        printSet("S1 ∩ S2", &d1);
        printSet("S2", &d2);                   /* 求交不动 S2 */

        freeList(&d1);
        freeList(&d2);
        return 0;
    }
    ```

??? note "解析"

    思路：三个运算都是"两条有序链一起走"的变体。并集：小的留下、大的搬过来、相等就丢掉 S2 那份；差集：S1 里在 S2 中出现过的表元删掉；交集：S1 里没在 S2 中出现的表元删掉。三个函数的运算结果都落在 S1 上。

    关键点：

    1. 两个集合都带辅助表元（题干明说）。表头结点不存数据，`head->next` 才是第 1 个元素，所以"删第 1 个元素"和"删中间元素"是同一段代码。
    2. 三个函数都只改指针、不新建表元——这就是"运算结果在链表 S₁"的实现方式：结果就是 S₁ 自己。
    3. 并集：S2 的表元小就摘下来插到 S1 里（四句：摘、接后、接前、推进）；相等说明 S1 已经有了，把 S2 的这份 `free` 掉；S1 小就 `p1` 前进。走完一条链后，`if (p1->next == NULL) p1->next = p2->next;` 把 S2 剩下的整段接上。
    4. 并集把 S2 的表元搬进了 S1，所以运算结束后 S2 是空表。这是"复用表元、不新建链表"的必然结果；要保留 S2，就先复制一份再求并集（复制函数见题 8）。程序里把 S2 打印出来，正是为了看清这一点。
    5. 差集：S1 的值小于 S2 当前值 → 这个值 S2 里没有，留下、`p1` 前进；大于 → `p2` 前进；相等 → 删掉 S1 这个表元，此时 `p1` 不动，因为顶上来的新邻居还要继续比。S2 走完就停，剩下的 S1 表元全保留。
    6. 交集：思路反过来——把 S1 里不该留的删掉。S2 已经走完，或者 S1 当前值小于 S2 当前值，都说明这个值不在 S2 里，删；S1 值大于 S2 值就 `p2` 前进；相等则两边一起前进、保留下来。
    7. 差集和交集只读 S2，所以它们跑完 S2 还是完整的，可以接着用。
    8. 时间 O(n+m)、额外空间 O(1)。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：S₁ = {2,3,5,6}、S₂ = {3,4,6,8} 时，程序输出 `S1 ∪ S2 = {2,3,4,5,6,8}`、`S1 - S2 = {2,5}`、`S1 ∩ S2 = {3,6}`，三组与题干给的样例完全一致；求并集后 S2 打印为空集，求差、求交之后再打印 S2 仍是 `{3,4,6,8}`。

    > 易错：① 并集里相等时把 S1 的表元删了（该删的是 S2 那一份）；② 并集忘了最后"整段接上"，S1 走完后 S2 剩下的表元没搬过来；③ 差集删掉表元之后 `p1` 还往前推一格，把刚顶上来的表元跳过去了；④ 交集用"S2 走完就结束"来收尾，S1 尾部该删的表元没删。

---

### 15 · 不带辅助表元：集合的并、差、交（结果产生新链表）

用不带辅助表元的有序整数链表表示整数集合，分别编写已知两个集合求集合和（S=S₁∪S₂）、集合差（S=S₁-S₂）、集合交（S=S₁∩S₂）的函数。运算结果产生一个新链表。

??? note "答案"

    ```c
    #include <stdio.h>
    #include <stdlib.h>

    /* 不带辅助表元的有序整数链表：表头指针就是第 1 个表元 */
    struct Node {
        int data;
        struct Node *next;
    };

    /* 尾插建表，返回表头指针 */
    struct Node *buildList(struct Node *head, const int a[], int n)
    {
        struct Node *tail = head;
        int i;

        for (i = 0; i < n; i++) {
            struct Node *p = malloc(sizeof(struct Node));

            p->data = a[i];
            p->next = NULL;
            if (tail == NULL)
                head = tail = p;
            else
                tail = tail->next = p;
        }
        return head;
    }

    void freeList(struct Node *head)
    {
        while (head != NULL) {
            struct Node *t = head;

            head = head->next;
            free(t);
        }
    }

    void printSet(const char *name, const struct Node *head)
    {
        const struct Node *p;

        printf("%s = {", name);
        for (p = head; p != NULL; p = p->next)
            printf(p == head ? "%d" : ",%d", p->data);
        printf("}\n");
    }

    /* 把值 v 接到新链表末尾，返回新的尾指针。dummy 只是函数里拼链用的临时哨兵 */
    static struct Node *append(struct Node *tail, int v)
    {
        struct Node *p = malloc(sizeof(struct Node));

        p->data = v;
        p->next = NULL;
        tail->next = p;
        return p;
    }

    /* S = S1 ∪ S2，产生新链表 */
    struct Node *setUnion(const struct Node *s1, const struct Node *s2)
    {
        struct Node dummy, *tail = &dummy;
        const struct Node *p;

        dummy.next = NULL;
        while (s1 != NULL && s2 != NULL) {
            if (s1->data < s2->data) {
                tail = append(tail, s1->data);
                s1 = s1->next;
            } else if (s1->data > s2->data) {
                tail = append(tail, s2->data);
                s2 = s2->next;
            } else {
                tail = append(tail, s1->data);  /* 重复的值只留一份 */
                s1 = s1->next;
                s2 = s2->next;
            }
        }
        for (p = (s1 != NULL) ? s1 : s2; p != NULL; p = p->next)
            tail = append(tail, p->data);       /* 剩下的一段整体收进来 */
        return dummy.next;
    }

    /* S = S1 - S2，产生新链表 */
    struct Node *setDifference(const struct Node *s1, const struct Node *s2)
    {
        struct Node dummy, *tail = &dummy;
        const struct Node *p;

        dummy.next = NULL;
        for (p = s1; p != NULL; p = p->next) {
            while (s2 != NULL && s2->data < p->data)
                s2 = s2->next;
            if (s2 == NULL || s2->data != p->data)
                tail = append(tail, p->data);   /* S2 里没有，才收进结果 */
        }
        return dummy.next;
    }

    /* S = S1 ∩ S2，产生新链表 */
    struct Node *setIntersection(const struct Node *s1, const struct Node *s2)
    {
        struct Node dummy, *tail = &dummy;
        const struct Node *p;

        dummy.next = NULL;
        for (p = s1; p != NULL; p = p->next) {
            while (s2 != NULL && s2->data < p->data)
                s2 = s2->next;
            if (s2 != NULL && s2->data == p->data)
                tail = append(tail, p->data);   /* 两边都有，收进结果 */
        }
        return dummy.next;
    }

    int main(void)
    {
        const int a[] = {2, 3, 5, 6}, b[] = {3, 4, 6, 8};
        struct Node *s1, *s2, *s3;

        s1 = buildList(NULL, a, 4);
        s2 = buildList(NULL, b, 4);
        s3 = setUnion(s1, s2);
        printSet("S1 ∪ S2", s3);
        freeList(s3);

        s3 = setDifference(s1, s2);
        printSet("S1 - S2", s3);
        freeList(s3);

        s3 = setIntersection(s1, s2);
        printSet("S1 ∩ S2", s3);
        freeList(s3);

        printSet("原来的 S1", s1);              /* 两个原链表一直没动过 */
        printSet("原来的 S2", s2);
        freeList(s1);
        freeList(s2);
        return 0;
    }
    ```

??? note "解析"

    思路：题干明说不带辅助表元，而且结果要产生一个新链表——原来的 S₁、S₂ 都不许动。三个函数都是"遍历两个原链表，把该收的值 `malloc` 成新表元接到结果链后面"。

    关键点：

    1. "不带辅助表元"指的是两个输入集合的表示法：表头指针直接就是第 1 个表元，空集合就是 `NULL`，所以循环条件都按 `s1 != NULL` 写，函数还要能处理空集合。
    2. 结果链表也不带辅助表元。拼结果时可以在函数里用栈上的临时哨兵 `struct Node dummy; tail = &dummy;`，最后 `return dummy.next;`——它只省掉"结果链还是空的"这个特判，不进结果链表。这和题 8 的 `newHead()` 不同：那个是堆上分配的表头，要 `free`；这里只是函数里的一个局部变量。
    3. 并集：两条链一起走，小的先收；相等只收一份、两条链同时前进；一条链走完，剩下的整段按值收进结果。
    4. 差集：对 S1 的每个值，让 `s2` 往后走到"不小于它"的位置，只有 `s2` 为空或值不相等，才把这个值收进结果。
    5. 交集：走法一样，`s2` 当前值等于 `p` 的值时才收。
    6. 两条链都有序，所以 `s2` 的游标只往前走、不用回头，三个函数都是 O(n+m) 时间，结果链表是新分配的 O(n+m) 个表元。
    7. 原链表一个表元都不动，三个结果可以依次求、随时重求，程序最后重新打印两个原集合来确认这一点。
    8. 结果链表用完逐个 `free`。

    > 真机实测（gcc 15.2.0，-O2 -std=gnu23 -Wall）：S₁ = {2,3,5,6}、S₂ = {3,4,6,8}，三个结果分别是 `{2,3,4,5,6,8}`、`{2,5}`、`{3,6}`，与题干样例一致；三次运算之后重新打印，"原来的 S1" 仍是 `{2,3,5,6}`、"原来的 S2" 仍是 `{3,4,6,8}`。

    > 易错：① 直接把 S1 的表元搬进结果（那就变成改 S1 了，和题 14 的做法混了）；② 差集和交集里对每个 `p` 都让 `s2` 从头找一遍，复杂度退化成 O(n·m)；③ 结果为空集时忘了返回 `NULL`，或者返回了栈上哨兵的地址（函数返回后它就不存在了）；④ 求差集时把相等的表元留下——差集要删的正是这些。

---

!!! todo "习题自测登记：做完了这一章的习题，在这里登记一下"

    <div class="read" id="read" data-page="chapter-7" data-done="你已经把这一章的习题过了一遍！">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已做完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
