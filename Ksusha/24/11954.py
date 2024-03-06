d=open('ItEge/Ksusha/24/24_11954 (2).txt').readline()[:-1]
keeperS=''
min_k=73479723974792972497
for letter in d:
    keeperS+=letter
    while keeperS[0]!='X':
        keeperS=keeperS[1:]
        if len(keeperS)==0:
            break
    if 'Y' in keeperS:
        keeperS=''
    if keeperS.count('X')==500 and keeperS.count('Y')==0:
        min_k=min(min_k,len(keeperS))
        keeperS = keeperS[keeperS.index('X')+1:]
print(min_k)