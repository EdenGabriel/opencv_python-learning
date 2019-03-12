# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  17:43:01 
VERSION: V-1.0
DESCRIPTION:

'''

import numpy as np
import cv2
global thre_value
thre_value = 50

def nothing(x):
    pass

#img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\opencv-logo.png')
img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\simple.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.namedWindow('Picture_Threshold')
cv2.createTrackbar('value','Picture_Threshold',0,255,nothing)

while(1):
    
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break
    thre_value = cv2.getTrackbarPos('value','Picture_Threshold')
    ret,img_thre = cv2.threshold(img_gray,thre_value,255,cv2.THRESH_BINARY)
    cv2.imshow('Picture_Threshold',img_thre)
    thre_value = cv2.getTrackbarPos('value','Picture_Threshold')

cv2.destroyAllWindows()
