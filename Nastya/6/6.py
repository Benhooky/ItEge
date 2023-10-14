my_values = [[1, 2], [11, 2], [1, 12]]
cnt = 0
for s, t in my_values:
    if s > 10 or t > 10:
        cnt += 1
    else:
        print("NO")
print(cnt)
