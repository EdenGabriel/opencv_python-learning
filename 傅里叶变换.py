# -*- coding: utf-8 -*-
'''
======================Welcome to Python====================
/-********Have a good time.********-/

FILE NAME:
AUTHOR: Eden·Gabriel 
DATE: Feb-26-Tue/2019  08:02:19
VERSION: V-1.0
DESCRIPTION:

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


########    numpy实现傅立叶变换
img = cv2.imread(
'E:\\A_BOOM_LEARNING_EDEN_GABRIEL\\2018.12.19start_opencv+python\\Images\\messi5.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img_gray.shape
crow,ccol = int(rows/2),int(cols/2)

f = np.fft.fft2(img_gray)
fshift = np.fft.fftshift(f)


fshift[crow-30:crow+30,ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

'''
#构建振幅图公式
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_RGB2BGR), cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
'''
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
'''
/*尤其是最后一章JET 颜色的图像，你会看到一些不自然的东西。
看上图那里有些条带装的结构，这被成为振铃效应。这是由于我们
使用矩形窗口做掩模造成的。这个掩模被转换成正弦形状时就会出
现这个问题。所以一般我们不适用矩形窗口滤波。最好的选择是高斯窗口
*/
'''
