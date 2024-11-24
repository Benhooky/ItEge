minR=10000
for N in range(1,1000):
    s=bin(N)[2:]
    for i in range(2):
        sum0 = 0
        for x in s:
            sum0+=int(x)
        a=str(sum0%2)
        s=s+a
    R=int(s,2)
    if R>75:
        minR=min(minR,R)
print(minR)