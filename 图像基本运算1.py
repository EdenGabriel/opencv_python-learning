# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-20-Thu/2018  15:09:15 
VERSION: V-1.0
DESCRIPTION:

'''
import numpy as np
import cv2

        
img1=cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\ml.png')
img2=cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\opencv-logo.png')


img3 = img2[0:min(img1.shape[0],img2.shape[0]),0:min(img1.shape[1],img2.shape[1])]
img4 = cv2.add(img1,img3)

dst=cv2.addWeighted(img1,0.7,img3,0.3,0)
cv2.imshow('dst',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
