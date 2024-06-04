f = open("probnik/24_11954.txt").readline()
lisansw=[]
keeperS=""
for e in f:
    keeperS+=e
    if "X"*500 in keeperS and "Y" not in keeperS:
        lisansw.append(len(keeperS)-1)
        lisansw=lisansw[-1]
print(min(lisansw))