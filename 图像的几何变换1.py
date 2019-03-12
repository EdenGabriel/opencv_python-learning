# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-21-Thu/2018  09:49:23 
VERSION: V-1.0
DESCRIPTION:
图形的缩放、平移、仿射变换、透视变换、旋转

'''
'''
import cv2
events=[i for i in dir(cv2) if 'INTER_'in i]
print(events)

['INTER_AREA', 'INTER_BITS', 'INTER_BITS2', 'INTER_CUBIC',
'INTER_LANCZOS4', 'INTER_LINEAR', 'INTER_LINEAR_EXACT',
'INTER_MAX', 'INTER_NEAREST', 'INTER_TAB_SIZE', 'INTER_TAB_SIZE2']

以下网址涵盖了各种插值法常用的情景
https://blog.csdn.net/jningwei/article/details/78822026
'''

import numpy as np
import cv2
#from matplotlib import pyplot as plt


img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\1.png')
#得到的行列实际上是y*x
height,weight = img.shape[:2]

'''
/***********************图形缩放***********************/
img1 = cv2.resize(img,None,0.5,2,cv2.INTER_CUBIC)
#自定义图像时要给图像的宽*高，也就是x*y
img2 = cv2.resize(img,(2*weight,height//2),cv2.INTER_LINEAR)
img3 = cv2.resize(img,(400,400),cv2.INTER_AREA)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imwrite('1.jpg',img3)
'''
'''
/***********************图形平移***********************/

H = np.float32([[1,0,100],[0,1,50]])
img4 = cv2.warpAffine(img,H,(weight,height))
cv2.imshow('img4',img4)
'''

'''
/***********************旋转矩阵***********************/
#L = [x for x in range(0,180)][::15]

M = cv2.getRotationMatrix2D((weight/2,height/2),45,0.5) 
img5 = cv2.warpAffine(img,M,(weight,height))
cv2.imshow('img5',img5)
'''
'''
/***********************仿射变换***********************/
pos1 = np.float32([[255,77],[488,66],[241,288]])
pos2 = np.float32([[164,87],[380,15],[245,260]])
pos11 = np.float32([[0,0],[weight,0],[0,height]])
pos22 = np.float32([[weight*0.3,height*0.3],[weight*0.8,height*0.2],
                    [weight*0.2,height*0.8]])

M = cv2.getAffineTransform(pos11,pos22)
img6 = cv2.warpAffine(img,M,(weight,height),borderValue=(150,52,44))

cv2.imshow('img6',img6)
*/
'''
'''
/***********************透视变换***********************/
pos1 = np.float32([[255,77],[488,66],[241,288],[486,287]])
pos2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pos1,pos2)
img7 = cv2.warpPerspective(img,M,(300,300),borderValue = (255,255,255))
cv2.imshow('img7',img7)
*/
'''
cv2.imshow('img',img)

k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()


'''
plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.subplot(132),plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.subplot(133),plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))

plt.show()
'''
