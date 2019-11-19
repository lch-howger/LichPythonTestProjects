print(2 ** 3)
print(3 ** 3)


def raise_to_power(base, pow):
    num = 1
    for i in range(pow):
        num = num * base
    return num


print(raise_to_power(2, 3))
print(raise_to_power(3, 3))
