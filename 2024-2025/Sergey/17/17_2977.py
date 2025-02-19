mas=[int(x) for x in open("ItEge/2024-2025/Sergey/17/17_2977.txt")]
cnt=0
maxSum=0
for i in range(len(mas)-1):
    if int(mas[i]**(1/2)) == mas[i]**(1/2) and  int(mas[i+1]**(1/2)) == mas[i+1]**(1/2) and mas[i]**(1/2)%2==0 and mas[i+1]**(1/2)%2==0:
        cnt+=1
        maxSum=max(maxSum, mas[i]+mas[i+1])
print(cnt, maxSum)