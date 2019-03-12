# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  10:27:30
VERSION: V-1.0
DESCRIPTION:

'''

#cap.read()返回两个参数赋给两个值。
#第一个参数ret的值为True或False，代表有没有读到图片。
#第二个参数是frame，是当前截取一帧的图片

import numpy as np
import cv2

cap = cv2.VideoCapture('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\Megamind.avi')

while(True):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame',gray)
    if cv2.waitKey(25) &0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
