from string import digits,ascii_uppercase
f=open("ItEge/Igor/24/24_59849.txt").readline()
alhapebet=(digits+ascii_uppercase)[:26]
keeperS=""
listansw=[]
for e in f:
    keeperS+=e
    if e not in alhapebet:
        listansw.append(len(keeperS)-1)
        keeperS=""
print(max(listansw))