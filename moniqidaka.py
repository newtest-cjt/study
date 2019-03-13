#encoding=utf-8
import  os
import time
import subprocess
import win32com.client as win32
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

pkn='com.isoftstone.client.ipsa'
act='com.isoftstone.ipsa.app.activity.SplashActivity'
daka=(178,956)                                                          #考勤打卡坐标
qiandao=(928,1725)                                                      #签到坐标
qiantui=(928,1825)                                                      #签退坐标
p1='adb shell am start '+pkn+'/'+act                                    #启动ipsa  app
p3='adb shell input tap '+str(daka[0])+' '+str(daka[1])                 #点击考勤打卡按钮
p4='adb shell input tap '+str(qiandao[0])+' '+str(qiandao[1])           #点签到按钮
email_list=['v_liukaili@baidu.com','v_niyaxing@baidu.com','v_chengjintao@baidu.com','v_liushanshan01@baidu.com']
port=62025

def sendmail(user_name):
    sub = '上班打卡结果通知'
    body = '本邮件为定时自动发送，请勿回复。打卡截图见附件！！！'
    outlook = win32.Dispatch('outlook.application')
    receivers = [user_name]
    mail = outlook.CreateItem(0)
    mail.To = receivers[0]
    mail.Subject = sub
    mail.Body = body
    mail.Attachments.Add(r'D:\daka\screen.png')
    mail.Send()
def screen_adb():
    os.popen('adb shell screencap -p /sdcard/screen.png')
    time.sleep(2)
    os.popen('adb pull ./sdcard/screen.png d:\daka')
def shuiyin():
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 60)
    imageFile = r"d:\daka\screen.png"
    im1 = Image.open(imageFile)
    res_t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    draw = ImageDraw.Draw(im1)
    draw.text((200, 500), res_t, '#FF0000', font=font)
    im1.save(r"d:\daka\screen.png")
def main():
    for i in range(4):
        #print(email_list[i])
        subprocess.Popen('d:\\daka\\start_'+str(i+1)+'.bat', shell=True)
        time.sleep(60)
        print('1.先重启adb服务，因为模拟器也起了个adb服务会冲突')
        os.popen('adb kill-server')
        time.sleep(5)
        os.popen('adb start-server')
        time.sleep(5)

        print('2.本机adb链接到模拟器端口')
        os.popen('adb connect 127.0.0.1:'+str(port+i))
        time.sleep(10)

        print('3.启动IPSA中...')
        os.popen(p1)
        time.sleep(20)

        print('4.初始化首页')
        os.popen('adb shell input tap 175 1854')
        time.sleep(5)

        print('5.点击考勤打卡区域')
        os.popen(p3)
        time.sleep(20)

        print('6.点击签到按钮，完成上班打卡')
        os.popen(p4)
        time.sleep(2)
        screen_adb()
        time.sleep(5)
        shuiyin()
        time.sleep(5)
        sendmail(email_list[i])
        print('7.关闭模拟器')
        os.system('d:\\daka\\killNox.bat')
        time.sleep(60)
if __name__ == '__main__':
    main()
