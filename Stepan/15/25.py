for A in range(1000):
    flag = True
    k = 0
    for x in range(1000):
        for y in range(1000): 
            if not((4 * x + 3 * y < A) or (x >= y) or (y >= 13)):
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break