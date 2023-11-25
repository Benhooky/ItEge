minn =10000000
for n in range(1,1000):
    i = bin(n)[2:]
    if n%3==0:
        i = i + i[-3:]
    else:
        ost = (n%3)*3
        ost2=bin(ost)[2:]
        i = (i + ost2)
    r = int(i,2)
    if r > 151:
        minn = min(r,minn)
print(minn)