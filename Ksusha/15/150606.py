MinLen=999999999
for Al in range(0,400):
    for Ar in range(Al+1,400):
        flag = True
        for X in range(1,800):
            X*=0.5
            if not(((175<=X<=300)<=(25<=X<=240)) or ((not(Al<=X<=Ar))<=(270<=X<=340))):
                flag=False
                break
        if flag:
            MinLen = min(MinLen, Ar-Al)
print(MinLen)