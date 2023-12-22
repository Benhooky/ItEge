f = open("ItEge/Ksusha/24/24_11241.txt").readline()
keeperS = ""
BAD = "ABCD"
maxLen = 0
for i in f:
    keeperS+=i
    if i in BAD:
        maxLen = max(maxLen,len(keeperS)-1)
        keeperS = ""
print(maxLen)