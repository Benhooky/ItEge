minR = 1000000000000
for N in range(1,1000):
    s = bin(N)[2:]
    s+=bin(N%4)[2:]
    R = int(s,2)
    if R>20:
        minR = min(minR,R)
print(minR)


d = {1:'4234',2:'42334'}
print(d[1])