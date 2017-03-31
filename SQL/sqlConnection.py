def sqlConfig(theFile):
	theDict = {}
	with open(theFile, "r") as f:
		for line in f:
			content = line.strip().split(":")
			theDict[content[0]] = content[1]
	return theDict

# imports
import mysql.connector

# configuration
config = sqlConfig("sqlConfig.txt")

# establish the connection
cnx = mysql.connector.connect(**config)

# close the connection
cnx.close()


"""
{
'number': 93, 
'name': 'HEUSTON STATION (CENTRAL)', 
'address': 'Heuston Station (Central)', 
'position': {'lat': 53.346603, 'lng': -6.296924}, 
'banking': False, 
'bonus': False, 
'status': 'OPEN', 
'contract_name': 'Dublin', 
'bike_stands': 40, 
'available_bike_stands': 40, 
'available_bikes': 0, 
'last_update': 1490279920000, 
'ow': 
	{
	'coord': 
		{
		'lon': -6.29, 
		'lat': 53.34
		}, 
	'weather': 
		[
			{
			'id': 803, 
			'main': 'Clouds', 
			'description': 'broken clouds', 
			'icon': '04d'
			}
		], 
	'base': 'stations', 
	'main': 
		{
		'temp': 8.51, 
		'pressure': 1022, 
		'humidity': 81, 
		'temp_min': 8, 
		'temp_max': 9
		}, 
	'visibility': 10000, 
	'wind': 
		{
		'speed': 7.7, 
		'deg': 40
		}, 
	'clouds': 
		{
		'all': 75
		}, 
	'dt': 1490277600, 
	'sys': 
		{
		'type': 1, 
		'id': 5237, 
		'message': 0.0931, 
		'country': 'IE', 
		'sunrise': 1490249918, 
		'sunset': 1490294722
		}, 
	'id': 6691018, 
	'name': 'Maryland', 
	'cod': 200
	}
}
"""