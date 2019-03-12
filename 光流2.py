# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-09-Thu/2019  07:49:29
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
计算稠密光流。结果是一个带有光流向量（u，v）的双通道数组
通过计算我们能得到光流的大小和方向。我们使用颜色对结果进
行编码以便于更好的观察。方向对应于H（Hue）通道，大小对应
于V（Value）通道

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np
#from matplotlib import pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'

cap = cv2.VideoCapture(filename)

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
#cv2.calcOpticalFlowFarneback(prev, next, pyr_scale, levels, winsize, iterations, poly_n,
#poly_sigma, flags[)
#pyr_scale – parameter, specifying the image scale (<1) to build pyramids for each image;
#pyr_scale=0.5 means a classical pyramid, where each next layer is twice smaller than the
#previous one.
#poly_n – size of the pixel neighborhood used to find polynomial expansion in each pixel;
#typically poly_n =5 or 7.
#poly_sigma – standard deviation of the Gaussian that is used to smooth derivatives used
#as a basis for the polynomial expansion; for poly_n=5, you can set poly_sigma=1.1, for
#poly_n=7, a good value would be poly_sigma=1.5.
#flag 可选0 或1,0 计算快，1 慢但准确
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 1)
#cv2.cartToPolar Calculates the magnitude and angle of 2D vectors.
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2',rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imshow('opticalfb',frame2)
        cv2.imshow('opticalhsv',rgb)
    prvs = next
cap.release()
cv2.destroyAllWindows()
