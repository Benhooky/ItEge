n = int(input())
cnt = 0
for i in range(n):
    current = int(input())
    if current % 10 == 9:
        cnt+=1
print(cnt)