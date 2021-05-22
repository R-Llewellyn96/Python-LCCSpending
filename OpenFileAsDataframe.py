import os

import pandas as pd
from datetime import datetime


# Function will attempt to open each file in the excelFiles folder and add a column for month/year using pandas
def openFileAsDataframe(passedFile):
    folder = os.getcwd() + '/excelFiles/'

    # Define Date/Time parser for UK standard date, without time
    # dateFormatUK = lambda x: datetime.strptime(x, '%d/%m/%Y')

    df = pd.read_excel(folder + passedFile, engine='openpyxl')
    df['Posting date'] = pd.to_datetime(df['Posting date'], dayfirst=True).dt.date
    # df = pd.read_excel(folder + passedFile, engine='openpyxl', parse_dates=['Posting date'])
    # converters={'COLUMN': pd.to_datetime}
    df = df.dropna(how='all', axis='columns')

    return df
