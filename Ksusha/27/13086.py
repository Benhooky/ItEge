f = open('ItEge/Ksusha/27/27-A_13086 (1).txt')
cnt=0
answer=[]
k=int(f.readline())
N=int(f.readline())
lst=[int(i) for i in f]
for x1 in range(N-2*k):
    for x3 in range(x1+2*k,N):
        for x2 in range(x1+1,x3):
            answer.append(lst[x1]+lst[x2]+lst[x3])
print(max(answer))