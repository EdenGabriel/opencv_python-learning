# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-26-Tue/2019  14:40:31
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np

#霍夫直线变换
img =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\shudu.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray,30,60,apertureSize = 3)
#img_gray = cv2.cvtColor(edges,cv2.COLOR_BGR2GRAY)

#img_gray1 = cv2.cvtColor(edges,cv2.COLOR_BGR2GRAY)

lines = cv2.HoughLines(edges,1,np.pi/180,240)
lines1 = lines[:,0,:]  #提取成二维!!!!!!!!!!!!!!!!!!

for rho,theta in lines1[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#cv2.imwrite('houghlines3.jpg',img)
cv2.imshow('img',img)

'''
#霍夫直线变换改进版
img =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\shudu.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray,30,50,apertureSize = 3)

minLineLength = 120
maxLineGap = 15
lines = cv2.HoughLinesP(edges,1,np.pi/180,90,minLineLength,maxLineGap)
lines1 = lines[:,0,:]  #提取成二维
for x1,y1,x2,y2 in lines1[:]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
cv2.imshow('edges',edges)
cv2.imshow('img',img)
'''
