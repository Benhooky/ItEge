l = [int(x) for x in open('ItEge/Stepan/17/17_9547.txt')]
min11 = 100000000000
cnt = 0
maxSum = -100000000000000
for x in l:
    if len(str(abs(x)))==3 and abs(x)%100==11:
        min11 = min(min11,x)
for i in range(len(l)-1):
    pair = [l[i],l[i+1]]
    cnt3 = 0
    for x in pair:
        if len(str(abs(x)))!=3:
            cnt3+=1
    if cnt3==1:
        if abs(pair[0]-pair[1])%min11 == 0:
            cnt+=1
            maxSum = max(maxSum,sum(pair))
print(cnt,maxSum)