minr=100000
nLast=0
for n in range(1,100000):
    r=bin(n)[2:]
    if n%5==0:
        r=r[0]+r[1]+r[2]+r
    if n%5>0:
        r=r+bin((n%3)*5)[2:]
    R=int(r,2)
    if R>39000:
        if minr>R:
            minr=R
            nLast=n
print(minr,nLast)