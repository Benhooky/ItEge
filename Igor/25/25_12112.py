import re
for i in range(3057,10**9+1,3057):
    if re.fullmatch(r"1\d{1}58\d*5\d{1}9",str(i)):
        print(i,i//3057)