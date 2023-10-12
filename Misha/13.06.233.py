a=[int (x) for x in open('Misha/17 (1).txt')]
k=0
s=0
maxa=0
m=0
for x in range (len(a)-1):
    for y in range (x+1,len(a)):
        if((a[x]+a[y])%60==0 and (a[x]%40==0 or a[y]%40==0)):
            maxa=max(maxa,a[x]+a[y])
            m+=1         
print(m,maxa)
