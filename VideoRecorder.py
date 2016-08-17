#from imutils.piWebStream import WebcamVideoStream
from vidUtil.piWebStream import WebcamVideoStream
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import time
import cv2
from ftplib import FTP

from datetime import date
import sys
from connection.mySFTP import uploadVideoSFTP

import os

#out = cv2.VideoWriter('output.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (640,480))
    

FPS = 10
PI_ID = 'FF5'   # ID of Device
TOTAL_FRAMES =  12000 # Change to 30s for test
TOTAL_SEC = 120

if __name__ == '__main__':
   
    #today = date.today()
    date_string = time.strftime("%Y-%m-%d-%H:%M")
    #filename = PI_ID + '_' + str(today.month) + '_' + str(today.day) + '_' + str(today.year) + '.mkv'
    filename = PI_ID + '_' + date_string + '.mkv'
    
    fast = WebcamVideoStream(src=0, resolution=(1280, 960)).start()
    
    time.sleep(5.0)

    print('Start Setting writer')
    

    
    
    #print(width, height)
    #fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
    fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
    writer = cv2.VideoWriter(filename, fourcc, 20.0, (fast.width, fast.height))
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
    start = time.time()
   
    query = 0
    current = time.time()
    while True:
	

	used = time.time() - start
	if int(used) > TOTAL_SEC:
            break
            
     
        if (time.time() - current) > (FPS/ 20.0):
            if (query % 500) == 0:
	        print(query, used)
	    frame = fast.read()
            writer.write(frame)
	    query = fast.frame_num
	    
            current = time.time()
                 
    print(time.time()-start)
    fast.stop()
    print('Camera release..')
    cv2.destroyAllWindows()
    #fast.release()
    print('Writer release..')
    writer.release()

    print('Starting uploading the files...')
    
    myDict = {'ip': '1.34.62.109', 'username' : 'guest', 'password' : 'guest', 
	      'home': '/home/guest/knightVideo/'}    

    print(uploadVideoSFTP(filename, **myDict))

    os.system("shutdown -r now")
