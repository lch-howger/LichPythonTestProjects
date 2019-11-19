colors = ['blue', 'red', 'yellow']
numbers = [1, 2, 3, 4, 5]

colors.extend(numbers)
print(colors)

colors.append(numbers)
print(colors)

colors.append('abc')
print(colors)

element = colors.pop()
print(element)
print(colors)

element = colors.pop()
print(element)
print(colors)

element = colors.pop(0)
print(element)
print(colors)

element = colors.pop(0)
print(element)
print(colors)

print(colors.index('yellow'))

colors.append('yellow')
print(colors)
print(colors.count('yellow'))

colors = ['yellow', 'red', 'blue']
print(colors)
colors.sort()
print(colors)

numbers=[6,2,8,5,4,3,6]
print(numbers)
numbers.sort()
print(numbers)
