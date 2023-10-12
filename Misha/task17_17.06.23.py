a=[int (x) for x in open('Misha/17 (3).txt')]
max3=0
maxa=0
k=0
for x  in range (len(a)):
    if len(str(a[x]))==3:
        max3=max(max3,a[x])
for x  in range (len(a)-1):
    if (len(str(a[x]))==3)^(len(str(a[x+1]))==3):
        if (a[x]+a[x+1])%max3==0:
            k+=1
            maxa=max(maxa,a[x+1]+a[x])
print(k,maxa)
        
