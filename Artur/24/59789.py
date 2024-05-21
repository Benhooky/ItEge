f = open('ItEge/Artur/24/24 (4).txt').readline()
keeperS = ''
maxLen = 0
for letter in f:
    keeperS += letter
    if keeperS.count('Y')==101:
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS = keeperS[keeperS.index('Y')+1:]
print(maxLen)