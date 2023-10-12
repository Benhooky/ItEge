import sys
minR = sys.maxsize
for i in range(1, 1000):
    N = bin(i)[2:]
    if i % 3 == 0:
        N += N[-3:]
    else:
        N += bin((i % 3)*3)[2:]
    R = int(N, 2)
    if R > 151:
        minR = min(R, minR)
print(minR)
