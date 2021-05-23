import os
import sys

from tabulate import tabulate

import GetNewFilesFromURL
import MergeDataframes
import MySQLConnector
import NamesOfMonths
import OpenFileAsDataframe
import locale
import PlotGraph


# This is the main function of this Python Project
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

        # Check user input and perform following action
        if txt == '1':

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
        elif txt == '2':

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
    # (error, inputting 100,000+ records to MySQL in one insertion operation results in missing records)
    # mergedDataframe = MergeDataframes.mergeDataframes(listOfDataFrames)

    # Check Database exists, if not create
    MySQLConnector.createDb()

    # Drop table if exists
    MySQLConnector.dropTable()

    # Check Table exists, if not create
    MySQLConnector.createTable()

    # Insert merged dataframe into MySQL database table
    for dataframe in listOfDataFrames:
        MySQLConnector.insertDataframeToTable(dataframe, tableName)
    print("Tables inserted to MySQL Successfully!")

    # Get sum of department spending per year
    yearSpendDF = MySQLConnector.selectSpendingPerYear(yearToSearch)

    # Get top 5 service areas from yearly spending so we know what to plot on line graph
    listOfSANames = MergeDataframes.getTopFive(yearSpendDF)

    # Make a copy for Graphing use (Conversion to currency changes dType to String)
    # yearSpendDFGraph = yearSpendDF.copy()

    # Get sum of department spending per month, list of dataframes
    dfSpendingPerMonth = MySQLConnector.selectSpendingPerMonth(yearToSearch)

    # Make a copy for Graphing use (Conversion to currency changes dType to String)
    dfSpendingPerMonthGraph = dfSpendingPerMonth.copy()

    # Add Month Column to per month spending for easy line plotting
    linePlotDf = MergeDataframes.addMonthToDataframes(dfSpendingPerMonthGraph, listOfSANames)

    # Merge monthly dataframes to plot per month as a line graph
    mergedDataframe = MergeDataframes.mergeDataframes(linePlotDf)

    # Set input loop flag to false,
    # gather user input to ask if they want to see bar charts
    inputLoopFlag = False

    # While flag is false repeat this...
    while not inputLoopFlag:

        # Prompt user whether they wish to continue
        txt2 = input(
            "\nThis program has fetched yearly and monthly spending for Liverpool City Council\n"
            "Do you wish to view this information in Bar and Line graphs?\n"
            "[1 = Yes, 2 = No]: \n")

        # Check user input and perform following action
        if txt2 == '1':

            # Tell user program is fetching new files
            print("Generating Graphs and Charts...")

            # MatPlotLib of spending for each department over a year line graph
            # Plot line graph
            PlotGraph.plotLineGraph(mergedDataframe, 'Yearly', yearToSearch)

            # MatPlotLib of spending per year in Bar chart
            PlotGraph.plotBarChart(yearSpendDF, 'Yearly', yearToSearch)

            # MatPlotLib of spending per year in Bar chart Logarithmic
            PlotGraph.plotBarChartLog(yearSpendDF, 'Yearly', yearToSearch)

            # For each month print the table with spending by department
            # Iterate over the month number until all records are done
            monthNum = 1
            for monthlyDf in dfSpendingPerMonth:

                # Check Month number is not greater than 12,
                # if it is then reset to 1 in case multiple years will be evaluated
                if monthNum > 12:
                    monthNum = 1

                # Get name of Month
                monthLabel = NamesOfMonths.getMonthName(monthNum)

                # Plot bar graph in both Standard and Logarithmic form
                PlotGraph.plotBarChart(monthlyDf, monthLabel, yearToSearch)
                PlotGraph.plotBarChartLog(monthlyDf, monthLabel, yearToSearch)

                # Iterate month number
                monthNum += 1

            print("Graphs finished and saved as .png in \'graphs/standard/\' and \'graphs/logs/\'")

            # Input loop flag set to true to prevent repeating loop
            inputLoopFlag = True

        # User chose not to view graphs
        elif txt2 == '2':

            # Input loop flag set to true to prevent repeating loop
            inputLoopFlag = True

            # Tell user program is analysing
            print("User selected not to view graphs, skipping...")

            # Break out of loop and end program run
            break

    # Convert spending dataframe amounts to use pounds
    # Set Locale to GB and GBPFormat to pounds
    locale.setlocale(locale.LC_ALL, 'en_GB')
    GBPFormat = '£{:,.2f}'

    # Apply currency to column
    yearSpendDF['TotalVals'] = yearSpendDF['TotalVals'].map(GBPFormat.format)

    # Spending per year in table
    print(tabulate(yearSpendDF, headers='keys', tablefmt='pretty', showindex=False))

    # For each month print the table with spending by department
    # Iterate over the month number until all records are done
    monthNum = 1
    for monthlyDf in dfSpendingPerMonth:

        # Check Month number is not greater than 12,
        # if it is then reset to 1 in case multiple years will be evaluated
        if monthNum > 12:
            monthNum = 1

        # Print Monthly spending per department in pounds, in a pretty printed table
        print("Month: " + str(monthNum))

        # Format values as currency, great british pounds
        monthlyDf['TotalVals'] = monthlyDf['TotalVals'].map(GBPFormat.format)

        # Print table
        print(tabulate(monthlyDf, headers='keys', tablefmt='pretty', showindex=False))

        # Iterate month number
        monthNum += 1

    # Prompt user that program has finished execution
    print("Program run finished!")
    sys.exit()
