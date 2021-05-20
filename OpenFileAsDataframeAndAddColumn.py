import os

import pandas as pd


# Function will attempt to open each file in the excelFiles folder and add a column for month/year using pandas
def openFileAsDataframeAndAddColumn(passedFile):
    folder = os.getcwd() + '/excelFiles/'
    dictFromExcel = pd.read_excel(folder + passedFile, engine='openpyxl', parse_dates=True, converters= {'COLUMN': pd.to_datetime})
   # dictFromExcel.Date = pd.to_datetime(dictFromExcel.Date)

    # Date time is done, select it as column here
    df = pd.DataFrame(dictFromExcel, columns=['Service Area', 'Expense Type', 'Description', 'SAP Document Number', 'Posting Date', 'Vendor', 'Actual Value'])
    #print(df.head())
    print(df.shape)
    #for key in dictFromExcel:
        #print(dictFromExcel[key].head())
