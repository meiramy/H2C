integer = int(input('Enter an integer: '))

if (integer > 0 and integer % 2 == 0):
    print('Number ',integer,' is:')
    print('- Positive')
    print('- Even')

if (integer > 0 and integer % 2 != 0):
    print('Number ',integer,' is :')
    print('- Positive')
    print('- Odd')

elif (integer < 0 and integer % 2 == 0):
    print('Number ',integer,' is:')
    print('- Negative')
    print('- Even')

elif (integer < 0 and integer % 2 != 0):
    print('Number ',integer,' is:')
    print('- Negative')
    print('- Odd')

elif (integer == 0):
    print('Number ',integer,' is:')
    print('- Origin')
    print('- Even')
