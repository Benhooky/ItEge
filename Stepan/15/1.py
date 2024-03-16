for i in range(100, 1, -1):
    k = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if (3*x + y > 48) or (x > y) or (4*x + y < i):
                k += 1
    if k!= 10000:
        print(i)
        break