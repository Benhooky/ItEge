mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_19749.txt')]
cnt=0
maxSum = -10000000000
for i in range(len(mas)-2):
    trig = [mas[i],mas[i+1],mas[i+2]]
    cnt3 = sum(1 for x in trig if x%3==min(mas)%3)
    cnt7 = sum(1 for x in trig if x%7==max(mas)%7)
    if cnt3 == 1 and cnt7>=2:
        cnt+=1
        maxSum = max(maxSum, sum(trig))
print(cnt,maxSum)