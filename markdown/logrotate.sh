/wwww/wwwroot/hty/logs/xmbd.qcinterface.com.log  /wwww/wwwroot/hty/logs/xmbd.qcinterface.com.error.log {
    create 600 www www
    daily
    dateext
    rotate 10
    missingok
    notifempty
    compress
    sharedscripts
    olddir /wwww/wwwroot/hty/logs/oldlogs  # 这个目录要事先创建好，并给相关权限
    postrotate
        kill -USR1 `cat /run/nginx.pid`
    endscript



    notifempty
    daily
    sharedscripts
    postrotate
    /bin/kill -USR1 `/bin/cat cat /run/nginx.pid`
    endscript

}