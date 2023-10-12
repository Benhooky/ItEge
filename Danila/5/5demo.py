Danila = 10000000000000
for i in range(1, 1000):
    N = bin(i)[2:]
    if i % 3 == 0:
        N = N + N[-3:]
    else:
        N = N + bin(i % 3*3)[2:]
    R = int(N, 2)
    if R > 151:
        Danila = min(Danila, R)
print(Danila)
