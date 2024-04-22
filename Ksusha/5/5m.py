lis=[]
for n in range(1,1000):
    s=n
    tr=''
    while s>0:
        tr+=str(s%3)
        s//=3
    tr = tr[::-1]
    if n%7==0:
        tr+=tr[-2:]
    else:
        os=''
        f=(n%7)*3
        while f > 0:
            os += str(f % 3)
            f = f // 3
        os = os[::-1]
        tr+=os
    r= int((tr),3)
    if r>369:
        lis.append(r)
print(min(lis))


