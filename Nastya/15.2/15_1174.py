M = int(input())
cnt = 0
while (M != 0):
    if len(str(M)) == 3:
        if M % 4 == 0:
            cnt += 1
    M = int(input())
print(cnt)
