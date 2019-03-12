# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  14:01:52
VERSION: V-1.0
DESCRIPTION:

'''
import numpy as np
import cv2


image = np.zeros((201,201,3),np.uint8)
cv2.line(image,(0,0),(200,200),(255,0,0),3)
cv2.line(image,(0,100),(200,200),(0,255,0),3)
cv2.line(image,(100,100),(200,200),(0,0,255),3)


cv2.rectangle(image,(100,100),(200,200),(120,100,0),3)
cv2.circle(image,(150,150),50,(0,0,255),-1)
cv2.ellipse(image,(100,100),(100,50),90,90,360,(255,0,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.LINE_AA
cv2.putText(image,'Eden',(50,50),font1,2,(255,255,255),5)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
