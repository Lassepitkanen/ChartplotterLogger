import csv
import time
import config
import subprocess
from button import ButtonEvent
from gps_poller import GpsPoller
from file_repository import createFileRepository
from system_time import setTimeFromGps

if __name__ == '__main__':
    gpsp = GpsPoller()
    gpsp.start()
    button = ButtonEvent()

    setTimeFromGps(gpsp)
    createFileRepository()
    button.start()

    try:
        while True:
            with open(config.csvDir + str(time.time()) + ".csv", "w") as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                for x in xrange(0, 1000):
                    unixTime = round(time.time(), 2)
                    subprocess.call(["fswebcam", "-b", "--rotate", "90", "--no-banner", "--jpeg", "90", "--delay", config.mainDelay, "-r", "640x480", config.usbPictureDir + str(unixTime) + ".jpg"])

                    #0.0 waterLevel, 20.0 airtemp, 10.0 watertemp placeholders
                    writer.writerow([unixTime, 0.0, config.buttonState, gpsp.fix.latitude, gpsp.fix.longitude, gpsp.fix.altitude, gpsp.fix.speed, gpsp.fix.track, gpsp.fix.epy, gpsp.fix.epx, gpsp.fix.epv, 20.0, 10.0])
                    config.buttonState = 0
                csvFile.close()
			
    except (KeyboardInterrupt, SystemExit):
        print ("\nTerminating process...")
        csvFile.close()
        gpsp.running = False
        gpsp.join()
        button.join
        print ("Done.\n")
