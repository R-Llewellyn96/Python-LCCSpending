import urllib3 as urllib3
import xmltodict


# Get LCC Xml page, to grab monthly reports
def getLCCXml(url):
    try:
        return xmltodict.parse(urllib3.PoolManager().request('GET', url).data)

    except Exception as e:
        print("XML Parsing failed.", e)
        pass


# Download file from url
def getFileFromUrl(url, filename):
    urlAndFilename = url + filename
    response = urllib3.PoolManager().request('GET', urlAndFilename)
    fileToSave = open('excelFiles/'+filename, 'wb')
    fileToSave.write(response.data)
    fileToSave.close()
    response.release_conn()


# Download files from URL
def getNewFiles(url):

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

    for file in listOfXlsxFilesFromXML:
        getFileFromUrl(url, file)
