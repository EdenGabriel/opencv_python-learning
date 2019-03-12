# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-07-Tue/2019  20:03:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:

1、读入参考图像，设置感兴趣区域（ROI）
2、获取感兴趣区域的色调直方图
3、读取新图像计算色调直方图的反向投影
4、使用meanshift算法在反向投影中定位

一个被叫做 CAMshift 的算法。这个算法首先要使用meanshift，
meanshift 找到（并覆盖）目标之后，再去调整窗口的大小，
s = 2 *sqrt{{M00}/{256}} 。它还会计算目标对象的最佳外接椭圆的
角度，并以此调节窗口角度。然后使用更新后的窗口大小和角度来在原
来的位置继续进行 meanshift。重复这个过程达到需要的精度。
与 Meanshift 基本一样，但是返回的结果是一个带旋转角度的矩形

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2 
import numpy as np
from matplotlib import pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\Megamind.avi'

cap = cv2.VideoCapture(filename)
#读取第一帧图像
ret, frame = cap.read()
#cv.imwrite('megamind.jpg', frame)
#设置初始窗口参数
r, h, c, w = 472, 42, 228, 47
track_window = (c, r, w, h)

#获取ROI
roi = frame[r:r+h, c:c+w]
cv2.rectangle(frame, (c, r), (c+w, r+h), (0, 255, 0), 2)
cv2.imshow('img', frame)
cv2.imshow('roi', roi)
#转成HSV格式
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 将低亮度的值忽略掉
lower_hsv = np.array([0, 60, 32])
upper_hsv = np.array([180, 255, 46]) #黑色
mask = cv2.inRange(hsv_roi, lowerb=lower_hsv, upperb=upper_hsv)
#颜色直方图
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])

#归一化
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

#确定窗口搜索停止的准则，迭代次数达到设置的最大值，或者窗口中心的漂移值小于设定值
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret,frame = cap.read()

    if ret is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #直方图反向投影
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        #返回迭代次数和更新后的边框
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        #print(ret)
        
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        cv2.imshow('img2',img2)

        k = cv2.waitKey(60)& 0xff
        if k == 27:
            break
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
