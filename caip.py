# coding:utf-8
#导入读取Excel的库
import xlrd
import pyecharts
from pyecharts import Bar
import numpy as np
#导入需要读取Excel表格的路径

#######彩票和值取件分析py
import xlrd
import pyecharts


data = xlrd.open_workbook(r'cp_data.xls')
table = data.sheets()[0]
#将列的值存入字符串
x=table.col_values(0)#读取列的值
y=table.col_values(1)
# i_i=[]
# for i in y:
#     list(i)
#     i_i.append(i)
hour=[[i]*2 for i in range(24)]
for i in range(len(hour)):
    hour[i][1]=0
for j in range(len(x)):
    q=int(x[j])
    r=map(int,str(q))
    g=list(r)
    res=(g[-4] * 10 ** 3 + g[-3] * 10 **2 + g[-2] * 10**1 + g[-1])//61
    if  list(y[j])[-2]==list(y[j])[-1]:
        #print(g,res,y[j],list(y[j])[-2],list(y[j])[-1])
        hour[res][1]=hour[res][1]+1
#print(hour)
x=[]
y=[]
for z in range(len(hour)):
    a=hour[z][0]
    b=hour[z][1]
    x.append(a)
    y.append(b)



line = pyecharts.Line("和值折线图", '2019-3-05')
line.add("和值折线图", x, y )
#line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True)
line.render('和值折线图.png')
