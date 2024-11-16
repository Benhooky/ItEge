a = int(input())
cnt0 = 0
sum0 = 0
for i in range(a):
    n = int(input())
    if n > 0:
        sum0 += n
        cnt0 += 1
print(sum0/cnt0)
print(cnt0)