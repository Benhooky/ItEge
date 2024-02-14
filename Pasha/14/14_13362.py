def five(a):
    b = ''
    while a != 0:
        b += str(a % 5)
        a //= 5
    return b[::-1]
s = 125 + 25 ** 3 + 5 ** 9
print(five(s))