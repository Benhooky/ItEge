def F(n):
    s=""
    while n>0:
        s= str(n%3) + s
        n//=3
    return s
res=[]
for x in range(1,10000):
    a=0
    R=0
    for i in F(x):
        a+=int(i)
    if a%4==0:
        R= int(("1"+F(x)[:-2]),3)
    else:
        R=int((F(x)+F(a%4*3)),3)
    if R>353:
        res.append(R)
print(min(res))