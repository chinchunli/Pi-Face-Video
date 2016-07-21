#from imutils.piWebStream import WebcamVideoStream
from piWebStream import WebcamVideoStream
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import time
import cv2
from ftplib import FTP

from datetime import date
import sys


#out = cv2.VideoWriter('output.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (640,480))
    

FPS = 15
PI_ID = 'FF1'   # ID of Device
TOTAL_SECONDS = 300  # Change to 30s for test

if __name__ == '__main__':
    
    today = date.today()
    filename = PI_ID + '_' + str(today.month) + '_' + str(today.day) + '_' + str(today.year) + '.avi'
    
    
    fast = WebcamVideoStream(src=0, resolution=(640, 480)).start()
    time.sleep(5.0)

    print('Start Setting writer')
    fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
    
    writer = cv2.VideoWriter(filename, fourcc, 15.0, (640, 480))
    #fast.setWriter(filename)
    if writer is None:
        print('writer Fail')
    else:
        print('writer successfully set')
    #ftp = ftplib.FTP('1.34.62.109')
    #ftp.login('bluekidds','aaa71421')
    #ftp.cwd(')
    #ftp.retrbinary('RETE '+filename, open(filename,'wb').write)
    #ftp.storbinary('STOR '+filename, open(filename,'rb'))
    
    print('Start Recording...')
    for _ in xrange(TOTAL_SECONDS):
        
        for i in xrange(FPS):
            frame = fast.read()
        
        writer.write(frame)
	
    fast.stop()
    print('Camera release..')
    fast.release()
    print('Writer release..')
    writer.release()
    cv2.destroyAllWindows()
