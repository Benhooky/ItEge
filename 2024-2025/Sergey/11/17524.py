from math import ceil

for a in range(0, 100000):
    if ceil(a * 10 / 8) * 862 <= 276 * 1024:
        print(a)