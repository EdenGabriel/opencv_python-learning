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
使用FLANN匹配时需要传入两个字典作为参数
第一个是IndexParams，用来传入针对不同描述方法下的不同算法
具体算法信息参照FLANN文档
第二个是SearchParams，用来指定递归遍历的此时，值越高越准确
但是消耗的时间也越多

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

sift = cv2.xfeatures2d.SIFT_create()
kp_boxS,des_boxS = sift.detectAndCompute(img_boxS,None)
kp_boxT,des_boxT = sift.detectAndCompute(img_boxT,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des_boxS,des_boxT,k = 2)
print(len(matches))
# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
flann_res = cv2.drawMatchesKnn(img_boxS,kp_boxS,img_boxT,kp_boxT,matches,None,**draw_params)

cv2.imshow('flann_res',flann_res)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
