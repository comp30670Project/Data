def sqlConfig(theFile):
	theDict = {}
	with open(theFile, "r") as f:
		for line in f:
			content = line.strip().split(":")
			theDict[content[0]] = content[1]
	return theDict

def sqlAddToTable(configFile):

	# imports
	import mysql.connector
	



# imports
import mysql.connector

# configuration
config = sqlConfig("sqlConfig.txt")

# establish the connection
cnx = mysql.connector.connect(**config)

# create cursor object
cursor = cnx.cursor()

# use database
DB_NAME = 'dbProject'
cnx.database = DB_NAME

# add data to the table


# close the cursor and connection
cursor.close()
cnx.close()