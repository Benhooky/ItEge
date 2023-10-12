f = open('Pasha/24/24_9845.txt').readline()[:-1]
s = f[0]
max0 = 0
latters = "ABC"
digits = "89"
for i in range(1, len(f)):
    s += f[i]
    if s[-2] in latters and s[-1] in latters or s[-2] in digits and s[-1] in digits:
        max0 = max(max0, len(s) - 1)
        s = s[-1]
print(max0)
