def F(n,a):
    s = ''
    while n>0:
        s = str(n%a) + s
        n//=a
    return s
for n in range(1000000,1,-1):
    s=F(n,7)
    if s.count("2")%2==0:
        s+="555"
    else:
        s="1"+s
    r=int(s,7)
    if r<3799:
        print(n)
        break
