#!/usr/bin/python

import json
#import requests
import serial
import time
import datetime
import RPi.GPIO as GPIO
import spidev

# Initialize SPI Interface

spi = spidev.SpiDev()
spi.open(0,0)

# Initialize GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup Serial Port to interface with serial to lcd converter board

port = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 0.1)

#####################################################
########## -----  Declare LCD Functions-------#######
#####################################################

def SelectLineOne():
    port.write(b'\xfe')
    time.sleep(0.15)
    port.write(b'\x80')
    time.sleep(0.15)
    return

def SelectLineTwo():
    port.write(b'\xfe')
    time.sleep(0.15)
    port.write(b'\xc0')
    time.sleep(0.15)
    return

def ClearScreen():
    port.write(b'\xfe')
    time.sleep(0.15)
    port.write(b'\x01')
    time.sleep(0.15)
    return

def SetScreenBacklight(brightness): # From 1 to 30

    port.write(b'\x7c')
    time.sleep(0.15)
    out = 127+brightness
    port.write(b'\x93')
    time.sleep(0.15)
    return

def WriteLine( line ):
    port.write(line)
    return

def WriteLines(line1, line2):
    ClearScreen()
    SelectLineOne()
    port.write(line1)
    time.sleep(0.15)
    SelectLineTwo()
    port.write(line2)
    time.sleep(0.15)
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

#####################################################
########## -----  Initiate Weather Data -------#######
#####################################################

# Get IP Address

#url = 'http://curlmyip.com'
#ip = requests.get(url)
#ip = ip.text.rstrip()
#print ip

# Get Zip Code and City

#f = open('code1.txt', 'r') #read in personal wunderground api code
#code1 = f.readline()
#code1 = code1.rstrip() #remove newline at end of string
#f.close()

#url = 'http://api.ipinfodb.com/v3/ip-city/?key='+code1+'&format=json&ip='+ip
#response = requests.get(url)
#data = json.loads(response.text)

#zipcode = data['zipCode']
#city = data['cityName']
#print zipcode
#print city

# Get Current Weather

#f = open('code2.txt', 'r') #read in personal wunderground api code
#code2 = f.readline()
#code2 = code2.rstrip() #remove newline at end of string
#f.close()

#urlnow = 'http://api.wunderground.com/api/'+code2+'/conditions/q/'+zipcode+'.json'
#urlfuture = 'http://api.wunderground.com/api/'+code2+'/forecast10day/q/'+zipcode+'.json'

#####################################################
############# -----  Run Infinite Loop -------#######
#####################################################

def PrintWeather():

	
    SetScreenBacklight(20)
    ClearScreen()
    WriteLine('    UPDATING    ')


    while GPIO.input(18) :
	
		# Get Weather Forecast

	#	response = requests.get(urlnow)
	#	data = json.loads(response.text)

	#	tempnow = data['current_observation']['temp_f']
	#	condnow = data['current_observation']['weather']

		#print tempnow
		#print condnow

	#	response = requests.get(urlfuture)
	#	data = json.loads(response.text)

	#	day1 = data['forecast']['simpleforecast']['forecastday'][0]['date']['weekday_short']
	#	day2 = data['forecast']['simpleforecast']['forecastday'][1]['date']['weekday_short']
	#	day3 = data['forecast']['simpleforecast']['forecastday'][2]['date']['weekday_short']
	#	day4 = data['forecast']['simpleforecast']['forecastday'][3]['date']['weekday_short']
	#	day5 = data['forecast']['simpleforecast']['forecastday'][4]['date']['weekday_short']

	#	cond1 = data['forecast']['simpleforecast']['forecastday'][0]['conditions']
	#	cond2 = data['forecast']['simpleforecast']['forecastday'][1]['conditions']
	#	cond3 = data['forecast']['simpleforecast']['forecastday'][2]['conditions']
	#	cond4 = data['forecast']['simpleforecast']['forecastday'][3]['conditions']
	#	cond5 = data['forecast']['simpleforecast']['forecastday'][4]['conditions']

	#	temphigh1 = data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
	#	temphigh2 = data['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
	#	temphigh3 = data['forecast']['simpleforecast']['forecastday'][2]['high']['fahrenheit']
	#	temphigh4 = data['forecast']['simpleforecast']['forecastday'][3]['high']['fahrenheit']
	#	temphigh5 = data['forecast']['simpleforecast']['forecastday'][4]['high']['fahrenheit']

	#	templow1 = data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
	#	templow2 = data['forecast']['simpleforecast']['forecastday'][1]['low']['fahrenheit']
	#	templow3 = data['forecast']['simpleforecast']['forecastday'][2]['low']['fahrenheit']
	#	templow4 = data['forecast']['simpleforecast']['forecastday'][3]['low']['fahrenheit']
	#	templow5 = data['forecast']['simpleforecast']['forecastday'][4]['low']['fahrenheit']

		# Display Loop Through Forecast Days

     SetScreenBacklight(0)		
     return

#####################################################
############# -----  Run Infinite Loop -------#######
#####################################################

SetScreenBacklight(20)
ClearScreen()
WriteLine('    UPDATING    ')


while 1 : 
    WriteNixie()

#	if GPIO.input(18):
#		if millis%10 == 1
#			printcondnow()
#		if millis%10 == 2
#			printcond1()
#		if millis%10 == 3
#			printcond2()
#		if millis%10 == 4
#			printcond3()


    time.sleep(0.1)









