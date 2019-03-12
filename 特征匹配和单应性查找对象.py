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
联合使用特征提取和calib3d 模块中的findHomography 在复杂图像
中查找已知对象。
首先在图像中来找到SIFT 特征点，然后再使用比值测试找到最佳匹配。

History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np

MIN_MATCH_COUNT = 10

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

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
#现在我们设置只有存在10 个以上匹配时才去查找目标（MIN_MATCH_COUNT=10），
#否则显示警告消息：“现在匹配不足！”
#如果找到了足够的匹配，我们要提取两幅图像中匹配点的坐标。把它们传
#入到函数中计算透视变换。一旦我们找到3x3 的变换矩阵，就可以使用它将查
#询图像的四个顶点（四个角）变换到目标图像中去了。然后再绘制出来。
        
if len(good)>MIN_MATCH_COUNT:
#获取关键点的坐标
    src_pts = np.float32([ kp_boxS[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp_boxT[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

# 第三个参数Method used to computed a 单应矩阵.
# The following methods are possible:
#theta - a regular method using all the points
#CV_RANSAC - RANSAC-based robust method
#CV_LMEDS - Least-Median robust method
#第四个参数取值范围为1-10，拒绝一个点对的阈值，
#原图像的点经过变换后点与目标图像上对应的点的误差
#超过误差即为outliner
#返回值中M为变换矩阵

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

#获取原图像的高和宽
    h,w = img_boxS.shape
#利用表换矩阵对原图像的四个角进行变换，获取在目标图象上对应的坐标
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    cv2.polylines(img_boxT,[np.int32(dst)],True,255,10, cv2.LINE_AA)
else:
    print('现在匹配不足！ - %d/%d' % (len(good),MIN_MATCH_COUNT))
    matchesMask = None
    
draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

res = cv2.drawMatches(img_boxS,kp_boxS,img_boxT,kp_boxT,good,None,**draw_params)

cv2.imshow('res',res)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
