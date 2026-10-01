---
icon: material/pencil-outline
---

# 作业 2：整数的和差积商余

从键盘读入两个整数，然后按 `和 差 积 商 余数` 的顺序打印这五项结果。

### 示例 1

```text
输入：17 5
输出：22 12 85 3 2
```

### 示例 2

```text
输入：-17 5
输出：-12 -22 -85 -3 -2
```

### 提示

- 输入一行，两个整数，中间用空格分隔，第二个数保证非零
- 两个数的绝对值都不超过 1000，结果都在 `int` 能表示的范围内
- 五项结果输出在同一行，用空格分隔，行末换行
- 商和余数都用整数运算，不要写成浮点除法
- C语言的整除是向零取整：`-17 / 5` 得 `-3`，不是 `-4`；余数的符号和被除数相同
- 除结果外不要输出任何内容，程序不要打印「请输入两个整数」之类的提示文字


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，然后先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业2">
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
