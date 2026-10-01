
# VSCode 自定义编译任务与调试

## 第一期：单文件与多文件调试

!!! quote "视频"

    [《在 macOS 上用 VSCode 调试 C代码》](https://www.bilibili.com/video/BV17M411D7kq)

    ![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260930091700441.jpg)

调试环境由两个配置文件组成，这期视频演示的就是它们的生成过程：

- `.vscode/tasks.json`：编译任务，由 C/C++ 插件生成，决定用哪条命令编译，以及确定生成的可执行文件叫什么名字
- `.vscode/launch.json`：调试任务，由 C/C++ 插件生成（视频中 MacOS 还需要使用 CodeLLDB 插件），决定调试器选择调试哪个可执行文件

这期的流程讲得最清楚，建议完整看一遍。

??? note "延伸：GNU 系与 LLVM 系的来历"

    课程里装的是 GCC 和 GDB，属于 GNU 系；视频中用到的工具是 Clang 和 LLDB，属于 LLVM 系。
    
    |        | GNU 系        | LLVM 系 |
    | ------ | ------------- | ------- |
    | 编译器 | `gcc` / `g++` | `clang` |
    | 调试器 | `gdb`         | `lldb`  |

    GCC 是 GNU Compiler Collection 的缩写，最初叫 GNU C Compiler（1987 年，Richard Stallman 发起）。
    
    LLVM 是 Apple 为了换掉 GCC 的开源生态而发展起来的：Apple 的自家产品一向不开源，而 GCC 从 4.3 版起改用 GPLv3，改过的编译器必须连源码一起发布，在闭源产品里放一份自己改的 GNU 工具链因此不可行。

因为使用的编译套件不同，所以看这期视频的时候不用照抄配置，重点是弄清两个文件各管什么，点击「运行」和「调试」的背后依次发生了什么。

## 第二期：换成 GCC 与 GDB

!!! quote "视频"

    [《VsCode 配置 | C/C++ | MakeFile | CMake | Minimal》](https://www.bilibili.com/video/BV1H24y1D7Kn?t=587)

    ![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914214845964.jpg)

这期在《VSCode 入门教程》里出现过，讲的是 C/C++ 开发环境的整套配置，从这里开始看即可。

照着配之前有一点要自己换：这期演示的是 C++，编译命令用的是 `g++`。而课程里写的是 C 代码，配置的时候把 `g++` 换成 `gcc` 即可，其余不需要改。

---

!!! todo "文档完成登记：完成本文全部流程后告知助教"

    <div class="read" id="read" data-page="vscode-debug">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
