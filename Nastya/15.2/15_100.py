N = int(input())
sum1 = 0
for i in range(N):
    a = int(input())
    if a % 3 == 0:
        sum1 += a
print(sum1)