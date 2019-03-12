# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-25-Mon/2019  14:04:44
VERSION: V-1.0
DESCRIPTION:

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt


#将颜色空间BGR转换到YUV。再单独作用Y通道即可均衡化彩色图像.
img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\3.png')
img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#自适应
clahe = cv2.createCLAHE(clipLimit = 2.0,tileGridSize = (8,8))
img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
cll = cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)
#均衡化
img_yuv[:,:,0]= cv2.equalizeHist(img_yuv[:,:,0])
equ = cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)

hist_img = cv2.calcHist([img],[0],None,[256],[0,256])
hist_equ = cv2.calcHist([equ],[0],None,[256],[0,256])
hist_cll = cv2.calcHist([cll],[0],None,[256],[0,256])


plt.subplot(231),plt.title('img'),plt.imshow(cv2.cvtColor(img,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(232),plt.title('img_gray'),plt.imshow(img_gray,'gray')
plt.subplot(233),plt.title('img_yuv'),plt.imshow(cv2.cvtColor(img_yuv,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(234),plt.title('equ'),plt.imshow(cv2.cvtColor(equ,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(235),plt.title('cll'),plt.imshow(cv2.cvtColor(cll,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(236),plt.plot(hist_img),plt.plot(hist_equ),plt.plot(hist_cll),plt.axis('off')

plt.show()


#cv2.imshow('cl1',equ)
