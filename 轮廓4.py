# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-23-Sat/2019  08:10:21
VERSION: V-1.0
DESCRIPTION:

'''
import cv2
import numpy as np

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\star.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray,(5,5),0)
ret,thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
#cv2.RETR_EXTERNAL寻找最外层轮廓
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,contours,-1,(0, 255, 150),4)

cnt = contours[0]
#图象上某一点都轮廓的最短距离
dist = cv2.pointPolygonTest(cnt,(50,50),True)
#查找凸包，设为false表示查找的是凸缺陷对应的轮廓上的点
hull = cv2.convexHull(cnt,returnPoints = False)
#查找凸缺陷，defects.shape[0]表示返回的数组的行数，也就是说有几个凸缺陷
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    #defects[i,0] => defects[i][0]降维的过程
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[255,0,120],2)
    cv2.circle(img,far,5,[200,100,50],-1)
    

cv2.imshow('thresh',thresh)
cv2.imshow('img',img)


k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

