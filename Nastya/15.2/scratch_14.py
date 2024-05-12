N = int(input())
cnt = 0
for i in range(N):
    a = int(input())
    if (a % 11 == 0) and (a % 3 != 0):
        cnt += 1
print(cnt)