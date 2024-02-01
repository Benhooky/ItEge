for i in range(210, 300):
    s = '3' + str(i) * 7
    while '27' in s or '337' in s or '777' in s:
        s = s.replace('27', '32', 1)
        s = s.replace('337', '27', 1)
        s = s.replace('777', '3', 1)
    if sum(int(digit) for digit in s) % 15 == 0:
        print(i)