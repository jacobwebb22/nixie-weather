#!/usr/bin/python

import serial
import time
import datetime
import spidev

# Initialize SPI Interface

spi = spidev.SpiDev()
spi.open(0,0)

#####################################################
########## -----  Nixie Print Function -------#######
#####################################################

def WriteNixie():
	
    current = datetime.datetime.now()
	
    one=current.second%10
    two=current.second/10
    one = one<<4

    seconds = one + two

    one=current.minute%10
    two=current.minute/10
    one = one<<4

    minutes = one + two

    houradjust = current.hour
    if houradjust == 0:
        houradjust = 12
    if houradjust > 12:
        houradjust = houradjust - 12

    one=houradjust%10
    two=houradjust/10
    one = one<<4

    hours = one + two

    one=current.month%10
    two=current.month/10
    one = one<<4

    months = one + two

    one=current.day%10
    two=current.day/10
    one = one<<4

    days = one + two
	
    spi.writebytes([days, months, seconds, minutes, hours])

    return

while 1 : 
    WriteNixie()
    time.sleep(0.2)
