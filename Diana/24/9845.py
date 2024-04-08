f=open("ItEge/Diana/24/24_9845 (2).txt").readline()
keeperS=f[0]
maxLen=0
digits='89'
letters='ABC'
for element in f[1:]:
    keeperS+=element
    if (keeperS[-2] in letters and keeperS[-1] in letters) or (keeperS[-2] in digits and keeperS[-1] in digits):
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=keeperS[-1]
if len(keeperS)!=0:
    maxLen= max(maxLen,len(keeperS))
print(maxLen)