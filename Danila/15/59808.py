for A in range(300, -1, -1):
    flag = True
    for x in range(300):
        for y in range(300):
            if not ((x+2*y > A) or (x > 13) or (y < 44)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
