def ДЕЛ(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(-1000,1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((ДЕЛ(108, x) <= (not(ДЕЛ(x,y)))) or (x + y > 80) or (A - y > x)):
                flag = False
                break
        if flag == False:
            break
    if flag:
        print(A)
        break