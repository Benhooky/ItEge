def f1(n,a):
    s = []
    while n > 0:
        s.append(str(n%a))
        n //= a 
    return s[::-1]
answer = 3*3125**9 + 2* 625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
s = f1(answer,25)
print(s.count('0'),s)
