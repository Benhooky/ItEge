file=open('Kate/107_26.txt')
NumperOfAliveTree=int(file.readline()[:-1])
Tree=[]
MaxRow=0
MinNum=200000000
for i in range(NumperOfAliveTree):
    Row,RowNum=file.readline()[:-1].split()
    Row=int(Row)
    RowNum=int(RowNum)
    if Row in Tree:
        Tree[Tree.index(Row)].append(RowNum)
    else: 
        Tree.append([int(Row),int(RowNum)])
Tree.sort()
for i in range(len(Tree)-13):
    for j in range(i+13,len(Tree)):
        if Tree[i][0]==Tree[j][1]:
            MaxRow=max(MaxRow,Tree[i][0]+1)
            MinNum=min(MinNum,Tree[j][1]+1)
            break
print(MaxRow,MinNum)