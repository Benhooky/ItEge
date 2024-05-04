from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
def perevod(n, a):
    x = ''
    while n > 0:
        x = alph[n % a] + x
        n //= a
    return x
max_N = 0
for N in range(1, 10000):
    s = perevod(N, 7)
    if s.count("2") % 2 == 0:
        s += "555"
    else:
        s = "1" + s
    R = int(s, 7)
    if R < 3799:
        max_N = max(max_N, N)
print(max_N)

