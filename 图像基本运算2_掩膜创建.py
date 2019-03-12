# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  16:05:18 
VERSION: V-1.0
DESCRIPTION:

'''
import numpy as np
import cv2
from matplotlib import pyplot as plt


img1 = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg')
img2 = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\logo2.png')


rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2_gray,40,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(img2,img2,mask = mask)
img2_fg = cv2.bitwise_and(roi,roi,mask = mask_inv)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst


cv2.imshow('img2',img2)
cv2.imshow('img2_gray',img2_gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('result',img1)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

