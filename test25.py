file = open('test.txt', 'r')

# print(file.readable())

# print(file.read())

# print(file.readline())

# for line in file:
#     print(line)

# print(file.readlines())

print(type(file.readlines()))

for line in file.readlines():
    print(line)

file.close()
