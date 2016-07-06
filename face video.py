import os
import datetime
import time
from threading import Thread

def picFunc():
    os.system("fswebcam -d /dev/video0 -r 1280x1080 pi/Prictures/%/s.png" %datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"))

t=5          #initialise the pause between pitures in second
count=30     #initialise the number of pictures to be taken
i=1          #initialise (reset) the counting sequence
totalTime=(t*count)
             #calculate the time in seconds
             #Take a series of pictures one every t seconds

while(i<=count):
    #initialise variables
    leftTimeH=0
    leftTimeM=0
    leftTimeS=0
    # taking a picture by calling a command line prompt
    x=Thread(target=picFunc)
    totalTime=(t*(count-i))
    #calculate the time in seconds
    print (i)#print the current count value to show progress

    while (totalTime>=3600):
        leftTimeH=leftTimeH+1
        totalTime=totalTime-60
    leftTimeS=totalTime
    percentDone=((i/count)*100)
    percentDone=round(percentDone,2)
    massage1=("Time left to finish " +repr(leftTimeH) +" Hours" +repr(leftTimeM) +"minutes and " +repr(leftTimeS) +"Seconds")
    massage2=(""+repr(percentDone) + "%Completed!")
    print(massage1)
    print(massage2)
    i=i+1
    if (i>count):   #leave the loop when count fulfilled (not really necessary)
        break
    time.sleep(t)   #wait the defined time t(s) between pictures
print ("Finished!") #print to show when finished
