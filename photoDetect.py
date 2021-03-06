# External Library
from vidUtil.piWebStream import WebcamVideoStream
from vidUtil.imgUtil import checkIfRepeat

# Python Library
import argparse
import imutils
import time
import os
import sys
import copy

# OpenCV Library
import cv2
import numpy as np

# Global Variables
param_face = {'sf': 1.1, 'mNbr': 5, 'size': (120, 120)}
target_directory = '/Data/FaceVideo/Useful/'
cascade_directory = '/home/bluekidds/opencv/data/haarcascades/'

def fetch_video_names(directory, eof='mkv'):

    video_list = list()
    for name in os.listdir(directory):
        if name.endswith(eof):
            videoname = os.path.join(directory, name) #JOIN HERE
            video_list.append(videoname)
    return video_list


def setCascade(cascade_path, objType):
    #if objType == 'face':
    #    print "Initialize " + objType + " cascade"
    #    return cv2.CascadeClassifier(filePath)
    #elif objType == 'Mouth':
    #    print "Initialize " + objType + " cascade"
    cascade = cv2.CascadeClassifier(cascade_path)
    if cascade is not None:
        return cascade
    else:
        raise ValueError('Check the path of cascade')
 


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
                                     flags=cv2.CASCADE_SCALE_IMAGE)

    if len(rects) == 0:
        return [0, None]
    else:
        rects[:, 2:] += rects[:, :2]
        return [1, rects]


def drawRects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        
        
        

def detectAndSaveFaces(videoname, cascade, index):

    ## Setup video capture
    cap = cv2.VideoCapture(videoname)
    #filename = os.path.join(tar_directory + videoname, "%05d" % index + '.png')

    flag, frame = cap.read() # Get first image
    firstFrame = np.zeros(frame.shape[:2])
    

    while True:
        # grab the frame from camera
        flag, frame = cap.read()
        
        if frame is None:
            break
        # Add if frame is None then break and CLOSE CAP

        # initialize for faceDetect module
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_equal = cv2.equalizeHist(gray)
        output, rects = ifFaceDetected(gray_equal, cascade, param_face)
        
        if output:
            if checkIfRepeat(firstFrame, gray_equal):
                continue
            else:
                firstFrame = gray_equal
	    print(output, rects)
            frame_copy = np.copy(frame)
            ## save image to index.jpg and index.png
	    drawRects(frame_copy, rects, (0, 255, 0))
            cv2.imwrite(target_directory + "%05d" % index + '.png', frame)
            cv2.imwrite(target_directory + "%05d" % index + '.jpg', frame_copy)
	    
            #cv2.imshow('Detect Face', frame)
            #cv2.waitKey(5)
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

    index = 615

    ## Prepare environment for face detect
    
    faceCascade = setCascade(cascade_directory + 'haarcascade_frontalface_alt.xml', 'face')
    profileCascade = setCascade(cascade_directory + 'haarcascade_profileface.xml', 'face')


    ## For each video, open and detect faces
    for videoname in video_list:
	print videoname
        new_index = detectAndSaveFaces(videoname, faceCascade, index)
        index = new_index

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
