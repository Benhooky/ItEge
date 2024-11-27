inDigit = int(input())
cnt = 0
while inDigit != 0:
    if inDigit % 5 == 0 or inDigit % 9 == 0:
        cnt += 1
    inDigit = int(input())
print(cnt)