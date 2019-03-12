# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  08:31:14 
VERSION: V-1.0
DESCRIPTION:简单的滑动条功能实现

'''
import cv2
import numpy as np

#回调函数必须有至少一个默认参数，即滑动条的位置
def nothing(x):
    pass



img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')


cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        color = [b,g,r]
        img[:] = color
cv2.destroyAllWindows()
