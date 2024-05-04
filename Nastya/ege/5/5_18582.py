minR = 10000000000
for N in range(1000,0,-1):
    s = bin(N)[2:]
    if s.count('1') > s.count('0'):
        s += "1"
    else:
        s += '0'
    R = int(s, 2)
    if R > 100:
        minR = min(minR,R)
print(minR)