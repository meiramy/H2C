year = int(input('Enter a year to see if it is a leap year or not: '))

if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0 and (year % 100 == 0) and (year % 400 == 0))):
    print('It is a Leap year')                                          
else:
    print('It is not a Leap year')
