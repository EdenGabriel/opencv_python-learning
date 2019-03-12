# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-07-Tue/2019  19:01:37
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:

1、读入参考图像，设置感兴趣区域（ROI）
2、获取感兴趣区域的色调直方图
3、读取新图像计算色调直方图的反向投影
4、使用meanshift算法在反向投影中定位

meanShift(probImage, window, criteria)
probImage: 概率分布图像，也就是ROI色调直方图的反向投影
window： 初始搜索窗口，就是定义ROI的rect
criteria:确定窗口搜索停止的准则，迭代次数达到设置的最大值；
窗口中心的漂移值小于某个设定的限值。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\Megamind.avi'

cap = cv.VideoCapture(filename)
#读取第一帧图像
ret, frame = cap.read()
#cv.imwrite('megamind.jpg', frame)
#设置初始窗口参数
r, h, c, w = 472, 42, 228, 47
track_window = (c, r, w, h)

#获取ROI
roi = frame[r:r+h, c:c+w]
cv.rectangle(frame, (c, r), (c+w, r+h), (0, 255, 0), 2)
cv.imshow('img', frame)
cv.imshow('roi', roi)
#转成HSV格式
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
# 将低亮度的值忽略掉
lower_hsv = np.array([0, 60, 32])
upper_hsv = np.array([180, 255, 46]) #黑色
mask = cv.inRange(hsv_roi, lowerb=lower_hsv, upperb=upper_hsv)
#颜色直方图
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0,180])

#归一化
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

#确定窗口搜索停止的准则，迭代次数达到设置的最大值，或者窗口中心的漂移值小于设定值
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret,frame = cap.read()

    if ret is True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #直方图反向投影
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        #返回迭代次数和更新后的边框
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        #print(ret)
        

        #在图像中画出
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        cv.imshow('img2', img2)




        k = cv.waitKey(60)& 0xff
        if k == 27:
            break
    else:
        break

cv.waitKey(0)
cv.destroyAllWindows()
cap.release()
