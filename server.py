# coding=utf-8
from socket import *
import threading

ip = '0.0.0.0'  # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port = 95  # 监听自己的哪个端口
buffsize = 1024  # 接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((ip, port))
s.listen(100)  # 最大连接数
conn, addr = s.accept()
print("当前链接ip:", addr)
while True:
    data = conn.recv(1024).decode('utf-8')
    # recvdata=clientsock.recv(buffsize).decode('utf-8')
    if not data:
        conn.close()
        break
    print("接收到：", data)
    serverdata = 'sb'
    conn.sendall(serverdata.encode())

    s.close()