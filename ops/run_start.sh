#!/bin/bash
 
while true
do 
    # test处为监控脚本文件名
    procnum=` ps -ef|grep "test"|grep -v grep|wc -l`
   if [ $procnum -eq 0 ]; then
       echo `test 不在运行,正在重启` 
       # 监控的脚本,绝对路径
       /home/test.sh&
   fi
   # 定时检测
   sleep 30
done