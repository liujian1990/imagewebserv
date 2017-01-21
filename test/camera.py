# -*- coding: utf-8 -*-

import numpy as np
import cv2
import cv
import time
#废弃
class camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def get_frame(self):
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLORMAP_AUTUMN)
        #cv2.VideoWriter(filename="1",fourcc=cv.CV_FOURCC('M','J','P','G'),fps=60,frameSize=1024).write(gray)
        print frame.tolist()
        #cv2.imwrite
        fstring = "".join(frame.tolist())
        return fstring
    def run(self):
        while (True):
            ret, frame = self.cap.read()
            #frame = get_frame()
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLORMAP_AUTUMN)
            # Display the resulting frame
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def stop(self):
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
