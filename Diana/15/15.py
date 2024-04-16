B=[int(x) for x in range(101,144)]
C=[int(x) for x in range(144,200)]

maxA=1
for Aleft in range(300):
    for Aright in range(300,Aleft,-1):
        if Aright-Aleft<maxA:
            break
        A = [x for x in range(Aleft,Aright+1)]
        flag = True
        for x in range(300):
            if not( (x in A)<= ((x in B) or (x in C))):
                flag=False
                break
        if flag:
            print(Aleft,Aright)
            maxA=max(maxA,Aright-Aleft)
print(maxA)