from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
r=3*3125**9+2*625**8-4*625**7+3*125**6-2*25**5-2024
d = ''
while r>0:
    d=(alph[r%25])+d
    r //=25
print(d.count("0"))