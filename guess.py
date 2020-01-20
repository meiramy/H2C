import random
numero = random.randrange(1,10)
maara = 1

print('Try to guess the number between 0 and 100')
guess = int(input('Guess> '))
if (guess < 0) or (guess > 100):
    print('Guess must be in the range of 0 - 100')
elif guess < numero:
    print('Your guess is too low')
elif guess > numero:
    print('Your guess is too high')

while guess != numero:
    guess = int(input('Guess> '))
    maara += 1
    if (guess < 0) or (guess > 100):
        print('Guess must be in the range of 0 - 100')
    elif guess < numero:
        print('Your guess is too low')
    elif guess > numero:
        print('Your guess is too high')

          
print('Congratulations! That is the right answer!')
print('You made', maara,'guesses')
    
