# -*- coding:utf-8 -*-
import socket


def sent(s):
    ip_port = ('127.0.0.1', 30005)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(s)
    server_reply = sk.recv(1024)
    sk.close()
    return server_reply
