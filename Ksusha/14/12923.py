from string import ascii_uppercase,digits
alph = digits+ascii_uppercase
def f(value,system):
    s = ''
    while value>0:
        s = alph[value%system]+s
        value//=system
    return s
result = f(3*3125**9+2*625**8-4*625**7+3*125**6-2*25**5-2024,25)
print(result)
print(result.count('0'))
