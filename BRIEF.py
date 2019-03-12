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

#CenSurE特征检测器在opencv中也叫STAR检测器
#创建STAR检测器
star =cv2.xfeatures2d_StarDetector.create()
#创建BRIEF描述符
brief =cv2.xfeatures2d_BriefDescriptorExtractor.create()

#用STAR寻找关键点
kp = star.detect(gray,None)
#计算描述符
kp, des = brief.compute(gray, kp)

print('bytes',brief.descriptorType())
print(des.shape)

'''
orb = cv2.ORB_create()
kp = orb.detect(gray,None)

kp,des = orb.compute(gray,kp)
img = cv2.drawKeypoints(gray,kp,None,color = (0,255,0),flags = 0)
cv2.imshow('img',img)
'''
