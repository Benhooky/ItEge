import re
for i in range (273,10**8+1,273):
    if re.fullmatch(r"12\d{2}36\d{0,}1",str(i)):
        print(i,i//273)