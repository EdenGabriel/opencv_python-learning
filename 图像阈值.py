# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  15:21:43 
VERSION: V-1.0
DESCRIPTION:
'''

import cv2
import numpy as np

from matplotlib import pyplot as plt

img_gray = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\1.png')
img = cv2.cvtColor(img_gray,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(img,72,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,72,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,72,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,72,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,72,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



