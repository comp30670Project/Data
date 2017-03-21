# # imports
# import dbGet as db
# import owGet as ow

# myData = db.dbData("dbAPI.txt")

# import time

# for d in myData:
	
# 	# latitude and longitude
# 	lat = d['position']['lat']
# 	lon = d['position']['lng']
	
# 	# Open Weather Data
# 	myWeather = ow.owData("owAPI.txt", lat, lon)
# 	time.sleep(1) # Open Weather only allows 60 calls per minute; making sure we adhere to this limit

# 	# combine the data
# 	d['ow'] = myWeather
# 	print(d)

def combineData(dbAPI, owAPI):

	# imports
	import time
	import dbGet as db
	import owGet as ow

	# get dbData
	data = db.dbData(dbAPI)

	# combine the data
	count = 0
	start = time.time()
	for d in data:

		# OW 60 calls per minute accomodation
		if count == 60:
			wait = max(0, 60 - (time.time() - start))
			time.sleep(wait)
			count = 0
			start = time.time()

		# count
		count += 1

		# latitude and longitude
		lat = d['position']['lat']
		lon = d['position']['lng']
	
		# Open Weather Data
		weather = ow.owData(owAPI, lat, lon)

		# combine the data
		d['ow'] = weather

combineData("dbAPI.txt", "owAPI.txt")