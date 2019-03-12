# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  09:15:30 
VERSION: V-1.0
DESCRIPTION:
图像平滑
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\pic2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#2D卷积滤波
kernel = np.ones((4,4),dtype = np.float32)/16
img_2D = cv2.filter2D(img_gray,-1,kernel)
#res1 = cv2.filter2D(img,-1,kernel)
#均值滤波
img_blur = cv2.blur(img_gray,(5,5))
#高斯模糊
img_gau = cv2.GaussianBlur(img_gray,(5,5),0)
#中值模糊
img_med = cv2.medianBlur(img_gray,5)
#双边滤波
img_bil = cv2.bilateralFilter(img_gray,9,105,105)

ret1,img_gray_thr = cv2.threshold(img_gray,155,255,cv2.THRESH_BINARY)
ret2,img_2D_thr = cv2.threshold(img_2D,155,255,cv2.THRESH_BINARY)
ret3,img_blur_thr = cv2.threshold(img_blur,155,255,cv2.THRESH_BINARY)
ret4,img_gau_thr = cv2.threshold(img_gau,155,255,cv2.THRESH_BINARY)
ret5,img_med_thr = cv2.threshold(img_med,155,255,cv2.THRESH_BINARY)
ret6,img_bil_thr = cv2.threshold(img_bil,155,255,cv2.THRESH_BINARY)


Images=[img_gray,img_2D,img_blur,img_gau,img_med,img_bil,img_gray_thr,img_2D_thr,
        img_blur_thr,img_gau_thr,img_med_thr,img_bil_thr]
titles = ['gray','gray_2D',
          'blur','gau','med','bilater','img_gray_thr','img_2D_thr','img_blur_thr',
          'img_gau_thr','img_med_thr','img_bil_thr']


for i in range(12):
    plt.subplot(5,3,i+2),plt.imshow(Images[i],'gray'),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.subplot(5,3,1),plt.imshow(img),plt.title('original'),plt.xticks([]),plt.yticks([])

plt.show()


    
