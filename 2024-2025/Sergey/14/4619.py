s = 343**1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 3* 7 **1530 - 1550
res = ''
while s > 0:
    res += str(s % 7)
    s //= 7
res = res[::-1]
print(res.count('0'))