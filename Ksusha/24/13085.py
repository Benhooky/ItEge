f=open('ItEge/Ksusha/24/24_13085.txt').readline()[:-1]
keeperS=''
max_k=0
for letter in f:
    keeperS+=letter
    if keeperS.count('X')==2 or keeperS.count('Y')==2:
        max_k=(max(max_k,len(keeperS)-1))
        keeperS=keeperS[keeperS.index('X')+1:] if keeperS.count('X')==2 else keeperS[keeperS.index('Y')+1:]
max_k=(max(max_k,len(keeperS)))
print(max_k)
