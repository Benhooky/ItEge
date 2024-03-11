for A in range(1, 1001):
    k = 0
    for i in range(1, 1000):
        if (A % 40 == 0) and ((780 % i == 0) <= ((A % i != 0) <= (180 % i != 0))):
            k+=1
        if k == 999:
            print(A)
            break
