file=open ('Misha/27B.txt')
n=int(file.readline()[:-1])
gap=int(file.readline()[:-1])
a=[int(x)for x in file]
maxLeft=0
maxPair=0
for i in range(gap,n):
    maxLeft=max(maxLeft,a[i-gap])
    maxPair=max(maxPair,a[i]+maxLeft)
print(maxPair)
