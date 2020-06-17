#!/bin/bash

time=$(date +"%Y%m%d")
last_day=$(date +"%Y%m%d" -d "-24hour")
for dir in `ls /www/mini_game/webapps/`
do
    dir1="$dir-$time"  
    zip -r /www/mini_game/webapps/$dir1.zip /www/mini_game/webapps/$dir    
    mv /www/mini_game/webapps/$dir1.zip /www/mini_game/backups/
    if [ -e /www/mini_game/webapps/$last_day.zip ]
    then 
        rm -f /www/mini_game/webapps/$last_day.zip
    fi
done


