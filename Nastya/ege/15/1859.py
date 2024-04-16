for A in range(1000, -1, -1):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not(((2 * x) + y != 70) or (x < y) or (A < x)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break