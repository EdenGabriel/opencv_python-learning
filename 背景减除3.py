# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-09-Thu/2019  09:20:37
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
BackgroundSubtractorGMG此算法结合了静态背景图像估计和每个像素的贝叶斯分割
它使用前面很少的图像（默认为前120 帧）进行背景建模。使用了概率前景估计算法
（使用贝叶斯估计鉴定前景）。这是一种自适应的估计，新观察到的对象比旧的对象
具有更高的权重，从而对光照变化产生适应。一些形态学操作如开运算闭运算等被用
来除去不需要的噪音。在前几帧图像中你会得到一个黑色窗口。
对结果进行形态学开运算对与去除噪声很有帮助。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'
cap = cv2.VideoCapture(filename)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret,frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
