f=open('ItEge/Diana/24/24var04.txt').readline()
keeperS=''
maxLen=0
for element in f:
    keeperS+=element
    if element=='E':
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=''
    if keeperS.count('A')>700:
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=keeperS[keeperS.index('A')+1:]
if len(keeperS)!=0:
    maxLen=max(maxLen,len(keeperS))
print(maxLen)