# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  09:43:14
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:


History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

#随机生成25个测试数据
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
#随机对25个数据置0或1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)
#红色为0
red = trainData[responses.ravel() == 0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
#蓝色为1
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

#测试数据

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

#knn = cv2.ml.KNearest_create()
#构建KNN分类器
knn = cv2.ml_KNearest.create()
#传入一个训练数据集，以及
#与训练数据对应的分类来训练kNN 分类器（构建搜索树）
knn.train(trainData, cv2.ml.ROW_SAMPLE,responses)

#最后要使用OpenCV 中的kNN 分类器，我们给它一个测试数据，让它来
#进行分类。在使用kNN 之前，我们应该对测试数据有所了解。我们的数据应
#该是大小为数据数目乘以特征数目的浮点性数组。然后我们就可以通过计算找
#到测试数据最近的邻居了
ret,results,neighbours,dist = knn.findNearest(newcomer,3)

print('results: ',results,'\n')
print('neighbours: ',neighbours,'\n')
print('dist: ',dist,'\n')
plt.show()
plt.show()
