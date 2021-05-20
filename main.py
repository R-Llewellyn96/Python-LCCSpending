# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import os

import GetNewFilesFromURL
import OpenFileAsDataframeAndAddColumn
import RegexFileName

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

    # Open each file in the excelFiles folder as dataframe and add column month / year to the dataframe
    for filename in os.listdir(excelFileDirectory):
        OpenFileAsDataframeAndAddColumn.openFileAsDataframeAndAddColumn(filename)

    # Create List of month/year strings to create column in dataframe for each file
    # Get the filename as month for input to database as month/year column
    nameOfFile = RegexFileName.regexFileName('april-2020.xlsx')



    # Prompt user that program has finished execution
    print("Program run finished!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
