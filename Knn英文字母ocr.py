# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  18:31:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
一个数据文件letter-recognition.data它有20000 行
实际上每一行的第一列是我们的一个字母标记。接
下来的16 个数字是它的不同特征。
这些特征来源于UCI Machine LearningRepository

取前10000 个作为训练样本，剩下的10000 个作为测试样本。
我们应在先把字母表转换成asc 码，因为我们不直接处理字母。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\letter-recognition.data'

data = np.loadtxt(filename,dtype = 'float32',delimiter = ',',
                  converters = {0:lambda ch:ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data,2)
# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])


#构建KNN分类器
knn = cv2.ml_KNearest.create()
#传入一个训练数据集，以及
#与训练数据对应的分类来训练kNN 分类器（构建搜索树）
knn.train(trainData, cv2.ml.ROW_SAMPLE,responses)
ret,results,neighbours,dist = knn.findNearest(testData,k = 5)

correct = np.count_nonzero(results == labels)
accuracy = correct*100.0/10000
print(accuracy,'%')



