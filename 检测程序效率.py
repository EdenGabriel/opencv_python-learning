# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  19:35:54 
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np
import time

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\logo2.png')


img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_thre = cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY)


e1 = cv2.getTickCount()
#t1 = time.time()
for i in range(5,9,2):
    img1 = cv2.medianBlur(img_gray,i)
e2 = cv2.getTickCount()
t2 = time.time()
t = (e2-e1)/cv2.getTickFrequency()
#tt = t2 - t1
print(t)
#print(tt)
