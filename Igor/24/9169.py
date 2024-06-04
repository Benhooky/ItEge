f = open("ItEge/Igor/24/24_9169.txt").readline()
keeperS=""
listansw=[]
for e in f:
    keeperS+=e
    if len(keeperS)>2:
        while "BAD" != keeperS[0:3] and "FAT" != keeperS[0:3]:
            keeperS=keeperS[1:]
            if len(keeperS)==0:
                break
    if keeperS.count("BAD")+keeperS.count("FAT")==3:
        listansw.append(len(keeperS))
        keeperS=keeperS[1:]
print(min(listansw))