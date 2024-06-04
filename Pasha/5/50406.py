mx = -100000000000
for n in range(1, 2000):
    s = bin(n)[2:]
    if sum(map(int, s)) % 2 == 0:
        s += '0'
        s = '10'+s[2:]
    else:
        s = '1' + s
        s = s[:-2] + '10'
    r = int(s, 2)
    if r < 224:
        mx = max(mx, n)
print(mx)