import re
for i in range(317,(10**8)+1,317):
    if re.fullmatch(r'12\d{2}1\d*56',str(i)):
        print(i,i//317)