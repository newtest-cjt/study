#encoding=utf-8
import requests
import re
import win32api
import win32con
import time
import win32gui
def get_num_list():
    url = 'https://www.biquge.info/0_328'
    req = requests.get(url)
    res = req.text.encode(req.encoding).decode(req.apparent_encoding)
    z = re.findall('href="[0-9]\\d{5,8}.html.*title=', res)
    num = []
    for y in z:
        x = re.findall('[0-9]\\d{5,8}', y)
        num.append(x[0])
    return num
def main(number):
    url='https://www.biquge.info/0_328/'+str(number)+'.html'
    req=requests.get(url)
    res=req.text.encode(req.encoding).decode(req.apparent_encoding)
    re_r = re.compile(u'[^\u4e00-\u9fa5.，,。？“”]+', re.UNICODE)
    resss=re_r.sub(' ', res)
    re_rr=re.compile(u'[。]', re.UNICODE)
    ressss=re_rr.sub('\n',resss)
    re_rrr=re.compile(u'.*官色', re.UNICODE)
    res_res = re_rrr.sub(' ', ressss)
    re_rrrr = re.compile(u'.*温馨提示.*', re.UNICODE)
    res_res1 = re_rrrr.sub(' ', res_res)
    re_rrrr1 = re.compile(u'.*文字章节', re.UNICODE)
    res_res2 = re_rrrr1.sub(' ', res_res1)
    print(res_res2)
def window_operation_click(x,y):
    point=(x,y)
    win32api.SetCursorPos(point)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 点击鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 抬起鼠标
num=get_num_list()
M=num.index(str(7614079))
while True:
    u = input('1 = 下一章;other=关闭')
    if u=='1':
        M=M+1
        O=num[M]
        window_operation_click(48,620)
        main(O)
        print('当前页码数是:', O)
    else:
        break
