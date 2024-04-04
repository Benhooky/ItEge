f = open('ItEge/Diana/24/24.3_14642.txt').readline()
maxLen = 0
keeperS = ''
for letter in f:
    keeperS += letter
    if keeperS.count('F')>1:
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS = keeperS[keeperS.index('F')+1:]
if len(keeperS)!= 0: 
    maxLen = max(maxLen,len(keeperS))
print(maxLen)