#!/bin/bash

## Script to take a picture and name it with time stamp


## Function to keep the Images folder from filling up with pictures
## This example limits the folder to the newest 4 .JPGs

CleanUp(){
    if [ `pwd` = '/home/pi/Images' ]
        then while [ "$(ls -1 | grep jpg | wc -l | tr -d ' ' | tr -d '\t')"  -gt 4 ]
                 do 
                     ls -1 -t | grep jpg | tail -n1 | xargs rm -f 
                 done 
    fi
}

## Main - Pull Datestamp, take picture and name it with Datestamp, clean up old pictures

NAME=`date +%Y_%m_%d_%H-%M`
raspistill -q 25 -o Images/"$NAME".jpg
cd /home/pi/Images
sleep 1m
CleanUp
cd ~/