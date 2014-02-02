#!/usr/bin/python
# Servo Control
# This requires Adafruit Occidentalis v0.2 with the rpi-pwm kernal module installed.
# At this time it will not work with regular "Whezzy Distro" 
# At this time Occidentalis v0.2 does not support the Pi Camera module so I had to break this script into two parts
# and use two Raspberry Pi, one for the servo and one for the camera.
# Rumor has it Occidentalis v0.3 will support the camera

import time

def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()	
	except:
		print("Error writing to: " + property + " value: " + value)


def setServo(angle):
	set("servo", str(angle))
	
		
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

feedTime = 25
stillPoint = 90

setServo(0)
time.sleep(.6)
setServo(179)
print("Servo turning feed screw for " + str(feedTime) + " seconds")
time.sleep(feedTime)
setServo(stillPoint)
print("Servo stopped")