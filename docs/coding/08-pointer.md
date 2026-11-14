# 指针

## 洛谷

| 题号                                            | 题目                     | 难度 | 链式结构       | 指针练习点                                                    |
| ----------------------------------------------- | ------------------------ | ---- | -------------- | ------------------------------------------------------------- |
| [P1739](https://www.luogu.com.cn/problem/P1739) | 表达式括号匹配           | ⭐    | 链式栈         | 压栈与出栈时只处理 char，逻辑约 20 行                         |
| [P1996](https://www.luogu.com.cn/problem/P1996) | 约瑟夫问题               | ⭐⭐   | 单向循环链表   | 把表尾的 next 指向表头，删除结点时要连接前后结点              |
| [P1449](https://www.luogu.com.cn/problem/P1449) | 后缀表达式               | ⭐⭐   | 链式栈         | 逐个读入 token，遇到数字就用 new 建结点，遇到运算符就弹出结点 |
| [P1540](https://www.luogu.com.cn/problem/P1540) | 机器翻译                 | ⭐⭐   | 链式队列       | 从队尾插入结点，从队头删除结点，并判重                        |
| [P1160](https://www.luogu.com.cn/problem/P1160) | 队列安排                 | ⭐⭐⭐  | 双向链表       | 两个指针域的改写，以及按编号定位结点指针                      |
| [P1981](https://www.luogu.com.cn/problem/P1981) | 表达式求值               | ⭐⭐   | 链式栈         | 涉及运算符优先级，栈里存 int                                  |
| [P4387](https://www.luogu.com.cn/problem/P4387) | 【深基15.习9】验证栈序列 | ⭐⭐⭐  | 顺序栈或链式栈 | 模拟入栈与出栈，判断出栈序列是否合法                          |
| [P2058](https://www.luogu.com.cn/problem/P2058) | 海港                     | ⭐⭐⭐  | 链式队列       | 滑动窗口，每次查询都从队头删除，数据量 $10^5$                 |


## 力扣

网址：<https://leetcode.cn/problemset/>

| 题号                                                                   | 题目                      | 难度 | 数据结构         | 练习点                   |
| ---------------------------------------------------------------------- | ------------------------- | ---- | ---------------- | ------------------------ |
| [203](https://leetcode.cn/problems/remove-linked-list-elements/)       | 移除链表元素              | ⭐    | 单链表           | 删除结点                 |
| [206](https://leetcode.cn/problems/reverse-linked-list/)               | 反转链表                  | ⭐    | 单链表           | 改 next 的指向           |
| [21](https://leetcode.cn/problems/merge-two-sorted-lists/)             | 合并两个有序链表          | ⭐    | 单链表           | 两个指针并行后移         |
| [83](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) | 删除排序链表中的重复元素  | ⭐    | 单链表           | 删除结点                 |
| [876](https://leetcode.cn/problems/middle-of-the-linked-list/)         | 链表的中间结点            | ⭐    | 单链表           | 快慢指针                 |
| [141](https://leetcode.cn/problems/linked-list-cycle/)                 | 环形链表                  | ⭐    | 单链表           | 判环                     |
| [160](https://leetcode.cn/problems/intersection-of-two-linked-lists/)  | 相交链表                  | ⭐    | 单链表           | 两条链同步前进           |
| [234](https://leetcode.cn/problems/palindrome-linked-list/)            | 回文链表                  | ⭐    | 单链表           | 找中点后反转一半         |
| [20](https://leetcode.cn/problems/valid-parentheses/)                  | 有效的括号                | ⭐    | 链式栈           | 遇右括号弹栈并配对       |
| [232](https://leetcode.cn/problems/implement-queue-using-stacks/)      | 用栈实现队列              | ⭐    | 栈               | 两个栈互相倒数据         |
| [225](https://leetcode.cn/problems/implement-stack-using-queues/)      | 用队列实现栈              | ⭐    | 队列             | 队列的入队与出队         |
| [933](https://leetcode.cn/problems/number-of-recent-calls/)            | 最近的请求次数            | ⭐    | 队列             | 超时请求从队头删除       |
| [707](https://leetcode.cn/problems/design-linked-list/)                | 设计链表                  | ⭐⭐   | 单链表或双向链表 | 自己 new 结点            |
| [24](https://leetcode.cn/problems/swap-nodes-in-pairs/)                | 两两交换链表中的节点      | ⭐⭐   | 单链表           | 连续改三个 next          |
| [19](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)   | 删除链表的倒数第 N 个结点 | ⭐⭐   | 单链表           | 两个指针间隔 N 步        |
| [61](https://leetcode.cn/problems/rotate-list/)                        | 旋转链表                  | ⭐⭐   | 单链表           | 接成环后断开             |
| [155](https://leetcode.cn/problems/min-stack/)                         | 最小栈                    | ⭐⭐   | 栈               | 结点附带当前最小值       |
| [150](https://leetcode.cn/problems/evaluate-reverse-polish-notation/)  | 逆波兰表达式求值          | ⭐⭐   | 链式栈           | 遇运算符弹出两个结点计算 |
| [622](https://leetcode.cn/problems/design-circular-queue/)             | 设计循环队列              | ⭐⭐   | 队列             | 环形队列                 |
| [641](https://leetcode.cn/problems/design-circular-deque/)             | 设计循环双端队列          | ⭐⭐   | 队列             | 两端插入与删除           |

---

!!! todo "题单完成登记：把本篇题单的题做完后在下方登记"

    <div class="read" id="read" data-page="08-pointer">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已做完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
