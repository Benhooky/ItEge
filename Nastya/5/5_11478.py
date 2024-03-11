from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
def perevod(n, a):
    x = ''
    while n > 0:
        x = alph[n % a] + x
        n //= a
    return x
min_N = 100000000000
for N in range(1, 1000):
    sum1 = 0
    s = perevod(N, 3)
    if N % 2 == 0:
        s = "1" + s + "00"
    else:
        for i in s:
            sum1 += int(i)
        s += perevod(sum1,3)
    R = int(s, 3)
    if R > 168:
        min_N = min(min_N, N)
print(min_N)