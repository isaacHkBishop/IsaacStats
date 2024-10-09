#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      teiga
#
# Created:     07/10/2024
# Copyright:   (c) teiga 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Initializes five test values in the list and the initial menu value
values = [1, 2, 3, 3, 4, 5]
menu = 11

#Prints off user options
print("1. Add Values", "2. Delete values by number", "3. Delete values by position in list", "4. Display Values", "\n")
print("5. Compute Mean", "6. Compute Median", "7. Compute Midpoint", "8. Compute Mode(s)", "9. Compute Standard Deviation", "0. Exit", "\n")

#Adds values to the list
def addValues():
    values.append(float(input("Add a number to the list")))

#Deletes specific values from the list based on a specific number
def delValuesByValue():
    delNum = float(input("What number do you want deleted from the list?"))
    values.remove(delNum)

#Delete a value based on its position in the list
def delValueByPos():
    delPos = float(input("What is the position of the value you want to delete in the list"))
    values.remove(values[delPos])

#Displays all current values in the list
def displayMenu():
    for x in range(0, len(values)):
        print(values[x])
    print("Length of List:",len(values))

def computeMean():
    sigma = 0
    for x in range(0, len(values)):
        sigma += values[x]
    mean = sigma/len(values)
    return mean

def computeMedian():
    values.sort()
    if len(values) % 2 == 1:
        medInd = int((len(values))/2)
        median = values[medInd]
        print("Median:", median)
    elif len(values) % 2 == 0:
        medInd1 = int(((len(values))/2)-.5)
        medInd2 = int(((len(values))/2)+.5)
        median = ((values[medInd1]+values[medInd2])/2)
        print("Median:", median)


def computeMidpoint():
    midPoint = (len(values)-1)/2
    print("The midpoint of the list is:", midPoint)

def computeMode():
    highRec = 0
    modeIndex = 0
    for x in range(0,len(values)):
        recurring = 0
        for y in range(0, len(values)):
            if values[x] == values[y]:
                recurring += 1
            if recurring > highRec:
                highRec = recurring
                modeIndex = x
    print("Mode:",values[modeIndex],"Times it occurs:",highRec)


def computeStandardDeviation():
    sigma = 0
    for x in range(0, len(values)):
        sigma += (values[x]-computeMean())*(values[x]-computeMean())
    standDev = sigma/(len(values)-1)
    print("Standard Deviation:",standDev)

while menu != 0:
    menu = int(input("Pick an option"))
    if menu == 1:
        addValues()
    if menu == 2:
        delValuesByValue()
    if menu == 3:
        delValueByPos()
    if menu == 4:
        displayMenu()
    if menu == 5:
        print("Mean:",computeMean())
    if menu == 6:
        computeMedian()
    if menu == 7:
        computeMidpoint()
    if menu == 8:
        computeMode()
    if menu == 9:
        computeStandardDeviation()
