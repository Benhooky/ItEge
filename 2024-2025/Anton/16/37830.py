num = int(input())
maxD = 0
for i in range(num):
    digit = int(input())
    if digit%5 == 0:
        maxD = max(maxD,digit)
print(maxD)