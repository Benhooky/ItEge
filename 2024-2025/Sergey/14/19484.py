s=5*729**2024+3*243**1413-7*81**169-2*9**107+3017
sumChet = 0
while s>0:
    myDigit = s%27
    if myDigit % 2 == 0 and myDigit <=25:
        sumChet+=myDigit
    s//=27
print(sumChet)