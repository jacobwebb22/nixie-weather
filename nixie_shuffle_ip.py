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

def checkval(val)
	if val == 10:
		val = 0
	return val
	
def WriteList(listval):
	
	sa = listval[0]<<4
	sb = listval[1]
	s1 = sa+sb
	
	sa = listval[2]<<4
	sb = listval[3]
	s1 = sa+sb
	
	sa = listval[4]<<4
	sb = listval[5]
	s1 = sa+sb
	
	sa = listval[6]<<4
	sb = listval[7]
	s1 = sa+sb
	
	sa = listval[8]<<4
	sb = listval[9]
	s1 = sa+sb

	spi.writebytes([s1, s2, s3, s4, s5])
	
	return

def WriteMonte()
	listout = [0,1,2,3,4,5,6,7,8,9]
	holder = 0
	for i in range(0, 210):
		WriteList(listout)
		time.sleep(0.3)
		holder = listout[0]
		listout[0] = listout[1]
		listout[1] = listout[2]
		listout[2] = listout[3]
		listout[3] = listout[4]
		listout[4] = listout[5]
		listout[5] = listout[6]
		listout[6] = listout[7]
		listout[7] = listout[8]
		listout[8] = listout[9]
		listout[9] = holder
	return


#####################################################
############# -----  Run Infinite Loop -------#######
#####################################################
### Every two hours run Montecarlo Deburn ###########

while 1 : 
	WriteNixie()
	time.sleep(0.2)
	currentnow = datetime.datetime.now()
	if currentnow.hour%2 == 0 and currentnow.minute/10 == 0 and currentnow.minute%10 == 1:
		WriteMonte()
		









