minR = 10000000
for N in range(1,1000):
    s=bin(N)[2:]
    N=N-s.count("0")
    b=bin(N)[2:]
    x=b[-3:]
    b= str(x) + b
    R=int(b,2)
    if R>224:
        minR = min(minR,R)
print(minR)
