for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not ((x & A == 0) or not (x & 37 == 0) or not (x & 12 == 0)):
            flag = False
            break
    if flag == True:
        print(A)