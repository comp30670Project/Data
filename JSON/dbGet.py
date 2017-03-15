import json
import urllib.request

# get the api
apiKey = ""
with open("dbAPI.txt", "r") as f: # make af file the contains your api key
	apiKey = f.readline()
# dbKey
dbKey = "&apiKey=" + apiKey

# get the station data for Dublin
url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin" + dbKey
with urllib.request.urlopen(url) as response:
	theResponse = response.read()
	data = json.loads(theResponse)
	for d in data:
		print(d)