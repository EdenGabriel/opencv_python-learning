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
DESCRIPTION:
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np



filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\butterfly.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#opencv将SIFT等算法整合到xfeatures2d集合里面了。
surf = cv2.xfeatures2d.SURF_create(50000)

#会检测关键点的方向
kp,des = surf.detectAndCompute(gray,None)

#不会检测关键点的方向U-SURF
#surf = cv2.xfeatures2d.SURF_create(50000,upright = True)
#kp = surf.detect(gray,None)

img = cv2.drawKeypoints(gray,kp,None,(255,0,0),4)

cv2.imshow('img',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
