maxR = 0
for N in range(1,13):
    R = bin(N)[2:]
    if N % 2  == 0:
        R = '10'+R 
    else: 
        R = '1'+ R + '01'
    R = int(R, 2)
    maxR = max(maxR, R)
print(maxR)