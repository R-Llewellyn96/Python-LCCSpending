# Python-LCCSpending
This program uses Python's Pandas, MySQL connector, urlLib3 and SQLAlchemy to gather Excel spreadsheets of Liverpool City Council spending. <br />
Processes them into dataframes, fixes formatting and import issues and outputs the combined results to a MySQL database in an automated fashion,
this program also performs automated SQL statement execution to retrieve results from a MySQL database. <br />
<br />
How to use: Run main.py in a Python3 virtual environment, ensure MySQL credentials are entered in the DBCredentials.py file. <br /> <br />
NOTE: This program requires the following Python libraries to function: <br />
tabulate, locale, urllib3, xmltodict, mysql.connector, pandas, sqlalchemy, pymysql, openpyxl <br />
<br /> <br />
What do you get with this program?<br />
- [x] Gather Excel Spreadsheets from XML webpage data hosted on an AWS Server in an automated way.
- [x] Conversion of Excel spreadsheets to Pandas dataframes with Excel perculiarities accounted for with no data loss.
- [x] Automated connection to a MySQL database.
- [x] Automated creation of MySQL database and table for holding data imported from Excel spreadsheets.
- [x] Automated insertion of dataframes to MySQL database using SQLAlchemy - 100,273 records.
- [x] Automated retrieval of Monthly spending per Service Area of the council as well as Yearly spending per Service Area.
- [x] Display of retrieved data in pretty printed table format using Tabulate, for evaluation.
- [x] Use of MatPlotLib to display graphs of retrieved data and save results to folders and files.
<!-- -->
<br />
Future Updates:<br />
<br />

- [ ] TBC
<br />
<!-- end of the list -->
