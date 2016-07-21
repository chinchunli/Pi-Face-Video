#from imutils.piWebStream import WebcamVideoStream
from piWebStream import WebcamVideoStream
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import imutils
import time
import cv2
from ftplib import FTP

from datetime import date
import sys


#out = cv2.VideoWriter('output.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (640,480))
    

FPS = 15
PI_ID = 'FF1'   # ID of Device
TOTAL_SECONDS = 648000  # Change to 30s for test

if __name__ == '__main__':
    
    today = date.today()
    filename=PI_ID + '_' + str(today.month) + '_' + str(today.day) + '_' + str(today.year) +'mp4v'
    fast = WebcamVideoStream(src=0, resolution=(640, 480)).start()
    time.sleep(5.0)

    print('Start Setting writer')
    fast.setWriter(filename)
    if fast.writer is None:
        print('writer Fail')
    else:
        print('writer successfully set')
    #ftp = ftplib.FTP('1.34.62.109')
    #ftp.login('bluekidds','aaa71421')
    #ftp.cwd(')
    #ftp.retrbinary('RETE '+filename, open(filename,'wb').write)
    #ftp.storbinary('STOR '+filename, open(filename,'rb'))
    
    
    for _ in xrange(TOTAL_SECONDS):
        
        for i in xrange(FPS):
            frame = fast.read()
        fast.write(frame)
	

    cv2.destroyAllWindows()
    fast.stop()
    fast.release()
    
