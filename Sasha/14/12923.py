from string import digits, ascii_uppercase
alph = digits+ascii_uppercase
f = 3*3125**9+2*625**8-4*625**7+3*125**6-2*25**5-2024
d = 25
s = ''
while f>0:
    s = alph[f%d] + s
    f//=d
print(s.count('0'))
print(s)