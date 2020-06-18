# 1. 接入方式
```
POST  http://ip:port/api_jsonrpc.php
# header中设置
content-type:application/json-rpc
content-type:application/json
content-type:application/jsonrequest
```
# 2. 接入步骤
## 1. 传入登录接口参数,参数为JSON字符串
## 2. 获取返回的token
## 3. 以后每个请求,需要再参数里加上auth:token


