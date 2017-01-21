import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        try:
            success, image = self.video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
        #jpeg.tobytes() python3使用此函数
        except Exception, e:
            print "[*]",e
        return jpeg.tostring()