def thr(a):
    b = ''
    while a != 0:
        b += str(a % 3)
        a //= 3
    return b[::-1]
mn = 100000000000
for n in range(1, 1000):
    s = thr(n)
    s += s[-2:] if n % 7 == 0 else thr((n % 7) * 3)
    r = int(s, 3)
    if r > 369:
        mn = min(r, mn)
print(mn)
