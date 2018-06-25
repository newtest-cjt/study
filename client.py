#coding=utf-8
from socket import *
address='123.207.127.103'   #服务器的ip地址
port=95           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
data='95'
s.sendall(data.encode())
receive=s.recv(1024).decode('utf-8')
print(receive)
s.close()