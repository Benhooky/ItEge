f=open('ItEge/Ksusha/24/24_13100 (1).txt').readline()[:-1]
keeperS=''
max_k=0
for letter in f:
    keeperS+=letter
    if keeperS.count('D')==3 or keeperS.count('C')==3:
        max_k=max(max_k,len(keeperS)-1 )
        keeperS=keeperS[keeperS.index('C')+1:] if keeperS.count('C')==3 else keeperS[keeperS.index('D')+1:]
keeperS=keeperS[keeperS.index('C')+1:] if keeperS.count('C')==3 else keeperS[keeperS.index('D')+1:]
print(max_k)