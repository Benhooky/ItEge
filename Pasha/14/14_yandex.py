import sys
f1 = sys.maxsize
f = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
s = []
while f != 0:
    s.append(f % 49)
    f //= 49
print(sum(s))