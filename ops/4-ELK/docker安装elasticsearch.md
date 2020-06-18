# 一. 安装elasticsearch7.7.0
## 1. 拉取elasticsearch 7.7.0 
`docker pull elasticsearch:7.7.0`

## 2. 创建容器
`docker run -di --name=myelasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v /etc/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml elasticsearch:7.7.0`

## 3. 虚拟内存过小
直接修改/etc/sysctl 
加入
```
vm.max_map_count=655360
fs.file_max=65536
```

## 4.修改配置,重启docker即可
```
docker restart myelasticsearch
```
测试elasticsearch
访问http://ip:9200

## 5. 安装IK分词器
进入elasticsearch容器
`/usr/share/elasticsearch/bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.7.0/elasticsearch-analysis-ik-7.7.0.zip`

安装完毕之后重启elasticsearch即可
`docker restart myelasticsearch`
POST方式请求http://ip:9200/_analyze 可以测试分词器效果

# 二. 安装LogStash
## 1. 拉取logstash的image
`docker pull docker.elastic.co/logstash/logstash:7.7.0`
## 2. 创建容器
`docker run --rm -di docker.elastci.co/logstash/logstash:7.7.0`
## 3. 将容器中的配置文件复制到宿主主机
```
# 创建用于存放配置的目录
mkdir -p /etc/logstash
# 复制配置文件,冒号前面为容器id
docker cp a407cd9e1354:/usr/share/logstash/config /etc/logstash/config/
# 复制logstash管道文件
docker cp docker cp a407cd9e1354:/usr/share/logstash/pipeline /etc/logstash/pipeline
```
## 4. 重新创建容器,并挂载上面两个文件夹
```
# 停止原有容器,否则无法删除
docker stop d7405af81c00
# 删除原有容器
docker rm d7405af81c00
# 创建新容器并且挂载目录
docker run -di --name=mylogstash -v /etc/logstash/config/config:/usr/share/logstash/config -v /etc/logstash/pipeline:/usr/share/logstash/pipeline docker.elastic.co/logstash/logstash:7.7.0
```
## 5. 插件安装需要进入容器内部
```
# 进入容器
docker exec -it mylogstash bash
# 进入logstash的bin目录
cd /usr/share/logstash/bin
# 安装插件,举例:jdbc
./logstash-plugin install logstash-input-jdbc
```
## 6. 日志查看
```
docker logs -f --tails=30 mylogstash
```
# 三. 安装kibana
## 1. 拉取镜像
`docker pull kibana:7.7.0`
## 2. 启动容器
`docker run -di -p 5601:5601 kibana:7.7.0`
## 3. 将容器中的配置文件复制到宿主机
```
# 创建存放配置文件的目录
mkdir -p /etc/kinana
# 复制
docker cp c5e2afd27de2:/usr/share/kibana/config /etc/kibana/config
```
## 4. 重新创建容器,并挂载配置文件目录
```
# 停止原有容器
docker stop c5e2afd27de2
# 删除原有容器
docker rm c5e2afd27de2
# 创建新容器
docker run -di --name=mykibana --net somenetwork -p 5601:5601 -v /etc/kibana/config:/usr/share/kibana/config kibana:7.7.0 
```

## 5. 修改配置文件
`vim /etc/kibana/config.yml`
修改后的配置文件内容如下:
```
server.name: kibana
# 允许所有地址访问
server.host: "0.0.0.0"
# elasticsearch的地址
elasticsearch.hosts: ["http://172.19.0.2:9200/"]
xpack.monitoring.ui.container.elasticsearch.enabled: true
# 中文
i18n.locale: "zh-CN"
```

## 6. 重启kibana
`docker restart mykibana`

## 7. 访问测试
`http://192.168.1.249:5601`














