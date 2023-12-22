f = open("ItEge/Ksusha/24/24_2024 (1).txt").readline()
keeperS = ""
i = 0
maxLen = 0
while keeperS.count("T")<100:
    keeperS+=f[i]
    i+=1
for letter in f[i:]:
    keeperS += letter
    if keeperS.count("T")>100:
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS = keeperS[keeperS.index("T")+1:]
print(maxLen)