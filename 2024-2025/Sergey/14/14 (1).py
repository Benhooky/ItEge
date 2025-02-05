s=5*729**2024+3*243**1413-7*81**169-2*9**107+3017
sumChet = 0
while s>0:
    ourDigit = s%27
    if ourDigit % 2 == 0 and ourDigit <= 25:
        sumChet += ourDigit
    s//=27
print(sumChet)