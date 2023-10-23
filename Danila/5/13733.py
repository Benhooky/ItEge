min1 = 1000000000000
for N in range(1, 1000):
    s = bin(N)[2:]
    sum1 = s.count('1')
    s += str(sum1 % 2)
    sum1 = s.count('1')
    s += str(sum1 % 2)
    R = int(s, 2)
    if R > 83:
        min1 = min(R, min1)
print(min1)
