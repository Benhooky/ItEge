from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
def perevod(n, a):
    x = ''
    while n > 0:
        x = alph[n % a] + x
        n //= a
    return x
min_R = 10000000000
for N in range(1, 100000):
    s = perevod(N, 12)
    if N % 4 == 0:
        s = "2" + s + "64"
    else:
        s += max(s)
    R = int(s, 12)
    if R > 1799:
         min_R = min(min_R, R)
print(min_R)


