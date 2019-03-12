# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-22-Fri/2019  08:25:40
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np


#opencv中路径选择用\\,否则会出现路径选择错误
#img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\opencv-logo.png')
#img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\LENA.png')
img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\simple.jpg')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,60,255,cv2.THRESH_BINARY)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print (contours[0])  
print(len(contours))
'''
for i in range(0,len(contours)): 
  x, y, w, h = cv2.boundingRect(contours[i])  
  cv2.rectangle(img, (x,y), (x+w,y+h), (153,153,0), 5)
'''

#img = cv2.drawContours(img,contours,-1,(0,255,0),3)
img = cv2.drawContours(img,contours,-1,(255,120,0),5)

#cv2.imshow('img1',img1)
cv2.imshow('img_gray',img_gray)
cv2.imshow('thresh',thresh)
cv2.imshow('image',image)
cv2.imshow('img',img)

k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()

