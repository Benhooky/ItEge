f = open('ItEge/Sasha/17/17_9840 (2).txt')
lst = [int(x) for x in f]
max39 = -1000000000
cnt = 0
maxSum = -100000000000
for x in lst:
    if 999<abs(x)<10000:
        if abs(x)%100 == 39:
            max39 = max(max39,x)
for i in range(len(lst)-1):
    pair = [lst[i],lst[i+1]]
    if len([x for x in pair if 999<abs(x)<10000]) == 1:
        if sum(pair)**2 <= max39**2:
            cnt+=1
            maxSum=max(maxSum,sum(pair))
print(cnt,maxSum)