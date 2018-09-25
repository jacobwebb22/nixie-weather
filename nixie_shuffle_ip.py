#!/usr/bin/python

import serial
import time
import datetime
import spidev

# Initialize SPI Interface

spi = spidev.SpiDev()
spi.open(0,0)

# Setup Serial Port to interface with serial to lcd converter board

port = serial.Serial("/dev/ttyAMA0", baudrate = 9600)

#####################################################
########## -----  Declare LCD Functions-------#######
#####################################################

# Set screen type to 16x2

#port.write(b'\x7C\x04')
#time.sleep(0.5)
#port.write(b'\x7C\x06')
#time.sleep(0.5)

def SelectLineOne():
    port.write(b'\xFE\x80')
    time.sleep(0.005)
    return

def SelectLineTwo():
    port.write(b'\xFE\xC0')
    time.sleep(0.005)
    return

def ClearScreen():
    port.write(b'\xFE\x01')
    time.sleep(0.005)
    return

def SetScreenBacklightHigh(): # From 1 to 30
    port.write(b'\x7C\x94')
    time.sleep(0.05)
    return

def SetScreenBacklightLow(): # From 1 to 30
    port.write(b'\x7C\x80')
    time.sleep(0.05)
    return

def WriteLine( line ):
    port.write(line)
    return

def WriteLines(line1, line2):
    SelectLineOne()
    port.write(line1)
    time.sleep(0.005)
    SelectLineTwo()
    port.write(line2)
    time.sleep(0.005)
    return

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
	
def WriteList(startval):
	
	sa = startval<<4
	sb = startval+1
	sb = checkval(sb)
	s1 = sa+sb
	startval = sb+1
	startval = checkval(startval)
	
	sa = startval<<4
	sb = startval+1
	sb = checkval(sb)
	s2 = sa+sb
	startval = sb+1
	startval = checkval(startval)
	
	sa = startval<<4
	sb = startval+1
	sb = checkval(sb)
	s3 = sa+sb
	startval = sb+1
	startval = checkval(startval)
	
	sa = startval<<4
	sb = startval+1
	sb = checkval(sb)
	s4 = sa+sb
	startval = sb+1
	startval = checkval(startval)
	
	sa = startval<<4
	sb = startval+1
	sb = checkval(sb)
	s5 = sa+sb
	startval = sb+1
	startval = checkval(startval)

	spi.writebytes([s1, s2, s3, s4, s5])
	
	return

def WriteMonte()
	for i in range(0, 100):
		WriteList(i)
		time.sleep(0.3)
	return


#####################################################
############# -----  Run Infinite Loop -------#######
#####################################################


while 1 : 
	WriteNixie()
	time.sleep(0.2)
	currentnow = datetime.datetime.now()
	if currentnow.hour%2 == 0
		WriteMonte()









