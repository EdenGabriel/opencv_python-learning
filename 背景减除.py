# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-09-Thu/2019  08:53:37
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
BackgroundSubtractorMOG以混合高斯模型为基础的前景/背景分割算法

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np


filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'
cap = cv2.VideoCapture(filename)

#cap = cv2.VideoCapture(0)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while(1):
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()
