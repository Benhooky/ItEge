cnt=0
a=[]
for N in range(245690,245756+1):
    flag=True
    cnt+=1
    for j in range(2,int(N**(1/2))+1):
        if N%j==0:
            flag=False
            break
    if flag:
        print(cnt,N)