
my_safe = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12),
           (-11, 12), (-12, 11), (10, 10), (10, 5)]
cnt_A = 0
for A in range(-100, 100):
    cnt_NO = 0
    for s, t in my_safe:
        if (s > 10) or (t > A):
            print("YES")
        else:
            print("NO")
            cnt_NO += 1
    if cnt_NO == 3:
        cnt_A += 1
print(cnt_A)
