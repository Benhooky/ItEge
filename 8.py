f = open("ItEge/24-181.txt").readline()
keeperS = ""
maxLen = 0
for i in range(len(f)):
    keeperS+=f[i]
    if "Y" in keeperS:
        maxLen = max(maxLen, len(keeperS)-1)
        keeperS = ""
    if keeperS.count('.')==6:
        maxLen = max(maxLen, len(keeperS)-1)
        keeperS = keeperS[keeperS.index('.')+1:]
print(maxLen)
    