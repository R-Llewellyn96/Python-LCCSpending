import os

from tabulate import tabulate

import GetNewFilesFromURL
import MergeDataframes
import MySQLConnector
import OpenFileAsDataframe
from IPython.display import display

# This is the main function of this Python Project
import PlotGraph

if __name__ == '__main__':

    # Flag determines run state of program
    inputLoopFlag = False

    # Year of results to search for
    yearToSearch = '2020'

    # Define Table name for database
    tableName = 'spendingrecords'

    # While flag is false repeat this...
    while not inputLoopFlag:

        # Prompt user whether they wish to continue
        txt = input(
            "\nThis program fetches and analyses Liverpool City Council Spending per department per month,\n"
            "Do you wish to get new files from server or analyse existing files?\n"
            "[1 = New Files, 2 = Existing Files]: \n")

        # Converts the string into a integer
        userChoice_number = int(txt)

        # Run program
        if userChoice_number == 1:

            # Tell user program is fetching new files
            print("User selected to fetch new files, fetching...")

            # Put a try catch block here in case fetching new files fails

            # Call function to get files from AWS
            GetNewFilesFromURL.getNewFiles('https://lpl-cl-files.s3-eu-west-1.amazonaws.com/')

            # Tell user program is fetching new files
            print("Files fetched from url successfully.")

            # Input loop flag set to true to prevent repeating loop
            inputLoopFlag = True

        # User chose to analyse existing files
        elif userChoice_number == 2:

            # Input loop flag set to true to prevent repeating loop
            inputLoopFlag = True

            # Tell user program is analysing
            print("User selected to analyse existing files, analysing...")

            # Break out of loop and end program run
            break

    # Define the file directory for excel files
    excelFileDirectory = os.getcwd()+'/excelFiles/'

    # Create a List of dataframes
    listOfDataFrames = []

    # Open each file in the excelFiles folder as dataframe and get back pandas dataframe for each
    for filename in os.listdir(excelFileDirectory):

        # Returns file as a pandas dataframe,
        fileAsDataFrame = OpenFileAsDataframe.openFileAsDataframe(filename)

        # Add returned dataframe to list of dataframes
        listOfDataFrames.append(fileAsDataFrame)

    # Merge list of dataframes together into one, for uploading to MySQL database
    #mergedDataframe = MergeDataframes.mergeDataframes(listOfDataFrames)
    print("stop")
    # Check MySQL Database connection
    mySQLConnection = MySQLConnector.connectToMySQL()

    # Check Database exists, if not create
    MySQLConnector.createDb(mySQLConnection)

    # Close MySQL Connection
    mySQLConnection.close()

    # Connect to Database
    dbConnection = MySQLConnector.connectToDb()

    # Drop table if exists
    # MySQLConnector.dropTable(dbConnection)

    # Check Table exists, if not create
    # MySQLConnector.createTable(dbConnection)

    # Insert merged dataframe into MySQL database table
    #for dataframe in listOfDataFrames:
    #    MySQLConnector.insertDataframeToTable(dataframe, tableName)
    print("Table inserted!")

    # Close database connection
    dbConnection.close()

    # Get sum of department spending per year
    yearSpendDF = MySQLConnector.selectSpendingPerYear(yearToSearch)

    # Get sum of department spending per month, list of dataframes
    dfSpendingPerMonth = MySQLConnector.selectSpendingPerMonth(yearToSearch)

    # MatPlotLib of spending per year in bar charts
    print(tabulate(yearSpendDF, headers = 'keys', tablefmt = 'pretty', showindex=False))

    #PlotGraph.plotBarChart(yearSpendDF)

    # MatPLotLib of spending per month in bar charts
    monthNum = 1
    for monthlyDf in dfSpendingPerMonth:
        print("Month: " + str(monthNum))
        print(tabulate(monthlyDf, headers='keys', tablefmt='pretty', showindex=False))
        monthNum += 1

    # MatPlotLib of spending per month in pie chart

    # MatPlotLib of spending per year in pie chart

    # MatPlotLib of spending for each department over a year line graph


    # Create List of month/year strings to create column in dataframe for each file
    # Get the filename as month for input to database as month/year column
    # nameOfFile = RegexFileName.regexFileName('april-2020.xlsx')

    # Close MySQL connection


    # Prompt user that program has finished execution
    print("Program run finished!")
