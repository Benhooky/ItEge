def ДЕЛ(n,m):
    if n%m==0:
        return True
    else:
        return False

for A in range(20000, 0, -1):
    flag = True
    for x in range(1, 20000):
        if not(ДЕЛ(x,263)<=ДЕЛ(x,A))and ДЕЛ(x,71):
            flag = False
            break
    if flag:
        print(A)
        break