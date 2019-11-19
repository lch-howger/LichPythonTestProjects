month = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March'
}

print(month)

print(month['Jan'])
print(month['Feb'])
print(month['Mar'])

print(month.get('Jan'))
print(month.get('Feb'))
print(month.get('Abc'))

print(month.get('Abc', 'Not a valid key.'))
