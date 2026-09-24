
# VSCode 入门教程

## 1. 跟着视频配置（强烈推荐）

下面这两期视频讲得很细，**非常建议大家跟着做一遍**：

- [《VSCode 配置 | 外观 | 通用型扩展 | Minimal》](https://www.bilibili.com/video/BV1YW4y1M7uX)
- [《VSCode 配置 | C/C++ | MakeFile | CMake | Minimal》](https://www.bilibili.com/video/BV1H24y1D7Kn)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914214817142.jpg)

![](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914214845964.jpg)


### 1.1 先新建一个配置文件（Profile）

视频里的第一步是新建一个配置文件（Profile）。这一步在视频里的操作画面被挡住了，看不清，所以这里补一份文字版步骤：

![视频里那一步的截图，菜单被挡住了一部分](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260921113808647.png)

#### 第 1 步：打开配置文件页面

点左下角的齿轮图标（Manage / 管理），菜单里有一项 Profiles。鼠标移上去会展开子菜单，在子菜单里点 Profiles：

![管理菜单里的 Profiles 子菜单](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260921113940672.png)

#### 第 2 步：创建新的配置文件并保存

配置文件页面打开后，点左上角的 New Profile，在 Name 里填个自己想要的名字，然后点 Create：

![New Profile 表单：填好 Name，再点 Create](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260921115659950.png)

#### 第 3 步：勾选启用新配置文件

回到左边的配置文件列表，找到刚建好的那个，点它名字后面的小方框勾选，把它切换成当前正在使用的配置文件：

![在列表中勾选新建的配置文件](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260921114101466.png)

启用之后，它旁边会显示 Active 字样，说明现在用的就是它。

到这里准备工作就完成了，视频后面的内容就可以接着往下做了。

## 2. 配置 Code Runner 的编译运行命令

点一下 ▷ 就能跑代码，是因为 Code Runner 在背后替你敲了一条命令。这条命令本身是可以改的 —— 改明白之后，你就能自己决定用什么编译器、生成的可执行文件叫什么名字、放到哪里去。

配置写在 **settings.json** 里，键名是 `code-runner.executorMap`。

### 第 1 步：先认识这些占位符

命令里那些以 `$` 开头的词，Code Runner 会在真正执行前把它们替换成实际的路径。它就是靠这套东西，才能做到「不管你跑的是哪个文件，命令都不用改」：

| 占位符                     | 替换成什么                                                                        |
| -------------------------- | --------------------------------------------------------------------------------- |
| `$workspaceRoot`           | 你在 VSCode 里打开的那个文件夹（工作区）的路径                                    |
| `$dir`                     | 需要运行的代码文件，所在的目录                                                    |
| `$dirWithoutTrailingSlash` | 同上，只是结尾不带斜杠                                                            |
| `$fileName`                | 需要运行的代码文件的名字                                                          |
| `$fileNameWithoutExt`      | 需要运行的代码文件的名字，再去掉扩展名                                            |
| `$fullFileName`            | 需要运行的代码文件的名字，并且带目录                                                  |
| `$driveLetter`             | 文件所在的盘符（只有 Windows 用得上）                                             |
| `$pythonPath`              | Python 解释器的路径（跑 Python 时才有意义，用 `Python: Select Interpreter` 设置） |

光看这张表还是很抽象，举个例子就清楚了。

假设你在 WSL 里打开的文件夹是 `/home/ethan/code`，现在要跑的是这个文件夹里的 `hello.c`：

| 占位符                | 替换结果                   |
| --------------------- | -------------------------- |
| `$workspaceRoot`      | `/home/ethan/code`         |
| `$dir`                | `/home/ethan/code`         |
| `$fullFileName`       | `/home/ethan/code/hello.c` |
| `$fileName`           | `hello.c`                  |
| `$fileNameWithoutExt` | `hello`                    |

### 第 2 步：两种常见写法

**写法一：可执行文件和源代码放在一起（推荐）**

```json title="settings.json"
"c": "cd $dir && gcc -o $fileNameWithoutExt $fileName && $dir$fileNameWithoutExt"
```

把上面的占位符代进去，这条命令展开后等价于：

```bash
cd /home/ethan/code && gcc -o hello hello.c && /home/ethan/code/hello
```

逐段看它是怎么工作的：

- `cd $dir`：切到代码文件所在的目录。`cd` 就是 change directory 的缩写。因为后面用到的都是相对路径，不切过去 gcc 就找不到你的文件。
- `&&`：把两条命令连起来，表示「左边成功了，才执行右边」。所以代码编译不通过的时候，右边那条命令就不会执行。
- `gcc -o $fileNameWithoutExt $fileName`：真正干活的一句，展开是 `gcc -o hello hello.c`。
    - `-o` 是 output 的缩写，跟在它后面的是「编译出来的可执行文件叫什么名字」。这里取的是去掉扩展名的文件名，所以 `hello.c` 编译出来得到的是 `hello`。
- `$dir$fileNameWithoutExt`：运行刚编译出来的那个程序。


**写法二：可执行文件单独放进 bin 目录（视频里演示的）**

```json title="settings.json"
"c": "cd $dir && mkdir -p bin && gcc -o bin/$fileNameWithoutExt $fileName && bin/$fileNameWithoutExt"
```

同样展开一遍：

```bash
cd /home/ethan/code && mkdir -p bin && gcc -o bin/hello hello.c && bin/hello
```

- `mkdir -p bin`：新建一个叫 `bin` 的目录。`mkdir` 就是 make directory 的缩写
    - `bin` 是 binary（二进制文件）的缩写，Linux 上习惯用它来装可执行程序
    - `-p` 的意思是「目录如果已经存在，就什么都不做」
- `gcc -o bin/$fileNameWithoutExt $fileName`：编译，但把程序输出到 `bin` 里面，也就是 `bin/hello`。
- `bin/$fileNameWithoutExt`：运行 `bin/hello`。

好处是源代码目录看着干净：一堆 `.c` 文件，加上一个 `bin` 目录，编译产物全在里面，不会和源码混在一起。

**但不太推荐这一条**，原因在后面的调试：等你要配 VSCode 的调试（`launch.json`、`tasks.json`）、或者用 Makefile 的时候，这些工具默认都假设可执行文件就躺在源代码旁边。放进 `bin` 之后，每一处都得手动改一遍路径，多一处配置就多一个踩坑的机会。

### 第 3 步：把配置写进去

改 settings.json 有两个入口，用哪个都行：

- 按 ++ctrl+shift+p++ 打开命令面板，输入 `Open User Settings (JSON)`，回车
- 或者按 ++ctrl+comma++ 打开设置界面，搜索 `code-runner.executorMap`，点旁边的「在 settings.json 中编辑」

打开后长这样，把 `executorMap` 那一项加进去（注意它要放在最外层的大括号里）：

```json title="settings.json"
{
    "code-runner.executorMap": {
        "c": "cd $dir && gcc -o $fileNameWithoutExt $fileName && $dir$fileNameWithoutExt"
    }
}
```

++ctrl+s++ 保存后立刻生效，不用重启 VSCode。

---

!!! todo "文档完成登记：告诉助教一下，你成功跑通了整个文档的流程"

    <div class="read" id="read" data-page="vscode">
      <div class="read__bar">
        <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="在这里输入你的学号">
        <button id="read-submit" type="button">我已读完</button>
      </div>
      <p class="read__note" id="read-note" hidden></p>
    </div>
