#!bin/bash 

scp -r /var/jenkins_home/workspace/game-admin/target/classes/com root@47.105.154.206:/www/wwwroot/hty/webapps/docker-admin/hty-admin/WEB-INF/classes/com \
&& scp -r /var/jenkins_home/workspace/game-admin/target/classes/ibatis root@47.105.154.206:/www/wwwroot/hty/webapps/docker-admin/hty-admin/WEB-INF/classes/ibatis \
&& ssh root@47.105.154.206 << eeooff
docker restart tomcat9-admin
exit
eeooff



scp -r /var/jenkins_home/workspace/admin-vue/dist/css root@47.105.154.206:/www/wwwroot/hty/root/css && 



rm -rf ~/.ssh/known_hosts


————————————————
版权声明：本文为CSDN博主「xtggbmdk」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xtggbmdk/java/article/details/82897521




scp -r /var/jenkins_home/workspace/admin-vue/dist/fonts root@47.105.154.206:/www/wwwroot/hty/root/fonts

scp -r /var/jenkins_home/workspace/admin-vue/dist/img root@47.105.154.206:/www/wwwroot/hty/root/img

scp -r /var/jenkins_home/workspace/admin-vue/dist/js root@47.105.154.206:/www/wwwroot/hty/root/js


scp /var/jenkins_home/workspace/admin-vue/dist/BannerLabel.json root@47.105.154.206:/www/wwwroot/hty/root/BannerLabel.json

scp /var/jenkins_home/workspace/admin-vue/dist/index.html root@47.105.154.206:/www/wwwroot/hty/root/index.html
