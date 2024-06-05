D = [int(x)*0.5 for x in range(14,139)]
C = [int(x)*0.5 for x in range(58,201)]
minA = 100000000
for ALeft in range(200):
    for Aright in range(ALeft+1,200):
        if Aright-ALeft > minA:
            break
        flag=True
        for x in range(400):
            x = 0.5*x
            if not((x in D)<=((not(x in C)and(not(ALeft<=x<=Aright)))<=(not(x in D)))):
                flag=False
                break
        if flag:
            minA = min(minA, Aright-ALeft)
print(minA)