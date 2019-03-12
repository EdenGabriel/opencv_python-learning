# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  21:20:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
使用非局部平均值去噪算法去除图像中的噪音
cv2.fastNlMeansDenoising()，cv2.fastNlMeansDenoisingColored()

OpenCV 提供了这种技术的四个变本。
1. cv2.fastNlMeansDenoising() 使用对象为灰度图。
2. cv2.fastNlMeansDenoisingColored() 使用对象为彩色图。
3. cv2.fastNlMeansDenoisingMulti() 适用于短时间的图像序列（灰
度图像）
4. cv2.fastNlMeansDenoisingColoredMulti() 适用于短时间的图
像序列（彩色图像）
共同参数有：
• h : 决定过滤器强度。h 值高可以很好的去除噪声，但也会把图像的细节
抹去。(取10 的效果不错)
• hForColorComponents : 与h 相同，但使用与彩色图像。（与h 相
同）
• templateWindowSize : 奇数。(推荐值为7)
• searchWindowSize : 奇数。(推荐值为21)

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''
#①
import cv2
import numpy as np

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\22.png'
img = cv2.imread(filename)

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

res = np.hstack((img,dst))
cv2.imshow('res',res)

#②
import cv2
import numpy as np
from matplotlib import pyplot as plt

#现在我们要对一段视频使用这个方法。第一个参数是一个噪声帧的列表。
#第二个参数imgtoDenoiseIndex 设定那些帧需要去噪，我们可以传入一
#个帧的索引。第三个参数temporaWindowSize 可以设置用于去噪的相邻
#帧的数目，它应该是一个奇数。在这种情况下temporaWindowSize 帧的
#图像会被用于去噪，中间的帧就是要去噪的帧。例如，我们传入5 帧图像，
#imgToDenoiseIndex = 2 和temporalWindowSize = 3。那么第一帧，第二帧，
#第三帧图像将被用于第二帧图像的去噪
filename1 = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\vtest.avi'
cap = cv2.VideoCapture(filename1)
# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]
# convert all to grayscale
gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
# convert all to float64
gray = [np.float64(i) for i in gray]
# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10
# Add this noise to images
noisy = [i+noise for i in gray]
# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]
# Denoise 3rd frame considering all the 5 frames
dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)
plt.subplot(131),plt.imshow(gray[2],'gray')
plt.subplot(132),plt.imshow(noisy[2],'gray')
plt.subplot(133),plt.imshow(dst,'gray')
plt.show()
