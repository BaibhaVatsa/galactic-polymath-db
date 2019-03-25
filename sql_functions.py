import csv
import mysql.connector


class SqlConverter:
    def __init__(self, username, password,hostIP,dbName,pathStr=""):
        self.username = username
        self.password = password
        self.hostIP = hostIP
        self.dbName = dbName
        self.pathStr = pathStr
        cnx = connect(username, password, hostIP, dbName)
        self.cursor = cnx.cursor()

    def queryTable(self,tableName, cursor, cols_wanted=("*")):
        query = "SELECT "
        if (cols_wanted == "*"):
            query += '*'
        else:
            for cols in cols_wanted:
                query += cols + ','
            query = query[:-1]
        query += " FROM " + tableName
        try:
            cursor.execute(query)
            for row in cursor:
                for el in row:
                    print(el),
                print()
        except mysql.connector.Error as err:
            print("Failed showing table: {}".format(err))



    def create_load_table(self,pathStr, tableName, cursor):
        with open(pathStr, 'rU') as csvfile:
            cvsreader = csv.reader(csvfile, delimiter=',')

            line_count = 0
            firstTwo = []
            for row in cvsreader:
                if (line_count == 0):
                    firstTwo.append(row)
                elif (line_count == 1):
                    firstTwo.append(row)
                    createTable(tableName, firstTwo, cursor)
                    loadData(row, tableName, cursor)
                else:
                    loadData(row, tableName, cursor)
                line_count += 1

def createTable(tableName, cols, cursor):
        query = "DROP TABLE IF EXISTS " + tableName
        cursor.execute(query)
        colIndex = 0
        query = "CREATE TABLE " + tableName + "( "
        for col in cols[0]:
            isDigit = cols[1][colIndex].isdigit()
            if (isDigit):
                query += col + " INT DEFAULT NULL, "
            else:
                try:
                    float(cols[1][colIndex])
                    query += col + " DOUBLE DEFAULT NULL, "
                except ValueError:
                    query += col + " VARCHAR(25) DEFAULT NULL, "

            colIndex += 1
        query = query[:-2]
        query += " )"
        try:
            cursor.execute(query)
            print("Created the table " + tableName)
        except mysql.connector.Error as err:
            print("Failed creating table: {}".format(err))

def loadData(values, tableName, cursor):

        query = "INSERT INTO " + tableName + " VALUES ("
        for value in values:
            if (value != ""):
                if (value.isalpha):
                    query += "'" + value + "'" + ','
                else:
                    query += value + ','
            else:
                query += "NULL" + ','
        query = query[:-1]
        query += ")"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed inserting values to table {}".format(err))



def connect(username,password,hostIP,dbName):
  cnx = mysql.connector.connect(user=username, password=password,
                              host = hostIP,
                              database=dbName)

  print("Connected to sql server at: " + hostIP + "/" + dbName)
  return cnx


