for A in range(-1000,1000):#1
    flag = True
    for x in range(1,1000):#2
        for y in range(1,1000):#3
            if not((7*y+x<A)or(2*x+3*y>98)):#4
                #значит A не подходит
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break