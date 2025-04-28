for x in range(1,10001):
    s=6**900+6**10-x
    cnt3=0
    cnt5=0
    while s>0:
        if s%6 == 3:
            cnt3+=1
        elif s%6 == 5:
            cnt5+=1
        s//=6
    if cnt3 == cnt5:
        print(x)