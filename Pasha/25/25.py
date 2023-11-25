from math import sqrt

mncnt = 0
for i in range(600000, 2000000):
    mindel = 1000000000
    for j in range(2, int(sqrt(i) + 1)):
        if i % j == 0:
            if j % 10 == 9 and j != 9:
                print(i, j)
                mncnt += 1
                break
            if i // j % 10 == 9 and i // j != 9:
                mindel = min(mindel, i // j)
    if mindel != 1000000000:
        print(i, mindel)
        mncnt += 1
    if mncnt == 5:
        break
