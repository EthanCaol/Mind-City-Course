---
icon: material/pencil-outline
---

# 作业 16：选择排序

从键盘读入 n 个整数，用选择排序把它们按从小到大的顺序排列后输出。

### 示例 1

输入：

```text
7
4 2 9 1 7 6 3
```

输出：

```text
1 2 3 4 6 7 9
```

### 示例 2

输入：

```text
4
0 -5 0 8
```

输出：

```text
-5 0 0 8
```

### 提示

- 第一行一个整数 n，范围是 1 到 1000
- 第二行 n 个整数，用空格分隔
- 输出一行 n 个整数，从小到大排列，用空格分隔，行末换行
- 选择排序一共做 n-1 趟。第 i 趟从第 i 个元素起，在没排好的那一段里找最小的元素
- 找到最小元素的下标后，把它和第 i 个元素交换，这一趟就定下了第 i 小的数
- 找最小值要单独用一个变量记下标，先假定起点就是最小的，再逐个往后比较
- 如果最小元素本来就在第 i 个位置，交换两个相同的下标也不影响结果
- 判题只看输出的序列，用别的方法排出同样的结果也算通过
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业16">
  <div class="judge__bar">
    <label class="judge__label" for="judge-id">你的学号：</label>
    <input id="judge-id" class="judge__id" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="11位学号">
    <button id="judge-submit" type="button">提交</button>
  </div>

  <div class="judge__editor">
    <pre class="judge__gutter" id="judge-gutter" aria-hidden="true"></pre>
    <pre class="judge__highlight" id="judge-highlight" aria-hidden="true"></pre>
    <textarea id="judge-code" class="judge__code" spellcheck="false" placeholder="// 在这里粘贴你的代码"></textarea>
  </div>

  <p class="judge__progress" id="judge-progress" hidden></p>
  <p class="judge__error" id="judge-error" hidden></p>
  <p class="judge-summary" id="judge-summary" hidden></p>

  <div class="judge__compile" id="judge-compile-error" hidden>
    <p>编译未通过，报错信息如下：</p>
    <pre></pre>
  </div>

  <div id="judge-cases" hidden></div>
</div>


!!! note "判题环境"

    判题用的是服务器的 `isolate` 沙箱：

    - 操作系统：Ubuntu-26.04
    - 编译器：GCC 15.2.0
    - 编译参数：`-O2 -std=gnu23`
    - 每个测试点限时 1 秒
    - 每个测试点限制内存 256 MB
