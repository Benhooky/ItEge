s = open("ItEge/Igor/24/24_11241 (1).txt").readline()
keeperS = ""
max1=0
for i in s:
    keeperS+=i
    if keeperS[-1] in "ABCD":
        max1=max(max1,len(keeperS)-1)
        keeperS=""
print(max1)
    
