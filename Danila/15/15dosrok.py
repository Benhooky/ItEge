minLen = 100000000
for Aleft in range(20,130):
    for Aright in range(Aleft+1,130):
        flag = True
        for x in range(20,130):
            if not((47<=x<=115)<=(((not(Aleft<=x<=Aright))and(24<=x<=90))<=(not(47<=x<=115)))):
                flag = False
                break
        if flag:
            minLen = min(minLen,Aright-Aleft)
print(minLen)