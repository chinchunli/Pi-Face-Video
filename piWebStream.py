# import the necessary packages
from threading import Thread
import cv2


class WebcamVideoStream(object):
    def __init__(self, resolution=(320, 240), src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.weight, self.height = resolution
        self.stream = cv2.VideoCapture(src)
        self.stream.set(3, self.weight)		# I have found this to be about the highest-
        self.stream.set(4, self.height)
        #(self.grabbed, self.frame) = self.stream.read()
        

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False
        self.writter = None

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

    def setWriter(self, fileName, param=None):
        #if param is not None:
        fourcc = cv2.cv.FOURCC(*'mp4v')
        self.writer = cv2.VideoWriter(fileName, fourcc, 15.0, (int(self.weight),int(self.height)))

    def write(self, frame):
        if self.writer is not None:
            self.writer.write(frame)

    def release(self):
        if self.writer is not None:
            self.writer.release()
        self.stream.release()