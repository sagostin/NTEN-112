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
