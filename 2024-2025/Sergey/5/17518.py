minN=10000
for N in range(1,1000):
    s=bin(N)[2:]
    sum0 = 0
    for x in s:
        sum0+=int(x)
    if sum0%2==0:
        s="10"+ s[2:] +"0"
    else:
        s="11"+s[2:]+"1"
    R=int(s,2)
    if R>50:
        minN=min(minN,N)
print(minN)