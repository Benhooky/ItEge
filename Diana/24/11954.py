
f=open("ItEge/Diana/24/24_11954 (3).txt").readline()
keeperS = ''
maxLen = 0
for element in f:
    keeperS+=element
    if keeperS[0]!='X':
        keeperS=''
    if element == 'Y':
        keeperS = ''
    if keeperS.count('X')==500:
        maxLen=max(maxLen,len(keeperS))
        keeperS=keeperS[1:]
        keeperS = keeperS[keeperS.index('X'):]
if len(keeperS)!=0:
    maxLen= max(maxLen,len(keeperS))
print(maxLen)