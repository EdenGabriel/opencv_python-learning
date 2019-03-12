# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  19:07:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
在kNN 中我们直接使用像素的灰度值作为特征向量。这次我们要使用方
向梯度直方图Histogram of Oriented Gradients （HOG）作为特征向量。
在计算HOG 前我们使用图片的二阶矩对其进行抗扭斜（deskew）处理

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\digits.png'

SZ=20
bin_n = 16


affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

def deskew(img):
    
    m = cv2.moments(img)
    
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    
    skew = m['mu11']/m['mu02']
    M = np.float32([[1,skew,-0.5*SZ*skew],[0,1,0]])
    img = cv2.warpAffine(img,M,(SZ,SZ),flags = affine_flags)
    return img

#接下来我们要计算图像的HOG 描述符，创建一个函数hog()。为此我们
#计算图像X 方向和Y 方向的Sobel 导数。然后计算得到每个像素的梯度的方
#向和大小。把这个梯度转换成16 位的整数。将图像分为4 个小的方块，对每
#一个小方块计算它们的朝向直方图（16 个bin），使用梯度的大小做权重。这
#样每一个小方块都会得到一个含有16 个成员的向量。4 个小方块的4 个向量
#就组成了这个图像的特征向量（包含64 个成员）。这就是我们要训练数据的特
#征向量。
#https://www.leiphone.com/news/201708/ZKsGd2JRKr766wEd.html
#详细过程解释见上述网址
def hog(img):
    gx = cv2.Sobel(img,cv2.CV_32F,1,0)
    gy = cv2.Sobel(img,cv2.CV_32F,0,1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))
    bin_cells = bins[:10,:10],bins[10:,:10],bins[:10,10:],bins[10:,10:]
    mag_cells = mag[:10,:10],mag[10:,:10],mag[:10,10:],mag[10:,10:]
    hists = [np.bincount(b.ravel(),m.ravel(),bin_n)
             for b, m in zip(bin_cells,mag_cells)]
    hist = np.hstack(hists)
    return hist

#最后，和前面一样，我们将大图分割成小图。使用每个数字的前250 个作
#为训练数据，后250 个作为测试数据

img = cv2.imread(filename,0)

cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]

train_cells = [i[:50] for i in cells]
test_cells = [i[50:] for i in cells]

#训练
#python3下的map()函数返回类型为iterators，不再是list，
deskewed = [list(map(deskew, row)) for row in train_cells]
hogdata = [list(map(hog, row)) for row in deskewed]
trainData = np.float32(hogdata).reshape(-1,64)
responses = np.repeat(np.arange(10),250)[:,np.newaxis]

svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)

svm.train(trainData, cv2.ml.ROW_SAMPLE,responses)
svm.save('svm_data.dat')

#测试
deskewed = [list(map(deskew, row)) for row in test_cells]
hogdata = [list(map(hog, row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1,bin_n*4)
result = svm.predict(testData)[1]

mask = result == responses
correct = np.count_nonzero(mask)
print(correct*100.0/result.size)




