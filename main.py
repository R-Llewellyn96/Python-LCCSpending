import os

import GetNewFilesFromURL
import MergeDataframes
import MySQLConnector
import OpenFileAsDataframe

# This is the main function of this Python Project
if __name__ == '__main__':

    # Flag determines run state of program
    inputLoopFlag = False

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

    print("stop")

    # Merge list of dataframes together into one, for uploading to MySQL database
    #mergedDataframe = MergeDataframes.mergeDataframes(listOfDataFrames)

    # Check MySQL Database connection
    mySQLConnection = MySQLConnector.connectToMySQL()

    # Check Database exists, if not create
    MySQLConnector.createDb(mySQLConnection)

    # Connect to Database
    dbConnection = MySQLConnector.connectToDb()

    # Drop table if exists
    MySQLConnector.dropTable(dbConnection)

    # Check Table exists, if not create
    MySQLConnector.createTable(dbConnection)

    # Insert merged dataframe into MySQL database table
    for dataframe in listOfDataFrames:
        MySQLConnector.insertDataframeToTable(dbConnection, dataframe, 'spendingrecords')
    print("Table inserted!")


    # Create List of month/year strings to create column in dataframe for each file
    # Get the filename as month for input to database as month/year column
    # nameOfFile = RegexFileName.regexFileName('april-2020.xlsx')

    # Prompt user that program has finished execution
    print("Program run finished!")
