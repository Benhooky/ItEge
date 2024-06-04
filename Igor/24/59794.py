f = open("ItEge/Igor/24/24 (9).txt").readline()[1:]
keeperS=""
listansw=[]
for e in f:
    keeperS+=e
    while keeperS[0]!="U":
        keeperS=keeperS[1:]
        if len(keeperS)==0:
            break
    if keeperS.count("U")==110:
        listansw.append(len(keeperS))
        keeperS=keeperS[1:]
print(min(listansw))