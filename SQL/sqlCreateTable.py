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
TABLES['dbProject'] = ("CREATE TABLE `dbProject` (""`number` int(11) NOT NULL, ""PRIMARY KEY (`number`)"") ")

TABLES['dbProject'] = (
    "  CREATE TABLE `dbProject` ("
    "  `number` int(11) NOT NULL,"
    "	`name` varchar(4)"
    "	`address` varchar(64)"
    " `banking` tinyint(1)"


    "  `emp_no` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

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

"""
{
	'number': 88, 
	'name': 'BLACKHALL PLACE', 
	'address': 'Blackhall Place', 
	'banking': False, 
	'bonus': False, 
	'status': 'OPEN', 
	'contract_name': 'Dublin', 
	'bike_stands': 30, 
	'available_bike_stands': 29, 
	'available_bikes': 1, 
	'last_update': '2017 Mar 31 09:59:51', 
	'lat': 53.3488, 
	'lon': -6.281637, 
	'Weather': 'few clouds', 
	'Temp': 11.49, 
	'TempMin': 11, 
	'TempMax': 12, 
	'Pressure': 1001, 
	'WindSpeed': 7.7, 
	'WindDegree': 210, 
	'SunRise': '2017 Mar 31 05:59:45', 
	'SunSet': '2017 Mar 31 18:59:31'
}
"""