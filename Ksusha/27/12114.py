f=open('ItEge/Ksusha/27/27A_12114 (1).txt')
k=int(f.readline())
n=int(f.readline())
maxSum=0
lst=[int(x) for x in f]
for i in range(n-2*k):
    for j in range(i+k,n-k):
        for l in range(j+k,n) :
            maxSum=max(maxSum,lst[i]+lst[l]+lst[j])
print(maxSum)