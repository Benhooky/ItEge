from re import fullmatch

for i in range(83,10**6+1,83):
    if fullmatch(r'1\d{0,}578\d{0,}',str(i)):
        print(i,i//83)