import threading
from gps import *

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.running = False
    
    def run(self):
        self.running = True
        while self.running:
            self.gpsd.next()

    def stopController(self):
        self.running = False
  
    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc
