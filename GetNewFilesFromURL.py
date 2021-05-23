import sys
import urllib3 as urllib3
import xmltodict


# Get LCC Xml page, to grab monthly reports
def getLCCXml(url):

    # Try catch block, attempt to get XML from URL, if it fails throw exception
    try:
        return xmltodict.parse(urllib3.PoolManager().request('GET', url).data)

    except Exception as e:
        print("Error: XML Parsing failed.\n", e)
        sys.exit()


# Download file from url
def getFileFromUrl(url, filename):

    # Try catch block, safely fail if getting files from server fails
    try:
        # Define URL and Filename for Excel file to download
        urlAndFilename = url + filename

        # Deal with HTTP response to get request
        response = urllib3.PoolManager().request('GET', urlAndFilename)

        # Create a new file in excelFiles directory and name it the filename from web XML
        fileToSave = open('excelFiles/'+filename, 'wb')

        # Write response data to the new excel file
        fileToSave.write(response.data)

        # Close data writer to excel file
        fileToSave.close()

        # Release HTTP Get request connection to server
        response.release_conn()

    except Exception as e:
        print("Error: Get File from URL: " + url + filename + " failed.\n", e)
        sys.exit()


# Download files from URL
def getNewFiles(url):

    # Try catch block shouldn't be necessary here, but included for safety
    try:
        # Get XML file from url
        xmlAsDict = getLCCXml(url)

        # Assign XML to a dictionary
        ContentXML = xmlAsDict.get("ListBucketResult").get("Contents")

        # Create List to store names of xlsx files
        listOfXlsxFilesFromXML = []

        # Get the length of contents, to fetch each xlsx file name
        # and loop through contents and strip the names of the xlsx files
        i = 0
        while i < len(ContentXML):
            listOfXlsxFilesFromXML.append(ContentXML[i]['Key'])
            i = i + 1

        # Get each ExcelFile listed in web XML from web server
        # and save to excelFiles directory
        for file in listOfXlsxFilesFromXML:
            getFileFromUrl(url, file)

    except Exception as e:
        print("Error: Get New Files from URL: " + url + " failed.\n", e)
        sys.exit()
