import json, requests,sys
# computer location from the command line

if len(sys.argv) < 2:
    print('Usage: checkWeather.py location ')
    sys.exit()
location= ''.join(sys.argv[1:])

#TODO: Download the JSON date from Openweather
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=3d362ed051daf6d4dd04b8a90ccc9116' %(location)
#url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=7&APPID=3d362ed051daf6d4dd04b8a90ccc9116' %(location)
response = requests.get(url)
response.raise_for_status()

# TODO: Load JSON data into a Python variable

weatherDate = json.load(response.text)
w = weatherDate['list']

