# name = input('Enter your name: ')
# print('Hello, {}, welcome to the test.'.format(name))

questions={
    'a b c1':'a',
    'a b c2':'b',
    'a b c3':'c',
}

for question in questions.keys():
    print(question)
    result=input('Enter your answer: ')
    if result==questions.get(question):
        print('Right.')
    else:
        print('Wrong.')
