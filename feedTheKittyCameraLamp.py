#!/usr/bin/python
# Lamp Control + Camera Control + Email

import os
import time
import smtplib
import commands
import subprocess
import RPi.GPIO as GPIO
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

# Use your own info here
USERNAME = "yourEmail@gmail.com"
PASSWORD = "password"
MAILTO = "sendtoEmail@gmail.com"

def lampControl(state):
	if state == 'on' :	
		GPIO.output(7, GPIO.HIGH)
	else :  GPIO.output(7, GPIO.LOW)

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
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
lampControl('on')

takePicture()

lampControl('off')
#GPIO.cleanup()

# Should make it use MAILTO variable, haven't tested that yet
sendEmail( ["sendtoEmail@gmail.com"],
	"Cat Feeder Message",
	"The Kitties have been fed.",
	["/home/pi/Images/" +  str(commands.getoutput("/home/pi/currentPicture"))] )