# -*- coding: utf-8 -*-

import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        #像素设置，200w摄像头（1600*1200）
        self.video.set(3,1600)
        self.video.set(4,1200)

    def __del__(self):
        self.video.release()
    def get_frame(self):
        try:
            #如果初始化摄像头失败了，打开摄像头
            #if self.video.Opened() != True:
             #   self.video.open()
            #捕获摄像头照片
            success, image = self.video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
        except Exception, e:
            print "[*]",e
        return jpeg.tostring()
        #jpeg.tobytes() python3使用此函数
