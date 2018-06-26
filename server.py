#coding=utf-8
from socket import *
import threading
from time import ctime
import time

ip='0.0.0.0'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=95             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind((ip,port))
tcpSerSock.listen(5)
socket=[]
def handle():
    while True:
        for i in socket:
            try :
                 data = i.recv(buffsize)     #到这里程序继续向下执行
            except Exception as e:
                continue
            if not data:
                socket.remove(i)
                continue
            i.sendall((time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+'\n'+str(data)).encode())
t=threading.Thread(target=handle)
if __name__ == '__main__':
    t.start()
    print ( u'我在%s线程中 ' % threading.current_thread().name)    #本身是主线程
    print ('waiting for connecting...'  )
    while True:
        clientSock,addr = tcpSerSock.accept()
        print ( 'connected from:', addr  )
        clientSock.setblocking(0)
        socket.append(clientSock)

