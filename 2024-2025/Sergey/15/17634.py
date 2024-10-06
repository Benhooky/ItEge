for A in range (1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not((x+y<=30) or (y<=x+2) or (y>=A)):
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)