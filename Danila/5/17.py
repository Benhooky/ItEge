for i in range(1, 1000):
    N = bin(i)[2:]
    if i % 2 == 0:
        N = "1" + N + "0"
    else:
        N = "11" + N + "11"
    R = int(N, 2)
    if R > 100:
        print(i)
        break
