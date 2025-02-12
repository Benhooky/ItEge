mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_17636.txt')]
max3 = -100000000000000
cnt = 0
maxSum = -1000000000
for x in mas:
    if abs(x)%10==3:
        if 100<=abs(x)<=999:
            max3 = max(max3, x)
"""
max3 = max(x for x in mas if abs(x)%10==3 and 100<=abs(x)<=999)
"""
for i in range(len(mas)-2):
    """
    tri = [mas[i], mas[i+1], mas[i+2]]
    if any(abs(x)%10==3 and 100<=abs(x)<=999 for x in tri):
        if sum(tri)<max3:
            cnt+=1
            maxSum = max(maxSum, sum(tri))
    """
    if abs(mas[i])%10==3 and 100<=abs(mas[i])<=999 or abs(mas[i+1])%10==3 and 100<=abs(mas[i+1])<=999 or abs(mas[i+2])%10==3 and 100<=abs(mas[i+2])<=999:
        if mas[i]+mas[i+1]+mas[i+2]<max3:
            cnt+=1
            maxSum = max(maxSum, mas[i]+mas[i+1]+mas[i+2])
print(cnt, maxSum)