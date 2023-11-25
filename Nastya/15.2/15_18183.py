N = int(input())
max5 = 0
for i in range(N):
    a = int(input())
    if a % 5 == 0:
        max5 = max(max5, a)
print(max5)
