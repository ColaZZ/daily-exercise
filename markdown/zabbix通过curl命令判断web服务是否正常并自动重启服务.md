# 一.编辑zabbix-agent客户端的配置文件
## 1. vim /etc/zabbix/zabbix_agented.conf
`添加命令参数`
UserParameter=script_status,/usr/bin/curl -I -s -w "%{http_code}" -o /dev/null http://1.1.1.1:9735/check

`打开远程命令调用`
EnableRemoteCommands = 1

`重启服务生效`
service zabbix-agent restart

## 2. visudo /  /etc/sudoers 打开关于zabbix操作的命令
### 1. 添加zabbix权限
`zabbix ALL=(ALL) NOPASSWD: ALL`

### 2. 注释掉如下一行, 否则命令无法执行
`# Default requiretty`

# 二. 添加需要被触发的脚本

# 三. zabbix-server的web配置

## 1. 测试远程命令是否ok
` # zabbix_get -s 1.1.1.1 -p 10050 -k script_status`

## 2. zabbix-server的web配置
### 2.1 添加监控项item
配置-->主机-->找到对应主机, 监控项-->创建监控项
```
名称:script_check
# key需要和zabbix-agentd.conf中定义的Parameter参数一致
key:script_status
```

### 2.2 创建对该监控项的触发器
配置-->主机-->找到对应主机, 触发器-->创建触发器
```
名称:(自定义)
表达式(Expression): {iZ23xtdqvgmZ:script_status.last()}<>200

```

### 2.3 设置动作
配置-->动作-->创建动作
```
name:(自定义)
# coditions
New condition：Trigger severity = Warning

New condition：Trigger name like yunva_scripts_port_9735_not_200

# Operations
# 在Operations选项中，添加新的”Action operation”，点击”New”，

Operation type：选择”Remote Command”

Target list：添加target为”Current host”

#agent在本机

Type：选择”Custom script”

Execute on：选择”Zabbix agent”，命令为 "sudo /bin/bash /usr/local/zabbix-agent/scripts/restart_script.sh"
```



script_status_253_8082



wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz -o /usr/lib/jvm/openjdk-11.0.1_linux-x64_bin.tar.gz

sudo tar -zxvf openjdk-11.0.1_linux-x64_bin.tar.gz

sudo sh -c 'for bin in /usr/lib/jvm/jdk-11.0.1/bin/*; do update-alternatives --install /usr/bin/$(basename $bin) $(basename $bin) $bin 100; done'

sudo sh -c 'for bin in /usr/lib/jvm/jdk-11.0.2/bin/*; do update-alternatives --install /usr/bin/$(basename $bin) $(basename $bin) $bin 100; done'


sudo sh -c 'for bin in /usr/lib/jvm/jdk-11.0.2/bin/*; do update-alternatives --set $(basename $bin) $bin; done'