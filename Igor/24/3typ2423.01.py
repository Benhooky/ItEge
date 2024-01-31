f = open("ItEge/Igor/24/24_demo (1).txt").readline()[:-1]
keeperS=""
max1=0
for i in f:
    keeperS+=i
    if i != "Y":
        max1=max(max1,len(keeperS)-1)
        keeperS=""
print(max1)
