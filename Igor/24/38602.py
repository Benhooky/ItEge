f=open("ItEge/Igor/24/24 (8).txt").readline()
listansw=[]
keeperS=""
for e in f:
    keeperS+=e
    if "PP" in keeperS:
        listansw.append(len(keeperS)-1)
        keeperS=keeperS[-1]
print(max(listansw)) 