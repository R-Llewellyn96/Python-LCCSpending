import os
import pandas as pd


# Function will attempt to open each file in the excelFiles folder and add a column for month/year using pandas
def openFileAsDataframe(passedFile):

    # Define directory where excel files have been downloaded and saved to
    folder = os.getcwd() + '/excelFiles/'

    # Read Excel file, using openpyxl engine
    df = pd.read_excel(folder + passedFile, engine='openpyxl')

    # Parse correct date from file in UK format
    df['Posting date'] = pd.to_datetime(df['Posting date'], dayfirst=True).dt.date

    # Drop NaN values and columns
    df = df.dropna(how='all', axis='columns')

    # Return clean dataframe to caller
    return df
