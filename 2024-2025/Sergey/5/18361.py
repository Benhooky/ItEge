minR=10000000
for N in range(1,1000):
    s=bin(N)[2:]
    sum1=0
    for x in s:
        sum1+=int(x)
    if sum1%2==0:
        s=s+"0"
        s="10"+s[2:]
    else:
        s=s+"1"
        s="11"+s[2:]
    R=int(s,2)
    if R>171:
        minR=min(minR,R)
print(minR)