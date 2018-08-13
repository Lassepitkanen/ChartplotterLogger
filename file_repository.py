import config
import datetime
import os

today = str(datetime.datetime.now().replace(second=0, microsecond=0))

def createFileRepository():
    setDirectoriesToConfig()
    createFolders()	
	
def setDirectoriesToConfig():
    config.csvDir = "data/" + today +"/csv/"
    config.usbPictureDir = "data/" + today +"/usb_pictures/"

def createFolders():
    os.makedirs(config.csvDir)
    os.makedirs(config.usbPictureDir)