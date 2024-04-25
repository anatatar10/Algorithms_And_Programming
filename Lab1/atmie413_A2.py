"""Determine a date (as day, month, year) starting from two integer numbers that represent the year and the number of the day in that year."""

year = int(input("Enter the year: "))
days = int(input("Enter the days: "))
ok = 0
if(year % 400 == 0) and (year % 100 == 0):
    ok = 1
elif(year % 4 == 0) and (year % 100 != 0):
    ok = 1
else:
    ok = 0
if days <= 31:
    print(days, 1, year)
if ok == 1:
    if days <= 60:
        print(days - 31, 2, year)
    elif days <= 91:
        print(days - 60, 3, year)
    elif days <= 121:
        print(days - 91, 4, year)
    elif days <= 152:
        print(days - 121, 5, year)
    elif days <= 182:
        print(days - 152, 6, year)
    elif days <= 213:
        print(days - 182, 7, year)
    elif days <= 244:
        print(days - 213, 8, year)
    elif days <= 274:
        print(days - 244, 9, year)
    elif days <= 305:
        print(days - 274, 10, year)
    elif days <= 335:
        print(days - 305, 11, year)
    elif days <= 366:
        print(days - 335, 12, year)

else:
    if days <= 59:
        print(days - 30, 2, year)
    elif days <= 90:
        print(days - 59, 3, year)
    elif days <= 120:
        print(days - 90, 4, year)
    elif days <= 151:
        print(days - 120, 5, year)
    elif days <= 181:
        print(days - 151, 6, year)
    elif days <= 212:
        print(days - 181, 7, year)
    elif days <= 243:
        print(days - 212, 8, year)
    elif days <= 273:
        print(days - 243, 9, year)
    elif days <= 304:
        print(days - 273, 10, year)
    elif days <= 334:
        print(days - 304, 11, year)
    elif days <= 365:
        print(days - 334, 12, year)
