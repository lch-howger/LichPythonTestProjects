file = open('test.txt', 'r')

print(type(file))

for line in file:
    print(line)

file.close()
