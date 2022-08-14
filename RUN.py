# -*- coding: utf-8 -*-

import os #导入库os
import qrcode 
import datetime
import tkinter as tk
import shutil
from Module_Private import *

#窗口
GUI = tk.Tk()
GUI.title('Odin二维码 ——仅供学习交流使用')
GUI.geometry("500x250")

#定义起始变量
text1 = tk.StringVar()
text2 = tk.StringVar()
Ontext = tk.StringVar()
text1.set("NONE")
text2.set("NONE")

#定义函数
mkdirAddress = GetDocumentPath() + "\QuickOdinQR"
mkdir(mkdirAddress)

def label1Command():
    shutil.copy(address,mkdirAddress + "\OdinLinkCfg_copy.xml")
    
    Ontext.set("正在加载二维码")
    
    now_time = datetime.datetime.now().strftime('%Y'+'%m'+'%d'+'%H'+'%M'+'%S')#获取时间
    
    GetDocumentContent = open(new_address,"r",encoding='UTF-8') #打开OdinLinkCfg.xml文件
    NumCom = 0
    Content = GetDocumentContent.readlines()
    for NumCom in range(len(Content)):
        sli = Content[NumCom]#注意在字符前面有两个空格
        if sli[2:15] == "<HotSpotName>":
            HotSpotName = sli[15:-15]
        if sli[2:15] == "<HotSpotCode>":
            HotSpotCode = sli[15:-15]
        NumCom += 1
    GetDocumentContent.close#关闭OdinLinkCfg.xml文件（必须关闭，否则占用内存）
    
    QuickResponseCodeContent = "WIFI:T:WPA;S:" + HotSpotName + ";P:" + HotSpotCode + ";;"
    img = qrcode.make(QuickResponseCodeContent)
    img.save(mkdirAddress + '\QR' + now_time + '.png')
    text1.set("热点名称：" + HotSpotName)
    text2.set("热点密码：" + HotSpotCode)
    Ontext.set("二维码已显示")
    os.system(mkdirAddress + '\QR' + now_time + '.png')

def cleartemp():
    for root,dirs,files in os.walk(mkdirAddress):
        for file in files:
            os.remove(root + "/" + file)
    Ontext.set("缓存清理完毕")

#！！！！！检查更新（如果可以，新建一个外置的文件，负责每次检查更新）

#检查文件，没有文件，则建立文件,好像还要复制一边在打开，否则会影响正常使用
address = GetDocumentPath() + "\OdinFiles\OdinLink\OdinLinkCfg.xml"#获取地址
path = GetDocumentPath() + "\OdinFiles\OdinLink"
path = path.strip()
path = path.rstrip("\\")
isExists = os.path.exists(path)
if not isExists:
    File.Add()#在Module_Private.py定义

shutil.copy(address,mkdirAddress + "\OdinLinkCfg_copy.xml")
new_address = mkdirAddress + "\OdinLinkCfg_copy.xml" 

Ontext.set("正在加载二维码")
now_time = datetime.datetime.now().strftime('%Y'+'%m'+'%d'+'%H'+'%M'+'%S')#获取时间
GetDocumentContent = open(new_address,"r",encoding='UTF-8') #打开OdinLinkCfg.xml文件
NumCom = 0
Content = GetDocumentContent.readlines()
for NumCom in range(len(Content)):
    sli = Content[NumCom]#注意在字符前面有两个空格
    if sli[2:15] == "<HotSpotName>":
          HotSpotName = sli[15:-15]
    if sli[2:15] == "<HotSpotCode>":
          HotSpotCode = sli[15:-15]
    NumCom += 1
GetDocumentContent.close#关闭OdinLinkCfg.xml文件（必须关闭，否则占用内存）
    
QuickResponseCodeContent = "WIFI:T:WPA;S:" + HotSpotName + ";P:" + HotSpotCode + ";;"
img = qrcode.make(QuickResponseCodeContent)
img.save(mkdirAddress + '\QR' + now_time + '.png')
text1.set("热点名称：" + HotSpotName)
text2.set("热点密码：" + HotSpotCode)
Ontext.set("二维码已显示")

#！！！！！二维码直接显示（可能会换库）

#！！！！！美化页面显示

#！！！！！显示转跳地址

#窗口的组件
Ontext.set("GUI运行正常")
label1 = tk.Label(GUI,textvariable=Ontext,width=15,height=2)
label1.pack()
label3=tk.Label(GUI,textvariable=text1,width=50,height=2)
label3.pack()
label4=tk.Label(GUI,textvariable=text2,width=50,height=2)
label4.pack()
button1 = tk.Button(GUI,text="加载QR",command=label1Command)
button1.pack()
button3 = tk.Button(GUI,text="清理缓存",command=cleartemp)
button3.pack()
label5=tk.Label(GUI,text="本软件制作者为天穹，此软件目前在github开源 ver.1.1")
label5.pack()
label6=tk.Label(GUI,text="https://github.com/TheTianQiong/Quick_Odin")
label6.pack()

#窗口显示
GUI.mainloop()
