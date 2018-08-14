# coding=utf-8
from socket import *
import threading
from time import ctime
import time
import json
import requests

ip = '0.0.0.0'  # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port = 95  # 监听自己的哪个端口
buffsize = 40000  # 接收从客户端发来的数据的缓存区大小
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ip, port))
tcpSerSock.listen(5)
socket = []
proxies = {
    "http": "localhost:8888",
    "https": "localhost:8888",
}


def handle():
    while True:
        for i in socket:
            try:
                data = i.recv(buffsize)  # 到这里程序继续向下执行
            except Exception as e:
                continue
            if not data:
                socket.remove(i)
                continue

            data = data.decode('utf-8')

            data = json.loads(data)

            if data['type'] == "MC-QQ":
                url = data['url']
                headers = {
                    'Cookie': data['cookie']
                }
                body = 'sid=2&ouin=' + data['DESTQQ'] + '&uin=' + data[
                    'OWNQQ'] + '&fuin=3540339695&sourceId=1&fupdate=1&qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F953400851&rd=0.9045006905949171&strmsg=&groupId=9&realname=%E8%B6%8A%E8%BF%87%E8%B0%8E%E8%A8%80%E5%8E%BB%E6%8B%A5%E6%8A%B1%E4%BD%A0%EF%BC%81&flag=0&key=&verify=&im=0&format=fs&from=9&from_source=11'

                res = requests.post(url=url, headers=headers, data=body)

                res = res.text

                i.sendall((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n' + str(res)).encode())

            else:
                print('error')
                i.sendall((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n' + 'error').encode())


t = threading.Thread(target=handle)
if __name__ == '__main__':
    t.start()
    print(u'我在%s线程中 ' % threading.current_thread().name)  # 本身是主线程
    print('waiting for connecting...')
    while True:
        clientSock, addr = tcpSerSock.accept()
        print('connected from:', addr)
        clientSock.setblocking(0)
        socket.append(clientSock)

