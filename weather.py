#!/usr/bin/python

import json
import requests

# Get IP Address

url = 'http://curlmyip.com'
ip = requests.get(url)
ip = ip.text.rstrip()
print ip

# Get Zip Code and City

f = open('code1.txt', 'r') #read in personal wunderground api code
code1 = f.readline()
code1 = code1.rstrip() #remove newline at end of string
f.close()

url = 'http://api.ipinfodb.com/v3/ip-city/?key='+code1+'&format=json&ip='+ip
response = requests.get(url)
data = json.loads(response.text)

zipcode = data['zipCode']
city = data['cityName']
print zipcode
print city

# Get Current Weather

f = open('code2.txt', 'r') #read in personal wunderground api code
code2 = f.readline()
code2 = code2.rstrip() #remove newline at end of string
f.close()

url = 'http://api.wunderground.com/api/'+code2+'/conditions/q/'+zipcode+'.json'

response = requests.get(url)
data = json.loads(response.text)

tempnow = data['current_observation']['temp_f']
condnow = data['current_observation']['weather']

print tempnow
print condnow

# Get Weather Forecast

url = 'http://api.wunderground.com/api/'+code2+'/forecast10day/q/'+zipcode+'.json'

response = requests.get(url)
data = json.loads(response.text)

day1 = data['forecast']['simpleforecast']['forecastday'][0]['date']['weekday_short']
day2 = data['forecast']['simpleforecast']['forecastday'][1]['date']['weekday_short']
day3 = data['forecast']['simpleforecast']['forecastday'][2]['date']['weekday_short']
day4 = data['forecast']['simpleforecast']['forecastday'][3]['date']['weekday_short']
day5 = data['forecast']['simpleforecast']['forecastday'][4]['date']['weekday_short']

cond1 = data['forecast']['simpleforecast']['forecastday'][0]['conditions']
cond2 = data['forecast']['simpleforecast']['forecastday'][1]['conditions']
cond3 = data['forecast']['simpleforecast']['forecastday'][2]['conditions']
cond4 = data['forecast']['simpleforecast']['forecastday'][3]['conditions']
cond5 = data['forecast']['simpleforecast']['forecastday'][4]['conditions']

temphigh1 = data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
temphigh2 = data['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
temphigh3 = data['forecast']['simpleforecast']['forecastday'][2]['high']['fahrenheit']
temphigh4 = data['forecast']['simpleforecast']['forecastday'][3]['high']['fahrenheit']
temphigh5 = data['forecast']['simpleforecast']['forecastday'][4]['high']['fahrenheit']

templow1 = data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
templow2 = data['forecast']['simpleforecast']['forecastday'][1]['low']['fahrenheit']
templow3 = data['forecast']['simpleforecast']['forecastday'][2]['low']['fahrenheit']
templow4 = data['forecast']['simpleforecast']['forecastday'][3]['low']['fahrenheit']
templow5 = data['forecast']['simpleforecast']['forecastday'][4]['low']['fahrenheit']

print day1
print cond1
print temphigh1
print templow1
