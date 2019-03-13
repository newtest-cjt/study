#coding=utf-8
import requests
import json
import xlwt
import time
import xlrd
import pyecharts
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
########接口获取彩票200期数据
global M
url='https://www.xgllvip2.com/lgw/draw/runChart/307/count/200'
str1='和值间隔折线图'
now = int(time.time())
timeStruct = time.localtime(now)
strTime = time.strftime("%Y.%m.%d %H-%M-%S", timeStruct)
cookie={
            'authorization':'53513dbd-794f-4f21-aebc-18e87faccf0e',
            'customerid':'2464748',
            'merchant':'sgl818',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }

result=[]
g_r=[]
def get_data():
    M = 0
    res = requests.get(url=url, headers=cookie)
    res = res.text
    jj = json.loads(res)
    for i in range(200):
        a = jj.get('diagramList')[i].get('numero')
        b = jj.get('diagramList')[i].get('item')
        r=map(int,str(a))
        g=list(r)
        if  list(b)[-2]==list(b)[-1]:
            L=g[-4] * 10 ** 3 + g[-3] * 10 **2 + g[-2] * 10**1 + g[-1]
            # print('M',M)
            res=M-L
            M = g[-4] * 10 ** 3 + g[-3] * 10 **2 + g[-2] * 10**1 + g[-1]
            # print('M1',M)
            # print('res %d g %s' % (res, M))
            g_r.append(str(M))
            result.append(res)
    return g_r,result
def create_chart():
    g_r,result=get_data()
    result[0]=0
    line = pyecharts.Line(str1, strTime)
    line.add(str1, g_r,result, is_label_show=True)
    #line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True)
    line.render('hezhi.png')
def sendmail():
    user = '793610576@qq.com'
    password = 'lrfiltnqejgpbbjd'
    title = str1
    #word = str1
    to = ['953400851@qq.com', '280479997@qq.com']
    #msg = MIMEText(word)  # 内容
    msg = MIMEMultipart('related')
    msg["Subject"] = title  # 标题
    msg["From"] = user
    msg["To"] = ','.join(to)
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')
    msg.attach(content)
    file = open(r'hezhi.png', 'rb')
    img_data = file.read()
    file.close()
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    msg.attach(img)
    for i in range(2):
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.ehlo()
        # s.starttls()
        s.login(user, password)
        s.sendmail(user, to[i], msg.as_string())
        s.quit()
        print('邮件发送成功')

if __name__ == '__main__':
    create_chart()
    sendmail()