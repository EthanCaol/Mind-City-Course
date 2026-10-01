---
icon: material/pencil-outline
---

# 作业 3：秒数换算

从键盘读入一个秒数，换算成小时、分钟、秒并输出。

### 示例 1

```text
输入：3725
输出：1 2 5
```

### 示例 2

```text
输入：86399
输出：23 59 59
```

### 提示

- 输入一行，一个非负整数，不超过 86399 秒
- 输出一行三个整数，依次是小时、分钟、秒，用空格分隔，行末换行
- 结果都在 `int` 能表示的范围内
- 除结果外不要输出任何内容，程序不要打印「请输入秒数」之类的提示文字


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业3">
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
