#setup cron job to feed kitties at 5:30 am and 3:30 pm everyday.
crontab -e
30 5,15 * * * /home/pi/feedKitty.py