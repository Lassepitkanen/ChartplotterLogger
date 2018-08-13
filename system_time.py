import time
import subprocess

def setTimeFromGps(gpsp):
    dateTimeSet = False
    while (dateTimeSet == False):
        print ("Waiting for GPS...")
        time.sleep(5)	
        if gpsp.fix.latitude > 0:
            timeFromGps = gpsp.fix.time
            if isinstance(timeFromGps, basestring): #sometimes GPS returns unix time
                subprocess.Popen(["sudo", "date", "--set", timeFromGps]).communicate()
                dateTimeSet = True	
