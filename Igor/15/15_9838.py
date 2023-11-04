for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x + 2*y > A) or (y < x) or (x < 30)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
