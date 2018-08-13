import RPi.GPIO as GPIO
import threading
import config

class ButtonEvent(threading.Thread):
    pin = 33

    def button_callback(self):
	    config.buttonState = 1

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin,GPIO.FALLING,callback=button_callback, bouncetime=200)
