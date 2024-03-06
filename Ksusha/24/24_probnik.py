f = open('ItEge/Ksusha/24/24_11667 (1).txt').readline()[:-1]
keeperS = ''
maxLen = 0
for i in f:
    keeperS += i
    if keeperS.count('INFINITY')==1001:
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS = keeperS[keeperS.index('INFINITY')+1:]
maxLen = max(maxLen,len(keeperS))
print(maxLen)