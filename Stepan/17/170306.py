a = [int(x) for x in open('ItEge/Stepan/17/17.txt')]
zero = []
for i in range(1,len(a)):
    if a[i] % 2 == 0 and a[i - 1] % 2 != 0 and a[i] % 4 == 0 and a[i - 1] % 11 == 0 or a[i-1] % 2 == 0 and a[i] % 2 != 0 and a[i-1] % 4 == 0 and a[i] % 11 == 0:
        zero.append(a[i] + a[i - 1])
print(len(zero), max(zero))