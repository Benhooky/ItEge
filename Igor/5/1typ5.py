def six(x):
    s = ""
    while x > 0:
        s = str(x % 6) + s
        x //= 6
    return s


min
for n in range(1, 1000):
    s = six(n)
    if n % 3 == 0:
        s = s + s[:2]
    else:
        s = int(s)
        ost = (s % 3) * 10
        s = str(s)
        s = s + six(ost)
    r = int(s, 6)
    if r > 680:
        print(r)
        break
