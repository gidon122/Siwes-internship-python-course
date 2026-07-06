<<<<<<< HEAD
year = int(input("Enter a year: "))

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year == True:
    print("This is a leap year.")
else:
=======
year = int(input("Enter a year: "))

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year == True:
    print("This is a leap year.")
else:
>>>>>>> b444ab0fd6834e70c012c2bf54af7fc6f8d54a36
    print("This is not a leap year.")