def bi(x):
    s=''
    while x:
        s=str(x%2)+s
        x=x//2
    return s
res=[]
for n in range(1000):
    biN=bi(n)
    if biN.count('1')%2==0:
        biR=biN+'00'
    else:
        biR=biN+'10'
    R=int(biR,2)
    if R>96:
        res.append(R)
    print(n,R)
print(min(res))