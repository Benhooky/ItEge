file=open("Kate/26_7274.txt")
Num=int(file.readline()[:-1])
Trees=[]
rad=[]
for i in range(Num):
    NumR,NumTrees=map(int,file.readline().split())
    if NumR not in rad:
        Trees.append([NumR,NumTrees])
        rad.append(NumR)
    else:
        Trees[rad.index(NumR)].append(NumTrees)
        #Trees[rad.index(NumR)]=Trees[rad.index(NumR)][0]+Trees[rad.index(NumR)][1:].sort()
for i in range(len(Trees)):
    firstSymbol=Trees[i][0]
    Trees[i]=[firstSymbol]+sorted(Trees[i][1:])
Trees.sort()
flag=False
for i in range(len(Trees)-1,0,-1):
    for j in range(1,len(Trees[i])-1):
        if Trees[i][j+1]-Trees[i][j]==14:
            print(Trees[i][0],Trees[i][j]+1)
            flag=True
            break
    if flag:break