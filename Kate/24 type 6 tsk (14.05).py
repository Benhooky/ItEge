S=open('24(6)(14.05).txt').readline()[:-1]
Max=0
keeperS=""
bad=['LDL','RDR','RLR','DLD','DRD','LRL']
for i in range(len(S)):
    keeperS+=S[i]
    if any(x in keeperS for x in bad):
        Max=max(Max,len(keeperS)-1)
        keeperS=keeperS[-3:]
Max=max(Max,len(keeperS)-1)
print(Max)