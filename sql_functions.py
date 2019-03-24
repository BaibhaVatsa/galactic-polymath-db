
import pandas
import mysql.connector


def main():
  username = 'root'
  password = ''
  hostIP = '127.0.0.1'
  dbName = 'galactic'
  cnx = connect(username,password,hostIP,dbName)
  cursor = cnx.cursor()
  pathStr = 'tortoise data.csv'
  tableName = 'tortoise'
  loadData(pathStr, tableName, cursor)
  query = "SELECT * FROM "+tableName
  try:
    cursor.execute(query)
  except mysql.connector.Error as err:
    print("Failed showing table: {}".format(err))

  print("Done")




  cnx.close()


def loadData(pathStr,tableName,cursor):
  #df = pandas.read_csv(pathStr)
  #print(df)
  query = "DROP TABLE IF EXISTS " + tableName
  cursor.execute(query)

  query = ("CREATE TABLE tortoise("
	"School	VARCHAR(20) NOT NULL,"
    "Day	VARCHAR(15) NOT NULL,"
    "col1	VARCHAR(15) NOT NULL,"
    "Weight	VARCHAR(15) NOT NULL,"
    "Walking	VARCHAR(15) NOT NULL,"
    "Eating  VARCHAR(15) NOT NULL,"
	"Movement VARCHAR(15) DEFAULT NULL)"
)
  try:
    cursor.execute(query)
  except mysql.connector.Error as err:
    print("Failed creating table: {}".format(err))

  pathStr = "'" + pathStr + "'"
  query = "LOAD DATA INFILE  "
  query += pathStr
  query += " INTO TABLE " + tableName
  query += (" FIELDS TERMINATED BY ','"
            " LINES TERMINATED BY "+"'\\r'"
            " IGNORE  1 ROWS")
  try:
    cursor.execute(query)
  except mysql.connector.Error as err:
    pass



def connect(username,password,hostIP,dbName):
  cnx = mysql.connector.connect(user=username, password=password,
                              host = hostIP,
                              database=dbName)

  return cnx

if __name__== "__main__":
  main()

