# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  08:41:08 
VERSION: V-1.0
DESCRIPTION:
Otsu's二值化
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\pic2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 =  cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


images = [img,0,th1,
          img,0,th2,
          blur,0,th3]
print(ret1,ret2,ret3)
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),10)
    plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.xticks([]), plt.yticks([])
plt.show()
