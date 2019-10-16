def isLeapYear(year):
    if year < 1582:
        return False
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True


def DaysInMonth(year, month):
    leapYear = isLeapYear(year)
    if leapYear and month == 2:
        return 29
    elif month == 2:
        return 28
    if month != 8:
        if month == 11:
            return 30
        elif month % 2 == 0:
            return 30
        else:
            return 31
    else:
        return 31


def dayOfYear(year, month, day):
    magicMonthNonLeap = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    magicMonthLeap = [6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

    if isLeapYear(year):
        magicMonth = magicMonthLeap[(month - 1)]
    else:
        magicMonth = magicMonthNonLeap[(month - 1)]

    yearForm = int(str(year)[0:2]) / 4
    yearNum = 0

    if yearForm == 6:
        yearNum = 6
    elif yearForm - 1 == 4:
        yearNum = 4
    elif yearForm - 2 == 2:
        yearNum = 2
    elif yearForm - 3 == 0:
        yearNum = 0

    doubleNumberYear = int(str(year)[2:4])
    doubleNumberYearQuotient = int(doubleNumberYear / 4)
    specialAddition = int(day + magicMonth + yearNum + doubleNumberYearQuotient + doubleNumberYear)
    print(day, magicMonth, yearNum, doubleNumberYearQuotient, doubleNumberYear, sep="+")

    finalDay = int(specialAddition % 7)

    # 0 = sunday, 1 = monday, 2 = tuesday, 3 = wednesday, 4 = thursday, 5 = friday, 6 = saturday
    return finalDay
    # 4n+


print(dayOfYear(1999, 8, 4))
# print(dayOfYear(2000, 12, 31))

testyears = [1900, 2000, 2016, 1987]
testmonths = [2, 2, 1, 11]

testresults = [28, 29, 31, 30]

for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "->", end="")
    result = DaysInMonth(yr, mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")
