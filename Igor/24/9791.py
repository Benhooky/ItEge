from string import digits,ascii_uppercase
f=open("ItEge/Igor/24/24_9791 (2).txt").readline()
alhapebet=(digits+ascii_uppercase)[:16]
keeperS=""
listansw=[]
for e in f:
    keeperS+=e
    while keeperS[0] not in alhapebet[1:]:
        keeperS=keeperS[1:]
        if len(keeperS)==0:
            break
    if e not in alhapebet:
        listansw.append(len(keeperS)-1)
        keeperS=""
print(max(listansw))