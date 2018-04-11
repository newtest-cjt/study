#coding=utf-8
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
global devices
#----------------------定义变量--------------------------------#
devices=[]  
packagelist=['com.kikaoem.qisiemoji.inputmethod.debug',
             'com.kikaoem.xiaomi.qisiemoji.inputmethod',      #如需添加或更改包名排序，请在此处修改
             'com.zzz']                           
def get_deviceid():                            #get设备id 
    readDeviceId = list(os.popen('adb devices').readlines())  
    for i in range(1,len(readDeviceId)-1):
        deviceId = re.findall(r'\w*', readDeviceId[i])[0]  
        devices.append(deviceId)
    return devices
root = tk.Tk()                                 #创建窗口
root.geometry("600x350+370+130")               #距离屏幕边缘值
root.wm_title('VIP')                           #root窗口标题
root.resizable(width=False, height=False)      #拒绝改变窗口大小，如需改变，请改为True
text_device=Text(root,width=30,height=1)
text_device.grid(row=0,column=1)

#-----------------------函数区--------------------------------#
def show_msg(*args):  
    return packagename.get()
def uninstall():
    p1='adb -s '+devices[0]+'  uninstall '+show_msg()
    os.system(p1)
def clear_data():
    p2='adb -s '+devices[0]+'  shell pm clear '+show_msg()
    os.system(p2)
def force_stop():
    p3='adb -s '+devices[0]+'  shell force-stop '+show_msg()
    os.system(p3)
def enable_inputmethod():
    p4='adb -s '+devices[0]+' shell ime enable '+show_msg()+'/com.android.inputmethod.latin.LatinIME'
    p5='adb -s '+devices[0]+' shell ime set '+show_msg()+'/com.android.inputmethod.latin.LatinIME'
    os.system(p4)
    os.system(p5)
def start_input():
    try:
        p6='adb -s '+devices[0]+' shell am start  yuside.cn.numbersonly/yuside.cn.numbersonly.MainActivity'
        os.system(p6)
    except:
        messagebox.showinfo(title='提示',message='该设备没有安装德哥版input输入框')#这还有点问题，提示弹不了
def devicee():
    text_device.delete(1.0,END)
    if len(get_deviceid())==0:
        messagebox.showinfo(title='提示',message='当前没有设备连接')
    else:
        text_device.insert(INSERT, devices)
        
#--------------------------按钮区-------------------------------#
btn_device=Button(root,text="检测设备",highlightbackground='#007947',command=devicee)#加颜色提醒你先检测设备
btn_device.grid(row=0,column=0,sticky=W)                                    
test=tk.StringVar()                                          #创建下拉框
packagename=ttk.Combobox(root,width=40,textvariable=test,state='readonly')#state=readonly输入框不可写入，如需写入请删掉state
packagename['values']=(packagelist)
packagename.grid(row=1,column=0)
packagename.current(0)                                     #下拉框默认显示值
packagename.bind("<<ComboboxSelected>>", show_msg)
btn_enable_inputmethod=Button(root,text='设为默认',command=enable_inputmethod)
btn_enable_inputmethod.grid(row=2,column=0,sticky=W)
btn_start_input=Button(root,text='启动input',command=start_input)
btn_start_input.grid(row=3,column=0,sticky=W)
btn_uninstall=Button(root,text='卸载',command=uninstall)
btn_uninstall.grid(row=4,column=0,sticky=W)
btn_clear_data=Button(root,text='清缓存',command=clear_data)
btn_clear_data.grid(row=5,column=0,sticky=W)
btn_force_stop=Button(root,text='强行停止',command=force_stop)
btn_force_stop.grid(row=6,column=0,sticky=W)                  #如需添加按钮，请在下面按着上面格式添加按钮并绑定函数











root.mainloop()
