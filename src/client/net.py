# -*- coding:utf-8 -*-
import socket


def sent(s):
    ip_port = ('127.0.0.1', 30011)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(s)
    server_reply = sk.recv(4096)
    sk.close()
    return server_reply
