import sys
import pandas as pd
import NamesOfMonths


# Merges a list of passed dataframes together into one large dataframe for uploading to SQL database
def mergeDataframes(dataFramesToMerge):

    # Try catch block to ensure dataframe merging fails safe, e.g. merging on disjointed columns
    try:
        # Merge dataframe list into one large dataframe, dont sort values, ignore index
        mergedDataframe = pd.concat(dataFramesToMerge, ignore_index=True, sort=False)

        # Reset Index of dataframe
        #mergedDataframe.reset_index()

        # Return merged dataframe to caller
        return mergedDataframe

    except Exception as e:
        print("Error: File could not be opened as Dataframe.\n", e)
        sys.exit()


# Add month column to dataframe
def addMonthToDataframes(dfList, listOfSANames):

    # Try catch block to ensure adding column to dataframe fails safely
    try:
        # Return list of dataframes with added month
        returnList = []

        # For each month print the table with spending by department
        # Iterate over the month number until all records are done
        monthNum = 1
        for monthlyDf in dfList:
            # Check Month number is not greater than 12,
            # if it is then reset to 1 in case multiple years will be evaluated
            if monthNum > 12:
                monthNum = 1

            # Get name of Month
            monthLabel = NamesOfMonths.getMonthName(monthNum)

            newDf = monthlyDf[monthlyDf['Service Area'].isin(listOfSANames)]

            # Add month label to column
            newDf['month'] = monthLabel

            # Add modified dataframe to List of dataframes
            returnList.append(newDf)

            # Increment month num
            monthNum += 1

        # List of dataframes returned to caller
        return returnList

    except Exception as e:
        print("Error: Adding Month to Dataframe failed.\n", e)
        sys.exit()


# Get top 5 rows from dataframe
def getTopFive(df):

    # List to hold names of top 5 spending SAs
    listOfServiceAreaNames = []

    # Loop through and get top 5 SAs
    i = 0
    try:
        while i < 5:
            valueInColumn = df['Service Area'].iloc[i]
            listOfServiceAreaNames.append(valueInColumn)
            i += 1

        # Return list of top 5 Service Areas to caller
        return listOfServiceAreaNames

    except Exception as e:
        print("Error: Get top 5 results in dataframe failed.\n", e)
        sys.exit()
