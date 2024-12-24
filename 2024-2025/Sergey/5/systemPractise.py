from string import ascii_uppercase,digits
alph = (digits + ascii_uppercase)[:13]
for N in range(151,10000):
    binN =bin(N)[2:]
    number = N
    triN = ''
    while number > 0:
        triN += str(number%3)
        number //= 3
    triN = triN[::-1]
    hexN = hex(N)[2:]
    N13 = ''
    number = N
    while number > 0:
        N13 += alph[number%13]
        number //= 13
    N13 = N13[::-1]
    pass