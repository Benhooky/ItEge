a= [int (x) for x in open('Misha/27_A_7627.txt')]
time=a[0]
maxa=0
for x in range (2,len(a)-time):
    for y in range (x+time,len(a)):
        maxa=max(maxa,a[x]+a[y])
print (maxa)
    
