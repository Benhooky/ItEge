N = int(input())
cnt = 0
sum1 = 0
while N!=0:
    if len(str(N))==2:
        cnt += 1
        sum1 += N
    N = int(input())
if cnt == 0:
    print("NO")
else:
    print(sum1/cnt)