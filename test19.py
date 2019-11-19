word = 'hello'
count = 0

while True:
    count = count + 1
    print('This is your time of guess: {}'.format(count))
    guess = input('Enter the word: ')

    if guess == word:
        print('You win.')
        break

    if count >= 3:
        print('You lose.')
        break
