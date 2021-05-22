import pandas as pd


# Merges a list of passed dataframes together into one large dataframe for uploading to SQL database
def mergeDataframes(dataFramesToMerge):

    # Merge dataframe list into one large dataframe, dont sort values, ignore index
    mergedDataframe = pd.concat(dataFramesToMerge, ignore_index=True, sort=False)
    return mergedDataframe