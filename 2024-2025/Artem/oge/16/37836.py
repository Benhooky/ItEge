number = int(input())
maxN = 0
for i in range(number):
    current = int(input())
    if current % 4 == 0:
        maxN = max(maxN, current)
print(maxN)