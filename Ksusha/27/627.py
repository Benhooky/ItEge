s=open('ItEge/Ksusha/27/27B.txt')
cnt=0
first=[int(i) for i in s.readline().split()]
n=first[0]
k=first[1]
lst=[int(i) for i in s]
for i in range(n-k+1):
    flag = True
    buffer = lst[i:i+k]
    if (sum(buffer[:k//2]) == sum(buffer[k//2+1:])) and buffer.count(0)>0:
        cnt+=1
print(cnt)