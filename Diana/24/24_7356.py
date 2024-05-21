f=open('ItEge/Diana/24/24_7356.txt').readline()
lst= [x for x in f]
keeperS=''
pairs=['CA','DA','FA','CO','DO','FO']
maxLen=0
cntPairs=0
for element in lst:   
    keeperS+=element
    if len(keeperS)>1:
        if keeperS[-2:] in pairs:
            cntPairs+=1
        if cntPairs>5:
            maxLen=max(maxLen,len(keeperS)-1)
            ind=[keeperS.find(x) for x in pairs if keeperS.find(x)!=-1]
            keeperS=keeperS[min(ind)+1:]
            cntPairs-=1
print(maxLen)
