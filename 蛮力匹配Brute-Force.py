# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-07-Tue/2019  8:52:37
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np



filename_boxS = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\box.png'
filename_boxT= 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\box_in_scene.png'

img_boxS = cv2.imread(filename_boxS,0)
img_boxT = cv2.imread(filename_boxT,0)

#对ORB描述符进行蛮力匹配
orb = cv2.ORB_create()
#使用SIFT方法寻找关键点并描述
kp_boxS,des_boxS = orb.detectAndCompute(img_boxS,None)
kp_boxT,des_boxT = orb.detectAndCompute(img_boxT,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)

#bf.match 返回值是一个DMatch对象列表
#DMatch.distance是描述符之间的距离越小越好
#DMatch.trainIdx是目标图像中描述符的索引
#DMatch.queryIdx是查询图像中描述符的索引
#DMatch.imgIdx是目标图像的索引
matches = bf.match(des_boxS,des_boxT)
matches = sorted(matches, key = lambda x:x.distance)

orb_res = cv2.drawMatches(img_boxS,kp_boxS,img_boxT,kp_boxT,matches[:10],None,flags=2)
cv2.imshow('orb_res',orb_res)


#对SIFT描述符进行蛮力匹配和比值测试
sift = cv2.xfeatures2d.SIFT_create()
kp_boxS,des_boxS = sift.detectAndCompute(img_boxS,None)
kp_boxT,des_boxT = sift.detectAndCompute(img_boxT,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des_boxS,des_boxT,k = 2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
    #if cv2.batchDistance(m) < 0.75*cv2.batchDistance(n):
        good.append([m])
sift_res = cv2.drawMatchesKnn(img_boxS,kp_boxS,img_boxT,kp_boxT,good[:10],None,flags=2)
cv2.imshow('sift_res',sift_res)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

