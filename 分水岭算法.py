# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-27-Wed/2019  09:41:58
VERSION: V-1.0
DESCRIPTION:

'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

img =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret ,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


#出去边界白噪声，先腐蚀再膨胀，开运算
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

dist_transform = cv2.distanceTransform(opening,1,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
#cv2.connectedComponents()会把背景标记为0，但是其他对象使用的是从1开始的正整数
#倘若把背景标记为0，那么分水岭算法就会把它当作是未知区域，
ret, markers1 = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]

res = np.hstack((sure_bg,sure_fg,unknown))
'''
cv2.imshow('thresh',thresh)
cv2.imshow('sure_bg',sure_bg)
cv2.imshow('sure_fg',sure_fg)
'''
cv2.imshow('res',res)
cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
