import csv
import picamera
import time
import config
import subprocess
import multiprocessing
import sys
from button import ButtonEvent
from gps_poller import GpsPoller
from file_repository import createFileRepository
from system_time import setTimeFromGps


sys.path.append('./server')
from server_app import ServerApp

if __name__ == '__main__':
    gpsp = GpsPoller()
    button = ButtonEvent()
    server = ServerApp(gpsp)

    gpsp.start()
    setTimeFromGps(gpsp)

    camera = picamera.PiCamera()

    createFileRepository()
    camera.resolution = (640, 480)

    button.start()
    server.start()

    try:
        while True:
            with open(config.csvDir + str(time.time()) + ".csv", "w") as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                for x in xrange(0, 1000):
                    time.sleep(config.mainDelay)
                    unixTime = round(time.time(), 2)

                    #0.0 waterLevel, 20.0 airtemp, 10.0 watertemp
                    writer.writerow([unixTime, 0.0, config.buttonState, gpsp.fix.latitude, gpsp.fix.longitude, gpsp.fix.altitude, gpsp.fix.speed, gpsp.fix.track, gpsp.fix.epy, gpsp.fix.epx, gpsp.fix.epv, 20.0, 10.0])
                    config.buttonState = 0
                    camera.capture(config.piPictureDir + str(unixTime) + ".jpeg", format="jpeg")
                csvFile.close()

    except (KeyboardInterrupt, SystemExit):
        print ("\nTerminating process...")
        csvFile.close()
        camera.close()
        server.stop()
        gpsp.running = False
        gpsp.join()
        button.join()
        server.join()
        print ("Done.\n")