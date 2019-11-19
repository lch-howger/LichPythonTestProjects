while True:
    try:
        # num=1/0
        num = input('Enter a number: ')
        num = float(num)
        print(num)
    except ZeroDivisionError as err:
        print('This is a zero division error.')
        print(err)
        break
    except ValueError as err:
        print('This is not a number.')
        print(err)
