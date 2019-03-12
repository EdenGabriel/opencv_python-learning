# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  09:23:27
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
当前程序运行出来的结果有很大噪音的问题，首先是两幅图片的选择
应该是由双目摄像头中的一个左摄像头一个摄像头拍摄得来的
其次就是numDisparities、blockSize的值的调整

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

filenamel = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\ll.png'
filenamer = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\rr.png'

imgL = cv2.imread(filenamel,0)
imgR = cv2.imread(filenamer,0)
#cv2.StereoBM
stereo = cv2.StereoBM.create(numDisparities=32, blockSize=5)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
