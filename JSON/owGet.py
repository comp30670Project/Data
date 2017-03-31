def owID(fileName):
	
	# input: fileName.txt; the file name of the file containing the API ID
	# output: Open Weather API key

	# attach API key
	with open(fileName, "r") as f: # make af file the contains your api key
		apiID = f.readline()
		owID = "&appid=" + apiID

	# output
	return owID


def owData(fileName, lat, lon):

	# imports
	import json
	import urllib.request

	# # latitute and longitute
	# lat = 35
	# lon = 139

	# url
	urlRoot = "http://api.openweathermap.org/data/2.5/weather?"
	urlUnits = "units=metric"
	urlLat = "&lat=" + str(lat)
	urlLon = "&lon=" + str(lon)
	api = owID(fileName)
	url = urlRoot + urlUnits + urlLat + urlLon + api

	# get data
	with urllib.request.urlopen(url) as response:
		stringData = response.read()
		dictData = json.loads(stringData)

	# parse data
	# collect data from ow
	ow_weather = dictData['weather'][0] # dictionary object
	ow_main = dictData['main'] # dict object
	ow_wind = dictData['wind'] # dict object
	ow_sys = dictData['sys'] # dict object


	ow = {}
	ow['Weather'] = ow_weather['description']
	ow['Temp'] = ow_main['temp']
	ow['TempMin'] = ow_main['temp_min']
	ow['TempMax'] = ow_main['temp_max']
	ow['Pressure'] = ow_main['pressure']
	ow['WindSpeed'] = ow_wind['speed']
	ow['WindDegree'] = ow_wind['deg']
	ow['SunRise'] = ow_sys['sunrise']
	ow['SunSet'] = ow_sys['sunset']
	
	return ow

# myThing = owData("owAPI.txt", 1, 5)
# for d in myThing:
# 	print(d, myThing[d])