N = int(input())
cnt40 = 0
avgSpeed = 0
for i in range(N):
    inSpeed = int(input())
    avgSpeed += inSpeed
    if inSpeed <= 40:
        cnt40 += 1
print(round((avgSpeed / N),1))
if cnt40 >= 2:
    print('YES')
else:
    print('NO')