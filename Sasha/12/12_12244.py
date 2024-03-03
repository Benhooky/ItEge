max1 = -1
for n in range(4,10000):
    s = '3'+'5'*n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555','3',1)
        else:
            s = s.replace('333','5',1)
    sum1=0
    for i in s:
        sum1 += int(i)
    max1 = max(max1, sum1) 
print(max1)