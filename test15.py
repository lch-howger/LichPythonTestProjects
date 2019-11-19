num1 = input('Enter the first number: ')
operator = input('Enter the operator: ')
num2 = input('Enter the second number: ')

num1 = float(num1)
num2 = float(num2)

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('Invalid operator.')
