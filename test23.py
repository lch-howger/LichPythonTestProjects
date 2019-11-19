vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter the word: ')
newword = ''
for letter in word:
    if letter in vowels:
        newword = newword + 'g'
    else:
        newword = newword + letter

print(newword)
