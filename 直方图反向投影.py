# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-25-Mon/2019  14:51:10
VERSION: V-1.0
DESCRIPTION:

'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
roi = cv2.imread(
'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\roi_res.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread(
'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\res.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )


h,s,v = cv2.split(hsvt)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

#使用圆盘算子做卷积，B=D×B，其中D为卷积核
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))#定义结构形状，5×5的椭圆
B=cv2.filter2D(B,-1,disc)#对图像进行卷积运算
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

ret,thresh = cv2.threshold(B,100,255,0)
mask = cv2.bitwise_not(thresh)
A = cv2.bitwise_and(target,target,mask = mask)

cv2.imshow('R',R)
cv2.imshow('B',B)
cv2.imshow('mask',mask)
cv2.imshow('thresh',A)
'''
roi = cv2.imread(
'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\roi_res.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread(
'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\res.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
#计算目标直方图
roihist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
#归一化：原始图、借过图、映射到结果图的最小值、最大值、归一化类型
#归一化后的直方图便于显示
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
'''
/*
void cv::calcBackProject(
	const Mat *        images,
	int                nimages,
	const int *        channels,
	InputArray         hist,
	OutputArray        backProject,
	const float **     ranges,
	double             scale = 1,
	bool               uniform = true
	)
 
//2.参数解释
//const Mat* images:输入图像，图像深度必须位CV_8U, CV_16U或CV_32F中的一种，尺寸相同，每一幅图像都可以有任意的通道数
//int nimages : 输入图像的数量
//const int* channels : 用于计算反向投影的通道列表，通道数必须与直方图维度相匹配，第一个数组的通道是从0到image[0].channels() - 1, 第二个数组通道从图像image[0].channels()到image[0].channels() + image[1].channels() - 1计数
//InputArray hist : 输入的直方图，直方图的bin可以是密集(dense)或稀疏(sparse)
//OutputArray backProject : 目标反向投影输出图像，是一个单通道图像，与原图像有相同的尺寸和深度
//const float ranges** : 直方图中每个维度bin的取值范围
//double scale = 1 : 可选输出反向投影的比例因子
//bool uniform = true : 直方图是否均匀分布(uniform)的标识符，有默认值true
*/
'''
dst1 = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
#卷积连接分散的点
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))#定义结构形状，5×5的椭圆
dst=cv2.filter2D(dst1,-1,disc)#对图像进行卷积运算

ret,thresh = cv2.threshold(dst,60,255,0)
# 别忘了是三通道图像，因此这里使用merge 变成3通道
thresh = cv2.merge((thresh,thresh,thresh))
# 按位操作
res = cv2.bitwise_and(target,thresh)

res = np.hstack((target,thresh,res))

cv2.imshow('res',res)


k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
