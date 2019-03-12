# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-25-Mon/2019  09:35:44
VERSION: V-1.0
DESCRIPTION:

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg')
#将颜色空间BGR转换到YUV。再单独作用Y通道即可均衡化彩色图像.
img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

img_yuv[:,:,0]= cv2.equalizeHist(img_yuv[:,:,0])
equ = cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)
#可横排显示多个照片
res = np.hstack((img,equ))

hist_img = cv2.calcHist([img],[0],None,[256],[0,256])
hist_equ = cv2.calcHist([equ],[0],None,[256],[0,256])

plt.subplot(221),plt.imshow(cv2.cvtColor(img,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(222),plt.imshow(cv2.cvtColor(res,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(223),plt.imshow(cv2.cvtColor(equ,cv2.COLOR_RGB2BGR),'gray')
plt.subplot(224),plt.plot(hist_img),plt.plot(hist_equ)

plt.show()
'''
cv2.imshow('img',img)
cv2.imshow('equ',res)
'''

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
    



