# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  15:54:46
VERSION: V-1.0
DESCRIPTION:

'''
'''
#利用如下代码可以查看所有被支持的鼠标事件
import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print(events)
'''

import numpy as np
import cv2


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
        print(x,y)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


while(1):
    k = cv2.waitKey(1)&0xFF
    cv2.imshow('image',img)
    
    if  k == 27:
        break
    
cv2.destroyAllWindows()


