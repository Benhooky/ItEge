f=open('ItEge/Diana/27/27A_9078.txt')
N,D,T=[int(x) for x in f.readline().split()]
lst = [int(x) for x in f]
res=[]
for i in range(N-1):
    for j in range(i+1,N):
        if lst[i]%D!=0 and lst[j]%D!=0:
            cnt=0
            for c in lst[i+1:j]:
                if c%D==0:
                    cnt+=1
            if cnt==T:
                res.append(lst[i]+lst[j])
print(max(res))