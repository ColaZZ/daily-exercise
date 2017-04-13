#!usr/bin/python
# coding=utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print u'等待连接...'
    tcpCliSock, addr = tcpSerSock.accept()
    print u'...连接来自:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(
            ctime(), data))

tcpSerSock.close()
