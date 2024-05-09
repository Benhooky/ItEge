def f5(x):
    if x>=0:
        return False
    else:
        x=abs(x)
        while x:
            if x%5==1:
                return False
            x=x//5
    return True
f=open('ItEge/Diana/27/27A_2495.txt')
N,K,D = [int(x) for x in f.readline().split()]
lst= [int(x) for x in f]
res=[]
for i in range(N):
    for j in range(i+1,N-1):
        cntUnique = len([x for x in lst[i:j+1] if f5(x)])
        if cntUnique%K==0:
            if sum(lst[i:j+1])%D==0:
                res.append(sum(lst[i:j+1]))
print(max(res))