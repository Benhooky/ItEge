file = open('ItEge/Pasha/24/24_934.txt').readline()
keeperS = file[0]
mx_len = 0
for i in range(1, len(file)):
    keeperS += file[i]
    if keeperS[-2] > keeperS[-1]:
        if len(set(keeperS[:-1])) == 3:
            mx_len = max(mx_len, len(keeperS) - 1)
            keeperS = keeperS[-1]
        else:
            keeperS = keeperS[-1]
    if len(set(keeperS)) == 4:
        mx_len = max(mx_len, len(keeperS) - 1)
        lastLetter = keeperS[0]
        while lastLetter in keeperS:
            keeperS = keeperS[1:]
print(mx_len)