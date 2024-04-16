P = [x for x in range(17,41)]
Q = [x for x in range(20,58)]
minLen = 1000000000000
for Aleft in range(1000):
    for Aright in range(1000):
        if Aright - Aleft > minLen:
            break
        flag = True
        A = [x for x in range(Aleft,Aright+1)]
        for x in range(0,60):
            if not((not(x in A))<=(((x in P)and(x in Q))<=(x in A))):
                flag = False
                break
        if flag:
            minLen = min(minLen,Aright-Aleft)
print(minLen)