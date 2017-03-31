def modify_status(theStatus):
	if theStatus == "OPEN":
		return 1
	else:
		return 0

def modify_boolean(theBoolean):
	if theBoolean == False:
		return 0
	else:
		return 1

def modify_db_last_update(theInt):

	# imports
	from time import gmtime, strftime

	# convert from miliseconds to seconds
	theInt = int(theInt / 1000)

	# convert to human readable time
	theInt = gmtime(theInt)

	# return
	return strftime("%Y %b %d %H:%M:%S", theInt)

# print(modify_db_last_update({'last_update':1490279920000}))


def modify_ow_times(theInt):

	# imports
	from time import gmtime, strftime

	# convert to human readable time
	theInt = gmtime(theInt)

	# return
	return strftime("%Y %b %d %H:%M:%S", theInt)


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

		# modify lat and lon
		lat = d['position']['lat']
		lon = d['position']['lng']
		del d['position']
		d['lat'] = lat
		d['lon'] = lon

		# modify last update
		d['last_update'] = modify_db_last_update(d['last_update'])

		# modify booleans to ints for SQL
		d['banking'] = modify_boolean(d['banking'])
		d['bonus'] = modify_boolean(d['bonus'])

		# modify status into ints for SQL
		d['status'] = modify_status(d['status'])

		# OW 60 calls per minute accomodation
		if count == 60:
			wait = max(0, 60 - (time.time() - start))
			time.sleep(wait)
			count = 0
			start = time.time()

		# count
		count += 1
	
		# Open Weather Data
		weather = ow.owData(owAPI, lat, lon)
		weather['SunRise'] = modify_ow_times(weather['SunRise'])
		weather['SunSet'] = modify_ow_times(weather['SunSet'])

		# combine the data
		for item in weather:
			d[item] = weather[item]

	# output
	return data

thisData = combineData("dbAPI.txt", "owAPI.txt")
for t in thisData:
	print(t)