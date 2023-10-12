
for n in range(1000, 3, -1):
    s = '5' + n * '2'
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    print(sum(map(int, s)))
    if sum(map(int, s)) == 64:
        print(n)
        break
