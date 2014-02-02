# Email when Kitties are fed

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Change to your own account information ========
to = 'sendtoEmail@gmail.com'
gmail_user = 'yourEmail@gmail.com'
gmail_password = 'password'
# ===============================================

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

msg = MIMEText('Kitties are fed at %s' % today.strftime('%b %d %Y')
msg['Subject'] = 'Cat Feeder Message'
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()