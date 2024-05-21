f = open('ItEge/Ksusha/27/27A_13622 (1).txt')
cnt=0
k=int(f.readline())
N=int(f.readline())
lst=sorted(int(i) for i in f)
for x in range(N-1):
    for j in range(x+1,N):
        if (lst[x]+lst[j])>k:
            cnt+=2
            lst[j]=-1000000000000000000
            lst[x]=-1000000000000000000
print(cnt)