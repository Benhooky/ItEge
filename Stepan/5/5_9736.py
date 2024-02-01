maxR = 0
for n in range(100000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3:]
    else:
        s += bin((n % 3) * 3)[2:] 
    r = int(s, 2) 
    if r <= 170:
        maxR = max(maxR, r)
print(maxR)