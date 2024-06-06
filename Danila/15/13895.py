
minLen=10000000000
for Aleft in range(100):
    for Aright in range(Aleft+1, 100):
        Flag = True
        for x in range(1, 200):
            x = 0.5 * x
            if not(((34<=x<=72)<=(Aleft<=x<=Aright)) and (not(32<=x<=61) or (Aleft<=x<=Aright))):
                Flag = False
                break
        if Flag:
            minLen = min(minLen, Aright-Aleft)
print(minLen)

answerLst = []
for Aleft in range(100):
    for Aright in range(Aleft+1, 100):
        Flag = True
        for x in range(1, 200):
            x = 0.5 * x
            if not(((34<=x<=72)<=(Aleft<=x<=Aright)) and (not(32<=x<=61) or (Aleft<=x<=Aright))):
                Flag = False
                break
        if Flag:
            answerLst.append(Aright-Aleft)
print(min(answerLst),max(answerLst))
