f=open('ItEge/Diana/27/27B_13622.txt')
K=int(f.readline())
N=int(f.readline())
lst=sorted([int(x) for x in f])
cnt=0
i=0
j=1
while i<len(lst)-1:
    if (lst[i]+lst[j]>K):
        lst.pop(i)
        lst.pop(j-1)
        cnt+=1
        j=i+1
    elif j!=len(lst)-1:
        j+=1
    else:
        i+=1
        j=i+1
print(cnt*2)