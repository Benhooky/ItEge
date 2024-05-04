min_N = 1000000000000000
for N in range(1000):
    s = bin(N)[2:]
    if N % 8 == 0:
        s += s[-2:]
    else:
        s += (bin((N % 8)* 2)[2:])
    R = int(s, 2)
    if R > 3000:
        min_N = min(min_N, N)#правильно но криво и непрофессионально
        #print(N) правильно и профессионально
        #break
print(min_N)


