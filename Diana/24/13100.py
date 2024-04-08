f=open("ItEge/Diana/24/24_13100 (2).txt").readline()
maxLen=0
keeperS=''
for letter in f:
    keeperS+=letter
    if keeperS.count("C")>2 or keeperS.count("D")>2:
        maxLen=max(maxLen,len(keeperS)-1)
        if letter == 'C':
            keeperS=keeperS[keeperS.index('C')+1:]
        elif letter == 'D':
            keeperS=keeperS[keeperS.index('D')+1:]
if len(keeperS)!=0:
    maxLen=max(maxLen,len(keeperS))
print(maxLen)
