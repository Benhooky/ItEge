min1 = 100000000
lastn = 0
for n in range(101, 1000):
    s = '1' *n
    while '111' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        if '222' in s:
            s = s.replace('222', '11', 1)
    if s.count('1') < min1:
        min1 = s.count('1')
        lastn = n
print(lastn)