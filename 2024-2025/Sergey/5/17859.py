maxR = 0
for N in range(1,13):
    s = bin(N)[2:]
    if N%2==0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    R = int(s,2)
    maxR = max(maxR,R)
print(maxR)