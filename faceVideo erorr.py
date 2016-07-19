from imutils.piWebStream import WebcamVideoStream

#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import imutils
import time
import cv2
from ftplib import FTP
from engine import detect, preprocessing
from imutils import drawing
import sys


out = cv2.VideoWriter('output.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (640,480))
    

def setCascade(filePath, objType):
    #if objType == 'face':
    #    print "Initialize " + objType + " cascade"
    #    return cv2.CascadeClassifier(filePath)
    #elif objType == 'Mouth':
    #    print "Initialize " + objType + " cascade"
    return cv2.CascadeClassifier(filePath)


def detect(image, cascade, param):
    rects = cascade.detectMultiScale(image,
                                     scaleFactor = param['sf'],
                                     minNeighbors = param['mNbr'],
                                     minSize = param['size'],
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    
   
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def drawRects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


def mouthAlarm(mouthRects, image):
    if len(mouthRects) == 0:
        # Draw no mouth
        cv2.putText(image, "Mouth and Nose Lost!!", (250, 40),
		   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) , 2)
    else:
        # Draw mouth detected
	cv2.putText(image, "Mouth Detect!!", (250, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0) , 2)
    
	
if __name__ == '__main__':
    import sys

    fast = WebcamVideoStream(src=0).start()
    time.sleep(5.0)

    param_face = {'sf':1.1, 'mNbr':5, 'size':(80, 80)}
    param_mouth = {'sf':1.1, 'mNbr':3, 'size':(40, 40)}

    
    #ftp = ftplib.FTP('1.34.62.109')
    #ftp.login('bluekidds','aaa71421')
    #ftp.cwd(')
    #ftp.retrbinary('RETE '+filename, open(filename,'wb').write)
    #ftp.storbinary('STOR '+filename, open(filename,'rb'))
    
    write = True
    while True:
        # grab the frame from camera
        frame = fast.read()

   
        cv2.imshow('face', frame)
        cv2.VideoCapture(-1)
	if cv2.waitKey(5) & 0xFF == ord('p'):
            cv2.imwrite('test.png', frame)
	    ftp = FTP('1.34.62.109')
            ftp.login('bluekidds','aaa71421')
            ftp.cwd('/home/bluekidds/Desktop/Facevideo/')
               
            ftp.retrbinary('STOR test.png', open("test.png", "wb").write)
            f.close()
            print"OK"
            ftp.quit()    

	if cv2.waitKey(5) & 0xFF == ord('r'):
            cv2.imwrite('test1.png', frame)

        if write:
            out.write(frame)

        if 0xFF & cv2.waitKey(5)== ord('q'):
            break

    cv2.destroyAllWindows()
    fast.stop()
    out.release()
