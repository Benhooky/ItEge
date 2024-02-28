for A in range(1000):
    flag = True
    for x in range (0,1001):
        for y in range (0,1001):
            if (((3*x + y > A) & (y < x) & (x < 30))):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
        