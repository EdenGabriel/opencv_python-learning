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
Lucas-Kanade方法计算稀疏特征集的光流
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np
#from matplotlib import pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'

cap = cv2.VideoCapture(filename)

#ShiTomasi角点检测参数
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

# lucas kanade 光流参数
#maxlevel为使用的图像金字塔层数
lk_params = dict(winSize = (15,15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))

color = np.random.randint(0,255,(100,3))
ret,old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray,mask = None,**feature_params)

mask = np.zeros_like(old_frame)
while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    p1,st,err = cv2.calcOpticalFlowPyrLK(old_gray,frame_gray, p0, None, **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]

    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = new.ravel()
        mask = cv2.line(mask,(a,b),(c,d),color[i].tolist(),2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)

    cv2.imshow('image',img)
    if cv2.waitKey(0) == 27:
        break
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()
