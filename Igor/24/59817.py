f = open("ItEge/Igor/24/24 (7).txt").readline()[1:]
keeperS=""
listansw=[]
alphabet="ABC"
for e in f:
    keeperS+=e
    if len(keeperS)>1:
        if keeperS[-1] in alphabet and keeperS[-2] in alphabet:
            listansw.append(len(keeperS)-1)
            keeperS=keeperS[-1]
print(max(listansw))