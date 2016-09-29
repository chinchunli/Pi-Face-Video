from IPython.display import clear_output
import time
import numpy as np
import os
import os.path
import cv2
from motionUtility import isMoving
from itertools import count
import sys
from connection.mySFTP import uploadVideoSFTP


def fetch_video_names(tar_directory, eof='mkv'):
    '''

    :param tar_directory: directory path(str) that contains videoes
    :param eof: file types(default = .mkv)
    :return: video_list of video names that end in eof
    '''
    # video_list = list()

    video_list = [name for name in os.listdir(tar_directory)
                  if name.endswith(eof)]
    return video_list


def video_to_image(videoname, directory, tar_directory):

    cap = cv2.VideoCapture(os.path.join(directory, videoname))
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    index = 1

    while True:
        #os.mkdir(os.path.join(tar_directory, videoname))

        filename = os.path.join(tar_directory + videoname, "%05d" % index + '.png')
        print (filename)

        ret, img = cap.read()
        # frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if img is None:
            break

        if isMoving(img, fgbg):
            print('Start Setting writer')
            cv2.imwrite(filename, img)
        index += 1

    cap.release()


if __name__ == '__main__':

    # Get directory
    directory = '/home/bluekidds/Pi-Face-Video/video'
    tar_directory = '/home/bluekidds/Pi-Face-Video/photo/'
    #path ='/home/bluekidds/Pi-Face-Video/photo/'
    video_list = fetch_video_names(directory)
    # Get list(XXXX) from fetch_video_names(directory)
    for videoname in video_list:
        print (videoname)

        video_to_image(videoname, directory, tar_directory)



    # videoname = '/home/bluekidds/Pi-Face-Video/FF5_8_5_2016_photo/FF5_8_5_2016.mkv'

    # videoname = '/home/bluekidds/Pi-Face-Video/video'
    # video_to_image(videoname)


    cv2.destroyAllWindows()

    # print('Starting uploading the files...')
    # myDict = {'ip': '118.163.149.167', 'username': 'videorecorder', 'password': 'ffi001', 'home': '/video/photo/'}
    # print(uploadVideoSFTP(filename, **myDict))
