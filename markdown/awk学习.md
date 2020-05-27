Awk使用及网站日志分析


# Awk简介

# Awk使用
## awk命令格式和选项
### 语法形式
```
awk [options] 'scrapt' var=value file(s)
awk [options] -f scriptfile var=value file(s)
```

### 常用命令选项
1. -F fs fs指定输入分隔符,fs可以是字符串或者正则表达式,如-F:
2. -v var=value 赋值一个用户定义变量,将外部变量传递给awk
3. -f scripfile 从脚本文件中读取awk命令
4. -m[fr] val 对val值设置内在限制,-mf 选项显示分配给val的最大块数; -mr选项限制记录的最大数目.这两个功能是BEll实验室版awk的扩展功能,在标准wak'中不适用.

### 模式
1. /正则表达式/: 使用通配符的扩展集
2. 关系表达式:使用运算符进行操作,可以是字符串或数字的比较测试
3. 模式匹配表达式: 用运算符~(匹配) 和~! (不匹配)
4. BEGIN语句块,pattern语句块,END语句块

## awk脚本基本结构

```
awk 'BEGIN{ print "start" } partten{ commands } END { print "end" }' file 
```

一个awk脚本通常由: BEGIN语句块,能够使用模式匹配的通用语句块,end语句块散步本组成,这三个部分是可选的.任意一个不笨都可以不出现在脚本中, 脚本通常是被单引号或双引号中,例如:
```
awk 'BEGIN{ i=0 } { i++ } END{ print i }' filename 

awk "BEGIN{ i=0 } { i++ } END{ print i }" filename
```

## awk的工作原理

```
awk 'BEGIN{ commands } pattern{ commands } END{ commands }'
```
第一步: 执行BEGIN{ commands }语句块中的语句
第二步: 从文件或者标准输入(stdin)读取一行,然后执行pattern{ commands }语句块,它逐行扫描文件,从第一行到最后一行重复这个过程,知道文件全部被读取完毕.
第三步: 当读至输入流末尾时,执行END{ commands } 语句块.

BEGIN语句块在awk开始从输入流中读取之前被执行,这是一个可选的语句块,比如变量初始话,打印输出表格的表头等语句通产可以写在BEGIN语句块中.

END语句块在awk从输入流中读取完所有的行之后即被执行, 比如打印所有行的分析结果这类信息汇总都是在END语句块中完成,他也是一个可选语句块.

pattern语句块中的通用命令是最重要的部分, 它也是可选的.如果没有提供pattern语句块,则默认执行{ print }, 即打印每一个读取到的行,awk读取的每一行都会执行该语句块.

### 示例
```
echo -e "A line 1\na line 2" | awk 'BEGIN{ print "Start" } { print } END{ print "END" }
```

打印结果
```
Start
A line 1
A line 2
End
```

当使用不带参数的print时, 它就打印当前行, 当print的参数是以都好进行分隔时, 打印时则以空格作为定界符.在awk的print语句块中双引号是被当成拼接符使用, 例如:
```
echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1,var2,var3; }'
```

打印结果:
```
v1 v2 v3 
```

双引号拼接使用
```
echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1"="var2"="var3; }'
```
打印结果
```
v1=v2=v3
```

## awk内置变量(只写G(gawk)和A(awk))
```
$n 当前记录的第n个字段,比如n为1表示第一个字段,n为2表示第二个字段
$0 这个变量包含执行过程中当前行的文本内容
[G] ARGIND 命令行中当前文件的位置(从0开始算)
[G] CONVFMT 数字转换格式（默认值为%.6g）。
[G] FIELDWIDTHS 字段宽度列表（用空格键分隔）。
[G] IGNORECASE 如果为真,则进行忽略大小写的匹配

[A] FILENAME 当前输入文件的名
[A] FS 字符分隔符(默认是任何空格)
[A] NF 表示字段数，在执行过程中对应于当前的字段数。
[A] NR 表示记录数，在执行过程中对应于当前的行号。
[A] OFMT 数字的输出格式（默认值是%.6g）。
[A] OFS 输出字段分隔符（默认值是一个空格）。
[A] ORS 输出记录分隔符（默认值是一个换行符）。
[A] RS 记录分隔符(默认值时一个换行符)
```

## 将外部变量值传递给awk
借助-v选项,可以将外部值(并非来自stdin)传递给awk:
```
VAR=10000 echo | awk -v VARIABLE=$VAR '{ print VARIBLE }' 
```

另一部传递外部变量方法:
```
var1="aaa"
var2="bbb"
echo | awk '{ print v1, v2 }' v1=$var1 v2=$var2
```

以上方法中, 变量之间用空格分隔作为awk的命令行参数跟随在BEGIN, {} 和 END语句块之后.


## awk高级输入输出
### 读取下一条记录
awk中next语句使用:在循环逐行匹配,如果遇到next, 就会跳过当前行,直接忽略下面语句.而进行下一行匹配.next语句一般用于多行合并:
```
cat text.txt
a
b
c
d
e
```

```
awk 'NR%2==1{next}{print NR,$0;}'
text.txt
2 b
4 d 
```

### 简单地读取一条记录
awk getline用法: 输出重定向需用到getline函数.getline从标准输入,管道或者当前正在处理的文件之外的其他输入文件获得输入. 它负责从输入获得下一行的内容, 并给NF, NR和FNR等内建变量赋值.如果得到一条记录, getline函数返回1, 如果到达文件的末尾就返回0, 如果出现错误, 例如打开文件失败, 就返回-1.

1. 当其左右无重定向符|或<时: getline作用于当前文件, 读取当前文件的第一行给其后跟的变量var或$0(无变量), 应该注意到, 由于awk在处理getline之前已经读入了一行, 所以getline得到的返回结果时隔行的.
2. 当其左右有重定向符|或<时候: getline则作用于定向输入文件,由于该文件是刚打开,并没有被awk读入一行,知识getline读入,那么getline返回的是该文件的第一行,而不是隔行.



示例:
```
awk 'BEGIN{ "date" | getline out; print out }'
```

执行shell的date命令,并通过管道输出给getline,然后getline从管道中读取并将输入赋值给out, split函数把变量out转化成数组mon,然后打印数组mon的第二个元素:
```
awk 'BEGIN{ "date" | getline out; split(out,mon); print mon[2]}'
```

命令ls的输出传给getline作为输入, 循环使getline从ls的输出中读取一行, 并把它打印到屏幕.这里没有输入文件, 因为BEGIN块在打开输出文件前执行,所以可以忽略输入文件.
```
awk 'BEGIN{ while( "ls" | getline) print }' 
```

### 关闭文件
awk中允许在程序中关闭一个输入或输出文件, 方法是使用awk的close语句
```
close("filename")
```

filename可以是getline打开的文件,也可以是stdin,包含文件名的变量或者getline使用的确切命令.或一个输出文件,可以是stout,包含文件名的变量或使用管道的确切命令.

### 输出到一个文件

awk中允许用如下凡是将结果输出到一个文件:
```
echo | awk '{printf("hello world!\n") > "datafile"}'
```

### 设置字段定界符
默认的字段定界符是空格, 可以使用-F"定界符"明确指定一个定界符:
```
awk -F: '{ print $NF }' /etc/passwd
```
或
```
awk 'BEGIN{ FS=":" } { print $NF }' /etc/passwd
```
在BEGIN语句块中则可以用OFS="定界符"设置输出字段的定界符.


## 流程控制语句
在linux awk的while, do-while和for语句中允许使用break, continue语句来控制流程走向, 也允许使用exit这样的语句来退出.break中断当前正在执行的循环并跳到循环外执行下一条语句. if是流程选择用法. awk中, 流程控制语句, 语法结构, 与c语言类型. 有了这些语句, 其实很多shell程序都可以交给awk, 而且性能是非常块的.下面是各个语句用法:

### 条件判断语句
```
if(表达式)
    语句1
else
    语句2
```

格式中语句1可以是多个语句, 为了方便判断和阅读, 最好将多个语句用{}括起来.

awk分支结构允许嵌套, 其格式为:
```
if(表达式)
    {语句1}
else if(表达式)
    {语句2}
else
    {语句3}
```

示例:
```
awk 'BEGIN{
    test=100;
    if(test>90){
        print "very good";

    }
    else if(test>60){
        print "good";
    }else{
        print "no pass";
    }
}'
```
每条命令语句后面可以用;分号结尾.

### 循环语句

while语句:
```
while(表达式)
    {语句}
```

示例:
```
awk 'BEGIN{
    test=100;
    total=0;
    while(i<=test){
        total+=i;
        i++;
    }
    print total;
}'
```

### for循环
for循环有两种格式
格式一:
```
for(变量 in 数组)
    {语句}
```
格式二:
```
for(变量;条件;表达式)
    {语句}
```

### do循环
```
do
{语句} while (条件)
```

示例:
```
awk 'BEGIN{
    total=0;
    i=0;
    do {total+=i;i++;} while (i<=100)
        print total;
}'
```

### 其他语句
1. break 当break语句用于while或for语句时, 导致退出程序循环
2. continue 当continue语句用于while或for语句时, 是程序循环移动到下一个迭代
3. exit语句使主输入循环退出并将控制转移到END,如果END存在的话. 如果没有定义END规则,或在END中应用exit语句, 则终止脚本的执行.

## 数组应用
数组是awk的灵魂, 处理文本中最不能少的就是它的数组处理. 因为数组索引(下标)可以数字和字符串在awk中数组(associative arrays). awk
中的数组不必提前声明, 也不必声明大小. 数组元素用0或空字符串来初始化, 这根据上下文而定. 

### 数组的定义
数字做数组索引(下标):
```
Array[1]="sun"
Array[2]="kai"
```

字符串做数组索引(下标):
```
Array["first"]="www"
Array["last"]="name"
Array["birth"]="1987"
```

### 读取数组的值
```
{ for(item in array) {print array[item]}; } # 输出的顺序是随机的
{ for(i=1;i<len;i++) {print array[i]}; } # len是数组的长度
```

### 数组相关函数
得到数组长度:
```

```







