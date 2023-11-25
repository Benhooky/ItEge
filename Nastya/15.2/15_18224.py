N = int(input())
sum8 = 0
for i in range(N):
    current = input()
    if current[-1] == '8':
        sum8 += int(current)
print(sum8)
