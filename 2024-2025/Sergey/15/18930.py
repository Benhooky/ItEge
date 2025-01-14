minLen = 1000000000
for Aleft in range(10,302):
    for Aright in range(Aleft+1,303):
        flag = True
        for n in range (5,650):
            x = n/2
            if not(((160<=x<=250)<=(10<=x<=150))or((not(Aleft<=x<=Aright))<=(240<=x<=300))):
                flag = False
                break
        if flag:
            minLen = min(minLen, Aright-Aleft)
print(minLen)