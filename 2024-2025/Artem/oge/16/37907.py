whatToPut = int(input())
min3 = 100000000000
while whatToPut != 0:
    if whatToPut % 3 == 0:
        min3 = min(min3, whatToPut)
    whatToPut = int(input())
print(min3)