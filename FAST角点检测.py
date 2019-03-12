# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-07-Tue/2019  7:41:58
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

fast = cv2.FastFeatureDetector_create(100)
#使用非最大值抑制
kp = fast.detect(gray,None)
img1 = cv2.drawKeypoints(gray,kp,None,color = (255,0,0))

print('Threshold: ',fast.getThreshold())
print('nonmaxSuppression: ',fast.getNonmaxSuppression())
print('neighborhood: ',fast.getType())
print('Total Keypoints with nonmaxSuppression: ',len(kp))

cv2.imshow('fast_true',img1)
#不使用非最大值抑制
fast.setNonmaxSuppression(0)
kp = fast.detect(gray,None)
print('Total Keypoints without nonmaxSuppression: ',len(kp))
img2 = cv2.drawKeypoints(gray,kp,None,color = (255,0,0))

cv2.imshow('fast_false',img2)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
