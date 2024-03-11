P = [x for x in range(5, 281)]
Q = [x for x in range(295, 401)]
R = [x for x in range(375, 451)]
minA = 1000000000
for Aleft in range(455):
    for Aright in range(Aleft + 1, 455):
        if Aright-Aleft > minA:
            break
        A = [x for x in range(Aleft, Aright + 1)]
        flag = True
        for x in range(455):
            if not (((x in Q) <= (x in P)) or ((x not in A) <= (x in R))):
                flag = False
                break
        if flag:
            minA = min(minA, Aright - Aleft)
print(minA)
