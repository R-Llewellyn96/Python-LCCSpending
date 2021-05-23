import sys
import pandas as pd


# Merges a list of passed dataframes together into one large dataframe for uploading to SQL database
def mergeDataframes(dataFramesToMerge):

    # Try catch block to ensure dataframe merging fails safe, e.g. merging on disjointed columns
    try:
        # Merge dataframe list into one large dataframe, dont sort values, ignore index
        mergedDataframe = pd.concat(dataFramesToMerge, ignore_index=True, sort=False)

        # Return merged dataframe to caller
        return mergedDataframe

    except Exception as e:
        print("Error: File could not be opened as Dataframe.\n", e)
        sys.exit()
