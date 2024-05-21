f = open("ItEge/Igor/24/24 (5).txt").readline()[:-1]
listanswer=[]
KeeperS=""
for e in f:
    KeeperS+=e
    while KeeperS[0]!="T":
        KeeperS=KeeperS[1:]
        if len(KeeperS)==0:
            break
    if KeeperS.count("T") == 210:
        listanswer.append(len(KeeperS))
        KeeperS=KeeperS[1:]
print(min(listanswer))