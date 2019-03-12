# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  15:38:39 
VERSION: V-1.0
DESCRIPTION:
自适应阈值
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\shudu.png')
img = cv2.medianBlur(img,5)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,img_thre1 = cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY)
img_thre2 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,15,2)
img_thre3 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY,11,2)
img_thre4 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY,15,2)


titles = ['Original','Original_gray','Threshold','ADPTIVE_THRESH_MEAN',
          'ADPTIVE_THRESH_GAUSSIAN','ADPTIVE_THRESH_GAUSSIAN1']
imgs = [img,img_gray,img_thre1,img_thre2,img_thre3,img_thre4]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
