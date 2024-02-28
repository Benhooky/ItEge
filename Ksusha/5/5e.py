for n in range(100000,1,-1):
    k=n
    dv=''
    while k>0:
        s=k%7
        dv=str(s)+dv
        k=k//7
    if dv.count('2')%2==0:
        dv+='555'
    else:
        dv='1'+dv
    r=int(dv,7)
    if r<3799:
        print(n)
        break