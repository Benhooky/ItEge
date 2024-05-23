s=open('ItEge/Ksusha/27/27_A (3).txt')
n=int(s.readline())
BestList = []
lst=[int(i) for i in s]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        summ=sum(lst[i:j+1])
        if (summ%89==0) and (summ%len(lst[i:j+1])==0):
            if summ>sum(BestList):
                BestList = lst[i:j+1]
            elif (summ==sum(BestList)) and (len(lst[i:j+1])<len(BestList)):
                BestList = lst[i:j+1]
print(len(BestList))