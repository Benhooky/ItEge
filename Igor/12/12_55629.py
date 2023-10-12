def is_Prime(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True


for i in range(100, 1000):
    s = '0'+i*'1'+i*'2'+'0'
    while '00' not in s:
        s = s.replace('02', '101')
        s = s.replace('11', '2')
        s = s.replace('12', '21')
        s = s.replace('010', '00')
    sum1 = 0
    for x in s:
        sum1 += int(x)
    if is_Prime(sum1):
        print(i)
        break
