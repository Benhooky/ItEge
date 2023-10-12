minR = 10000000000000000000
for N in range(1, 1000):
    s = bin(N)[2:]
    sum_of_our_s = sum(map(int, s))
    s += str(sum_of_our_s % 2)
    sum_of_our_s = sum(map(int, s))
    s += str(sum_of_our_s % 2)
    R = int(s, 2)
    if R > 43:
        minR = min(minR, R)
print(minR)
