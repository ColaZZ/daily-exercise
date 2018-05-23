# coding=utf-8
from __future__ import absolute_import

from celery import Celery

# 添加delery_ex.tasks模块
app = Celery('celery_ex', include=['celery_ex.tasks'])
# 配置
app.config_from_object('celery_ex.celeryconfig')

if __name__ == '__main__':
    app.start()
