import random

i = random.randint(1, 100)

while True:
    guess = input('Enter your guess: ')
    guess = float(guess)
    if guess == i:
        print('You got it.')
        break
    elif guess > i:
        print('Your guess is bigger.')
    elif guess < i:
        print('Your guess is smaller.')
