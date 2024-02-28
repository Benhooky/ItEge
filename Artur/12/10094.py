for n in range(9999, 3, -1):
    s = '5' + n*'2'
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if sum(int(i) for i in s) == 64:
        print(n)
        break
