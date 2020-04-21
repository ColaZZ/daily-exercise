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

1. 当其左右无重定向符|或<时: getline作用于当前文件, 读取当前文件的第一行给其后跟的变量var或$0(无变量), 应该注意到, 由于awk在处理getline之前已经读入了一行, 所以ge't




