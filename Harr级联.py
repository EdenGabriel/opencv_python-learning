# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-11-Mon/2019  21:58:34
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
Harr级联
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''
#所需的Harry库从这个网站下载https://github.com/opencv/opencv
import numpy as np
import cv2

filename1 = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\opencv-master\\data\\haarcascades\\haarcascade_eye.xml'
filename2 = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(filename2)
eye_cascade = cv2.CascadeClassifier(filename1)

filename = 'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\data\\lena.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
