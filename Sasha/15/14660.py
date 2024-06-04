Alist = []
for Aleft in range(1,100):
    for Aright in range(Aleft+1,100):
        flag = True
        for x in range(1,200):
            x*=0.5
            if not(((Aleft<=x<=Aright)<=(16<=x<=84))or(27<=x<=43)):
                flag = False
                break
        if flag:
            Alist.append(Aright-Aleft)
print(max(Alist))