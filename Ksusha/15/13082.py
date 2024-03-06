for a in range(1000,0,-1):
    a = 60
    flag = False
    for y in range (1,1000):
        for x in range(1, 1000):
            if ((3*x+y>48)or(x>y)or(4*x+y<a))==0:
                print(a)
                flag = True
        if flag:
            break
    if flag:
        break
