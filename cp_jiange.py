# coding:utf-8
#导入读取Excel的库
import xlrd
import pyecharts
from pyecharts import Bar
import numpy as np
#导入需要读取Excel表格的路径


#######彩票和值间隔折线图
import xlrd
import pyecharts
import time
now = int(time.time())
timeStruct = time.localtime(now)
strTime = time.strftime("%Y.%m.%d %H:%M:%S", timeStruct)


data = xlrd.open_workbook(r'cp_data.xls')
table = data.sheets()[0]
#将列的值存入字符串
x=table.col_values(0)#读取列的值
y=table.col_values(1)
# i_i=[]
# for i in y:
#     list(i)
#     i_i.append(i)
global M
M=0
result=[]
g_r=[]
for j in range(len(x)):

    q=int(x[j])
    r=map(int,str(q))
    g=list(r)
    if  list(y[j])[-2]==list(y[j])[-1]:
        L=g[-4] * 10 ** 3 + g[-3] * 10 **2 + g[-2] * 10**1 + g[-1]
        ##print('M',M)
        res=M-L

        M = g[-4] * 10 ** 3 + g[-3] * 10 **2 + g[-2] * 10**1 + g[-1]
        #print('M1',M)
        #print('res %d g %s' % (res, M))
        g_r.append(str(M))
        result.append(res)


result[0]=0
str='和值间隔折线图'

line = pyecharts.Line(str, strTime)
line.add(str, g_r,result, is_label_show=True,is_datazoom_show=True, is_fill=True, line_opacity=0.2,area_opacity=0.4)
#
#line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True)
line.render(str+'.html')
