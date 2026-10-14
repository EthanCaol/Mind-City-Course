---
icon: material/pencil-outline
---

# 作业 6：绩点换算

从键盘读入一个百分制成绩，输出它对应的等级和绩点。

复旦的课程考核成绩和绩点的换算关系如下表：

| 等级 | 绩点 | 百分制 |
| ---- | ---- | ------ |
| A    | 4.0  | 90 ~ 100 |
| A-   | 3.7  | 85 ~ 89  |
| B+   | 3.3  | 82 ~ 84  |
| B    | 3.0  | 78 ~ 81  |
| B-   | 2.7  | 75 ~ 77  |
| C+   | 2.3  | 71 ~ 74  |
| C    | 2.0  | 66 ~ 70  |
| C-   | 1.7  | 62 ~ 65  |
| D    | 1.3  | 60 ~ 61  |
| F    | 0    | 59 及以下 |

表中的 `D-`、`P`、`NP` 三档不按百分制分数划分（`D-` 是补考合格，`P`、`NP` 用于两级记分），本题不涉及。

### 示例 1

```text
输入：85
输出：A- 3.7
```

### 示例 2

```text
输入：59
输出：F 0.0
```

### 提示

- 输入一行，一个 0 到 100 的整数
- 输出一行，等级和绩点，中间用一个空格分隔，行末换行
- 绩点保留一位小数，用 `%.1f` 输出。表中 `F` 的绩点写的是 `0`，按一位小数打出来是 `0.0`
- 分档看区间端点：`90` 是 A、`89` 是 A-、`85` 仍是 A-、`84` 是 B+
- 除结果外不要输出任何内容，程序不要打印「请输入成绩」之类的提示文字


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业6">
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
