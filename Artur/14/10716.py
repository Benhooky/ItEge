def toTen(s, system):
    rez = 0
    s = s[::-1]
    for i in range(len(s)):
        rez += s[i] * system**i
    return rez

for x in range(150):
    result = toTen([5, 1, x, 2, 9], 150) + toTen([x, 0, 2, 3], 150)
    if result % 149 == 0:
        print(result // 149)