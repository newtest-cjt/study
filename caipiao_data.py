#coding=utf-8
import requests
import re
import json
import time
import xlwt,xlrd
import time
########接口获取彩票200期数据
#url='https://www.xgllvip2.com/lgw/draw/307'
url='https://www.xgllvip2.com/lgw/draw/runChart/307/count/200'
now = int(time.time())
timeStruct = time.localtime(now)
strTime = time.strftime("%Y.%m.%d %H-%M-%S", timeStruct)

f=xlwt.Workbook(encoding='utf-8')
sheet=f.add_sheet(strTime,cell_overwrite_ok=True)
# for i in range(15):
#     print(i)
#     # parama={
#     #
#     #     'page':i,
#     #     'size':100
#     #     }
#     cookie={
#             'authorization':'043581fe-eccd-44c5-a285-d67eee8dc3f4',
#             'customerid':'2464748',
#             'merchant':'sgl818',
#             'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
#         }
#     #"[0-9]\\d{5,8}.html.*title=', res)
#     def main():
#         res = requests.get(url=url, params=parama, headers=cookie)
#         print(res)
#         res = res.text
#         jj = json.loads(res)
#         print(jj)
#         l = len(jj.get('content'))
#         for i in range(l):
#             a = jj.get('content')[i].get('numero')
#             b = jj.get('content')[i].get('winNo')
#             f.write(a + '\t' + b + '\n')
#     if i%100==0:
#         print('sleep')
#         #time.sleep(20)
#     else:
#
#         main()
#
# f.close()

cookie={
            'authorization':'53513dbd-794f-4f21-aebc-18e87faccf0e',
            'customerid':'2464748',
            'merchant':'sgl818',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
    #"[0-9]\\d{5,8}.html.*title=', res)
def main():
    res = requests.get(url=url, headers=cookie)
    res = res.text
    jj = json.loads(res)
    for i in range(200):
        a = jj.get('diagramList')[i].get('numero')
        b = jj.get('diagramList')[i].get('item')
        sheet.write(i,0,a)
        sheet.write(i, 1, b)

main()
f.save('cp_data.xls')