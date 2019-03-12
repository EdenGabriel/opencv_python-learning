# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  08:59:31 
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np



drawing = False
mode = True
ix,iy = -1,-1

def nothing(x):
    pass

def draw_rect(event,x,y,flags,param):
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    #global color
    color = (b,g,r)
    
    global ix,iy,mode,drawing


    #按下左键是获取坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),color,-1)
                cv2.imshow('image',img)
            elif mode == False:
                #以鼠标拖拽的终点与起点之差为半径
#                r =int(np.sqrt(np.square(ix-x)+np.square(iy-y)))
#                cv2.circle(img,(x,y),r,(255,0,0),-1)
                cv2.circle(img,(x,y),2,color,-1)
                cv2.imshow('image',img)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

def do():
    global mode
    mode = True
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)
    cv2.setMouseCallback('image',draw_rect)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1)&0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
            
            #s = cv2.getTrackbarPos(switch,'image')
            #global color
            #color = (b,g,r)
            
    cv2.destroyAllWindows()

