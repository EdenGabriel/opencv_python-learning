import cv2
import numpy as np


#in function cvtColor
#scn (the number of channels of the source),
#i.e. self.img.channels(), is neither 3 nor 4.
#
#depth (of the source),
#i.e. self.img.depth(), is neither CV_8U nor CV_32F.
# 所以不能用[0,255,0]，而要用[[[0,255,0]]]
# 这里的三层括号应该分别对应于cvArray，cvMat，IplImage
green=np.uint8([[[255,0,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
