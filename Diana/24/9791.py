f=open("ItEge/Diana/24/24_9791 (1).txt").readline()
keeperS = ''
maxLen = 0
alph16 = '0123456789ABCDEF'
for element in f:
    keeperS+=element
    if keeperS[0]=='0':
        keeperS=''
    if element not in alph16:
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=''
if len(keeperS)!=0:
    maxLen= max(maxLen,len(keeperS))
print(maxLen)