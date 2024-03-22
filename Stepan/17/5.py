l = [int(x) for x in open('ItEge/Stepan/17/17_9748.txt')]
mx15 = -100000000
maxSum = -100000000
cnt = 0
for x in l:
    if abs(x)%100 == 15:
        mx15 = max(mx15, x)
for i in range(len(l) - 2):
    lst = [l[i], l[i + 1], l[i + 2]] 
    cnt4 = 0
    for x in lst:
        if len(str(abs(x))) == 4:
            cnt4+=1
    if cnt4 == 1:
        if sum(lst) >= mx15:
            cnt += 1 
            maxSum = max(maxSum,sum(lst)) 
print(cnt, maxSum)