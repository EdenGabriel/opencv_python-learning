# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  17:06:15 
VERSION: V-1.0
DESCRIPTION:
Canny边缘检测
'''

import numpy as np
import cv2

def CannyThreshold(x):
    pass


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\logo6.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gau = cv2.GaussianBlur(img_gray,(3,3),0)

#_,thresh1 = cv2.threshold(img_gau,57,255,cv2.THRESH_BINARY )
thresh1 = cv2.adaptiveThreshold(img_gau,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
thresh1 = cv2.bitwise_not(thresh1)
kernel = np.ones((2,2),dtype = np.uint8)
thresh1 = cv2.erode(thresh1,kernel,iterations = 1)
kernel1 = np.ones((1,1),dtype = np.uint8)
thresh1 = cv2.dilate(thresh1,kernel1,iterations = 1)


cv2.namedWindow('Canny')
cv2.createTrackbar('thre_low','Canny',0,255,CannyThreshold)
cv2.createTrackbar('thre_high','Canny',0,255,CannyThreshold)

while(1):
    low_value = cv2.getTrackbarPos('thre_low','Canny')
    high_value = cv2.getTrackbarPos('thre_high','Canny')

    edges = cv2.Canny(img_gau,low_value,high_value)
    res = cv2.bitwise_and(img,img,mask = edges )

    cv2.imshow('original',img)
    cv2.imshow('thresh1',thresh1)
    cv2.imshow('Canny',edges)
    cv2.imshow('res',res)
    low_value = cv2.getTrackbarPos('thre_low','Canny')
    high_value = cv2.getTrackbarPos('thre_high','Canny')


    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
