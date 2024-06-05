mx = -10000000000000000
for al in range(34, 72):
    for ar in range(32,61,):
        flag = True
        a = [y for y in range(al, ar + 1)]
        if ar - al <= mx:
            flag = False
            break
        for d in range(1, 500):
            x = d*0.5
            if ((al<=x<=ar) <= ((101<=x<=143) or (144<=x<=199))) == 0:
                flag = False
                break  
        if flag:
            mx = max(mx, ar-al)
print(mx)