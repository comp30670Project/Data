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
	
	return dictData