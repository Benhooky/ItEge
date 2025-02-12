"""
f = open('ItEge/2024-2025/Sergey/17/17_17558.txt')
mas = []
for x in f:
    mas.append(int(x))
"""
mas = [int(x) for x in open('ItEge/2024-2025/Sergey/17/17_17558.txt')]
cntPairs = 0
cnt32 = 0
maxSum = 0
for x in mas:
    if x%32==0:
        cnt32+=1
for i in range(len(mas)-1):
    if mas[i]<0 or mas[i+1]<0:
        if mas[i]+mas[i+1]<cnt32:
            cntPairs += 1
            maxSum = max(maxSum, mas[i]+mas[i+1])
print(cntPairs, maxSum)