minLen = 10000000
for ALeft in range(1,1000):
    for ARight in range(ALeft+1,1000):
        if ARight - ALeft > minLen:
            break
        flag = True
        for x in range(1000):
            if not((7<=x<=68)<=((x<29 or x>100)and(x<ALeft or x>ARight))<=(x<7 or x>68)):
                flag = False
                break
        if flag:
            minLen = min(minLen,ARight-ALeft)
            break
print(minLen)