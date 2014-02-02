#!/usr/bin/python
# Servo Control
# This requires Adafruit Occidentalis v0.2 with the rpi-pwm kernal module installed.
# At this time it will not work with regular "Whezzy Distro" 
# At this time Occidentalis v0.2 does not support the Pi Camera module so I had to break this script into two parts
# and use two Raspberry Pi, one for the servo and one for the camera.
# Rumor has it Occidentalis v0.3 will support the camera

import os
import time
import smtplib
import subprocess
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

# Use your own info here
USERNAME = "yourEmail@gmail.com"
PASSWORD = "password"
MAILTO = "sendtoEmail@gmail.com"

def takePicture():
	subprocess.call(['/home/pi/takePicture'])

def sendEmail(to, subject, text, files=[]):
        assert type(to)==list
        assert type(files)==list

        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach( MIMEText(text) )

        for file in files:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(file, "rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(file))
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo_or_helo_if_needed()
                server.starttls()
                server.ehlo_or_helo_if_needed()
                server.login(USERNAME,PASSWORD)
                server.sendmail(USERNAME, MAILTO, msg.as_string())
                server.quit()

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
print("Sending Email")
time.sleep(5)

takePicture()
sendEmail( ["sendtoEmail@gmail.com"],
	"Cat Feeder Message",
	"The Kitties have been fed.",
	["/home/pi/Images/" +  str(commands.getoutput("/home/pi/currentPicture"))] )