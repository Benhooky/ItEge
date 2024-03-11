def F(x):
    s=""
    while x>0:
        s =str(x%4) + s
        x=x//4
    return s
r=0

for N in range(10000,1,-1):
    a=F(N)
    if (len(a)-a.count("0"))%2==0:
        r = int(a[:(len(a) // 2)] + "0" + a[(len(a) // 2 + 1):])
    else:
        r=int(a)
    if r<180:
        print(N)
        break