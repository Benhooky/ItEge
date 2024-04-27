max5 = 0
minN = 0
for n in range(51,500):
    s = n*'5'
    while '55555' in s:
        s = s.replace('55555','88',1)
        s = s.replace('888','55',1)
    if s.count('5')>max5:
        minN = n
        max5 = s.count('5')
print(minN)