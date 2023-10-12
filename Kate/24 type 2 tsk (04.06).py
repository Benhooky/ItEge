S=open("Kate/24(2)(04.06).txt").readline()[:-1]
keeperS=""
Latters="DR"
Numbers="18"
Max=0
for i in range(len(S)):
    keeperS+=S[i]
    if len(keeperS)==2:
        if (keeperS[0] in Latters):
            if keeperS[-1] in Numbers:
                keeperS=keeperS[1:]
            else:
                keeperS=""
        elif (keeperS[-1] in Latters):
            keeperS=""
    if len(keeperS)>=3:
        if keeperS[-1] in Numbers and keeperS[-2] in Numbers and keeperS[-3] in Numbers:
            Max=max(Max,len(keeperS)-3)
            keeperS=keeperS[-2:]
            continue
        if keeperS[-1] in Latters and keeperS[-2] in Latters:
            Max=max(Max,len(keeperS)-1)
            keeperS=""
            continue
        if keeperS[-1] in Latters and keeperS[-2] in Numbers and keeperS[-3] in Latters:
            Max=max(Max,len(keeperS)-2)
            keeperS=""
            continue
Max=max(Max,(len(keeperS)-1)//3)
print(Max//3)