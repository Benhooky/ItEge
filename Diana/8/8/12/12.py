max5 = 0
lowestN = 0
for N in range(51,1000):
    s = '5'*N
    while '55555' in s:
        s = s.replace('55555','88',1)
        s = s.replace('888','55',1)
    if s.count('5')>max5:
        lowestN = N
        max5 = s.count('5')
print(lowestN)