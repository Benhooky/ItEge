mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_10004.txt')]
cnt = 0
minSum = 100000000000000
for step in range(2,len(mas)//2+1):
    for i in range(len(mas)-step*2):
        tri = [mas[i],mas[i+step],mas[i+step*2]]
        cnt4 = sum(1 for x in tri if 1000<=abs(x)<=9999)
        first = cnt4==2
        second = sum(tri)**(1/2) == int(sum(tri)**(1/2)) if sum(tri)>=0 else False
        if first and second:
            cnt+=1
            minSum = min(minSum,sum(tri))
print(cnt,minSum)