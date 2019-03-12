# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:鼠标回调2
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  21:31:21
VERSION: V-1.0
DESCRIPTION:实现在图片上的自由框选

'''
'''
#利用如下代码可以查看所有被支持的鼠标事件
import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print(events)
'''

import numpy as np
import cv2



def draw_rect(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        print('start_point := ',ix,iy)
    elif event == cv2.EVENT_LBUTTONUP:
        print('end_point := ',x,y)
        print('length = ',x - ix)
        print('width = ',y - iy)
        '''画圆
        rrr = (x - ix)//2
        cv2.circle(image,(ix+rrr,iy+rrr),rrr,(0,255,0),1)
        '''
        cv2.rectangle(image,(ix,iy),(x,y),(255,0,0),1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,str(x-ix),(x,y),font,0.5,(0,255,255),2)
        cv2.putText(image,'/',(x+20,y),font,0.5,(0,255,255),2)
        cv2.putText(image,str(y-iy),(x+30,y),font,0.5,(0,255,255),2)
#image =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\1.png')
image =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\maliao.jpg')
#image = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg')
cv2.namedWindow('image_choose')
cv2.setMouseCallback('image_choose',draw_rect)

while(1):  
    cv2.imshow('image_choose',image)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
