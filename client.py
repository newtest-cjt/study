#coding=utf-8
from socket import *
import threading
import time
address='123.207.127.103'   #服务器的ip地址
port=95           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
def send(sock,test):
    while True:
        try:
            data=input()
            s.sendall(data.encode())
            if data == 'quit':
                break
        except KeyboardInterrupt:
            s.send('quit')
            break
def recv(sock,test):
    while True:
        data=s.recv(buffsize).decode('utf-8')
        if data == 'quit':
            print('person is logout')
            continue
        print((time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+'\n'+str(data)))

#receive=s.recv(1024).decode('utf-8')
if __name__ == '__main__':
    print('Successful connection')
    recvMessage = threading.Thread(target=recv, args=(s, None))
    sendMessage = threading.Thread(target=send, args=(s, None))
    sendMessage.start()
    recvMessage.start()
    sendMessage.join()
    recvMessage.join()

