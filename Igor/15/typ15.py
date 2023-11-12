for A in range(100):
    flag = True
    for x in range(100):
        if not (((x & 52 != 0) and (x & 36 == 0)) <= (not (x & A == 0))):
            flag = False
            break
    if flag:
        print(A)
        break
