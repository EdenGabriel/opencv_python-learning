# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

* Copyright (c) 2019,************
* All rights reserved.
FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Mar-06-Wed/2019  08:14:11
VERSION: V-1.0
Function List: // 主要函数列表，每条记录应包括函数名及功能简要说明
DESCRIPTION:
History: // 历史修改记录
<author>    <time>    <version >    <desc>
                                    build this moudle

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\messi5.jpg')
newmask = cv2.imread('E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\messi5_mask.jpg',0)

mask = np.zeros(img.shape[:2],np.uint8)
mask[newmask == 0] = 0
mask[newmask == 255] = 1


bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#rect = (50,50,450,290)
mask,bgdModel,fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask == 2)|(mask == 0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]

'''cv2.imshow('img',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
'''
plt.imshow(img),plt.colorbar(),plt.show()
