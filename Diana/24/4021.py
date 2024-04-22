f=open('C:/progs/20.04/24_4021.txt').readline()
maxLen=0
keeperS=''
for element in f:
    keeperS+=element
    if keeperS.count('.')>5:
        maxLen=max(maxLen,len(keeperS)-1)
        keeperS=keeperS[keeperS.index('.')+1:]
if len(keeperS)!=0:
    maxLen=max(maxLen,len(keeperS))
print(maxLen)
