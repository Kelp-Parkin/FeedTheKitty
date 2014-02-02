#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
# This reports that there is no initial param
#GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

# Turn on lamp
GPIO.output(7, GPIO.HIGH)

# Turn off lamp
GPIO.output(7, GPIO.LOW)

# Cleanup
# This reports there is no cleanup method
#GPIO.cleanup()

def lampControl(state) :
	if state == 'on' :
		GPIO.output(7, GPIO.HIGH)
	else : GPIO.output(7, GPIO.LOW)
