from re import fullmatch
for i in range(2658,10**9,2658):
    if fullmatch(r'85\d{1}16\d{0,}4',str(i)):
        print(i,i//2658)