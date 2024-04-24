def convertListToMins(timeList):
    days = timeList[0]
    hours = timeList[1]
    mins = timeList[2]
    newMins = mins + (hours * 60) + (days * 24 * 60)
    return newMins

def convertListToHours(timeList):
    days = timeList[0]
    hours = timeList[1]
    mins = timeList[2]
    newHours = (mins/60) + hours + (days * 24)
    return newHours

def convertUnitToList(timeIn, unit):
    if unit == "hours":
        timeIn *= 60
    elif unit == "days":
        timeIn *= 60
        timeIn *= 24
    hours = timeIn//60
    leftoverMins = timeIn%60
    days = hours//24
    leftoverHours = hours%24
    newList = [days, leftoverHours, leftoverMins]
    return newList

def convertListToString(list):
    days = list[0]
    hours = list[1]
    minutes = list[2]
    string = f"{days} days, {hours} hours, and {round(minutes, 1)} minutes"
    return string

def retrieveUserInputList():
    formatList = ["Days", "Hours", "Minutes"]
    while True:
        try:
            timeList = [float(input(f"Please enter value for {x}: ")) for x in formatList]
            if ValueError == True:
                raise ValueError
            else:
                return timeList
        except ValueError:
            print("Please enter a valid float input")

def retrieveUserInput(unit):
    while True:
        try:
            timeDivision = float(input(f"Please enter a number of {unit}: "))
            if ValueError == True:
                raise ValueError
            else:
                return timeDivision
        except ValueError:
            print("Please enter a valid float input")

def addTwoTimes(time1, time2):
    mins1 = convertListToMins(time1)
    mins2 = convertListToMins(time2)
    totalMins = mins1 + mins2
    newTime = convertUnitToList(totalMins, "mins")
    return newTime

def differenceTwoTimes(time1, time2):
    mins1 = convertListToMins(time1)
    mins2 = convertListToMins(time2)
    largerMins = max([mins1, mins2])
    smallerMins = min([mins1, mins2])
    differenceMins = largerMins - smallerMins
    timeDifference = convertUnitToList(differenceMins, "mins")
    return timeDifference


menu = {
    1 : "Add 2 times.",
    2 : "Find difference between two times.",
    3 : "Convert time to hours.",
    4 : "Convert time to minutes.",
    5 : "Convert minutes to time.",
    6 : "Convert hours to time.",
    7 : "Convert days to time.",
    8 : "Exit."
}

print("Menu:")
for x in menu:
    print(f"{list(menu.keys())[x-1]}.\t{list(menu.values())[x-1]}")

while True:
    try:
        selected = int(input("Please select: "))
        if ValueError == True or selected > 8 or selected < 1:
            raise ValueError
        else:
            if selected == 1:
                timeList1 = retrieveUserInputList()
                timeList2 = retrieveUserInputList()
                print(f"The two times add up to {convertListToString(addTwoTimes(timeList1, timeList2))}")
            elif selected == 2:
                timeList1 = retrieveUserInputList()
                timeList2 = retrieveUserInputList()
                print(f"The difference between the two times are {convertListToString(differenceTwoTimes(timeList1, timeList2))}")
            elif selected == 3:
                timeList = retrieveUserInputList()
                print(f"The time given is {convertListToHours(timeList)} hours")
            elif selected == 4:
                timeList = retrieveUserInputList()
                print(f"The time given is {convertListToMins(timeList)} minutes")
            elif selected == 5:
                mins = retrieveUserInput("minutes")
                print(f"{mins} minutes converted into time is {convertListToString(convertUnitToList(mins, "mins"))}")
            elif selected == 6:
                hours = retrieveUserInput("hours")
                print(f"{hours} hours converted into time is {convertListToString(convertUnitToList(hours, "hours"))}")
            elif selected == 7:
                days = retrieveUserInput("days")
                print(f"{days} days converted into time is {convertListToString(convertUnitToList(days, "days"))}")
            elif selected == 8:
                quit()
    except ValueError:
        print("Please enter a valid input (1-8)")