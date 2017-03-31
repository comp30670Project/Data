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

# create cursor object
cursor = cnx.cursor()

# SQL stuff
DB_NAME = 'dbProject'
TABLES = {}
TABLES['dbProject'] = ("CREATE TABLE `dbProject` (""`dbID` int(11) AUTO_INCREMENT, ""`number` int(11), ""`name` VARCHAR(4),  ""`address` VARCHAR(64), ""`banking` tinyint(1), ""`bonus` tinyint(1), ""`status` tinyint(1), ""`contract_name` VARCHAR(4), ""`bike_stands` INT(3), ""`available_bike_stands` INT(3), ""`available_bikes` INT(3), ""`last_update` char(20), ""`lat` decimal(18,9), ""`lon` decimal(18,9), ""`Weather` VARCHAR(32), ""`Temp` DECIMAL(3,3), ""`TempMin` DECIMAL(3,3), ""`TempMax` DECIMAL(3,3), ""`Pressure` INT(6), ""`Windspeed` DECIMAL(3,3), ""`WindDegree` INT(3), ""`Sunrise` CHAR(20), ""`SunSet` CHAR(20), ""PRIMARY KEY (`dbID`)"") ")

# use DB_NAME
cnx.database = DB_NAME

# create the table
for key, value in TABLES.items():

	try:
		cursor.execute(value)

	except mysql.connector.Error as err:
		pass

# close the cursor and connection
cursor.close()
cnx.close()