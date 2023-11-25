def tre(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

minR = 100000000
for n in range(11, 1000):
    s = tre(n)
    if (s.count("2") + s.count("0")) > s.count("1"):
        s = "22" + s
    else:
        s = "11" + s
    r = int(s, 3)
    if r > 100:
        minR=min(r,minR)
print(minR)
