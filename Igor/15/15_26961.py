for A in range(500, 1, -1):
    flag = True
    for x in range(500):
        for y in range(500):
            if not ((x+3*y > A) or (y < 30) or (x < 30)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
