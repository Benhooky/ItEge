D = [int(x) for x in range(7,69)]
C = [int(x) for x in range(29,101)]
minA = 100000000
for ALeft in range(200):
    for Aright in range(ALeft+1,200):
        if Aright-ALeft > minA:
            break
        flag=True
        for x in range(200):
            if not((x in D)<=((not(x in C)and(not(ALeft<=x<=Aright)))<=(not(x in D)))):
                flag=False
                break
        if flag:
            minA = min(minA, Aright-ALeft+1)
print(minA)