from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
def perevod(n, a):
    x = ''
    while n > 0:
        x = alph[n % a] + x
        n //= a
    return x
min_R = 100000000000
for N in range(1, 10000):
    s = perevod(N, 6)
    if N % 3 == 0:
        s += s[:2]
    else:
        s += perevod(N%3*10, 6)
    R = int(s, 6)
    if R > 680:
        min_R = min(min_R, R)
print(min_R)