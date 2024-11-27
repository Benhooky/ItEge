numberDigits = int(input())
cnt6 = 0
for i in range(numberDigits):
    currentDigit = int(input())
    if currentDigit%6==0:
        cnt6+=1
print(cnt6)