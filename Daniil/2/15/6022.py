for A in range(0,1000):#1
    flag = True
    for x in range(0,1000):
        for y in range(0,1000):
            if not((x<A)or(y<A)or(x+2*y>150)):#2
                #значит A не подходит
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break