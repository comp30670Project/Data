# imports
import sys
import os
import mysql
import mysql.connector
# importing from a local file
newPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'JSON'))
sys.path.append(newPath)
from jsonData import ProjectData


class sqlConfig():

	def __init__(self, configFile):

		# INPUTS
		# configFile: the name of the file containing the sql configuration information

		# Attributes
		self.configFile = configFile

	def sql_configuration_dictionary(self):
		
		theDict = {}
		with open(self.configFile, "r") as f:
			for line in f:
				content = line.strip().split(":")
				theDict[content[0]] = content[1]
		return theDict

# # quick test
# config = sqlConfig("sqlConfig.txt").sql_configuration_dictionary()
# print(config)


class sqlTable():

	def __init__(self, configFile):

		# INPUTS
		# configFile: the name of the file containing the sql configuration information
		# dbCommand: dictionary containing the tuples containing the sql code to create a table
		
		# Attributes
		self.configFile = configFile

	def create(self):

		# configuration dictionary
		config = sqlConfig(configFile).sql_configuration_dictionary()

		# establish the connection
		cnx = mysql.connector.connect(**config)

		# create cursor object
		cursor = cnx.cursor()

		# use database
		cnx.database = config['database']

		# create the table
		dbTable = {}
		dbTable['dbProject'] = ("CREATE TABLE dbProject (""dbID int(11) AUTO_INCREMENT, ""number int(11), ""name VARCHAR(4),  ""address VARCHAR(64), ""banking tinyint(1), ""bonus tinyint(1), ""status tinyint(1), ""contract_name VARCHAR(4), ""bike_stands INT(3), ""available_bike_stands INT(3), ""available_bikes INT(3), ""last_update char(20), ""lat decimal(18,9), ""lon decimal(18,9), ""Weather VARCHAR(32), ""Temp DECIMAL(3,3), ""TempMin DECIMAL(3,3), ""TempMax DECIMAL(3,3), ""Pressure INT(6), ""Windspeed DECIMAL(3,3), ""WindDegree INT(3), ""Sunrise CHAR(20), ""SunSet CHAR(20), ""PRIMARY KEY (dbID)"") ")
		for key, value in dbTable.items():

			try:
				cursor.execute(value)

			except mysql.connector.Error as err:
				pass

		# close the cursor and connection
		cursor.close()
		cnx.close()

	def add_data(self, dataList):

		# INPUT
		# dataList: Python list resulting form jsonData.py

		# configuration dictionary
		config = sqlConfig(configFile).sql_configuration_dictionary()

		# establish the connection
		cnx = mysql.connector.connect(**config)

		# create cursor object
		cursor = cnx.cursor()

		# use dbName
		cnx.database = dbName

		# sql command
		# add_data = (
		# 	"INSERT INTO dbProject"
		# 	"(number, name, address, banking, bonus, status, contract_name, bike_stands, available_bike_stands, available_bikes, last_update, lat, lon, Weather, Temp, TempMin, TempMax, Pressure, WindSpeed, WindDegree, SunRise, SunSet)" 
		# 	"VALUES (%(number)s), %(name)s), %(address)s), %(banking)s), %(bonus)s), %(status)s), %(contract_name)s), %(bike_stands)s), %(available_bike_stands)s), %(available_bikes)s), %(last_update)s), %(lat)s), %(lon)s), %(Weather)s), %(Temp)s), %(TempMin)s), %(TempMax)s), %(Pressure)s), %(WindSpeed)s), %(WindDegree)s), %(SunRise)s), %(SunSet)s)"
		# 	)

		sql = "insert into dbProject(number, name, address, banking, bonus, status, contract_name, bike_stands, available_bike_stands, available_bikes, last_update, lat, lon, Weather, Temp, TempMin, TempMax, Pressure, WindSpeed, WindDegree, SunRise, SunSet) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

		# iterate over items to update
		for d in dataList:
			dv = tuple(d.values())
			cursor.execute(sql, dv)

		# commit the changes
		cnx.commit()

		# close the cursor and connection
		cursor.close()
		cnx.close()

# quick test
configFile = "sqlConfig.txt"
dbName = 'dbProject'
myTable = sqlTable(configFile)
myTable.create()
# myData = [{'number': 83, 'name': 'EMMET ROAD', 'address': 'Emmet Road', 'banking': 0, 'bonus': 0, 'status': 1, 'contract_name': 'Dublin', 'bike_stands': 40, 'available_bike_stands': 40, 'available_bikes': 0, 'last_update': '2017 Apr 03 13:17:09', 'lat': 53.340714, 'lon': -6.308191, 'Weather': 'light rain', 'Temp': 12, 'TempMin': 12, 'TempMax': 12, 'Pressure': 1016, 'WindSpeed': 8.7, 'WindDegree': 200, 'SunRise': '2017 Apr 03 05:52:22', 'SunSet': '2017 Apr 03 19:05:19'}, {'number': 92, 'name': 'HEUSTON BRIDGE (NORTH)', 'address': 'Heuston Bridge (North)', 'banking': 0, 'bonus': 0, 'status': 1, 'contract_name': 'Dublin', 'bike_stands': 40, 'available_bike_stands': 38, 'available_bikes': 2, 'last_update': '2017 Apr 03 13:16:41', 'lat': 53.347802, 'lon': -6.292432, 'Weather': 'light rain', 'Temp': 12, 'TempMin': 12, 'TempMax': 12, 'Pressure': 1016, 'WindSpeed': 8.7, 'WindDegree': 200, 'SunRise': '2017 Apr 03 05:52:16', 'SunSet': '2017 Apr 03 19:05:15'}, {'number': 88, 'name': 'BLACKHALL PLACE', 'address': 'Blackhall Place', 'banking': 0, 'bonus': 0, 'status': 1, 'contract_name': 'Dublin', 'bike_stands': 30, 'available_bike_stands': 30, 'available_bikes': 0, 'last_update': '2017 Apr 03 13:11:08', 'lat': 53.3488, 'lon': -6.281637, 'Weather': 'light rain', 'Temp': 12, 'TempMin': 12, 'TempMax': 12, 'Pressure': 1016, 'WindSpeed': 8.7, 'WindDegree': 200, 'SunRise': '2017 Apr 03 05:52:14', 'SunSet': '2017 Apr 03 19:05:13'}]

apiDB = newPath + "/apiDB.txt"
apiOW = newPath + "/apiOW.txt"
myData = ProjectData(apiDB, apiOW).getData()
myTable.add_data(myData)