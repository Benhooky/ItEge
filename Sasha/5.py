
for N in range(10000,1,-1):
    s = bin(N)[2:]
    if N%3==0:
        s += s[-3:]
    else:
        s += bin(N%3*3)[2:]
    R = int(s,2)
    if (R<500): 
        print(N)
        break