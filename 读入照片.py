# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Dec-19-Wed/2018  08:51:06
VERSION: V-1.0
DESCRIPTION:

'''

import numpy as np
import cv2


'''
#imdecode指的是从内存中读取照片,这种方法可以用来读取中文路径
cv_img = cv2.imdecode(np.fromfile('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg',
                                  dtype = np.uint8),-1)
#RGB指的是三原色光模式，只不过在opencv中RGB的通道顺序是B\G\R
img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2BGRA)

'''

#opencv中路径选择用\\,否则会出现路径选择错误
img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\lena.jpg',0)

#用来调整窗口大小WINDOW_NORMAL
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

#给waitkey一个0指的是需要等待任意一个键盘输入才会执行下一句
k = cv2.waitKey(0)


#这里表示等待按下esc退出界面
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena.png',img)#保存照片
    cv2.destroyAllWindows()
    
