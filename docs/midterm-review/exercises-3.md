---
icon: material/format-list-checks
---

# 期中复习习题 3

本页是课件《期中复习习题-3》的文字版，8 页。答案按材料上的标注给出。

## 一、单选题

### 1

请选出可以作为 C 语言用户标识符的一组标识符（B）。

- A. void、define、WORD
- B. A3_B3、_123、abc
- C. FOR、-abc、Case
- D. 2a、Do、Sizeof

### 2

设有说明：`char w; int x; float y; double z;`，则表达式 `w*x+z-y` 值的数据类型为（D）。

- A. float
- B. char
- C. int
- D. double

### 3

若定义 `a[][2]={1,2,3,4,5,6,7};`，则 a 数组中行的大小是（C）。

- A. 2
- B. 3
- C. 4
- D. 无确定值

### 4

如果 a=3，b=2，c=1，则下列表达式的值为 0 的是（C）。

- A. `a>b`
- B. `(a>b)==c`
- C. `b+c<a`
- D. `c=a>b`

### 5

执行语句 `char str[]="ab\tde\\fg\n";printf("%d",strlen(str));` 后输出（B）。

- A. 12
- B. 9
- C. 14
- D. 10

### 6

有如下程序，输入数据 `12345M678<CR>` 后（`<CR>` 表示回车），x 的值是（A）。

```c
#include<stdio.h>
int main(){
int x; float y;
scanf("%6d%f",&x,&y); return 0;}
```

- A. 12345
- B. 12345M
- C. 123456
- D. 345

### 7

有如下程序：

```c
#include<stdio.h>
int main()
{
int x=1,y=0,a=1,b=1;
switch(x){
case 1: switch(y){
case 0:b++; break;
case 1:a++;}
case 2: b++;
case 3: a++;
}
printf("a=%d,b=%d",a,b); return 0;
}
```

该程序的输出结果是（C）。

- A. a=3,b=3
- B. a=1,b=3
- C. a=2,b=3
- D. a=1,b=2

### 8

以下程序执行后 sum 的值是（D）。

```c
#include<stdio.h>
int main( )
{
int i,sum;
for (i=1;i<6;i++) sum+=i;
printf("%d\n",sum);
return 0;
}
```

- A. 15
- B. 14
- C. 0
- D. 不确定

## 二、程序阅读题

### 1

以下程序运行所产生的输出是 2+4+8+16+32+64+128=256。

```c
#include<stdio.h>
int main( )
{
int a,s,n,count;
a=2;
s=0;
n=1;
count=1;
while(count<=7){
n=n*a;
s=s+n;
++count;
}
printf("s=%d",s);
return 0;
}
```

### 2

以下程序运行所产生的输出是 5，1，-1。

```c
#include<stdio.h>
int main()
{
int a=1,b=5,c=4;
while(c-->0&&++a<6)
b=b-1;
printf("%d,%d,%d\n",a,b,c);
return 0;
}
```

### 3

写出下面程序的功能和执行后的显示结果。

```c
#include <stdio.h>
int main(void)
{ int n=10, i, j, t, a[10]={7,3,66,-5,22,90,34,11,58,19};
for( i = 1; i < n; i++ )
for (j = 0; j < n-i; j++ )
if (a[j] < a[j+1])
{
t=a[j];
a[j]=a[j+1];
a[j+1]=t;
}
for(i=0; i<n; i++)
printf("%3d",a[i]);
return 0;
```

材料上：将数组中数据从大到小排序，输出 90 66 58 34 22 19 11 7 3 -5。

### 4

写出下面程序的功能和执行后的显示结果。

```c
#include<stdio.h>
int main()
{ int arr[5][5] = { 0 }; int a = 1; int b = 1;
for (a = 0; a < 5; a++) {
arr[a][0] = 1;
for (b = 0; b <=a; b++){
if(a==b) arr[a][b] = 1;
if(a>1 && b>=1)
arr[a][b] = arr[a - 1][b - 1] + arr[a - 1][b];
printf("%d ", arr[a][b]);
}
printf("\n");
}
return 0;
}
```

材料上：杨辉三角。

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```
