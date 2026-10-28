---
icon: material/pencil-outline
---

# 作业 14：矩阵乘法

从键盘读入两个矩阵 A 和 B，其中 A 是 m 行 n 列、B 是 n 行 p 列，输出它们的乘积 C。

### 示例 1

输入：

```text
2 3 2
1 2 3
4 5 6
7 8
9 10
11 12
```

输出：

```text
58 64
139 154
```

解析：C 的第一行第一列是 A 的第一行与 B 的第一列对应相乘再相加，即 1×7 + 2×9 + 3×11 = 58；C 的第一行第二列是 1×8 + 2×10 + 3×12 = 64；第二行同理。

### 示例 2

输入：

```text
1 1 1
3
4
```

输出：

```text
12
```

解析：A 是 1 行 1 列，B 是 1 行 1 列，结果就是 3×4。

### 提示

- 第一行三个整数 m、n、p，范围都是 1 到 100
- 接着 m 行是矩阵 A，每行 n 个整数；再接着 n 行是矩阵 B，每行 p 个整数
- 结果矩阵 C 有 m 行 p 列，C 的第 i 行第 j 列等于 A 的第 i 行与 B 的第 j 列对应元素相乘再相加
- 求 C 的一个元素要用一个从 0 开始的累加变量；走完 A 的 n 个元素（也就是 B 的这一列的 n 个元素）才有结果
- 三个矩阵都可以直接开 `[100][100]`，实际只用前 m 行、n 行、p 列
- 元素绝对值不超过 100，n 不超过 100，结果落在 `int` 能表示的范围内
- 输出 m 行，每行 p 个整数，用空格分隔，行末换行
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业14">
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
