from string import ascii_uppercase,digits
alph = digits + ascii_uppercase
def perevod(n, a):
    x = ''
    while n > 0:
        x = alph[n % a] + x
        n //= a
    return x
min_R = 10000000000000000000000000
for N in range(1, 10000):
    s = perevod(N, 3)
    sum1 = 0 
    for i in s:                                                                                                                                                                                                                     
        sum1+=int(i)
    if  sum1 % 4 == 0:
        s = "1" + s
        s = s[:-2]
    else:
        s += perevod((sum1%4 * 3), 3)
    R = int(s, 3)
    if R > 353:
        min_R = min(min_R, R)
print(min_R)

