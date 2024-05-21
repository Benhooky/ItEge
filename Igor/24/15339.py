f = open("ItEge/Igor/24/24_15339.txt").readline()[:-1]
letters='ABC'
digits="6789"
KeeperS=""
listansw=[]
for e in f:
    KeeperS+=e 
    if len(KeeperS) >= 2:
        if (KeeperS[-1] in letters and KeeperS[-2] in letters) or (KeeperS[-1] in digits and KeeperS[-2] in digits):
            listansw.append(len(KeeperS)-1)
            KeeperS=KeeperS[-1]
print(max(listansw))