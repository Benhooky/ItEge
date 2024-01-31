f = open("ItEge/Igor/24/24 (1).txt").readline()[:-1]
max1=0
keeperS=""
for i in f:
    keeperS+=i
    if keeperS[-1]=="E":
        if keeperS.count("A")>=3:
            max1=max(max1,len(keeperS)-1)
            keeperS=""
        else:
            keeperS=""
print(max1)