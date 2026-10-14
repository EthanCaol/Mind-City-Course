---
icon: material/pencil-outline
---

# 作业 8：四则运算

第一行读入一个整数 n，之后 n 行每行是一个算式，形如 `a op b`，其中 a、b 是两个浮点数，op 是加、减、乘、除中的一个运算符。输出每个算式的计算结果。

### 示例 1

```text
输入：
3
7.5 + 2.5
10 / 3
-3.5 * -2
输出：
10.00
3.33
7.00
```

### 示例 2

```text
输入：
1
1.25 - 0.75
输出：
0.50
```

### 提示

- 第一行一个整数 n，范围是 1 到 100
- 之后 n 行，每行形如 `12.5 * 2`，参与运算的两个数与运算符之间各有一个空格
- a、b 是浮点数，用 `double` 存放，读入时转换说明符用 `%lf`
- 运算符只有 `+`、`-`、`*`、`/` 四个，可以用 `switch` 按运算符分路
- 保证除法的除数不为 0
- 输出 n 行，每行一个结果，保留两位小数（`%.2f`），行末换行
- 除结果外不要输出任何内容，程序不要打印「请输入算式」之类的提示文字


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业8">
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
