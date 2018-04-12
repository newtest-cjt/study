#encoding=utf-8
import requests
import re
from lxml import etree
import xlrd
import xlwt
import win32ui
import time
loop=1
Key=[]
def chfile():
    global filename
    dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框 
    dlg.DoModal()
    filename=dlg.GetPathName() # 获取选择的文件名称
    return filename
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=tqjeo50nql148lrutujhfhaho6; UM_distinctid=162b7e5aabe228-04390d9510467d-4446062d-100200-162b7e5aabf187; zg_did=%7B%22did%22%3A%20%22162b7e5aadae6-0098947d54de89-4446062d-100200-162b7e5aadb170%22%7D; hasShow=1; acw_tc=AQAAAFQ2wn+vVAUATKmHPXGYj9y6lQbU; _uab_collina=152350371706055027040967; _umdata=486B7B12C6AA95F255DDA31F1200699BA60BC480571BFDF59869EFC1C97508EDB3D8A2BA4D66C954CD43AD3E795C914C4A16773D94CAE3E427FB3595A64627B0; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1523503705,1523505712; CNZZDATA1254842228=83472213-1523502333-https%253A%252F%252Fwww.baidu.com%252F%7C1523523933; acw_sc__=5acf276dd874725127c6b693c48ad9e6b40c32a4; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201523522831823%2C%22updated%22%3A%201523525497329%2C%22info%22%3A%201523503704801%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%222f265445e47660bc71fb5a438c4dd443%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1523525497',    
    'Host': 'www.qichacha.com',
    'Referer': 'http://www.qichacha.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'         
       }
filename=chfile()#选文件
data=xlrd.open_workbook(filename)
sheet_name=data.sheet_names() #获取所有sheet的名字
sheet=data.sheet_by_name(sheet_name[0]) #通过sheet名字来找sheet

def getphonenumber():
    for k in range(sheet.ncols):
            if sheet.row_values(0)[k]=='联系电话':
                return k
def getgongsiname():
    for k in range(sheet.ncols):
            if sheet.row_values(0)[k]=='企业名称':
                return k
def getname():
    for k in range(sheet.ncols):
            if sheet.row_values(0)[k]=='法定代表人':
                return k
a=getgongsiname()
b=getname()
c=getphonenumber()
############################################################################################################

newfile=xlwt.Workbook()
sheet1 = newfile.add_sheet('企查猫(企业查询宝)',cell_overwrite_ok=True)
sheet1.write(0,0,sheet.col_values(a)[0])
sheet1.write(0,1,sheet.col_values(b)[0])
sheet1.write(0,2,sheet.col_values(c)[0])
gongsinamelist=sheet.col_values(a)
namelist=sheet.col_values(b)
numlist=sheet.col_values(c)#电话列表用于拼接url
for i in numlist:
    if len(i)==11:
        Key.append(i)
for key in Key:
    url='http://www.qichacha.com/search?key='+key
    res=requests.get(url=url,headers=headers).content.decode('utf-8')
    z=etree.HTML(res)
    l=z.xpath('//*[@id="countOld"]/span')
    for i in l:
        value=int(i.text)
        if value>0 and value <3:
            sheet1.write(loop,0,gongsinamelist[loop])
            sheet1.write(loop,1,namelist[loop])
            sheet1.write(loop,2,numlist[loop])
            print(str(numlist[loop])+':'+str(value)+'写入')
        else:
            print(str(numlist[loop])+':'+str(value)+'扔掉')
        loop=loop+1 
    newfile.save('D:\\test.xlsx')
