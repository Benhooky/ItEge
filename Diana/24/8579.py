
f=open('ItEge/Diana/24/24_8579.txt').readline()
maxLen=0
keeperS=''
flag = True
for element in f:
    keeperS+=element
    if keeperS[0] not in '0123456789':
        keeperS=''
    if len(keeperS)!=0:
        if keeperS[0] in '0123456789' and flag:
            flag = False
            a=int(keeperS[0])
            goodNumbers = {a}
    if element in '0123456789' :
        if a%2!=int(element)%2:
            goodNumbers.add(int(element))
            if len(goodNumbers)==3:
                goodNumbers.clear()
                goodNumbers.add(int(element))
                keeperS=keeperS[-1]
                a = int(keeperS[0])
            else:
                maxLen=max(maxLen,len(keeperS))
        else:
            goodNumbers.add(int(element))
            if len(goodNumbers)==3:
                goodNumbers.remove(a)
                for j in goodNumbers:
                    if j!=element:
                        b = j
                keeperS=keeperS[keeperS.index(str(b)):]
                a=int(keeperS[0])
            else:
                maxLen=max(maxLen,len(keeperS))
print(maxLen)