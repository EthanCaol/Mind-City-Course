# 第15章 位操作

## 二进制整数与字节

!!! abstract "语法形式"

    ```text
    第 7 位 ... 第 0 位
    值 = b7*128 + b6*64 + ... + b0*1
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char b = 0xff;   /* 11111111 */
        signed char s = -1;       /* 补码 11111111 */
        printf("%u %d\n", b, s);
        return 0;
    }
    ```

    输出：

    ```text
    255 -1
    ```

!!! note "说明"

    - C 的字节位数由实现决定，本章按 8 位说明
    - 8 位无符号范围是 0 到 255，共 256 个位组合
    - 8 位有符号范围是 -128 到 127，同样是 256 个位组合
    - 位编号与 2 的幂一一对应，最高位称为高阶位
    - 同一个位组合的含义由类型决定

    ![图15.1 位编号和位值](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00075.jpg)

!!! warning "常见错误"

    - 把 1 字节固定当作 8 位
    - 把 11111111 一律读作 255 或 -1，忽略类型

## 有符号整数的表示

!!! abstract "语法形式"

    ```text
    -n = ~n + 1
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        signed char n = -128;             /* 10000000 */
        unsigned char u = (unsigned char)n;
        printf("%u %d\n", u, (signed char)(~u + 1));
        return 0;
    }
    ```

    输出：

    ```text
    128 -128
    ```

!!! note "说明"

    - 符号量： 最高位存符号，范围 -127 到 127，有 +0 与 -0
    - 反码： 逐位反转得到负数，范围 -127 到 127，有 -0
    - 补码： 反转再加 1 得到负数，范围 -128 到 127，只有一个 0
    - 补码是常用表示，有符号数的表示方式由实现决定
    - 取补码的相反数，先反转每一位再加 1

!!! warning "常见错误"

    - 把 `10000000` 按符号量读成 -0
    - 认为有符号表示由 C 标准统一规定

## 八进制记数法

!!! abstract "语法形式"

    ```c
    int n = 0377;   /* 前导 0 表示八进制 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int n = 0377;
        printf("0%o %d\n", n, n);
        return 0;
    }
    ```

    输出：

    ```text
    0377 255
    ```

    表15-1 与八进制位等价的二进制位

    | 八进制位 | 二进制位 | 八进制位 | 二进制位 |
    | -------- | -------- | -------- | -------- |
    | 0 | 000 | 4 | 100 |
    | 1 | 001 | 5 | 101 |
    | 2 | 010 | 6 | 110 |
    | 3 | 011 | 7 | 111 |

!!! note "说明"

    - 每个八进制位对应 3 个二进制位
    - 前导 0 是八进制记号的组成部分，不能省略
    - 转成二进制时中间的 0 不能去掉
    - `0173` 的二进制是 `01111011`，不是 `0111111`
    - 一个 3 位八进制数可能要用 9 位二进制表示
    - 掩码常写成八进制，便于按位阅读

!!! warning "常见错误"

    - 把 `0377` 当作十进制 377
    - 转换时删掉中间的 0

## 十六进制记数法

!!! abstract "语法形式"

    ```c
    int n = 0xA3F;   /* 0x 或 0X 开头, 大小写等价 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        int n = 0xA3F;
        printf("0x%X %d\n", n, n);
        return 0;
    }
    ```

    输出：

    ```text
    0xA3F 2623
    ```

    表15-2 十进制，十六进制与等价的二进制

    | 十进制 | 十六进制 | 二进制 | 十进制 | 十六进制 | 二进制 |
    | ------ | -------- | ------ | ------ | -------- | ------ |
    | 0 | 0 | 0000 | 8 | 8 | 1000 |
    | 1 | 1 | 0001 | 9 | 9 | 1001 |
    | 2 | 2 | 0010 | 10 | A | 1010 |
    | 3 | 3 | 0011 | 11 | B | 1011 |
    | 4 | 4 | 0100 | 12 | C | 1100 |
    | 5 | 5 | 0101 | 13 | D | 1101 |
    | 6 | 6 | 0110 | 14 | E | 1110 |
    | 7 | 7 | 0111 | 15 | F | 1111 |

!!! note "说明"

    - 每个十六进制位对应 4 个二进制位
    - 两个十六进制位恰好对应 1 个字节
    - 字母 A 到 F 表示 10 到 15，大小写均可
    - `0xC2` 对应 `11000010`，`0xD5` 对应 `11010101`
    - 表示位的位置时，十六进制比十进制直观

!!! warning "常见错误"

    - 漏写 `0x` 前缀
    - 把 `0x10` 当作十进制 10

## 按位取反

!!! abstract "语法形式"

    ```c
    ~整数
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char val = 2;            /* 00000010 */
        printf("%u %u\n", val, (unsigned char)~val);
        return 0;
    }
    ```

    输出：

    ```text
    2 253
    ```

!!! note "说明"

    - `~` 是一元运算符，把每一位的 0 与 1 对换
    - 运算不改变操作数本身，只产生新值
    - 需要改变原变量时写 `val = ~val`
    - 整型提升会把窄类型转成 `int`，截回原宽度用强制转换或掩码
    - 掩码中常与 `~` 配合清空某些位

!!! warning "常见错误"

    - 以为 `~val` 修改了 `val`
    - 直接打印 `unsigned char` 的 `~val`，得到提升后的 32 位结果

## 按位与

!!! abstract "语法形式"

    ```c
    a & b
    a &= b
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char a = 0x93;   /* 10010011 */
        unsigned char b = 0x3d;   /* 00111101 */
        printf("0x%02X\n", (unsigned char)(a & b));
        return 0;
    }
    ```

    输出：

    ```text
    0x11
    ```

!!! note "说明"

    - 两位都为 1 时结果位为 1，否则为 0
    - 结果不影响操作数的其他位
    - `a &= b` 等价于 `a = a & b`
    - 按位与常用于掩码与截取低位

!!! warning "常见错误"

    - 与逻辑与 `&&` 混用
    - 以为 `&` 返回 0 或 1，它返回完整的位组合

## 按位或

!!! abstract "语法形式"

    ```c
    a | b
    a |= b
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char a = 0x93;   /* 10010011 */
        unsigned char b = 0x3d;   /* 00111101 */
        printf("0x%02X\n", (unsigned char)(a | b));
        return 0;
    }
    ```

    输出：

    ```text
    0xBF
    ```

!!! note "说明"

    - 任一位为 1 时结果位为 1
    - 两位都为 0 时结果位才为 0
    - `a |= b` 等价于 `a = a | b`
    - 按位或常用于打开指定的位

!!! warning "常见错误"

    - 与逻辑或 `||` 混用
    - 以为 `|` 会把两个数的数值相加

## 按位异或

!!! abstract "语法形式"

    ```c
    a ^ b
    a ^= b
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char a = 0x93;   /* 10010011 */
        unsigned char b = 0x3d;   /* 00111101 */
        printf("0x%02X\n", (unsigned char)(a ^ b));
        return 0;
    }
    ```

    输出：

    ```text
    0xAE
    ```

!!! note "说明"

    - 两位不同时结果位为 1，相同时为 0
    - 与 1 异或翻转该位，与 0 异或保持该位
    - `a ^= b` 等价于 `a = a ^ b`
    - 同一个值异或两次可恢复原值

!!! warning "常见错误"

    - 把 `^` 当作乘方运算符
    - 与按位或 `|` 混用

## 掩码

!!! abstract "语法形式"

    ```c
    值 & 掩码
    值 &= 掩码
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char flags = 0xab;       /* 10101011 */
        printf("0x%02X 0x%02X\n",
               flags & 0x02, flags & 0x0f);
        return 0;
    }
    ```

    输出：

    ```text
    0x02 0x0B
    ```

    ![图15.2 掩码示例](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00076.jpg)

!!! note "说明"

    - 掩码是若干位为 1，其余位为 0 的位组合
    - 与掩码为 1 的位保留原值，为 0 的位清 0
    - 掩码宽度至少要与被覆盖的值相同
    - `ch &= 0xff` 把 `ch` 截成低 8 位，其他位清 0
    - `0xff` 与 `0377` 都表示 8 个 1

!!! warning "常见错误"

    - 掩码比目标值窄，高位信息漏过边界
    - 用 `|` 做掩码，结果保留了不该保留的位

## 打开位

!!! abstract "语法形式"

    ```c
    flags |= MASK;
    flags = flags | MASK;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char flags = 0x0f;       /* 00001111 */
        unsigned char mask = 0xb6;        /* 10110110 */
        printf("0x%02X\n", (unsigned char)(flags | mask));
        return 0;
    }
    ```

    输出：

    ```text
    0xBF
    ```

!!! note "说明"

    - 掩码为 1 的位强制置 1
    - 掩码为 0 的位保持原值
    - 打开多个位时用按位或组合多个掩码
    - 例： 用 `BLUE | RED` 同时打开蓝色位与红色位

!!! warning "常见错误"

    - 用 `&=` 打开位，结果只会清位
    - 把掩码写反，实际清掉了目标位

## 关闭位

!!! abstract "语法形式"

    ```c
    flags &= ~MASK;
    flags = flags & ~MASK;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char flags = 0x0f;       /* 00001111 */
        unsigned char mask = 0xb6;        /* 10110110 */
        printf("0x%02X\n", (unsigned char)(flags & ~mask));
        return 0;
    }
    ```

    输出：

    ```text
    0x09
    ```

!!! note "说明"

    - `~MASK` 把掩码取反，原掩码为 1 的位变成 0
    - 与取反后的掩码做按位与，目标位清 0
    - 掩码为 0 的位在取反后为 1，原值保持不变
    - `~` 的结果是 `int`，赋回窄类型时按原宽度截断

!!! warning "常见错误"

    - 写成 `flags &= MASK`，实际保留了目标位
    - 写成 `flags &= !MASK`，逻辑非只得到 0 或 1

## 切换位

!!! abstract "语法形式"

    ```c
    flags ^= MASK;
    flags = flags ^ MASK;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char flags = 0x0f;       /* 00001111 */
        unsigned char mask = 0xb6;        /* 10110110 */
        printf("0x%02X\n", (unsigned char)(flags ^ mask));
        return 0;
    }
    ```

    输出：

    ```text
    0xB9
    ```

!!! note "说明"

    - 掩码为 1 的位被翻转，0 变 1 或 1 变 0
    - 掩码为 0 的位保持原值
    - 连续执行两次同一操作可恢复原值
    - 切换位也称转置位

!!! warning "常见错误"

    - 用 `|` 代替 `^`，已打开的位无法关闭
    - 用 `&` 代替 `^`，已关闭的位无法打开

## 检查位的值

!!! abstract "语法形式"

    ```c
    if ((flags & MASK) == MASK)
        /* 位已打开 */
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define MASK 0x02
    int main(void)
    {
        unsigned char flags = 0xab;       /* 10101011 */
        if ((flags & MASK) == MASK)
            puts("bit 1 is set");
        return 0;
    }
    ```

    输出：

    ```text
    bit 1 is set
    ```

!!! note "说明"

    - 先用掩码覆盖其他位，只留下待检查的位
    - 再把结果与掩码比较，相等表示该位为 1
    - 圆括号不能省，`&` 的优先级低于 `==`
    - 只检查一位时也可写成 `if (flags & MASK)`
    - 掩码宽度至少要与被检查的值相同

!!! warning "常见错误"

    - 写成 `if (flags == MASK)`，其他位会使比较失败
    - 漏写圆括号，表达式变成 `flags & (MASK == MASK)`

## 左移

!!! abstract "语法形式"

    ```c
    值 << n
    值 <<= n
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char x = 0x8a;           /* 10001010 */
        printf("0x%02X %d\n", (unsigned char)(x << 2), 1 << 3);
        return 0;
    }
    ```

    输出：

    ```text
    0x28 8
    ```

!!! note "说明"

    - 每一位向左移动 `n` 位
    - 移出左端的位丢弃，右端空位补 0
    - 运算产生新值，不改变原操作数
    - `x << n` 等价于 `x` 乘以 2 的 `n` 次幂
    - 对负数左移或有符号结果溢出属于未定义行为
    - `1 << n` 表示只有第 `n` 位为 1 的值，常用于生成掩码

!!! warning "常见错误"

    - 移位位数大于等于类型宽度
    - 指望移出左端的位仍然保留

## 右移

!!! abstract "语法形式"

    ```c
    值 >> n
    值 >>= n
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    int main(void)
    {
        unsigned char u = 0x8a;           /* 10001010 */
        signed char s = (signed char)0x8a;
        printf("0x%02X %d\n", (unsigned char)(u >> 2), s >> 2);
        return 0;
    }
    ```

    输出：

    ```text
    0x22 -30
    ```

!!! note "说明"

    - 每一位向右移动 `n` 位
    - 移出右端的位丢弃
    - 无符号类型空位补 0
    - 有符号类型空位补 0 或补符号位，由实现决定
    - 非负值右移 `n` 位等价于除以 2 的 `n` 次幂
    - 本机 GCC 对有符号负数采用算术右移，空位补符号位

!!! warning "常见错误"

    - 假定有符号负数右移一定补 0
    - 把右移当作精确的除法，忽略负数与截断

## 移位的用途

!!! abstract "语法形式"

    ```c
    x << n
    x >> n
    (x >> 偏移) & 掩码
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    #define BYTE_MASK 0xff
    int main(void)
    {
        unsigned long color = 0x002a162f;
        printf("0x%02lX 0x%02lX\n",
               color & BYTE_MASK,
               (color >> 8) & BYTE_MASK);
        return 0;
    }
    ```

    输出：

    ```text
    0x2F 0x16
    ```

!!! note "说明"

    - 左移 `n` 位实现乘以 2 的 `n` 次幂
    - 非负值右移 `n` 位实现除以 2 的 `n` 次幂
    - `0x002a162f` 的低字节，次低字节，第三字节
      分别存放红，绿，蓝的强度
    - 提取字段时先右移到低位，再用等宽掩码截取
    - `(color >> 16) & 0xff` 取第三字节

!!! warning "常见错误"

    - 只移位不掩码，把相邻字段一并取出
    - 掩码宽度大于字段宽度

## 位字段的声明

!!! abstract "语法形式"

    ```c
    struct 标签 {
        unsigned int 字段名 : 宽度;
        ...
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    struct {
        unsigned int autfd : 1;
        unsigned int bldfc : 1;
        unsigned int undln : 1;
        unsigned int itals : 1;
    } prnt;

    int main(void)
    {
        prnt.itals = 0;
        prnt.undln = 1;
        printf("%u %u\n", prnt.itals, prnt.undln);
        return 0;
    }
    ```

    输出：

    ```text
    0 1
    ```

!!! note "说明"

    - 位字段是 `int` 或 `unsigned int` 中一组相邻的位
    - 字段类型也可用 `_Bool`，此时宽度只能为 1
    - 宽度为 `n` 的字段可存 0 到 2 的 `n` 次幂减 1
    - 用普通成员运算符 `.` 访问字段
    - 总宽度超过一个存储单元时，编译器换用下一个单元
    - 字段的存储顺序与边界位置由实现决定，通常不可移植

!!! warning "常见错误"

    - 赋给字段的值超出字段宽度
    - 对位字段使用取地址运算符 `&`
    - 假定位字段的布局与某硬件寄存器一致

## 未命名字段

!!! abstract "语法形式"

    ```c
    unsigned int : 宽度;
    unsigned int : 0;
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    struct {
        unsigned int field1 : 1;
        unsigned int        : 2;
        unsigned int field2 : 1;
        unsigned int        : 0;
        unsigned int field3 : 1;
    } stuff;

    int main(void)
    {
        printf("%zu\n", sizeof stuff);    /* GCC 下为 8 */
        return 0;
    }
    ```

    输出：

    ```text
    8
    ```

!!! note "说明"

    - 未命名字段用作填充，不能访问
    - 宽度为 0 的未命名字段迫使下一字段从下一存储单元开始
    - 本例中 `field1` 与 `field2` 之间隔 2 位
    - `field3` 被移到下一个 `unsigned int` 单元
    - 存储单元的大小与对齐由实现决定

!!! warning "常见错误"

    - 试图给未命名字段赋值
    - 认为 `: 0` 不占空间但仍允许后续字段跨界

## 联合与位字段

!!! abstract "语法形式"

    ```c
    union 标签 {
        结构类型 st_view;
        整数类型 us_view;
    };
    ```

!!! example "示例"

    ```c
    #include <stdio.h>
    union {
        struct { unsigned int a : 1, b : 3; } st;
        unsigned char uc;
    } v;
    int main(void)
    {
        v.st.a = 1;
        v.st.b = 2;
        printf("%02X\n", v.uc);
        return 0;
    }
    ```

    输出：

    ```text
    05
    ```

    ![图15.3 作为整数和结构的联合](https://image-1379176255.cos.ap-shanghai.myqcloud.com/c-primer-plus/images/Image00077.jpg)

!!! note "说明"

    - 联合的成员共享同一块内存
    - `st` 视图按字段访问，`uc` 视图按位组合访问
    - 字段对应哪些位由实现与字节序决定
    - 示例输出 `05` 是本机小端 GCC 的结果
    - 位字段版本可直接赋值，例如 `box.fill_color = CYAN`
    - 按位版本需要位置常量，设置前通常先清空字段
    - 修改同一字段时，位字段写法比按位写法简单

!!! warning "常见错误"

    - 假定第一个字段一定位于最低位
    - 用位字段布局解析外部文件或硬件数据
    - 在联合中初始化多个成员

## 复习题

（1）把下面的十进制转换为二进制
a. `3`
b. `13`
c. `59`
d. `119`

??? note "答案"

    a. `00000011`
    b. `00001101`
    c. `00111011`
    d. `01110111`

（2）把下面的二进制值转换为十进制，八进制和十六进制
a. `00010101`
b. `01010101`
c. `01001100`
d. `10011101`

??? note "答案"

    a. `21, 025, 0x15`
    b. `85, 0125, 0x55`
    c. `76, 0114, 0x4C`
    d. `157, 0235, 0x9D`

（3）对下面的表达式求值，假设每个值都为 8 位
a. `~3`
b. `3 & 6`
c. `3 | 6`
d. `1 | 6`
e. `3 ^ 6`
f. `7 >> 1`
g. `7 << 2`

??? note "答案"

    a. `252`，b. `2`，c. `7`，d. `7`，e. `5`，f. `3`，g. `28`

（4）对下面的表达式求值，假设每个值都为 8 位
a. `~0`
b. `!0`
c. `2 & 4`
d. `2 && 4`
e. `2 | 4`
f. `2 || 4`
g. `5 << 3`

??? note "答案"

    a. `255`，b. `1`，c. `0`，d. `1`，e. `6`，f. `1`，g. `40`

（5）ASCII 码只使用最后 7 位，用掩码关闭其他位
这个掩码的二进制，十进制，八进制和十六进制各是什么

??? note "答案"

    `1111111`，`127`，`0177`，`0x7F`

（6）把下面的代码
```c
while (bits-- > 0)
{
    mask |= bitval;
    bitval <<= 1;
}
```
换成
```c
while (bits-- > 0)
{
    mask += bitval;
    bitval *= 2;
}
```
程序照常工作，这是否说明 `*= 2` 等同于 `<<= 1`，`+=` 是否等同于 `|=`

??? note "答案"

    `bitval * 2` 与 `bitval << 1` 都把当前值加倍，两者等效
    `mask += bitval` 与 `mask |= bitval` 只在没有重叠的 1 位时等效
    例如 `2 | 4` 得 `6`，而 `3 | 6` 也得 `6`，但 `3 + 6` 得 `9`

（7）Tinkerbell 计算机的一个硬件字节存放下列信息
位 0 到 1 是软驱数量，位 2 未使用，位 3 到 4 是 CD-ROM 数量
位 5 未使用，位 6 到 7 是硬盘数量
a. 从右往左填充位字段，写出位字段模板
b. Klinkerbell 从左往右填充，写出对应的模板

??? note "答案"

    a.

    ```c
    struct tb_drives {
        unsigned int diskdrives  : 2;
        unsigned int             : 1;
        unsigned int cdromdrives : 2;
        unsigned int             : 1;
        unsigned int harddrives  : 2;
    };
    ```

    b.

    ```c
    struct kb_drives {
        unsigned int harddrives  : 2;
        unsigned int             : 1;
        unsigned int cdromdrives : 2;
        unsigned int             : 1;
        unsigned int diskdrives  : 2;
    };
    ```

## 编程练习

!!! question "编程练习"

    1. 编写一个函数，把二进制字符串转换为一个数值
    例如把 `char * pbin = "01001001";` 的 `pbin` 传入后
    函数返回 `int` 类型的值 73

    2. 编写一个程序，通过命令行参数读取两个二进制字符串
    对这两个数使用 `~`，`&`，`|`，`^` 运算符
    并以二进制字符串形式打印结果
    无法使用命令行环境时，改用交互方式读取字符串

    3. 编写一个函数，接受一个 `int` 类型的参数
    返回该参数中打开位的数量，并在一个程序中测试

    4. 编写一个程序，接受两个 `int` 类型的参数
    一个是值，一个是位的位置
    指定位为 1 时函数返回 1，否则返回 0，并在程序中测试

    5. 编写一个函数，把 `unsigned int` 值中的所有位向左旋转指定位数
    例如 `rotate_l(x, 4)` 把 `x` 的所有位左移 4 位
    从最左端移出的位重新出现在右端，并在程序中测试

    6. 设计一个位字段结构储存下面的字体信息
    字体 ID: `0` 到 `255` 之间的数
    字体大小： `0` 到 `127` 之间的数
    对齐： `0` 到 `2`，表示左对齐，居中，右对齐
    加粗： 开 `1` 或闭 `0`
    斜体： 开 `1` 或闭 `0`
    在程序中使用该结构打印字体参数，并用循环菜单修改参数
    用按位与运算符和合适的掩码把字体 ID 与大小限制在指定范围

    7. 编写一个与第 6 题功能相同的程序
    改用 `unsigned long` 变量储存字体信息
    并用按位运算符代替位字段管理这些信息
