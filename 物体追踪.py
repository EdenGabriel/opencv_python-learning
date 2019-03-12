# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  20:24:14 
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np

'''
import cv2
flags=[i for in dir(cv2) if i startswith('COLOR_')]
print(flags)
可以显示cvtColor中的任意可以转换的类型
'''
#https://www.cnblogs.com/wangyblzu/p/5710715.html
#上述网址可查看各颜色的HSV的阈值范围
cap = cv2.VideoCapture(0)


while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
#蓝色空间阈值
        lower_blue = np.array([100,43,46])
        upper_blue = np.array([124,255,255])
#构建蓝色掩膜
        mask = cv2.inRange(frame_hsv,lower_blue,upper_blue)

        res = cv2.bitwise_and(frame,frame,mask = mask)

#        cv2.imshow('frame',frame)
#        cv2.imshow('frame_hsv',frame_hsv)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(1)&0xFF
        if k == 27:
            break
cv2.destroyAllWindows()
cap.release()

        

       
