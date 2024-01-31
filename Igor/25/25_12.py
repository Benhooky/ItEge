import re
for i in range(2024,10**10+1,2024):
    if re.fullmatch(r'3\d{1}2258\d*4',str(i)):
        print(i)