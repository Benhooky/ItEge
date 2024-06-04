f= open("ItEge/Igor/24/24_demo (2).txt").readline()
KeeperS=[]
listansw=[]
for e in f:
    KeeperS+=e
    while KeeperS[0]!="X":
        KeeperS=KeeperS[1:]
        if len(KeeperS)==0:
            break
    if len(KeeperS)>0:
        if not((((len(KeeperS)-1)%3==0) and e=="X") or (((len(KeeperS)-1)%3==1) and e=="Y") or (((len(KeeperS)-1)%3==2) and e=="Z")):
            listansw.append(len(KeeperS[:-1]))
            KeeperS=KeeperS[-1]
print(max(listansw))