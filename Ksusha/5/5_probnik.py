def troy(n):
    troy = ""
    while n > 0:
        troy = str(n % 3) + troy
        n //= 3
    return troy

for n in range(1, 10000):
    s = troy(n)
    summa = troy(s.count("1") + s.count("2") * 2)
    if n % 2 == 1:
        s = s + str(summa)
    else:
        s = "1" + s + "00"
    r = int(s, 3)
    if r > 168:
        print(n)
        break