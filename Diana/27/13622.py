f=open('ItEge/Diana/27/27A_13622.txt')
K=int(f.readline())
N=int(f.readline())
lst=sorted([int(x) for x in f])
alreadyUsed=[]
cnt=0

for i in range(N-1):
    for j in range(i+1,N):
        if (lst[i]+lst[j]>K) and (i not in alreadyUsed) and (j not in alreadyUsed):
            alreadyUsed.append(i)
            alreadyUsed.append(j)
            cnt+=1
print(cnt*2)