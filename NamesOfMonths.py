
# Function gets the name of the month using a switch case statement,
# and returns either the name or error message to caller
def getMonthName(monthNum):
    monthNames = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    # Return name to caller, or error message
    return monthNames.get(monthNum, "Invalid Month Number entered!")
