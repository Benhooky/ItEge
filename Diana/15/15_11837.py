for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((x**2+y**2>1024-x)or(y<-2*x+A)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break