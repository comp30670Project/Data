import json
import urllib.request

# api
apiKey = ""
with open("owAPI.txt", "r") as f: #make a file that contains your api key
	apiKey = f.readline()
owKey = "&appid=" + apiKey

# lat and lon
lat = 35
lon = 139

# url
urlRoot = "http://api.openweathermap.org/data/2.5/weather?"
urlUnits = "units=metric"
urlLat = "&lat=" + str(lat)
urlLon = "&lon=" + str(lon)
url = urlRoot + urlUnits + urlLat + urlLon + owKey

# print out the response
with urllib.request.urlopen(url) as response:
	theResponse = response.read()
	data = json.loads(theResponse)
	print(data)