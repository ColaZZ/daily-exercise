# coding=utf-8

# 使用rabbitMQ作为消息代理
BROKER_URL = 'amqp://reilinumatoiMac:123456@localhost:5672/web_develop'
# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6739/0'
# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'
# 读取任务结果一般性能要去不高,所以使用了可读性更好的json
CELERY_RESULT_SERIALIZER = 'json'
# 任务过期时间
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']