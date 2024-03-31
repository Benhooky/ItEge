def ДЕЛ(n,m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(10, 0, -1):
    flag = True
    for y in range(1, 200):
        for x in range(1, 200):
            for z in range(1, 200):
                if not((ДЕЛ(z, 115)) or (ДЕЛ(y, 78)) or (ДЕЛ(x, 51))) <= (ДЕЛ(x, A)):
                    flag = False
                    break
            if flag == False:
                break
        if flag == False:
            break
    if flag:
        print(A)
        break