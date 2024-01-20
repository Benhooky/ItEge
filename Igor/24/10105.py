f = open("ItEge/Igor/24/24_10105.txt").readline()
keeperS = ""
max1 = 0
for i in f:
    keeperS+=i
    if keeperS.count("T")>100:
        max1=max(max1,len(keeperS)-1)
        keeperS=keeperS[keeperS.find("T")+1:]
print(max1)
