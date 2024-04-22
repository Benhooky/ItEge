f = open('ItEge/Artur/17/17 (13).txt')
allNumbers = [int(x) for x in f]
max121 = -1000000000000
cnt = 0
maxSum = -10000000000
for i in allNumbers:
    if abs(i)%1000 == 121:
        max121 = max(max121, i)
for i in range(len(allNumbers)-2):
    triple = allNumbers[i:i+3]
    cnt4chet = 0
    for element in triple:
        if 1000<=abs(element)<=9999:
            if element%2 == 0:
                cnt4chet+=1
    if cnt4chet<=1:
        if sum(triple)<=max121:
            maxSum = max(maxSum,sum(triple))
            cnt+=1
print(cnt,maxSum)