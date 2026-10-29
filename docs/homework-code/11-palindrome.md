---
icon: material/pencil-outline
---

# 作业 11：回文判断

从键盘读入一行英文字母，判断它正着读和倒着读是否相同。

读的时候不区分大小写，`L` 和 `l` 算同一个字母。

### 示例 1

输入：

```text
Level
```

输出：

```text
yes
```

### 示例 2

输入：

```text
Fudan
```

输出：

```text
no
```

### 提示

- 输入一行，只含大小写英文字母，长度是 1 到 100
- 字符串长度用 `strlen`，要包含 `<string.h>`
- 比较之前可以先把两个字符统一成同一种大小写：统一成小写用 `tolower`，统一成大写用 `toupper`
- `strlwr` 和 `strupr` 是微软特供编译器 MSVC 提供的函数，不在 C 语言的标准库里：判题用的 gcc 没有这两个函数，写进去会编译失败，转大小写请用上面那两种标准写法
- 先比较第 `0` 个和第 `n-1` 个，然后接着比较第 `1` 个和第 `n-2` 个
    两个下标逐位往中间走，直到相遇就结束判断
- 用一个变量记下结果，发现有一对不相等的字符就可以结束比较
- 输出 `yes` 或 `no`，小写，行末换行
- 除结果外不用输出其他内容


## 提交和评测

!!! note "先自测，再提交"
    - 使用 IDE 写好代码，先在本机运行一遍样例
    - 所有样例通过后，再把代码粘贴到这里进行提交
    - 助教服务器的性能有限，建议先自测再提交
    - 2 分钟最多交 5 次，如果提交太频繁会被拒绝，稍后再提交即可

<div class="judge" id="judge" data-homework="作业11">
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
