# import the necessary packages
from threading import Thread
import cv2


class WebcamVideoStream:
    def __init__(self, resolution=(320, 240), src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        self.stream.set(3, 640)		# I have found this to be about the highest-
        self.stream.set(4, 480)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the current frame
        return self.frame

    def stop(self):
        self.stopped = True
