f = open('ItEge/Artur/17/17_12926.txt')#!!!!!!!!!!!!!!!!!!
numbers = [int(i) for i in f]
A = -100000000000
max2 = -1000000000000
cnt = 0
minSum = 1000000000
for i in range(len(numbers)-3):
    if abs(numbers[i])%10 == abs(numbers[i+1])%10 == abs(numbers[i+2])%10 == abs(numbers[i+3])%10:
        A = max(A,numbers[i]+numbers[i+1]+numbers[i+2]+numbers[i+3])
for i in range(len(numbers)):
    if 9<abs(numbers[i])<100:
        max2 = max(max2,numbers[i])
print(A,max2)
for i in range(len(numbers)-4):
    five = numbers[i:i+5]
    cnt5 = 0
    for j in five:
        if j<A:
            cnt5+=1
    if cnt5==1 and abs(sum(five))%max2==0:
        cnt+=1
        minSum = min(minSum,sum(five))
        print(five)
print(cnt, minSum)