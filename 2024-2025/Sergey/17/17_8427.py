mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_8427.txt')]
cnt=0
maxSum=0
sumFirst = sum(int(str(x)[0]) for x in mas)
min3=min(x for x in mas if 100<=x<=999 and x%10==3)
for i in range(len(mas)-1):
    p=[mas[i],mas[i+1]]
    cnt4=sum(1 for x in p if 1000<=x<=9999)
    first=cnt4==1
    second=(p[0]**2+p[1]**2)%min3==0
    if first and second:
        cnt+=1
        maxSum=max(maxSum,p[0]**2+p[1]**2)
print(cnt,maxSum)
