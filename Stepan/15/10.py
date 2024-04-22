for a in range(1000):
    flag = True
    k = 0
    for m in range(1000):
        for n in range(1000):
            if not((2*m + 3*n > 40) or ((m < a) and (n <= a))):
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)
        break