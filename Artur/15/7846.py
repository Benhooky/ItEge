aMax = 0
for Aleft in range(1,1000):
    for Aright in range(1000,Aleft,-1):
        if Aright-Aleft<aMax:
            break
        flag = True
        for x in range(1000):
            if not(not(not(13<=x<=19)<=(17<=x<=23))<=((Aleft<=x<=Aright)<=(not(17<=x<=23)<=(13<=x<=19)))):
                flag = False
                break
        if flag:
            aMax = max(aMax, Aright-Aleft)
print(aMax)