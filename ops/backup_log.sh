#!/bin/bash

time=$(date +"%Y%m%d%H")
# 备份今天日志(记录到小时)
cp /var/lib/docker/containers/d2c4ba1e1b66539bfd7b1ca988859935451efa48de50f2ae9c3101ba58750812.log  /var/lib/docker/containers/$time.log

# 清空日志文件
> /var/lib/docker/containers/d2c4ba1e1b66539bfd7b1ca988859935451efa48de50f2ae9c3101ba58750812.log

# 删除前一天的日志文件

for i in $(seq 4 7)
do
day="$(expr $i \* 24)hour"
last_day=$(date +"%Y%m%d%H" -d -$day)
if [ -e /var/lib/docker/containers/d2c4ba1e1b66539bfd7b1ca988859935451efa48de50f2ae9c3101ba58750812/$last_day.log ]
then 
    rm -f /var/lib/docker/containers/d2c4ba1e1b66539bfd7b1ca988859935451efa48de50f2ae9c3101ba58750812/$last_day.log
fi
done 



