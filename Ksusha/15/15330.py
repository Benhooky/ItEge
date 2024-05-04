minA=[]
for Aleft in range(22,120):
    for Aright in range (Aleft+1,121):
        flag=True
        for x in range(44,240):
            x=x*0.5
            if not((47<=x<=115)<=(((not(Aleft<=x<=Aright))and (24<=x<=90))<=(not(47<=x<=115)))):
                flag=False
                break
        if flag:
            minA.append(Aright-Aleft)
print(min(minA))
