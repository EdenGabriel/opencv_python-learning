# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  18:18:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
OpenCV 安装包中有一副图片digits.png）, 其中有5000 个手写数字（每个数
字重复500遍）。每个数字是一个20x20 的小图。所以第一步就是将这个图像分
割成5000个不同的数字。我们在将拆分后的每一个数字的图像重排成一行含有400
个像素点的新图像。这个就是我们的特征集，所有像素的灰度值。这是我们能创建
的最简单的特征集。我们使用每个数字的前250 个样本做训练数据，剩余的
250 个做测试数据。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\digits.png'

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)

train = x[:,:50].reshape(-1,400).astype(np.float32)
test = x[:,50:100].reshape(-1,400).astype(np.float32)

k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

#构建KNN分类器
knn = cv2.ml_KNearest.create()
#传入一个训练数据集，以及
#与训练数据对应的分类来训练kNN 分类器（构建搜索树）
knn.train(train, cv2.ml.ROW_SAMPLE,train_labels)
ret,results,neighbours,dist = knn.findNearest(test,k = 5)

matches = results == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/results.size
'''
#knn_data保留为分类器，之后只需要从文件中读取这些数据开始进行分类就可以了
np.savez('knn_data.npz',train=train, train_labels=train_labels)

# Now load the data
with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
'''
print(accuracy,'%')



