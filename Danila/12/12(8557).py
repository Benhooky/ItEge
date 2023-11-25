maxN = 0
maxSum = 0
for n in range(0, 1000):
    s = "13" * n
    while ("13" in s) or ("31" in s) or ("11" in s):
        if "13" in s:
            s = s.replace("13", "4", 1)
        if "33" in s:
            s = s.replace("31", "1", 1)
        if "11" in s:
            s = s.replace("11", "2", 1)
        if "44" in s:
            s = s.replace("44", "1", 1)
    sum1 = 0
    for i in s:
        sum1 += int(i)
    if 9 < (sum1) < 100:
        if sum1 > maxSum:
            maxSum = sum1
            maxN = n
            print(f"maxN = {maxN} maxSum ={maxSum}")
