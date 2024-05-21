from string import digits,ascii_uppercase
f = open("ItEge/Igor/24/24_59848.txt").readline()[:-1]
alphabet = (digits+ascii_uppercase)[:24]
keeperS=""
listansw=[]
for e in f:
    keeperS+=e
    while keeperS[0]=="0" and keeperS[0] not in alphabet:
        keeperS=keeperS[1:]
        if len(keeperS)==0:
            break
    if keeperS[-1] not in alphabet:
        listansw.append(len(keeperS)-1)
        keeperS=''
print(max(listansw))