P=[int(x) for x in range(10,41)]
Q=[int(x) for x in range(5,16)]
R=[int(x) for x in range(35,51)]
minA= 1000000
for Aleft in range(1200):
    for Aright in range(Aleft+1,1200):
        if Aright-Aleft>minA:
            break
        flag= True
        for x in range(1200):
            if not(((Aleft<=x<=Aright)or(x in P))or((x in Q)<=(x in R))):
                flag=False
                break
        if flag:
            minA=min(minA,Aright-Aleft+1)
print(minA)