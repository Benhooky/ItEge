mas=[int(x) for x in open("ItEge/2024-2025/Sergey/17/17_9969.txt")]
cnt=0 
sumPoln=0
max3=-100000000000
maxDigit=0
for x in mas:
    currentDigitCnt = len(set(str(abs(x))))
    if currentDigitCnt > maxDigit:
        max3=x 
        maxDigit=currentDigitCnt
    elif currentDigitCnt== maxDigit:
        max3=max(max3,x)
for i in range(len(mas)-2):
    cntS=0
    sumDvuh = 0
    whatToAdd = 0
    if int(mas[i]**1/2)==mas[i]**1/2 and mas[i]>0:
        cntS+=1
        sumDvuh = mas[i+1]+mas[i+2]
        whatToAdd = mas[i]
    if int(mas[i+1]**1/2)==mas[i+1]**1/2 and mas[i+1]>0:
        cntS+=1
        sumDvuh = mas[i]+mas[i+2]
        whatToAdd = mas[i+1]
    if int(mas[i+2]**1/2)==mas[i+2]**1/2 and mas[i+2]>0:
        sumDvuh = mas[i+1]+mas[i]
        cntS+=1
        whatToAdd = mas[i+2]
    if cntS==1:
        if sumDvuh>=max3: 
            cnt+=1
            sumPoln+=whatToAdd
print(cnt,sumPoln)