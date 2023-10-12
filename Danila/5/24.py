
for N in range(2, 1000):
    s = bin(N)[2:]
    s = s[:-1] + s[1] * 2
    R = int(s, 2)
    if R > 76:
        print(N)
        break
