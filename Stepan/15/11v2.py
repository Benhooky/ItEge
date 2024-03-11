for A in range(0, 1000):
    A_p = True
    for x in range(0, 1000):
        if not (((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & A != 0))):
            A_p = False
            break
    if A_p:
        print(A)
        break
