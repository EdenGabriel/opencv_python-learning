# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  12:26:25 
VERSION: V-1.0
DESCRIPTION:
形态学变换
'''

import numpy as np
import cv2


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\pic2.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gau = cv2.GaussianBlur(img_gray,(5,5),0)
ret,thre = cv2.threshold(img_gau,150,255,cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel = np.ones((5,5),np.uint8)

res = cv2.erode(thre,kernel,iterations = 1)
opening = cv2.morphologyEx(thre,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(thre,cv2.MORPH_CLOSE,kernel)
opening_inv = cv2.bitwise_not(opening)
gradient = cv2.morphologyEx(closing,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(closing,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(closing,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('tophat',tophat)
cv2.imshow('blackhat',blackhat)
cv2.imshow('gradient',gradient)
cv2.imshow('closing',closing)
cv2.imshow('opening_inv',opening_inv)
cv2.imshow('opening',opening)
#res1 = cv2.dilate(thre,kernel,iterations = 1)
cv2.imshow('res',res)
#cv2.imshow('res1',res1)
cv2.imshow('thre',thre)

k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
