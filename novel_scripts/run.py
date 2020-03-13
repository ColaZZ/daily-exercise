#!/usr/bin/python3
# -*- coding: utf-8 -*-

import site

from tornado.options import parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
from peewee_async import Manager

import redis
from lib.routes import route

Root = os.path.abspath(os.path.dirname(__file__))
path = lambda *a: os.path.join(*a)
site.addsitedir(path('vendor'))


class Application(tornado.web.Application):
    def __init__(self):
        # redis_pool = redis.ConnectionPool(host=)
        handlers = route.get_routes()

        app_settings = dict(
            debug=DEBUG,
            autoescape=None,
            gzip=True,
        )
        tornado.web.Application.__init__(self, handlers, **app_settings)


for app_name in APPS:
    __import__("apps.%s" % app_name. fromlist=["handlers"])

def main():
    parse_command_line()
    logging.getLogger().setLevel(logging.DEBUG)
    application = Application()

    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    api_port = 9200\
    http_server.bind(api_port)
    http_server.start()

    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        logging.info("API Server stoped")
        sys.exit(0)

if __name__ == "__main__":
    main()
