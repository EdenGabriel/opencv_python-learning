# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-27-Wed/2019  08:30:39
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np

img =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\opencv-logo.png',0)
img = cv2.GaussianBlur(img,(5,5),0)
#img = cv2.bilateralFilter(img,5,35,75)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
edges = cv2.Canny(img,50,100,apertureSize = 3)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1 = 50,param2 = 50,minRadius = 0,maxRadius = 0)
#四舍五入，取整
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),4)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),5)


cv2.imshow('circles1',edges)
cv2.imshow('circles',cimg)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
    
'''
import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow("image")
cv.createTrackbar("d","image",0,255,nothing)
cv.createTrackbar("sigmaColor","image",0,255,nothing)
cv.createTrackbar("sigmaSpace","image",0,255,nothing)
img =  cv.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\logo3.png',0)
while(1):
    d = cv.getTrackbarPos("d","image")
    sigmaColor = cv.getTrackbarPos("sigmaColor","image")
    sigmaSpace = cv.getTrackbarPos("sigmaSpace","image")
    out_img = cv.bilateralFilter(img,d,sigmaColor,sigmaSpace)
    cv.imshow("out",out_img)
    k = cv.waitKey(1) & 0xFF
    if k ==27:
        break
cv.destroyAllWindows()
'''
