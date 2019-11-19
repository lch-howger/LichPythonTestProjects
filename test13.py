is_male=True
is_tall=True

if is_male:
    if is_tall:
        print('you are male and you are tall')
    else:
        print('you are male and you are not tall')
else:
    if is_tall:
        print('you are not male and you are tall')
    else:
        print('you are not male and you are not tall')

if is_male or is_tall:
    print('you are male or you are tall')

if is_male and is_tall:
    print('you are male and you are tall')