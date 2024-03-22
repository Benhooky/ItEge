f = [int(x) for x in open('ItEge/Stepan/17/17_9786.txt')]
max_25 = -1000000
count = 0
max_sum = -100000
for num in f:
    if abs(num) % 100 == 25:
        max_25 = max(max_25, num)
for i in range(len(f) - 2):
    lst = [f[i], f[i + 1], f[i + 2]]
    #1
    four_cnt = sum(1 for num in lst if len(str(abs(num))) == 4)
    #2
    cnt4 = 0
    for x in lst:
        if len(str(abs(x))) == 4:
            cnt4+=1
    if cnt4 <= 2 and sum(lst) <= max_25:
        count += 1
        max_sum = max(max_sum, sum(lst))

print(count, max_sum)
