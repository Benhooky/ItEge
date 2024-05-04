f = open("probnik/24var04.txt").readline()[:-1]
max1=0
keeperS=""
for i in f:
    keeperS+=i
    if keeperS.count("A")>=700 or keeperS.count("E")==0:
        max1=max(max1,len(keeperS)-1)
    keeperS=keeperS[keeperS.index(i)+1:]
print(max1)