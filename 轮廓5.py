# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-23-Sat/2019  08:47:15
VERSION: V-1.0
DESCRIPTION:
cv2.matchShape() 可以帮我们比较两个形状或轮廓的相似度。
如果返回值越小，匹配越好。它是根据Hu 矩来计算的.0
'''

import cv2
import numpy as np

img1 = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\shape_sample\\1.png',0)
img2 = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\shape_sample\\2.png',0)

ret, thresh1 = cv2.threshold(img1, 127, 255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img2, 127, 255,cv2.THRESH_BINARY)

image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
image,contours,hierarchy = cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)
