# -*- coding: utf-8 -*-
 
import os
import time
import serial
import socket

#def serial_init():
#    portx=""
#    bps=""
#    timex=""
#    ser=serial.Serial(portx,bps,timeout=timex)
#
#def serial_uninit():
#    ser.close()
#
#def serial_send(data):
#    ser.write(data)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def socket_init():
  IP_ADDR = "172.16.16.148"
  PORT = 8081
  server_address = (IP_ADDR,PORT)
  client_socket.bind(("172.16.16.100",8082))
  client_socket.connect(server_address)

def socket_uninit():
  client_socket.close()
  
def socket_send(data):
  client_socket.send(data)

def take_picture(): 
# 点亮手机
    os.system("adb shell input keyevent 224")
    time.sleep(1)
 
# 启动相机
    os.system("adb shell am start -a android.media.action.STILL_IMAGE_CAMERA")
    time.sleep(3) #多留点时间自动对焦
 
# camera键 拍照
    os.system("adb shell input keyevent 27")
    time.sleep(1) #留点时间存储照片 以免死机
    myfilename = os.popen("adb shell ls -t /storage/emulated/0/DCIM/Camera/ | head -n 1 | tr -d '\n' ").read()
    print("--")
    print(myfilename) 
    print("--") #debug看看前后是否有换行符
 
# 将这个文件pull到本地电脑上
    adbcode = "adb pull /storage/emulated/0/DCIM/Camera/"+str(myfilename)+""
    os.system(adbcode)

# delete this pic to avoid mem out
    os.system("adb shell rm /storage/emulated/0/DCIM/Camera/*.jpg")
# back键 暂退相机
    os.system("adb shell input keyevent 4")
    time.sleep(1)
 
# Power键 黑屏
    os.system("adb shell input keyevent 26")

#serial_init()
#for i in range(0,99):
#  serial_send()
#  time.sleep(20)
#  take_picture()
#  serial_send()
#  time.sleep(10)

#serial_uninit()

socket_init()

for i in range(0,9999):
  socket_send("313101")
  time.sleep(25)
  take_picture()
  socket_send("313102")
  time.sleep(10)

socket_uninit()
