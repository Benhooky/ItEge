file=open('Kate/26.txt')
N=int(file.readline()[:-1])
a=[]
for i in range(N):
    a.append(int(file.readline()[:-1]))
a.sort()
a.reverse()
current=a[0]
cnt=1
for i in range(1,N):
    if (current-a[i])>=3:
        current=a[i]
        cnt+=1
print(cnt,current)