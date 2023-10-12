import sys
min0 = sys.maxsize
for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[-3:] if n % 3 == 0 else bin(n % 3 * 3)[2:]
    r = int(s, 2)
    if r > 151:
        min0 = min(min0, r)
print(min0)
