import csv
import sys
import mysql.connector

#arg1 is the name of the table to be created
#arg2 is the path to .csv file
def main():
    converter = SqlConverter('root','','127.0.0.1','galactic')
    converter.create_load_table(sys.argv[1],sys.argv[2])
    converter.queryTable(sys.argv[1])

class SqlConverter:
    def __init__(self, username, password,hostIP,dbName):
        self.username = username
        self.password = password
        self.hostIP = hostIP
        self.dbName = dbName
        self.con = connect(username, password, hostIP, dbName)
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()

    def queryTable(self,tableName, cols_wanted=("*")):
        query = "SELECT "
        if (cols_wanted == "*"):
            query += '*'
        else:
            for cols in cols_wanted:
                query += cols + ','
            query = query[:-1]
        query += " FROM " + tableName
        try:
            self.cursor.execute(query)
            for row in self.cursor:
                for el in row:
                    print(el),

                print()

        except mysql.connector.Error as err:
            print("Failed showing table: {}".format(err))



    def create_load_table(self, tableName, pathStr):
        with open(pathStr, 'rU') as csvfile:
            cvsreader = csv.reader(csvfile, delimiter=',')

            line_count = 0
            firstTwo = []
            for row in cvsreader:
                if (line_count == 0):
                    firstTwo.append(row)
					print(row)
                elif (line_count == 1):
                    firstTwo.append(row)
                    create_table(tableName, firstTwo, self.cursor)
                    load_data(row, tableName, self.cursor)
                else:
                    load_data(row, tableName, self.cursor)
                line_count += 1


def create_table(tableName, cols, cursor):
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
            #print("Created the table " + tableName)
        except mysql.connector.Error as err:
            print("Failed creating table: {}".format(err))


def load_data(values, tableName, cursor):

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

  #print("Connected to sql server at: " + hostIP + "/" + dbName)
  return cnx

if __name__ == "__main__":
    main()

