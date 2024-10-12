minLen = 10000000000
for Aleft in range (30,80):
    for Aright in range (Aleft+1,81):
        flag = True
        for x in range (30,160):
            x/=2
            if not (not((32<=x<=68)or(54<=x<=76))==(not(Aleft<=x<=Aright))):
                flag = False
                break
        if flag:
            minLen = min(minLen, Aright-Aleft)
print(minLen)