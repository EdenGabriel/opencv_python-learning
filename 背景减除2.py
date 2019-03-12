# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-09-Thu/2019  09:08:15
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
BackgroundSubtractorMOG2也以混合高斯模型为基础的前景/背景分割算法
这个算法的一个特点是它为每一个像素选择一个合适数目的高斯分布。
（上一个方法中我们使用是K 高斯分布）。
这样就会对由于亮度等发生变化引起的场景变化产生更好的适应。

和前面一样我们需要创建一个背景对象。但在这里我们我们可以选择是否
检测阴影。如果detectShadows = True（默认值），它就会检测并将影子标记
出来，但是这样做会降低处理速度。影子会被标记为灰色。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'
cap = cv2.VideoCapture(filename)

#cap = cv2.VideoCapture(0)
cv2.createBackgroundSubtractorMOG2
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret,frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(100) == 27:
        break

cap.release()
cv2.destroyAllWindows()
