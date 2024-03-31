def ПОДАРКИ(n, m):
    if (n % m == 0):
        return True
    else:
        return False


for A in range(1000):
    A = 89999099
    flag = True
    for x in range(1, 1000):
        if not(((ПОДАРКИ(x, 17)) <= (not(ПОДАРКИ(x, 53)))) or (not(A < 90000000 - x))):
            flag = False
            break
    if flag:
        print(A)
        break