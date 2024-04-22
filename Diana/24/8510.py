from itertools import product
f=open('ItEge/Diana/24/24_8510.txt').readline()
maxLen=0
keeperS=''
lst =[''.join(x) for x in product('NOP',repeat=2)]
for element in f:
    keeperS+=element
    if any(x in keeperS for x in lst):
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=keeperS[-1]
        print(maxLen)
if len(keeperS)!= 0:
    maxLen=max(maxLen,len(keeperS))