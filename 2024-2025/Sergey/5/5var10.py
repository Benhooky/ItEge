minR=100000000
for N in range(1,1000):
    s=''
    sum0=0
    while N>0:
        s = str(N%3) + s
        N//=3
    if N%3==0:
        s=s[-2:] +s
    else:
        for elem in s:
            sum0+=int(elem)
        x=""
        while sum0>0:
            x = str(sum0%3) + x
            sum0//=3
        s=x+s
    R=int(s,3)
    if R>418:
        if R%2!=0:
            minR=min(minR,R)
print(minR)