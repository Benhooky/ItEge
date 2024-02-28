minLen = 1000000000
for Aleft in range(1000):   
    for Aright in range(Aleft+1,1000):
        if Aright-Aleft>minLen:
            break
        flag = True
        for x in range(1000):
            if not((not(Aleft<=x<=Aright))<=(((17<=x<=46)and(22<=x<=57))<=(Aleft<=x<=Aright))):
                flag = False
                break
        if flag:
            minLen = min(minLen, Aright-Aleft)
print(minLen)