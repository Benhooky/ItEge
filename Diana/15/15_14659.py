P=[int(x)*0.5 for x in range(12,35)]
Q=[int(x)*0.5 for x in range(26,57)]
maxLen=0
for Aleft in range(1,100):
    for Aright in range(Aleft+1,100):
        Flag=True
        for x in range(1000):
            x = 0.5 * x
            if not(((Aleft<=x<=Aright)<=(x in P))or (x in Q)):
                Flag=False
                break
        if Flag:
            maxLen=max(maxLen,Aright-Aleft)
print(maxLen)
