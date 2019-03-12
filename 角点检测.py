# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-06-Wed/2019  09:55:14
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:角点检测+亚像素角点检测
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np

#①
'''
filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\blox.jpg''

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 输入图像必须是float32，最后一个参数在0.04 到0.05 之间
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)#图像膨胀

img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
'''
#②
filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\blox.jpg'

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 输入图像必须是float32，最后一个参数在0.04 到0.05 之间
#找harris角点
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)#图像膨胀
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
#找质心
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
#定义迭代截止条件和精度
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)

corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
res = np.hstack((centroids,corners))
#np.int0 可以省略小数点后面的数字（非四舍五入）
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]#harris角点用红色
img[res[:,3],res[:,2]] = [0,255,0]#修正后的像素用绿色

cv2.imshow('img',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
