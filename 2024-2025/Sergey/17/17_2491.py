mas=[int(x) for x in open("ItEge/2024-2025/Sergey/17/17_2491.txt")]
cnt=0
"""
num = -19432423
flagHas9 = False
while num != 0:
currentDigit = abs(num) % 10
if currentDigit == 9:
    flagHas9 = True
    break
num = num // 10
"""
avg=sum(mas)/len(mas)
maxSum=-1000000000000
for i in range(len(mas)-2):
    if mas[i]<avg or mas[i+1]<avg or mas[i+2]<avg:
        if ('9' in str(mas[i])) and ('9' in str(mas[i+1])) and ('9' in str(mas[i+2])):
            cnt+=1
            maxSum=max(maxSum, mas[i]+mas[i+1]+mas[i+2])
print(cnt,maxSum)