for A in range(1000, -1, -1):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((y + (2 * x) != 48) or (A < x) or (A < y)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break