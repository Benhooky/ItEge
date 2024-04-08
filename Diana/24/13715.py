f=open("C:/progs/06.04/24_13715.txt").readline()
maxLen=0
keeperS=''
for letter in f:
    keeperS+=letter
    if keeperS.count('AB')>50:
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=keeperS[keeperS.index('AB')+1:]
if len(keeperS)!=0:
    maxLen=max(maxLen,len(keeperS))
print(maxLen)
