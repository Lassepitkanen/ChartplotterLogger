import config
import datetime
import os

today = str(datetime.datetime.now().replace(second=0, microsecond=0))

def createFileRepository():
    setDirectoriesToConfig()
    createFolders()

def setDirectoriesToConfig():
    time  = today.replace(":", ".")
    config.csvDir = "data/" + time +"/csv/"
    config.piPictureDir = "data/" + time +"/pi_pictures/"

def createFolders():
    os.makedirs(config.csvDir)
    os.makedirs(config.piPictureDir)
