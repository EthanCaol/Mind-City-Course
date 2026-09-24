# Dev-C++ 使用教程

## 1. 安装 Dev-C++

### 1.1 下载安装包

打开下面的发布页面，下载 **Dev-Cpp 5.11 TDM-GCC 4.9.2 Setup.exe**。该安装包包含 Dev-C++ 和编译器。

<https://sourceforge.net/projects/orwelldevcpp/files/Setup%20Releases/>

![Dev-C++ 下载页面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700001.png)

### 1.2 开始安装

1. 双击安装文件。在 **Installer Language** 窗口中选择 **English**，单击 **OK**。

   ![安装程序语言选择](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700002.png)

2. 进入 **License Agreement** 页面后，单击 **I Agree**。

3. 在 **Choose Components** 页面保留默认组件，确认其中包含 **TDM-GCC 4.9.2 compiler** 和 **Language files**，然后单击 **Next**。

   ![安装组件选择](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700005.png)

4. 在 **Choose Install Location** 页面选择安装位置，单击 **Install**。

5. 安装完成后，保留 **Run Dev-C++ 5.11**，单击 **Finish**。

   ![安装完成页面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700003.png)

6. 首次启动时，在 **Select your language** 列表中选择简体中文或 **Chinese**，单击 **Next**，按向导完成设置。

   ![首次启动语言选择](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700004.png)

## 2. 切换为中文界面

软件已经打开时，可以在环境选项中更改界面语言。

1. 单击 **Tools**，再单击 **Environment Options**。中文界面对应「工具」和「环境选项」。
2. 打开「基本」选项卡，在「语言」列表中选择「简体中文 Chinese」。
3. 单击「确定」。如果菜单没有立即变化，关闭并重新打开 Dev-C++。

![环境选项中的语言设置](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700006.png)

## 3. 认识 Dev-C++ 主界面

![Dev-C++ 5.11 主界面](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700007.png)

1. 顶部菜单栏用于新建、保存、编译和运行程序。
2. 中间编辑区用于输入代码。标签中的星号表示当前修改尚未保存。
3. 底部信息区显示编译结果和错误信息。
4. 右上方编译器列表显示 **TDM-GCC 4.9.2 64-bit Release**。

## 4. 新建并保存代码

### 4.1 新建源文件

1. 单击「文件」，选择「新建」，再选择「源代码」。也可以按 ++ctrl+n++。

   ![新建源代码](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700008.png)

2. 在编辑区输入下面的代码。代码中的括号、引号和分号均使用英文符号。

```c title="hello.c"
--8<-- "code/hello.c"
```

### 4.2 保存代码

1. 按 ++ctrl+s++，打开保存窗口。
2. 进入 `D:\CppPractice\lesson01` 文件夹。
3. 在文件名中输入 `hello.c`，文件类型选择 **C source files**，然后单击「保存」。

![保存 hello.c](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700009.png)

保存完成后，编辑器标签显示 `hello.c`。以后可通过「文件」中的「打开项目或文件」重新打开该文件。

## 5. 编译运行程序

1. 按 ++ctrl+s++ 保存代码。
2. 单击「运行」，再单击「编译运行」，或直接按 ++f11++。

   ![编译运行命令](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700010.png)

3. 编译成功后，控制台窗口显示 `Hello, Fudan!`。底部编译信息中的错误数应为 0。

   ![控制台运行结果](https://image-1379176255.cos.ap-shanghai.myqcloud.com/20260914141700011.png)

控制台显示「请按任意键继续」时，按任意键关闭窗口。回到编辑器后，可以修改双引号中的文字，保存并再次按 ++f11++ 查看新结果。

## 阅读登记

读完这一篇的话，填上学号点一下就行。不计分，只是让助教知道大家跟到哪了。

<div class="read" id="read" data-page="dev-cpp">
  <div class="read__bar">
    <input id="read-id" class="read__input" type="text" inputmode="numeric" autocomplete="off" maxlength="11" placeholder="11 位学号">
    <button id="read-submit" type="button">我已读完</button>
  </div>
  <p class="read__note" id="read-note" hidden></p>
</div>
