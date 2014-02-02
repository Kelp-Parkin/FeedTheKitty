#!/usr/bin/python
# Servo Control
# This requires Adafruit Occidentalis v0.2 with the rpi-pwm kernal module installed.
# At this time it will not work with regular "Whezzy Distro" 

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
set("servo_max", "170")
set("active", "1")

delay_period = 0.01

while True:
	for angle in range(0, 170):
		setServo(angle)
		print("Angle set to " + str(angle))
		time.sleep(delay_period)
	for angle in range(0, 170):
		setServo(170 - angle)
		print("Angle set to " + str(170 - angle))
		time.sleep(delay_period)