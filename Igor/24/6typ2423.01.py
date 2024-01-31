f = open("ItEge/Igor/24/24 (2).txt").readline()[:-1]
max1=0
keeperS=""
for i in f:
    keeperS+=i
    if keeperS.count("X")>1 or keeperS.count("Y")>1:
        if keeperS[:-1].count("X")==1 and keeperS[:-1].count("Y")==1:
            max1=max(max1,len(keeperS)-1)
        keeperS=keeperS[keeperS.index(i)+1:]
print(max1)