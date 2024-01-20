f = open("ItEge/Igor/24/24_11954.txt")
s = f.readline()
keeperS = ""
min1=10000000
for i in s:
    keeperS+=i
    if 'X' not in keeperS:
        keeperS=""
    elif keeperS[0]!='X':
        keeperS=keeperS[keeperS.find("X"):]
    if "Y" in keeperS:
        keeperS=""
    if keeperS.count("X")==500:
        min1=min(min1,len(keeperS))
        keeperS = keeperS[1:]
print(min1) 