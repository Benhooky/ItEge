cnt=0
a=[]
for N in range(245690,245756+1):
    flag=True
    cnt+=1
    for j in range(2,int(N**(1/2))+1):
        if N%j==0:
            flag=False
        if (N//j)%2==0:flag=False
    if flag:
        a.append(N)
        a.append(cnt)
print(a)