P = [x for x in range(19,85)]
Q = [x for x in range(4,52)]
minA = 1000000000
for Aleft in range(86):
    for Aright in range(Aleft+1,86):
        A = [x for x in range(Aleft,Aright+1)]
        flag = True
        for x in range(86):
            if not((x in P)<=((x not in Q)<=(not((x in P)and(x not in A))))):
                flag = False
                break
        if flag:
            minA = min(minA, Aright-Aleft)
print(minA)