# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-06-Wed/2019  19:01:14
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:角点检测+亚像素角点检测
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np



filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\home .jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#opencv将SIFT等算法整合到xfeatures2d集合里面了。
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)#寻找关键点

img = cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#img = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
cv2.imshow('img',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
