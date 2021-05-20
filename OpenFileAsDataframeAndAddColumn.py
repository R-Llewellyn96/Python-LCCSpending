import os

import pandas as pd
from datetime import datetime

# Function will attempt to open each file in the excelFiles folder and add a column for month/year using pandas
def openFileAsDataframeAndAddColumn(passedFile):
    folder = os.getcwd() + '/excelFiles/'
    dateparser = lambda x: datetime.strptime(x, '%Y-%m-%d')
    df = pd.read_excel(folder + passedFile, engine='openpyxl', parse_dates=True, date_parser=dateparser, converters= {'COLUMN': pd.to_datetime})
   # dictFromExcel.Date = pd.to_datetime(dictFromExcel.Date)

    # Date time is done, select it as column here
    #df = pd.DataFrame(dictFromExcel, columns=['Service Area', 'Expense Type', 'Description', 'SAP Document Number', 'Posting Date', 'Vendor', 'Actual Value'])
    #df['Posting Date'] = pd.to_datetime(df['Posting Date'], errors='coerce')
    #df['Posting Date'] = df['Posting Date'].apply(lambda x: df.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    print(df.head())
    #print(df.shape)
    #for key in dictFromExcel:
        #print(dictFromExcel[key].head())
