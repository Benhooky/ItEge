maxSum = 0
for n in range(4,10000):
    s = '4'+n*'1'
    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411','14',1)
        if '1111' in s:
            s = s.replace('1111','1',1)
    mySum = 0
    for x in s:
        mySum += int(x)
    maxSum = max(maxSum,mySum)
print(maxSum)