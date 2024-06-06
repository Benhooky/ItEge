def srDel(a):
    sm = 0
    dels = set()
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            dels.add(b)
            dels.add(a//b)
    if len(dels) == 0:
        return 0
    else:
        return sum(dels) // len(dels)
tCnt = 0
for i in range(700001, 0, -1):
    M = srDel(i)
    if str(M)[-3:] == '313':
        tCnt += 1
        print(i, int(M))
    if tCnt == 7:
        break