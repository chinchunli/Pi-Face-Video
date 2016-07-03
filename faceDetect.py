from imutils.piWebStream import WebcamVideoStream

#from picamera.array import PiRGBArray
#from picamera import PiCamera
import argparse
import imutils
import time
import cv2

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
    time.sleep(2.0)

    faceCascade = setCascade('cascade/haarcascade_frontalface_alt.xml', 'face')
    profileCascade = setCascade('cascade/haarcascade_profileface.xml', 'face')
    mouthCascade = setCascade('cascade/haarcascade_mcs_mouth.xml', 'mouth')
    #mouthCascade = setCascade('cascade/mouth.xml', 'mouth')
    #mouthCascade = cv2.CascadeClassifier('cascade/haarcascade_mcs_mouth.xml')

    param_face = {'sf':1.1, 'mNbr':5, 'size':(80, 80)}
    param_mouth = {'sf':1.1, 'mNbr':3, 'size':(40, 40)}
    while True:
        # grab the frame from camera
        frame = fast.read()

        # initialize for faceDetect module
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#gray_equal = cv2.equalizeHist(gray)
        faceRects = detect(gray, faceCascade, param_face)
	if len(faceRects) == 0:
	    faceRects = detect(gray, profileCascade, param_face)
        if len(faceRects) > 0 :
            drawRects(frame, faceRects, (0, 255, 0))
            for x1, y1, x2, y2 in faceRects:
                roi = gray[(y1+y2)/2:y2, x1:x2]
                frame_roi = frame[(y1+y2)/2:y2, x1:x2]
                mouthRects = detect(roi, mouthCascade, param_mouth)				
                
		if len(mouthRects) > 0:
		    drawRects(frame_roi, mouthRects, (0, 0, 255))
		
		mouthAlarm(mouthRects, frame)
            #mouths = detect()
        #else :
        #    profileRects = detect(gray, profileCascade)
        #    if len(profileRects) > 0:
        #        drawRects(frame, profileRects, (0, 255, 0))

        cv2.imshow('face', frame)
	if cv2.waitKey(5) & 0xFF == ord('p'):
	    cv2.imwrite('test.png', frame)

	if cv2.waitKey(5) & 0xFF == ord('r'):
            cv2.imwrite('test1.png', frame)

        if 0xFF & cv2.waitKey(5)== ord('q'):
            break

    cv2.destroyAllWindows()
    fast.stop()

