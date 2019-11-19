def sayhi():
    print('hello')


sayhi()


def sayhi(name):
    print('hello, {}'.format(name))


sayhi('Bob')


def sayhi(name, age):
    print('hello, {}, you are {}.'.format(name, age))


sayhi('Tom', 20)
