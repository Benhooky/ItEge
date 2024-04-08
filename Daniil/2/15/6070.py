for A in range(0,1000):
    flag = True
    for x in range(0,1000):
        for y in range(0,1000):
            if not((A>y)or(3*x+2*y>53)or(A>x)):#1
                #значит A не подходит
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break