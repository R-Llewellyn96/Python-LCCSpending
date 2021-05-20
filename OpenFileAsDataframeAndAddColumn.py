import os

import pandas as pd


# Function will attempt to open each file in the excelFiles folder and add a column for month/year using pandas
def openFileAsDataframeAndAddColumn(passedFile):
    folder = os.getcwd() + '/excelFiles/'

    df = pd.read_excel(folder + passedFile, engine='openpyxl', parse_dates=True,
                       converters={'COLUMN': pd.to_datetime})
    print(df.head())
