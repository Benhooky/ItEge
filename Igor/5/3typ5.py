def tre(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s


for n in range(1000, 1, -1):
    s = tre(n)
    if sum(list(map(int, s))) % 3 == 0:
        s = "20" + s
    else:
        s = "10" + s
    r = int(s, 3)
    if r < 100:
        print(n)
        break
