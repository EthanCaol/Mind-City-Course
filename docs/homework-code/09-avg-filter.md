---
icon: material/pencil-outline
---

# 作业 9：很多个数的平均分

从键盘读入若干个整数，每行一个，读到 `-1` 就停止读入。

这些数里，0 到 100 之间的记入统计，其余范围内的跳过不计。输出记入的这些数的平均分。

### 示例 1

输入：

```text
85
72
-5
90
-1
```

输出：

```text
82.33
```

解析：`85`、`72`、`90` 在 0 到 100 之间，计入统计；`-5` 超出范围，跳过；`-1` 表示输入结束。三个数之和是 247，平均分 247 / 3 ≈ 82.33。

### 示例 2

输入：

```text
90
-1
70
-1
```

输出：

```text
90.00
```

解析：读到第一个 `-1` 就结束，后面的 `70` 和第二个 `-1` 都不再读。只有 `90` 计入统计，一个数的平均分就是它本身。

### 提示

- 每行一个整数，读到 `-1` 为止
- `-1` 用来说明输入结束，它本身不参与统计；`-1` 之后可能还有内容，都不用再读
- 记入的范围是 0 到 100（含两端），范围之外的整数跳过不计
- 数的个数事先不知道，读数和累加在同一个循环里完成
- 保证至少有一个数落在 0 到 100 之间
- 输出一行，平均分保留两位小数，行末换行
- 平均分要用浮点除法算，两个整数相除会丢掉小数部分
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业9">
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
