f=open('ItEge/Diana/24/24_4203.txt').readline()
maxLen=0
f = f.replace('AB','*')
f = f.replace('CB','*')
keeperS=''
for element in f:
    keeperS+=element
    if keeperS[-1]!='*':
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS=''
if len(keeperS)!=0:
    maxLen=max(maxLen,len(keeperS))
print(maxLen)

