from string import ascii_uppercase, digits
alph = digits + ascii_uppercase
for x in range(1,10001):
    s=6**900+6**10-x
    res=""
    while s>0:
        res+= alph[s%12]
        s//=12
    res=res[::-1]
    if res.count("3")==res.count("5"):
        print(x)