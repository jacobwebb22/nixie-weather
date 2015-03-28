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

url = 'http://api.wunderground.com/api/'+code2+'/forecast/q/'+zipcode+'.json'

response = requests.get(url)
data = json.loads(response.text)

#day
#cond
#templow
#temphigh

day1 = data['forecast']['simpleforecast']['forecastday'][2]['conditions']

