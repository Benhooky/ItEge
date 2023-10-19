min0 = 1000000000
for Aleft in range(1, 999):
    for Aright in range(Aleft + 1, 1000):
        flag = True
        if Aright-Aleft > min0:
            break
        for x in range(1, 1000):
            if ((not ((47 <= x <= 92) <= ((24 <= x <= 77) or (82 <= x <= 116)))) <= (not (Aleft <= x <= Aright) <= (not (47 <= x <= 92)))) == 0:
                flag = False
                break
        if flag:
            min0 = min(min0, Aright - Aleft)
print(min0)
