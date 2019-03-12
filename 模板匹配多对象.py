# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-26-Tue/2019  09:29:09
VERSION: V-1.0
DESCRIPTION:

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img =  cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\maliao.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = img_gray[61:80,243:261]
w,h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res>=threshold)
for n in zip(*loc[::-1]):
    cv2.rectangle(img,n,(n[0]+w,n[1]+h),(0,0,255),1)

cv2.imshow('template',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
