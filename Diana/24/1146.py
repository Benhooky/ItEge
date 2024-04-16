f=open("ItEge/Diana/24/24_1146.txt").readline()
keeperS = ''
maxLen = 100000000

for element in f:
    keeperS+=element
    if keeperS[0]!='D':
        keeperS=''
    if len(keeperS)>1 and keeperS[-2]=="D":
        if element!='D':
            maxLen=min(maxLen,len(keeperS)-1)
            keeperS=''
if len(keeperS)!=0 :
    maxLen= min(maxLen,len(keeperS))
print(maxLen)