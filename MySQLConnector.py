import sys

import mysql.connector
import pymysql
from sqlalchemy import create_engine


# Connect to MySQL Database
import Cfg


def connectToMySQL():

    try:
        # Define connection parameters
        myDb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password'
        )

        # Return connection object to caller
        return myDb
    except Exception as e:
        print("Connecting to MySQL database failed, please check login details and database status and try again")
        print("Exception: ", e.__cause__)
        sys.exit()


# Create Database
def createDb(myDb):

    # Terminal cursor allows for execution of SQL Queries
    dbCursor = myDb.cursor()

    # Create Database to hold our excel data
    dbCursor.execute('CREATE DATABASE IF NOT EXISTS lccspending')

# When database has been created, connect to it.
def connectToDb():

    # Connection parameters to connect to database directly
    lccSpendingDbConnection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='lccspending'
    )

    # Return database connection object to caller
    return lccSpendingDbConnection


# Create table
def createTable(lccSpendingDbConnection):

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL statement to create table to hold excel records
    dbCursor.execute("CREATE TABLE IF NOT EXISTS `lccspending`.`spendingrecords` ( `id` INT NOT NULL AUTO_INCREMENT , `Service Area` VARCHAR(255) NOT NULL , `Expense Type` VARCHAR(255) NOT NULL , `Description` VARCHAR(255) NOT NULL , `SAP Document Number` BIGINT NOT NULL , `Posting date` DATE NOT NULL , `Vendor` VARCHAR(255) NOT NULL , `Actual Value` FLOAT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

# Delete Table (Useful for repeated runs)
def dropTable(lccSpendingDbConnection):

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL statement to create table to hold excel records
    dbCursor.execute('DROP TABLE IF EXISTS spendingrecords')

# Insert DataFrame to table
def insertDataframeToTable(lccSpendingDbConnection, df, tableName):

    # Create engine from pymysql
    engine = create_engine("mysql+pymysql://" + Cfg.username + ":" + Cfg.password + "@" + Cfg.host + "/" + Cfg.database)
    df.to_sql(con=engine, name=tableName, if_exists='append', index=False)


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
