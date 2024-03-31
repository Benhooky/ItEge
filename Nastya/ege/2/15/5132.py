def ОД(n, m):
    nListDel = [n]
    mListDel = [m]
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            nListDel.append(i)
            nListDel.append(n//i)
    for i in range(2, int(m**0.5)+1):
        if m%i == 0:
            mListDel.append(i)
            mListDel.append(m//i)
    for i in mListDel:
        if i in nListDel:
            return True
    return False


for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not((ОД(x, 42) <= (not(ОД(x, 7))) or (x + A >= 25))):
            flag = False
            break
    if flag:
        print(A)
        break