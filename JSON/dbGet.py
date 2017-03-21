def dbKey(fileName):
	
	# input: fileName.txt; the file name of the file containing the API key
	# output: Dublin Bikes API key

	# attach API key
	# https://developer.jcdecaux.com/#/opendata/vls?page=getstarted
	with open(fileName, "r") as f: # make af file the contains your api key
		apiKey = f.readline()
		dbKey = "&apiKey=" + apiKey

	# output
	return dbKey


def dbData(fileName):

	# input: filename.txt; the file name of the file containing the API key
	# output: Python dictionary of the Dublin Bikes contract

	# imports
	import json
	import urllib.request

	# url
	api = dbKey(fileName)
	url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin" + api

	# get data
	with urllib.request.urlopen(url) as response:
		stringData = response.read()
		dictData = json.loads(stringData)
	
	# output
	return dictData