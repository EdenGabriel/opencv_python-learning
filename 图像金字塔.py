# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-54-Thu/2018  10:35:19 
VERSION: V-1.0
DESCRIPTION:
图像金字塔
'''

import numpy as np
import cv2

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\1.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
up1 = cv2.pyrUp(img)
#up2 = cv2.pyrUp(up1)

down1 = cv2.pyrDown(img)
down2 = cv2.pyrDown(down1)
down3 = cv2.pyrDown(down2)

down_up = cv2.pyrUp(down1)
laplace = img - down_up

down11 = cv2.bitwise_and(down_up,laplace)

cv2.imshow('down11',down11)

cv2.imshow('original',img)
cv2.imshow('up1',up1)
#cv2.imshow('up2',up2)
cv2.imshow('down1',down1)
cv2.imshow('down2',down2)
cv2.imshow('down3',down3)
cv2.imshow('laplace',laplace)

k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
