# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  12:44:43 
VERSION: V-1.0
DESCRIPTION:

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg')
#px = img[100,100]
#print(px)

'''
#返回图像行列及通道
img.shape
#返回图像像素数目
img.size
#返回图像数据类型
img.dtype

'''
img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\opencv-logo.png')
#在进行操作之前最好利用img.shape获取图片的行列信息，以免在操作中进行溢出操作
#ball = img[285:342,335:400]
#img[272:329,100:165] = ball
#b,g,r = cv2.split(img)

#b = img[:,:,0]
#g = img[:,:,1]
#r = img[:,:,2]

#cv2.namedWindow('image_roi')
BLUE =  [255,0,0]
img1 = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value = BLUE)


plt.subplot(121),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(122),plt.imshow(img1,'gray'),plt.title('First')
#img = cv2.merge([b,g,r])
#img[:,:,2] = 0
plt.show()

#cv2.imshow('image_roi',b)
'''
k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
    '''
  
