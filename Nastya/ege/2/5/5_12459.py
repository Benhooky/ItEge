def perevod(n,a):
    x = ''
    while n>0:
        x = str(n%a) + x
        n //=a
    return x
for N in range(10000,0,-1):
    s=perevod(N,4)
    if len(s)%2==0:
        s=s[:len(s)//2]+'0'+s[len(s)//2:]
    R=int(s)
    if R<=180:
        print(N)
        break