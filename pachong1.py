#encoding=utf-8
import requests
import re
from lxml import etree
import xlrd
import xlwt
import win32ui
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.common.action_chains import ActionChains
num=[]
loop=1
Key=[]
driver = webdriver.PhantomJS()
def get_cookie_from_network(): 
    url_login = 'http://www.qichacha.com/user_login' 
    driver.get(url_login) 
    driver.set_window_size(1366, 768)
    time.sleep(1)
    cc1=driver.find_element_by_link_text('密码登录')
    cc1.click()
    xpath1=driver.find_element_by_xpath('//*[@id="nameNormal"]')
    xpath1.send_keys('手机号 ') 
    time.sleep(2)
    xpath2=driver.find_element_by_xpath('//*[@id="pwdNormal"]')
    xpath2.send_keys('密码')
    time.sleep(2)
    source=driver.find_element_by_xpath("//*[@id='nc_2__scale_text']/span") 
    action = ActionChains(driver)
    def huadong(pra):
            action.click_and_hold(pra).perform() #鼠标左键按下不放
            action.move_by_offset(400, 0).perform() #平行移动鼠标
            time.sleep(2) #等待停顿时间
            
    try:
        huadong(source)
    except :
        huadong(source)
    cc2=driver.find_element_by_xpath('//*[@id="user_login_normal"]/button')
    cc2.click()
    time.sleep(1)
    a = driver.get_cookies() 
    driver.save_screenshot('2.png')
    driver.quit()
    for i0 in range(len(a)):
        if a[i0]['name']=='PHPSESSID':
            num.append(i0)
    for i1 in range(len(a)):
        if a[i1]['name']=='UM_distinctid':
            num.append(i1)
    for i2 in range(len(a)):
        if a[i2]['name']=='zg_did':
            num.append(i2)
    for i3 in range(len(a)):
        if a[i3]['name']=='acw_tc':
            num.append(i3)
    for i4 in range(len(a)):
        if a[i4]['name']=='_uab_collina':
            num.append(i4)
    for i5 in range(len(a)):
        if a[i5]['name']=='Hm_lvt_3456bee468c83cc63fb5147f119f1075':
            num.append(i5)
    for i6 in range(len(a)):
        if a[i6]['name']=='_umdata':
            num.append(i6)
    for i7 in range(len(a)):
        if a[i7]['name']=='CNZZDATA1254842228':
            num.append(i7)
    for i8 in range(len(a)):
        if a[i8]['name']=='zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f':
            num.append(i8)
    for i9 in range(len(a)):
        if a[i9]['name']=='Hm_lpvt_3456bee468c83cc63fb5147f119f1075':
            num.append(i9)

    ress=a[num[0]]['name']+'='+a[num[0]]['value']+'; '+a[num[1]]['name']+'='+a[num[1]]['value']+'; '+a[num[2]]['name']+'='+a[num[2]]['value']+'; '+a[num[3]]['name']+'='+a[num[3]]['value']+'; '+a[num[4]]['name']+'='+a[num[4]]['value']+'; '+a[num[5]]['name']+'='+a[num[5]]['value']+';'+' hasShow=1; '+a[num[6]]['name']+'='+a[num[6]]['value']+'; '+a[num[7]]['name']+'='+a[num[7]]['value']+'; '+a[num[8]]['name']+'='+a[num[8]]['value']+'; '+a[num[9]]['name']+'='+a[num[9]]['value']
    driver.quit()
    return ress

def chfile():
    global filename
    dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框 
    dlg.DoModal()
    filename=dlg.GetPathName() # 获取选择的文件名称
    return filename

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
cookies=get_cookie_from_network()
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie':cookies,
    'Host': 'www.qichacha.com',
    'Referer': 'http://www.qichacha.com/user_login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'         
       }

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
    if len(l)==0:
        source1=driver.find_element_by_xpath("//*[@id='nc_1__scale_text']/span") 
        action1 = ActionChains(driver)
        def huadong():
            action1.click_and_hold(source1).perform() #鼠标左键按下不放
            action1.move_by_offset(400, 0).perform() #平行移动鼠标
            time.sleep(2) #等待停顿时间
            driver.save_screenshot('3.png')
            cc3=driver.find_element_by_xpath("//*[@id='verify']/strong")
            cc3.click()
            print('验证滑块成功')
            time.sleep(1)
        huadong(source1)
        if len(l)==0:
            print('change cookie')
            cookies=get_cookie_from_network()
            headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie':cookies,
                'Host': 'www.qichacha.com',
                'Referer': 'http://www.qichacha.com/user_login',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'         
                   }
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
    time.sleep(2)
    newfile.save('D:\\test.xlsx')
