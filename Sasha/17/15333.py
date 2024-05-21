f = open('ItEge/Sasha/17/17_15333 (1).txt')
lst = [int(x) for x in f]
max19 = -10000000000
cnt = 0
maxSum = -1000000000
for x in lst:
    if x%19==0:
        max19 = max(max19,x)
for i in range(len(lst)-1):
    pair = [lst[i],lst[i+1]]
    if len([x for x in pair if x>max19])>0:
        cnt+=1
        maxSum = max(maxSum,lst[i]+lst[i+1])
print(cnt,maxSum)