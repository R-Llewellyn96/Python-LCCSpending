import mysql.connector


# Connect to MySQL Database
def connectToMySQL():
    myDb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    return myDb


# Create Database
def createDb(myDb):
    dbCursor = myDb.cursor()
    dbCursor.execute("CREATE DATABASE lccspending")


# Check the database i want to connect to exists
def checkDbExists(myDb):

    # Get cursor to make SQL commands
    dbCursor = myDb.cursor()

    # Show databases execution command on mysql db
    dbCursor.execute("SHOW DATABASES")

    # found flag is set to false, set to True if database lccspending is found
    dbFoundFlag = False
    for db in dbCursor:
        print(db)
        if db == 'lccspending':
            dbFoundFlag = True

    # if flag is false create the db
    if not dbFoundFlag:
        createDb(myDb)


# When database has been created, connect to it.
def connectToDb():
    lccSpendingDbConnection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="lccspending"
    )
    return lccSpendingDbConnection


# Create table
def createTable(lccSpendingDbConnection):

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL statement
    dbCursor.execute("CREATE TABLE spendingrecords ("
                     "id INT AUTO_INCREMENT PRIMARY KEY, "
                     "service_area VARCHAR(255), "
                     "expense_type VARCHAR(255),"
                     "description VARCHAR(255),"
                     "sap_document_number INT,"
                     "posting_date DATE,"
                     "vendor VARCHAR(255),"
                     "actual_value FLOAT)")


# Check if table exists in Database
def checkTableExists(lccSpendingDbConnection):

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL command to get all tables in database
    dbCursor.execute("SHOW TABLES")

    # Set table found flag to False
    tableFoundFlag = False

    # Loop through tables in Database, if table i want is not present create it
    for table in dbCursor:
        print(table)
        if table == 'spendingrecords':
            tableFoundFlag = True

    # if flag is false create the db
    if not tableFoundFlag:
        createTable(lccSpendingDbConnection)


# Insert values into table
def insertValuesToTable(lccSpendingDbConnection,
                        serviceArea,
                        expenseType,
                        description,
                        sapDocumentNumber,
                        postingDate,
                        vendor,
                        actualValue):

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # SQL Statement
    sqlStatement = "INSERT INTO spendingrecords (" \
                   "service_area, " \
                   "expense_type, " \
                   "description, " \
                   "sap_document_number, " \
                   "posting_date, " \
                   "vendor, " \
                   "actual_value) VALUES (" \
                   "$service_area, " \
                   "$expense_type, " \
                   "$description, " \
                   "$sap_document_number, " \
                   "$posting_date, " \
                   "$vendor, " \
                   "$actual_value)"

    # Values to insert
    values = (serviceArea, expenseType, description, sapDocumentNumber, postingDate, vendor, actualValue)

    # Execute SQL statement
    dbCursor.execute(sqlStatement, values)
