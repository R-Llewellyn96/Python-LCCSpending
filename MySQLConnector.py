import sys

import mysql.connector
import pandas as pd
import pymysql
from sqlalchemy import create_engine


# Connect to MySQL Database
import DBCredentials


def connectToMySQL():

    # Define connection parameters
    mySQLCon = mysql.connector.connect(host=DBCredentials.host,
                                   user=DBCredentials.username,
                                   password=DBCredentials.password)

    # Return connection object to caller
    return mySQLCon


# Create Database
def createDb():

    # Connect to MySQL Server
    mySQLCon = connectToMySQL()

    # Terminal cursor allows for execution of SQL Queries
    dbCursor = mySQLCon.cursor()

    # Create Database to hold our excel data
    dbCursor.execute("CREATE DATABASE IF NOT EXISTS lccspending;")

    # Close Cursor
    dbCursor.close()

    # Close DB connection after use
    mySQLCon.close()


# When database has been created, connect to it.
def connectToDb():

    # Connection parameters to connect to database directly
    lccSpendingDbConnection = mysql.connector.connect(host=DBCredentials.host,
                                                      user=DBCredentials.username,
                                                      password=DBCredentials.password,
                                                      database=DBCredentials.database)

    # Return database connection object to caller
    return lccSpendingDbConnection


# Create table
def createTable():

    # Connect to DB
    lccSpendingDbConnection = connectToDb()

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL statement to create table to hold excel records
    dbCursor.execute("CREATE TABLE IF NOT EXISTS `lccspending`.`spendingrecords` ( `id` INT NOT NULL AUTO_INCREMENT , `Service Area` VARCHAR(255) NOT NULL , `Expense Type` VARCHAR(255) NOT NULL , `Description` VARCHAR(255) NOT NULL , `SAP Document Number` BIGINT NOT NULL , `Posting date` DATE NOT NULL , `Vendor` VARCHAR(255) NOT NULL , `Actual Value` DECIMAL(18,2) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

    # Close Cursor
    dbCursor.close()

    # Close DB connection after use
    lccSpendingDbConnection.close()


# Delete Table (Useful for repeated runs)
def dropTable():

    # Connect to DB
    lccSpendingDbConnection = connectToDb()

    # Get cursor to make SQL commands
    dbCursor = lccSpendingDbConnection.cursor()

    # Execute SQL statement to create table to hold excel records
    dbCursor.execute("DROP TABLE IF EXISTS spendingrecords;")

    # Close Cursor
    dbCursor.close()

    # Close DB connection after use
    lccSpendingDbConnection.close()


# Insert DataFrame to table
def insertDataframeToTable(df, tableName):

    # Create engine from pymysql
    engine = create_engine("mysql+pymysql://" + DBCredentials.username + ":" + DBCredentials.password + "@" + DBCredentials.host + "/" + DBCredentials.database)

    # Upload Dataframe to MySQL
    df.to_sql(con=engine, name=tableName, if_exists='append', index=False)

    # Destroy engine after use
    engine.dispose()


# Select spending per department per year
def selectSpendingPerYear(yearToSearch):

    # Select statement to get per department spending for a year
    sqlStatement = "SELECT `Service Area`, SUM(`Actual Value`) AS `TotalVals` FROM `spendingrecords` WHERE YEAR(`Posting date`) = "+yearToSearch+" GROUP BY `Service Area` ORDER BY `TotalVals` DESC;"

    # Create engine from pymysql
    engine = create_engine(
        "mysql+pymysql://" + DBCredentials.username + ":" + DBCredentials.password + "@" + DBCredentials.host + "/" + DBCredentials.database)

    # Execute SQL statement to get spending per month as dataframe
    df = pd.read_sql(sqlStatement, con=engine)

    # Destroy engine after use
    engine.dispose()

    # Return dataframe of yearly spending to caller
    return df


# Select spending per department per month
def selectSpendingPerMonth(yearToSearch):

    # Create list of dataframes to store results and return to caller
    listOfDataframes = []

    # Create engine from pymysql
    engine = create_engine(
        "mysql+pymysql://" + DBCredentials.username + ":" + DBCredentials.password + "@" + DBCredentials.host + "/" + DBCredentials.database)

    # Iterate through each month of the year
    # and get resulting dataframe for each
    monthToIterate = 1
    while monthToIterate < 13:

        # Convert to String for input into SQL Statement
        monthToSearch = str(monthToIterate)

        # Select statement to get per department spending for a month
        sqlStatement = "SELECT `Service Area`, SUM(`Actual Value`) AS `TotalVals` FROM `spendingrecords` WHERE YEAR(`Posting date`) = " + yearToSearch + " AND MONTH(`Posting date`) = " + monthToSearch + " GROUP BY `Service Area` ORDER BY `TotalVals` DESC;"

        # Execute SQL statement to get spending per month as dataframe
        df = pd.read_sql(sqlStatement, con=engine)

        # Add dataframe result to listOfDataframes
        listOfDataframes.append(df)

        # Iterate month
        monthToIterate += 1

    # Destroy engine after use
    engine.dispose()

    # Return list of dataframes for each month to caller
    return listOfDataframes


# Select Spending for a specific Month
def selectSpendingPerSpecificMonth(monthToSearch, yearToSearch):

    # Create engine from pymysql
    engine = create_engine(
        "mysql+pymysql://" + DBCredentials.username + ":" + DBCredentials.password + "@" + DBCredentials.host + "/" + DBCredentials.database)

    # Select statement to get per department spending for a month
    sqlStatement = "SELECT `Service Area`, SUM(`Actual Value`) AS `TotalVals` FROM `spendingrecords` WHERE YEAR(`Posting date`) = " + yearToSearch + " AND MONTH(`Posting date`) = " + monthToSearch + " GROUP BY `Service Area` ORDER BY `TotalVals` DESC;"

    # Execute SQL statement to get spending per month as dataframe
    df = pd.read_sql(sqlStatement, con=engine)

    # Destroy engine after use
    engine.dispose()

    # Return dataframe to caller
    return df
