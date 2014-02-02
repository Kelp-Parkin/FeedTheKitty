#!/bin/bash
## Script to return the latest picture name.

cd /home/pi/Images
echo `ls -1 -t | grep jpg | tr -d ' ' | tr -d '\t' | head -n1`