import re


# Function will attempt to find the filename of the file
def regexFileName(passedFileString):

    # Check whether passed string is empty or not, first evaluates to true if string is empty
    if not (passedFileString and not passedFileString.isspace()):

        # If the passed string is empty then return zero
        return 0

    # If the passed string is not empty then continue method
    else:

        # Define regular expression pattern (Perl regex format)
        pattern = '[ \w-]+?(?=\.)'

        # Call findall function to return array of all matches in string
        matchesArr = re.findall(pattern, passedFileString)

        # Check whether match is a supported image extension
        if matchesArr[0] != 0:

            # Set returned match as image extension
            imgName = matchesArr[0]

            # Return image extension as string to caller
            return imgName

        # If image extension is not supported return zero to caller
        else:

            # Return zero to caller
            return 0
