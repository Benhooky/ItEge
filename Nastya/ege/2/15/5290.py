for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(not((x + 5 < A) <= (y > A)) or (x * y >= 76)):
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)
        break