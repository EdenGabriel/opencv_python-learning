# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  10:27:30
VERSION: V-1.0
DESCRIPTION:

'''


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480),False)

while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        frame = cv2.flip(frame_gray,1)
#写入视频帧
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
