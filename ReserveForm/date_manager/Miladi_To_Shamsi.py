

def convert_miladi_to_shamsi(miladiDate):
    isLeap = False
    if (miladiDate['year'] - 2004)%4 == 0:
        isLeap = True
    totalDayInMiladi = (miladiDate['year']-1)*365 + month_convert_to_day(miladiDate['month'], isLeap) + miladiDate['day']+\
                       count_day_of_leapYear(miladiDate['year'])
    totalDayInShamsi = totalDayInMiladi - 226899
    return count_year_month_day_according_to_day(totalDayInShamsi)


def count_day_of_leapYear(numOfYear):
    return int((numOfYear-1)/4)

def count_year_month_day_according_to_day(numOfDays):
    numOfYear = int(numOfDays/365)
    numOfLeap = int((numOfYear-1)/4)
    days = int(numOfDays%365)
    while numOfLeap > days:
        numOfYear -= 1
        days += 365
    days -= numOfLeap
    numOfYear += 1
    monthAndDay = count_month_and_day_from_totalDay(days)
    return {'year':numOfYear, 'month':monthAndDay['month'], 'day':monthAndDay['day']}


def count_month_and_day_from_totalDay(numOfDay):
    numOfMonth = 1
    if numOfDay <= 186:
        while numOfDay > 31:
            numOfDay -= 31
            numOfMonth += 1
    elif numOfDay > 186:
        numOfDay -= 186
        numOfMonth += 6
        while numOfDay > 30:
            numOfDay -= 30
            numOfMonth += 1
    return {'month':numOfMonth, 'day':numOfDay}


def month_convert_to_day(numOfMonth, isLeap):
    numOfDays = 0
    if numOfMonth > 1:
        numOfDays += 31
    if numOfMonth > 2:
        if isLeap == True:
            numOfDays += 29
        else:
            numOfDays += 28
    if numOfMonth > 3:
        numOfDays += 31
    if numOfMonth > 4:
        numOfDays += 30
    if numOfMonth > 5:
        numOfDays += 31
    if numOfMonth > 6:
        numOfDays += 30
    if numOfMonth > 7:
        numOfDays += 31
    if numOfMonth > 8:
        numOfDays += 31
    if numOfMonth > 9:
        numOfDays += 30
    if numOfMonth > 10:
        numOfDays += 31
    if numOfMonth > 11:
        numOfDays += 30
    return numOfDays