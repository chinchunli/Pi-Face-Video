# External Library
from vidUtil.piWebStream import WebcamVideoStream
from vidUtil.imgUtil import checkIfRepeat

# Python Library
import argparse
import imutils
import time
import os
import sys


# OpenCV Library
import cv2
import numpy as np

# Global Variables
param_face = {'sf': 1.1, 'mNbr': 3, 'size': (120, 120)}
target_directory = '/home/bluekidds/projects/Pi-Face-Video/Useful/'
cascade_directory = '/home/bluekidds/opencv/data/haarcascades'

def fetch_video_names(directory, eof='mkv'):

    video_list = list()
    for name in os.listdir(directory):
        if name.endswith(eof):
            videoname = os.path.join(directory, name) #JOIN HERE
            video_list.append(videoname)
    return video_list


def setCascade(filePath, objType):
    #if objType == 'face':
    #    print "Initialize " + objType + " cascade"
    #    return cv2.CascadeClassifier(filePath)
    #elif objType == 'Mouth':
    #    print "Initialize " + objType + " cascade"
    return cv2.CascadeClassifier(filePath)


def ifFaceDetected(image, cascade, param):

    '''Help
    :param image:
    :param cascade:
    :param param:
    :return: 1 if face detected, 0 if not
    '''

    rects = cascade.detectMultiScale(image,
                                     scaleFactor = param['sf'],
                                     minNeighbors = param['mNbr'],
                                     minSize = param['size'],
                                     flags=cv2.CASCADE_FIND_BIGGEST_OBJECT)
    if len(rects) == 0:
        return 0
    else:
        return 1

def detectAndSaveFaces(videoname, cascade, index):

    ## Setup video capture
    cap = cv2.VideoCapture(videoname)
    #filename = os.path.join(tar_directory + videoname, "%05d" % index + '.png')

    flag, frame = cap.read() # Get first image
    firstFrame = np.zeros(frame.shape)


    while True:
        # grab the frame from camera
        flag, frame = cap.read()

        if frame is None:
            break
        # Add if frame is None then break and CLOSE CAP

        # initialize for faceDetect module
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_equal = cv2.equalizeHist(gray)
        output = ifFaceDetected(gray_equal, cascade, param_face)

        if output:
            ##if checkIfRepeat(firstFrame, gray_equal):
            ##    continue


            ## save image to index.jpg and index.png
            cv2.imwrite("%05d" % index + '.png', output)
            cv2.imwrite("%05d" % index + '.jpg', output)
            print 'Detect Face'
            index += 1
        else:
            continue

    cap.release()
    return index








def main():
    ## Load Videos Directory -> list of videoes
    tar_directory = '/home/bluekidds/projects/Pi-Face-Video/Useful/'
    directory = '/home/bluekidds/projects/Pi-Face-Video/'
    video_list = fetch_video_names(directory)

    index = 0

    ## Prepare environment for face detect

    faceCascade = setCascade('cascade/haarcascade_frontalface_alt.xml', 'face')
    profileCascade = setCascade('cascade/haarcascade_profileface.xml', 'face')


    ## For each video, open and detect faces
    for videoname in video_list:
        new_index = detectAndSaveFaces(videoname, faceCascade, index)
        index = new_index

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
