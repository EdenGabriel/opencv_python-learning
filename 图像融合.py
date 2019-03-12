# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-54-Thu/2018  12:14:58 
VERSION: V-1.0
DESCRIPTION:
图像融合
'''

import cv2
import numpy as np

apple = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\apple.jpg')
orange = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\orange.jpg')

row,col,sh = apple.shape
row1,col1,sh1 = orange.shape

G = apple.copy()
gpA = [G]
#对apple进行高斯金字塔处理
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
#对orange进行高斯金字塔处理
G = orange.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
#对apple作拉普拉斯金字塔处理
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
#对orange作拉普拉斯金字塔处理
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
    
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,channels = la.shape
    ls = np.hstack((la[:,0:cols//2],lb[:,cols//2:]))
    LS.append(ls)

ls_ = LS[0]#LS[0]是高斯金字塔中最小的图片
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_,LS[i])#采用金字塔拼接的方式


real = np.hstack((apple[:,:cols//2],orange[:,cols//2:]))#直接拼接的方式

ls_new = cv2.resize(ls_,(400,400))
#ls_gray = cv2.cvtColor(ls_,cv2.COLOR_BGR2GRAY)
cv2.imshow('ls_new',ls_new)
cv2.imshow('real',real)
cv2.imshow('ls_',ls_)

k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
    
