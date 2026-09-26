# 知识点 10 · 结构体与链表

> 这是整门课最重要的一章——链表在每一类题型中都至少出现过一次。
> 全章主线只有一条：你要改的永远是"某个结点的 `next` 字段"，而不是那个指针变量本身。

### 1 · 结构体的定义与访问（12 分）

下列程序实现对学生的成绩进行统计，计算每位同学三门课程的平均分，平均分保留 2 位小数。输出结果为：

```
ID: 1001, Average: 85.00
ID: 1002, Average: 83.33
ID: 1003, Average: 92.67
```

```c
#include <stdio.h>

#define N 3      // 学生人数
#define C 3      // 每个学生的课程数
typedef struct{
    int id;
    int score[C];
}Student;
int *p;

int main(void) {
    struct Student stu[N] = {
        {1001, {80, 90, 85}},
        {1002, {70, 88, 92}},
        {1003, {90, 95, 93}}
    };
    int i, j, sum;
    for (i = 0; i < N; i++) {
        sum = 0;
        p = &stu[i].score;
        for (j = 0; j < C; j++) {
            sum += *p[j];
        }
        printf("ID: %d, Average: %.2f\n", stu[i].id, sum / C);
    }
    return 0;
}
```

??? note "答案"

    4 处错误：

    | 错误语句                    | 改正                                                                       | 错因                                                                                                 |
    | --------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
    | `struct Student stu[N] = {` | `Student stu[N] = {`                                                       | 已经 `typedef ... Student`，`Student` 就是类型名，前面不能再加 `struct`                              |
    | `p = &stu[i].score;`        | `p = stu[i].score;` 或 `p = (*(stu+i)).score` 或 `p = &(stu[i].score[0]);` | `&数组名` 得到的是数组指针 `int(*)[3]`，与 `int *p` 类型不符；数组名 `stu[i].score` 才退化为 `int *` |
    | `sum += *p[j];`             | `sum += p[j];` 或 `sum += *(p+j);` 或 `sum += stu[i].score[j];`            | `p[j]` 已经是元素值，再解引用 `*` 就错了（等价 `*(p[j])`，把整数值当地址）                           |
    | `sum / C`                   | `sum / (float)C` 或 `(float)sum / C`                                       | `sum` 和 `C` 都是 `int`，整数除法会截断（85 还好，83.33 会变成 83）                                  |

    > 也可替换第 4 处改法（备选）：把 `int i, j, sum;` 改为 `int i, j; float sum;` —— 这样 `sum` 是浮点，除法自然是浮点除法。

    >

    > 特别说明：这两种改法只能选一种，不能同时改，否则会超出"每个错的修改数量"限制。

??? note "解析"

    这一题把结构体最常考的 4 个点全包了，务必吃透：

    1. `typedef` 之后不用再写 `struct`（写了不算语法错误，但会因找不到 `struct Student` 标签而报错——因为本题定义时是匿名结构体 `typedef struct { ... } Student;`，没有 `Student` 这个 tag）。
       > 辨析：`typedef struct Student { ... } Student;` ← tag 和 typedef 名同名，两种写法都能用；
       > 本题是 `typedef struct { ... } Student;` ← 只有 typedef 名，`struct Student` 不存在。
    2. 数组名 vs 取地址：`a` 退化后是元素指针，`&a` 是数组指针，两者类型不同。
    3. `p[j]` ≡ `*(p+j)`，已经是值了；`*p[j]` ≡ `*(p[j])` 是再次解引用，语义完全变了。
    4. 整数除法陷阱：`sum / C` 结果仍是 `int`，想保留小数必须让其中一方是浮点。

---

### 2 · 结构体成员的访问（`.` 与 `->`）

以下链表操作的结果是什么？

```c
struct Node {
    int data;
    struct Node* next;
} n1 = {10, NULL}, n2 = {20, &n1};
printf("%d\n", n2.next->data);
```

- A. 10
- B. 20
- C. NULL
- D. 编译出错

??? note "答案"

    A

??? note "解析"

    `n2.next` 的值是 `&n1`（指向 `n1` 的指针），`->data` 取出 `n1.data = 10`。

    !!! tip "必背语法：`.` 与 `->` 的优先级"
        注意：`n2.next->data` 里 `->` 的优先级高于 `.`？不——其实 `n2.next` 先结合，因为 `.` 和 `->` 同级且左结合。所以是 `(n2.next)->data`。

        | 写法            | 等价                |
        | --------------- | ------------------- |
        | `p->data`       | `(*p).data`         |
        | `n2.next->data` | `(*(n2.next)).data` |

        `*p.data` 是错的（`.` 优先级更高，会被解析成 `*(p.data)`）。

        顺带记住：`n1 = {10, NULL}`、`n2 = {20, &n1}` 这种"在定义时用一个结点的地址去初始化下一个结点的 `next`"的写法，就是"静态造链表"，用来出选择题最方便。

---

### 3 · 结构体变量与成员（说法辨析）

在 C 语言中，关于结构变量的说法，错误的是（　）。

- A. 结构变量之间不能使用 `==` 运算符比较其每个成员变量是否相等
- B. 结构类型定义时一定要有类型名称
- C. 对两个同类型的结构变量 `a` 和 `b`，可以直接用 `b=a` 赋值
- D. 可以通过结构指针使用 `->` 运算符访问结构成员变量

??? note "答案"

    B

??? note "解析"

    - A 对：结构体不支持整体比较，`==` 编译报错。要逐成员比，得自己写 `a.id == b.id && ...` 或者用 `memcmp`。
    - B 错：可以没有类型名。`typedef struct { int id; } Student;` 里结构体是匿名的（没有 tag），只靠 `Student` 这个名字用；甚至 `struct { int a; } x;` 这种"直接用匿名结构体定义变量"也完全合法。所以"一定要有类型名称"是错的。
    - C 对：同类型结构变量可以直接赋值（`b = a;`），效果是逐成员的浅拷贝（相当于 `memcpy`）。这一点和数组不同——数组名不能赋值。
    - D 对：`p->data` 正是 `(*p).data` 的简写。

    > 易错：把"A 不能整体比较"和"C 可以整体赋值"记混——同类型结构体变量能整体赋值，但不能用 `==` 整体比较。另外注意 B 的坑：匿名结构体是合法的，只是没法再写 `struct Xxx` 去引用它。

---

### 4 · 链表 vs 数组（说法辨析）

关于链表，下列说法错误的是（　）。

- A. 链表的节点可以通过动态分配内存获得
- B. 链表的删除效率更高
- C. 链表的插入操作效率与数组相同
- D. 单链表的遍历，需要从首表元开始

??? note "答案"

    C

??? note "解析"

    - A 对：`malloc` 动态申请结点是标准做法。
    - B 对：已知待删结点位置时，链表删除只需 `O(1)` 改指针；数组删除要移动后续所有元素 `O(n)`。
    - C 错：链表插入只需改指针（`O(1)`，前提是已定位）；数组插入要整体后移（`O(n)`）。两者效率完全不同。
    - D 对：单链表只有后继指针，必须从头开始走。

    !!! tip "链表 vs 数组 必背对比表"
        | 操作            | 数组             | 链表                               |
        | --------------- | ---------------- | ---------------------------------- |
        | 随机访问第 k 个 | O(1) ✅           | O(n)                               |
        | 按序插入/删除   | O(n)（要搬元素） | O(1) ✅（改指针）                   |
        | 内存            | 连续、需预分配   | 分散、动态申请                     |
        | 找前驱          | 不需             | 需要（单链表常带辅助表元简化边界） |

        注意 C 的陷阱措辞："插入操作效率与数组相同"——错的不是前半句，而是"相同"。链表和数组的插入都能做到"在已知位置上 O(1) 改指针"，但数组额外还要搬元素，所以整体是 O(n)。

---

### 5 · 链表结点与指针（删除结点·改错）

在不增删语句的情况下指出错误行并改正。

```c
/* 第 1 行 */ struct node {
/* 第 2 行 */     int data;
/* 第 3 行 */     struct node next;
/* 第 4 行 */ };
/* 第 5 行 */ typedef struct node* ptr;
/* 第 6 行 */ ptr delnode(ptr head, int n) {
/* 第 7 行 */     ptr tmp,p;
/* 第 8 行 */     if (head->data = n) {
/* 第 9 行 */         return head->next;
/* 第 10 行 */    }
/* 第 11 行 */    for (p = head;p->next != NULL;p = p->next) {
/* 第 12 行 */        if (p->data == n) {
/* 第 13 行 */            p->next = p->next->next;
/* 第 14 行 */            return head;
/* 第 15 行 */        }
/* 第 16 行 */    }
/* 第 17 行 */ }
```

??? note "答案"

    3 处错误：

    | 行  | 错误                  | 改正                      | 错因                                                                                          |
    | --- | --------------------- | ------------------------- | --------------------------------------------------------------------------------------------- |
    | 3   | `struct node next;`   | `struct node *next;`      | 链表结点必须存指向下一个结点的指针；写成普通结构体成员会导致无限递归定义（`sizeof` 无法确定） |
    | 8   | `if (head->data = n)` | `if (head->data == n)`    | `=` 是赋值（恒为真），比较要用 `==`                                                           |
    | 12  | `if (p->data == n)`   | `if (p->next->data == n)` | 第 13 行删的是 `p` 的后继，所以判断的应该是后继的值                                           |

??? note "解析"

    - 第 3 行是本课程链表题的"头号错误"。`struct node next;` 会让结构体包含自身 → 大小无法确定 → 编译报错（`incomplete type`）。必须是 `struct node *next;`。记住：链表结点里放的是"指针"，不是"结点"。
    - 第 8 行的 `=` / `==` 混淆是 C 的经典陷阱（`if (avg = 60.0)` 同理）。
    - 第 12 行是链表删除的"前驱视角"：`p` 一直站在前驱位置（第 11 行的循环体里 `p` 只声明了 `p->next != NULL` 这一条路），所以要判断的是 `p->next->data`。这正是"带辅助表元"能简化问题的地方——辅助表元让首结点也有前驱。
    - 另外第 13 行少了一句 `free(...)`（释放被删结点），但"不得增行"所以不好补。

    !!! warning "还有一处更要紧的：函数末尾没有 `return`"
        第 17 行的 `}` 之前缺一条 `return head;`。真机实测（gcc 15.2.0）：当要删的值不在表中时，`for` 循环走到底，函数从末尾掉出去，返回值不确定（未定义行为）——

        - `-O0` 下这次返回的是 `NULL`，而调用者会把返回值当成新头指针 → 整条链表被静默丢弃；
        - `-O2` 下返回值不可预测，实测也可能直接崩溃。

        所以严格说这段代码有 4 处问题：材料上标出的 3 处是"以行为单位写错的地方"，缺 `return` 属于"漏写"。考试按材料上标出的 3 处作答即可，但自己写代码时必须补上 `return head;`。

    > 看第 9 行 `return head->next;`：删除首结点时直接返回了第二个结点——这个写法是对的（链表没有"头指针的指针"可用时，只能靠返回值更新头指针）。这就是"不带辅助表元"付出的代价。

---

### 6 · 链表插入到末尾（结点 vs 指针）（6 分）

以下函数实现将数据插入到链表末尾。

```c
struct Node* insertEnd(struct Node* head, int data) {
/* 1 */    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node*));
/* 2 */    newNode->data = data;
/* 3 */    newNode->next = NULL;
/* 4 */    struct Node* temp = head;
/* 5 */    if (head == NULL) {
/* 6 */        head = newNode;
           }
/* 7 */    while (temp != NULL) {
/* 8 */        temp = temp->next;
           }
/* 9 */    temp = newNode;
           return head;
}
```

??? note "答案"

    3 处错误：

    | 行  | 错误                   | 改正                         | 错因                                                                                                                                                                                                   |
    | --- | ---------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | 1   | `sizeof(struct Node*)` | `sizeof(struct Node)`        | 申请的是指针的大小（8 字节），不是结点的大小（16 字节）→ 内存不够：`data` 在偏移 0、8 字节内还写得下，紧跟着第 3 行写 `newNode->next`（偏移 8、写 8 字节）就越界了（ASan 实测 `heap-buffer-overflow`） |
    | 7   | `while (temp != NULL)` | `while (temp->next != NULL)` | 循环结束时 `temp` 变成 `NULL`，再也回不到尾结点                                                                                                                                                        |
    | 9   | `temp = newNode;`      | `temp->next = newNode;`      | 应该修改尾结点的 next，而不是修改局部变量 `temp`（函数返回后 `temp` 就消失了）                                                                                                                         |

??? note "解析"

    - 第 1 行是最阴险的一处：`sizeof(struct Node*)` 写法"合法"、编译不报错，但申请的内存少了一半。这是链表题目的头号高频错误，请务必记牢：`sizeof(结点类型)`，不要加 `*`。
    - 第 7 行的正确写法是 `temp->next != NULL`——让 `temp` 停在最后一个结点上，这样才能在第 9 行处接上新结点。
      - 对比记忆：要"停在尾结点"，条件写 `temp->next != NULL`；要"走完全程"，条件写 `temp != NULL`。
      - 顺带一提：第 7 行的循环体 `{ }` 在题面里是空的（只要 `temp = temp->next` 这一句），排版上看不出来，实际就是 `while (temp->next != NULL) temp = temp->next;`。
    - 第 9 行揭示了链表操作的核心：你要改的永远是"某个结点的 `next` 字段"，而不是那个指针变量本身。

    !!! warning "改完这 3 处，空链表上仍会崩"
        但这 3 处都改完，程序在「空链表」上仍会崩（真机实测：`Segmentation fault`，退出码 139）。

        原因：第 4 行 `temp = head;` 写在 `if (head == NULL)` 之前，所以空表时 `temp` 恒为 `NULL`，而第 9 行的 `temp->next = newNode;` 要求 `temp` 非空 → 解引用空指针。

        两种补法（任选其一）：

        1. 让空表提前返回：把第 6 行改成 `return newNode;`（推荐，即下面「正确的实现」的思路）；
        2. 把第 9 行写成 `if (temp != NULL) temp->next = newNode;`。

        也就是说：材料上只标了 3 处错误，但只改这 3 处是跑不通的——这是"代码必须亲自跑一遍"的典型例子。

    正确的实现：

    ```c
    struct Node* insertEnd(struct Node* head, int data) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->next = NULL;
        if (head == NULL) return newNode;      // 空链表特判
        struct Node* temp = head;
        while (temp->next != NULL) temp = temp->next;
        temp->next = newNode;                  // ★ 改 next，不是改 temp
        return head;
    }
    ```

---

### 7 · 辅助表元（升序链表删除区间）（8 分）

以下程序的目的是从升序链表中删除从 `min` 到 `max` 范围内的表元，同时释放被删结点空间。

- 例如链表结点值依次为 `10 20 30 40 50`：
  - 若 `min=10, max=35`，`DeleteSome` 将使得链表中结点值被删为 `"10 40 50"`；
  - 若 `min=5, max=55`，链表将被删空。

```c
struct Node
{
    int data;
    struct Node *next;
};

void DeleteSome(struct Node *head, int min, int max)
{
    struct Node *node;
    struct Node *middle;
    struct Node *frontend;      /* 前端最后一个保留节点 */
    frontend =    (25.6)    ;
    node = head->next;
    while(node &&    (25.7)    )   /* 查找前端最后一个保留节点 */
    {
        frontend = node;
        node = node->next;
    }
    while(node && node->data < max)      /* 删除节点 */
    {
        middle = node;
        node = node->next;
        (25.8)    ;
    }
    (25.9)    = node;
}
```

??? note "答案"

    | 序号 | 答案                | 说明                                                                                      |
    | ---- | ------------------- | ----------------------------------------------------------------------------------------- |
    | 25.6 | `head`              | 因为是带辅助表元的链表，`frontend` 的初始值是辅助表元，保证"一个都不用删"时也有合法的前驱 |
    | 25.7 | `node->data <= min` | 前端保留条件：值是 `min` 的结点也要保留（例 1 中 `10` 被保留了），所以用 `<=`             |
    | 25.8 | `free(middle);`     | 释放被删结点。顺序不能颠倒：必须先 `node = node->next` 保住后继，再 `free(middle)`        |
    | 25.9 | `frontend->next`    | 把前端的最后一个保留结点接上后半段，完成"摘除中间一段"                                    |

??? note "解析"

    按例 1 走一遍：`head`(辅助) → `10` → `20` → `30` → `40` → `50`，`min=10, max=35`

    | 阶段                                                                                                                         | 结果                 |
    | ---------------------------------------------------------------------------------------------------------------------------- | -------------------- |
    | `frontend = head`，`node = head->next`（=10）                                                                                |                      |
    | 循环 25.7：`10 <= 10` ✓ → `frontend = 10结点`，`node = 20结点`；`20 <= 10` ✗ → 退出                                          | `frontend` 停在 `10` |
    | 循环删除：`20 < 35` ✓ → 记下 20，`node = 30`，`free(20)`；`30 < 35` ✓ → 记下 30，`node = 40`，`free(30)`；`40 < 35` ✗ → 退出 | 20、30 被释放        |
    | `frontend->next = node`（即 `10->next = 40`）                                                                                | `10 40 50` ✅         |

    按例 2 走一遍：`min=5, max=55`

    - `10 <= 5` ✗ → `frontend` 停在辅助表元
    - 删除循环：`10 < 55`、`20 < 55`、…、`50 < 55` 全部满足 → 全部释放，`node` 最终为 `NULL`
    - `frontend->next = NULL` → 链表被删空 ✅

    !!! tip "答题技巧：遇到链表填空，先问自己三个问题"
        这道题完美展示了"辅助表元"的价值：例 2 要把首结点也删掉，如果有特判就会很麻烦；有了辅助表元，`frontend` 一开始就指向它，"删掉全部"和"一个都不删"走的是同一条代码路径。

        1. 这个链表带辅助表元吗？（看有没有 `head = malloc(...)`）
        2. 这个循环是"停在某个结点"还是"走完全程"？（决定用 `node` 还是 `node->next` 作条件）
        3. 指针赋值的顺序对吗？（先保住后继，再改指针，最后 `free`）

---

### 8 · 辅助表元（升序链表的插入）

```c
typedef struct member { int num; struct member *next; } Member;

void InsertUp(Member *head, Member *newp) {
    /* 在链表中按升序插入一个结点(表元)的函数*/
    Member *pre;
    for(pre=head; pre->next; pre=pre->next) {
        if(pre->next->num >= newp->num)   /* 查找结点在链表中的插入位置*/
            (4.2.1);
    }
    (4.2.2);          /* 按升序插入结点*/
    (4.2.3);
}

Member *MakeLink(Member *head) {
    Member *newp;
    int n;
    while((scanf("%d", &n)) == 1) {
        if ((newp=(Member *)malloc(sizeof(Member))) == NULL)
            return(NULL);
        newp->num = n;
        InsertUp(   4.2.4   );
    }
    return head;
}

int main() {
    Member empty, *node, *head=&empty;    /* 设置辅助表元*/
    (4.2.5);            /* 初始将链表设置为空*/
    head = MakeLink(head);
    for(node=head->next; node; node=node->next)
        printf("%d\n", node->num);
    return 0;
}
```

??? note "答案"

    | 序号  | 答案                     |
    | ----- | ------------------------ |
    | 4.2.1 | `break`                  |
    | 4.2.2 | `newp->next = pre->next` |
    | 4.2.3 | `pre->next = newp`       |
    | 4.2.4 | `head, newp`             |
    | 4.2.5 | `head->next = NULL`      |

??? note "解析"

    - 4.2.1：在 `for` 里找到插入位置后要跳出循环（`break`），此时 `pre` 就是"新结点的前驱"。
      > 注意这个 `for` 的写法很巧：循环头和判断体分工合作——`for` 负责推进 `pre`，`if` 负责发现"该停了"。（判断的永远是 `pre->next`，这样 `pre` 停在插入点的前驱上。）
    - 4.2.2 / 4.2.3：插入的两句话，顺序不能颠倒！
      ```c
      newp->next = pre->next;   // 先接后
      pre->next  = newp;        // 再接前
      ```
      若先写 `pre->next = newp`，`pre` 原来的后继就丢了（再也找不到），这是链表插入最常见的错误。
    - 4.2.4：`InsertUp` 的两个形参是 `head` 和 `newp`。
    - 4.2.5：辅助表元初始化——`head->next = NULL`，表示"空链表"。
      > 注意 `main` 里 `head = &empty;` 用的是栈上的结构体 `empty` 作辅助表元（而不是 `malloc`），这是一种省内存的写法（也是"带辅助表元"≠"一定要动态分配"的证明）。所以 25.6 这类空的判断依据要放宽：看 `head` 是不是一个"不存数据的额外结点"。

    "带辅助表元的链表"里，插入和删除是一对：

    > | | 插入（本题） | 删除 |
    > |---|---|---|
    > | 辅助表元的作用 | 空链表也能插 | 删空链表也能做 |
    > | 需要几个指针 | `pre` | `frontend` + `node` + `middle` |
    > | 关键顺序 | 先接后、再接前 | 先保后路、再改指针、最后 `free` |

---

### 9 · 链表算法 · 去重（4 分）

```c
typedef struct NODE { int value; struct NODE* next; } node_t;

void func(node_t* head) {
    node_t* prev_node = head;
    node_t* next_node = head->next;
    while (next_node != NULL) {
        if (prev_node->value == next_node->value) {
            node_t* del_node = next_node;
            prev_node->next = next_node->next;
            next_node = prev_node->next;
            free(del_node);
        } else {
            prev_node = next_node;
            next_node = next_node->next;
        }
    }
}
```

输入链表：`3 -> 3 -> 4 -> 4 -> 2 -> 1 -> 5 -> 5 -> 6 -> NULL`

??? note "答案"

    `3 -> 4 -> 2 -> 1 -> 5 -> 6 -> NULL`

    功能：删除链表中相邻重复的结点（连续相同值只保留第一个）。

??? note "解析"

    逐步演算：

    | 步骤 | `prev_node` | `next_node` | 判断 | 动作                                             |
    | ---- | ----------- | ----------- | ---- | ------------------------------------------------ |
    | 1    | 3(a)        | 3(b)        | 相等 | 删 3(b)，`prev->next = 4(a)`，`next_node = 4(a)` |
    | 2    | 3(a)        | 4(a)        | 不等 | `prev = 4(a)`，`next = 4(b)`                     |
    | 3    | 4(a)        | 4(b)        | 相等 | 删 4(b)，`prev->next = 2`，`next_node = 2`       |
    | 4    | 4(a)        | 2           | 不等 | `prev = 2`，`next = 1`                           |
    | 5    | 2           | 1           | 不等 | `prev = 1`，`next = 5(a)`                        |
    | 6    | 1           | 5(a)        | 不等 | `prev = 5(a)`，`next = 5(b)`                     |
    | 7    | 5(a)        | 5(b)        | 相等 | 删 5(b)，`prev->next = 6`，`next_node = 6`       |
    | 8    | 5(a)        | 6           | 不等 | `prev = 6`，`next = NULL` → 循环结束             |

    结果：`3 -> 4 -> 2 -> 1 -> 5 -> 6` ✅

    关键设计：

    - 删除时 `prev_node` 不动——因为删掉 `next_node` 之后，`prev_node` 的"下一个"变成了新结点，新结点仍可能与 `prev_node` 相同（例如 `3->3->3`），必须再比一次。这是本题最容易写错的地方。
    - `next_node = prev_node->next;` 在 `free` 之前执行，且用的是 `prev_node->next`（删完后的新后继）——顺序完全正确。

    > 这题的前提是"链表已按值分组（相同值相邻）"。 如果相同的值不相邻（比如 `3->4->3`），这个算法就删不掉——它只比"相邻的一对"，不做全局查重。

---

### 10 · 链表算法 · 反转

说明 `function1` 的功能。

```c
typedef struct sListNode {
    int data;
    struct sListNode* next;
} SListNode;

SListNode* function1(SListNode* head)
{
    SListNode* prev = NULL;
    SListNode* current = head;
    while (current) {
        SListNode* next = current->next;   /* ① 保后路 */
        current->next = prev;              /* ② 掉头 */
        prev = current;                    /* ③ 前驱前进 */
        current = next;                    /* ④ 当前前进 */
    }
    return prev;
}
```

??? note "答案"

    函数功能是"就地反转单链表"，返回反转后的新头指针。

??? note "解析"

    这是链表题的头号模板，四步走顺序不能乱：

    | 步骤                     | 作用                   | 忘了会怎样                   |
    | ------------------------ | ---------------------- | ---------------------------- |
    | ① `next = current->next` | 先保住后路             | ② 一执行，后面的结点就全丢了 |
    | ② `current->next = prev` | 让当前结点掉头指向前面 | —                            |
    | ③ `prev = current`       | 前驱前进               | —                            |
    | ④ `current = next`       | 当前前进               | 死循环                       |

    手动演算（输入 `1→2→3→NULL`）：

    | 轮次 | `current` | `next` | 操作后链表   | `prev` | `current` |
    | ---- | --------- | ------ | ------------ | ------ | --------- |
    | 1    | 1         | 2      | `1→NULL`     | 1      | 2         |
    | 2    | 2         | 3      | `2→1→NULL`   | 2      | 3         |
    | 3    | 3         | NULL   | `3→2→1→NULL` | 3      | NULL      |

    循环结束，返回 `prev`（= 3 号结点）→ `3→2→1→NULL` ✅

    !!! quote "同一个原则的正反两面"
        注意返回的是 `prev` 不是 `head`——`head` 已经变成尾结点了。

        `insertEnd` 出错在"改的是 `temp` 而不是 `temp->next`"；本题是"改的是 `current->next` 而不是 `current`"——同一个原则的正反两面。

---

### 11 · 链表算法 · 插入排序（阅读·不带辅助表元）

假设输入函数的链表 `h`，输入数据链接关系如下：`23 → 13 → 15 → 23 → 23 → 16 → 54 → 23 → NULL`
请给出函数 `func` 执行完后返回的链表 `h2` 的数据链接关系。

```c
struct intNode
{
    int data;
    struct node * next;
};

struct intNode * func(struct intNode *h)
{
    struct intNode *p = h, *u;
    struct intNode* h2 = NULL;
    struct intNode* p2, *u2;
    while(p)
    {
        u = p->next;                      /* ① 记住下一個 */
        p2 = h2;
        while(p2 && p2->data < p->data)   /* ② 在 h2 中找插入位置 */
        {
            u2 = p2; p2 = p2->next;
        }
        if(p2 == h2)                      /* ③ 插到最前面 */
        {
            p->next = h2;
            h2 = p;
        }
        else                              /* ④ 插到 u2 和 p2 之间 */
        {
            u2->next = p;
            p->next = p2;
        }
        p = u;                            /* ⑤ 处理原链表的下一个结点 */
    }
    return h2;
}
```

??? note "答案"

    `13 → 15 → 16 → 23 → 23 → 23 → 23 → 54 → NULL`

    功能：把原链表 `h` 的结点逐个摘下并有序插入到新链表 `h2` 中，返回升序链表（即对链表做插入排序）。原链表被破坏。

??? note "解析"

    完整演算：

    | 步骤 | 取出的 `p` | 在 `h2` 中的插入位置         | `h2` 变化                 |
    | ---- | ---------- | ---------------------------- | ------------------------- |
    | 1    | 23         | `h2` 为空 → 插最前           | `23`                      |
    | 2    | 13         | 13 < 23 → 插最前             | `13→23`                   |
    | 3    | 15         | 13 < 15 ≤ 23 → 插在 13 之后  | `13→15→23`                |
    | 4    | 23         | 停在第一个 23 → 插在 15 之后 | `13→15→23→23`             |
    | 5    | 23         | 同上 → 插在 15 之后          | `13→15→23→23→23`          |
    | 6    | 16         | 15 < 16 ≤ 23 → 插在 15 之后  | `13→15→16→23→23→23`       |
    | 7    | 54         | 比所有都大 → 插到末尾        | `13→15→16→23→23→23→54`    |
    | 8    | 23         | 停在第一个 23 → 插在 16 之后 | `13→15→16→23→23→23→23→54` |

    三个关键设计：

    - ① `u = p->next`：在动 `p->next` 之前先记住原链表的下一个，否则找不到后续结点。这是所有链表遍历改造题的通用模式。
    - ② 内层循环 `while(p2 && p2->data < p->data)`：找到第一个不小于 `p->data` 的结点 `p2`，插入点就在它前面（由 `u2` 记录前驱）。
    - ③ `if (p2 == h2)`：`p2` 没动过，说明要插到最前面——这时必须更新头指针 `h2`，这是最容易漏的一步。
    - ④ `u2->next = p; p->next = p2;`：标准的"中间插入"两句话。

    > 这个 `func` 其实就是"没有辅助表元的链表插入排序"。如果加上辅助表元，③的特判就可以省掉——再一次印证了辅助表元的价值。

    !!! note "顺带指出题面上的一处笔误"
        结构体定义里写的是 `struct node * next;`，但类型标签其实是 `struct intNode`，`struct node` 根本没有定义。

        这属于题面笔误（实际编译会报错）；考试时按 `struct intNode *next;` 理解即可。

---

### 12 · 链表删除结点（填空·不带辅助表元）（12 分）

已知一个不带辅助表元的单向链表，每个结点保存一个整数值。要求完善函数实现删除链表中所有值为奇数的结点，返回最终链表的头指针。

```c
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node* deleteOdd(struct Node *head)
{
    struct Node *p = head;
    struct Node *prev = NULL;
    while (p != NULL) {
        if (    (1)    ) {
            struct Node *tmp = p;
            if (prev == NULL) {
                (2)    ;
                p = head;
            } else {
                prev->next = p->next;
                (3)    ;
            }
            (4)    ;
        } else {
            prev = p;
            p = p->next;
        }
    }
    return head;
}
```

??? note "答案"

    | 序号 | 答案               |
    | ---- | ------------------ |
    | (1)  | `p->data % 2 != 0` |
    | (2)  | `head = p->next`   |
    | (3)  | `p = p->next`      |
    | (4)  | `free(tmp)`        |

??? note "解析"

    这是"双指针删结点"的标准模板：

    ```c
    prev = NULL;  p = head;
    while (p) {
        if (要删) {
            tmp = p;                       // ① 记下待删结点
            if (prev == NULL)              // ② 删的是首结点
                head = p->next;            //    头指针后移
            else                           // ③ 删的是中间/尾结点
                prev->next = p->next;      //    前驱跳过它
            p = p->next;                   // ④ p 前进（注意：在 free 之前！）
            free(tmp);                     // ⑤ 释放
        } else {
            prev = p;                      // ⑥ 保留，prev 跟上
            p = p->next;
        }
    }
    ```

    !!! tip "关键点"
        1. `prev == NULL` 就是"要删的是首结点"的判据 —— 这也是"不带辅助表元"必须付出的代价（带辅助表元就不用判断了）。删首结点时头指针要跟着后移，本质上是同一个问题。
        2. 顺序必须是"先 `p = p->next` 再用 `tmp` 释放"。若先 `free(p)` 再访问 `p->next`，就是访问已释放内存。
        3. 空指针保护：`head = p->next` 时，如果删的是最后一个结点，`p->next` 是 `NULL`，`head` 变成 `NULL`，`p = head` = `NULL` → 循环正确结束。

        链表的插入和删除都遵循同一句话——改的是"前驱的 `next`"，不是那个游标指针。

        `insertEnd` 里是把 `temp = newNode` 改成 `temp->next = newNode`；本题里是把 `p = p->next`（游标前进）和 `prev->next = p->next`（跳过结点）分开写，别混。

---

### 13 · 链表算法 · 插入排序（编程·带辅助表元）（13 分）

编写使用插入排序将无序链表排序的函数。结构体如下，`list_t` 是包含辅助表元的链表。

```c
typedef struct NODE { int value; struct NODE* next; } node_t;
typedef struct LIST { node_t* head; } list_t;
```

函数声明：`void list_insert_sort(list_t* list);`
要求：不允许新建任何新节点。 函数调用结束后，`list` 中节点的 `value` 按从小到大排序。

??? note "答案"

    参考实现：

    ```c
    void list_insert_sort(list_t* list) {
        node_t *sorted = NULL;              /* 已排好序部分的表头（不带辅助表元） */
        node_t *cur = list->head->next;     /* 待处理的第一个数据结点 */

        while (cur != NULL) {
            node_t *next = cur->next;       /* ① 先摘下 cur，保住后路 */

            if (sorted == NULL || cur->value <= sorted->value) {
                cur->next = sorted;         /* ② 插到最前面 */
                sorted = cur;
            } else {
                node_t *p = sorted;         /* ③ 在 sorted 中找插入位置 */
                while (p->next != NULL && p->next->value < cur->value)
                    p = p->next;
                cur->next = p->next;
                p->next = cur;
            }
            cur = next;                     /* ④ 处理原链表的下一个 */
        }

        list->head->next = sorted;          /* ⑤ 挂回辅助表元后面 */
    }
    ```

??? note "解析"

    解题思路（"拆链 + 重建"）：这个算法把链表拆成两部分：

    - `sorted`：已经排好序的部分（一开始是空）；
    - `cur`：还没处理的部分（从 `list->head->next` 开始）。

    每轮从 `cur` 摘下一个结点，有序插入到 `sorted` 中，直到 `cur` 走完。

    五个关键点：

    1. ① `next = cur->next` 必须在动 `cur->next` 之前——否则原链表就断了。
    2. `sorted == NULL` 要单独处理（空表插入第一个结点），否则 `sorted->value` 会解引用空指针。
    3. 想保持"稳定性"（相等元素保持原有相对顺序），要这样配：前插判断用 `<`、内层查找用 `<=`。本题代码写的是"前插 `<=` + 内层 `<`"，效果恰好相反——相等元素会被逆序（真机实测：输入 `3#1 1#1 3#2 2#1 3#3 1#2`，输出 `1#2 1#1 2#1 3#3 3#2 3#1`；改成"前插 `<` + 内层 `<=`"才得到 `1#1 1#2 … 3#1 3#2 3#3`）。题目只要求"从小到大"、没要求稳定，所以这份实现照样得分，但"用 `<=` 就稳定"的说法是错的。
    4. 内层 `while` 找的是 `p->next`，这样 `p` 停在"插入位置的前驱"上。
    5. ⑤ 别忘了挂回去——最终的 `sorted` 要接到 `list->head->next`，否则 `list` 还是空的。

    !!! quote "带辅助表元省掉了什么"
        不带辅助表元的写法要写 `if (p2 == h2) { ...; h2 = p; }` 特判首结点；本题带辅助表元（`list_t`），
        用 `sorted = NULL` 起始 + 最后统一挂回，就省掉了这个特判，代码也更干净。

    验证：`5 -> 2 -> 8 -> 1 -> 9`

    | 步骤 | 取出的 cur | 插入后 sorted             |
    | ---- | ---------- | ------------------------- |
    | 1    | 5          | `5`                       |
    | 2    | 2          | `2 -> 5`                  |
    | 3    | 8          | `2 -> 5 -> 8`             |
    | 4    | 1          | `1 -> 2 -> 5 -> 8`        |
    | 5    | 9          | `1 -> 2 -> 5 -> 8 -> 9` ✅ |

---

### 14 · 结构体指针成员的访问（`typedef` 指针陷阱）

下面程序中，对 pp 出生年月输出正确的是________。

```c
typedef struct date
{
    int year;
    int month;
    int day;
}* DATE;

typedef struct student
{
    long studentID;
    char studentName[10];
    char studentSex;
    DATE birthday;
    int score[4];
}STUDENT;
STUDENT pp;
```

- A. `printf("%d,%d", pp. DATE ->year,pp. DATE ->month)`
- B. `printf("%d,%d", pp.birthday ->year,pp. birthday ->month)`
- C. `printf("%d,%d", pp.birthday.year,pp. birthday.month)`
- D. `printf("%d,%d",pp-> DATE.year,pp-> DATE.month)`

??? note "答案"

    B

??? note "解析"

    `typedef struct date { ... } *DATE;` 里那个 `*` 是关键——

    `DATE` 被定义成指针类型（等价于 `struct date *`），所以 `STUDENT` 的成员 `birthday` 本质就是一根 `struct date *`。

    访问"指针所指结构体"的成员必须用 `->`，即 `pp.birthday->year`，选 B；C 用 `.` 是把 `birthday` 当成了结构体变量本体，错。

    D 反过来把 `pp` 当成了指针，可 `pp` 是普通结构体变量，只能用 `.`。

    typedef 名字后面带 `*` 时，这个名字本身就是指针，访问它一律用 `->`。

---

### 15 · 链表与数组的对比

链表相较于数组的一个重要优势是？

- A. 链表支持随机访问
- B. 链表插入和删除操作不需要移动其他元素
- C. 链表在内存中占用更少空间
- D. 链表在查找元素时比数组更高效

??? note "答案"

    B

??? note "解析"

    链表插入/删除只改几个 `next` 指针就能完成（拿到位置后是 O(1)），不像数组那样要把后面所有元素整体搬移（数组插入/删除是 O(n)），这就是 B 说的优势。

    A 恰好说反了——能随机访问的是数组（`a[i]` 由首地址直接算出），链表必须从头逐个走。

    C、D 也都是数组占优：链表每个结点还要多存一个指针，查找只能顺序遍历 O(n)。

    一句话记忆：数组"查得快、改得慢"，链表"改得快、查得慢"。

---

## 说明

1. 第 11 题的题干有一处笔误：题面里的结构体定义写的是 `struct node * next;`，而结构体标签其实是 `struct intNode`，`struct node` 并未定义——照抄会编译报错，按 `struct intNode *next;` 理解即可（解析中已说明）。
