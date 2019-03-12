# 待排版 有问题无法运行
#!/usr/bin/env python
'''
Camshift tracker
================
This is a demo that shows mean-shift based tracking
You select a color objects such as your face and it tracks it.
This reads from video camera (0 by default, or the camera number the user enters)
http://www.robinhewitt.com/research/track/camshift.html
Usage:
------
camshift.py [<video source>]
To initialize tracking, select the object with mouse
Keys:
-----
ESC - exit
b - toggle back-projected probability visualization
'''
import numpy as np
import cv2
# local module
import video

class App(object):
    def __init__(self, video_src):
        self.cam = video.create_capture(video_src)
        ret, self.frame = self.cam.read()
        cv2.namedWindow('camshift')
        cv2.setMouseCallback('camshift', self.onmouse)
        self.selection = None
        self.drag_start = None
        self.tracking_state = 0
        self.show_backproj = False
    def onmouse(self, event, x, y, flags, param):
        x, y = np.int16([x, y])
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
            self.tracking_state = 0
# 官方示例中下面一行判断有问题，作如下修改就可以了
        if self.drag_start and event == cv2.EVENT_MOUSEMOVE:
# print x,y
            if flags==cv2.EVENT_FLAG_LBUTTON:
# print 'ok'
                h, w = self.frame.shape[:2]
                xo, yo = self.drag_start
                x0, y0 = np.maximum(0, np.minimum([xo, yo], [x, y]))
                x1, y1 = np.minimum([w, h], np.maximum([xo, yo], [x, y]))
                self.selection = None
                if x1-x0 > 0 and y1-y0 > 0:
                    self.selection = (x0, y0, x1, y1)
                    print(self.selection)
            else:
                self.drag_start = None
                if self.selection is not None:
                    self.tracking_state = 1
def show_hist(self):
    bin_count = self.hist.shape[0]
    bin_w = 24
