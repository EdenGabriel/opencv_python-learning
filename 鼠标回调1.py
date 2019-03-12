# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  17:26:35
VERSION: V-1.0
DESCRIPTION:

'''
'''
#利用如下代码可以查看所有被支持的鼠标事件
import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print(events)
'''
import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)
drawing = False

mode = True
ix = -1
iy = -1

def draw_circle(event,x,y,flags,param):
    global ix,iy,mode,drawing
    #按下左键是获取坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                cv2.imshow('image',img)
            elif mode == False:
                #以鼠标拖拽的终点与起点之差为半径
#                r =int(np.sqrt(np.square(ix-x)+np.square(iy-y)))
#                cv2.circle(img,(x,y),r,(255,0,0),-1)
                cv2.circle(img,(x,y),2,(0,0,255),-1)
                cv2.imshow('image',img)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False



def do():
    global mode
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1)&0xFF
        if k == ord('m'):
            mode = not mode
#        elif k == ord('r'):
#            model = False
        elif k == 27:
            break
    cv2.destroyAllWindows()
