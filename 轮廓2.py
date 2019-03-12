# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-22-Fri/2019  09:38:40
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\simple.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray,(5,5),0)
ret,thresh = cv2.threshold(blur,62,255,cv2.THRESH_BINARY)

image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for cnt in range(len(contours)):
    

    M = cv2.moments(contours[cnt])
    area = cv2.contourArea(contours[cnt])  #计算轮廓面积
    perimeter = cv2.arcLength(contours[cnt],True)
    print('面积:',area,'轮廓面积:',perimeter)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    cv2.drawContours(img,contours,-1,(0, 255, 0),4)
    cv2.circle(img, (cX, cY), 3, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('img',img)
    cv2.waitKey(500)



cv2.imshow('thresh',thresh)
cv2.imshow('img',img)


k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
