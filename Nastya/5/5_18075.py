minR = 10000000000
for N in range(1,1000):
    s = bin(N)[2:]
    sumBin = s.count('1')
    s += str(sumBin % 2)
    sumBin = s.count('1')
    s += str(sumBin % 2)
    R = int(s, 2)
    if R > 123:
        minR = min(minR,R)
print(minR)