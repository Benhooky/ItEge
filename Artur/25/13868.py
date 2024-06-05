from fnmatch import fnmatch
for i in range(2024, 10 ** 10 + 1, 2024):
    if fnmatch(str(i), '112?57*4'):
        summa = 0
        for x in str(i):
            summa += int(x)
        if summa % 2 == 1:
            print(i, i // 2024)