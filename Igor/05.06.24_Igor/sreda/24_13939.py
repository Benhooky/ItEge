f = open("probnik/sreda/24_13939.txt").readline()
listansw=[]
keeperS=""
troi="0123"
cnt=0
for e in f:
    keeperS+=e
    if e in troi and e[0]!="0":
        cnt+=1
        keeperS=''
print(cnt)