mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_2979.txt')]
cnt = 0
minSum = 9999999999999999999
for i in range(len(mas) - 1):
    if (abs(mas[i]) + abs(mas[i+1]))>17043 and (abs(mas[i])+abs(mas[i+1]))%3==0:
        cnt += 1
        minSum = min(minSum,mas[i]+mas[i+1])
print(cnt, minSum)