def to_triple(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

for n in range(1, 1000):
    s = to_triple(n)
    if n % 2 == 0:
        s = "1" + s + "00"
    else:
        s = s + to_triple((s.count("1")) + (s.count("2") * 2))
    r = int(s, 3)
    if r > 168:
        print(n)
        break
