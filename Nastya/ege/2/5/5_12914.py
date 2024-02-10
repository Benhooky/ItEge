maxR = 0
for N in range(1,1000):
    s = bin(N)[2:]
    if N%3==0:
        s = s.replace('0','11')
    else:
        s = s.replace('1','10')
    R = int(s,2)
    if R<=161:
        maxR = max(maxR,R)
print(maxR)