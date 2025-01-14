number = int(input())
sum6 = 0
for i in range (number):
    current = int(input())
    if current % 6 == 0:
        sum6 += current
print(sum6)