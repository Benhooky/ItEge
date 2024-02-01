def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s
for n in range(100000, 1, -1):
    s = f(n)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        print(n)
        break