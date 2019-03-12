# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  14:47:59 
VERSION: V-1.0
DESCRIPTION:
图像梯度
'''

import numpy as np
import cv2


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\13.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gau = cv2.GaussianBlur(img_gray,(5,5),0)


ksize = 3
sobelx = cv2.Sobel(img_gau,cv2.CV_64F,1,0,ksize )
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img_gau,cv2.CV_64F,0,1,ksize)
sobely = cv2.convertScaleAbs(sobely)
sobel_res = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

sobelx1 = cv2.Sobel(img_gau,cv2.CV_8U,1,0,ksize )
sobely1 = cv2.Sobel(img_gau,cv2.CV_8U,0,1,ksize)
sobel_res1 = cv2.addWeighted(sobelx1,0.5,sobely1,0.5,0)


scharrx = cv2.Scharr(img_gau,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img_gau,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)
scharry_res = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

laplace = cv2.Laplacian(img_gau,cv2.CV_64F,ksize = 3)
laplace = cv2.convertScaleAbs(laplace)

cv2.imshow('original',img_gray)
cv2.imshow('sobel_res',sobel_res)
cv2.imshow('scharry_res',scharry_res)
cv2.imshow('laplace',laplace)
cv2.imshow('sobel_res1',sobely1)

k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
