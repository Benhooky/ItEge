
my_safe = [(9, 10), (11, 5), (-2, 8), (9, 9), (2, 8),
           (-1, 3), (-4, 5), (10, 9), (4, -3)]
cnt_NO = 0
for s, t in my_safe:
    if s > 8 and t > 8:
        print("YES")
    else:
        print("NO")
        cnt_NO += 1
print(cnt_NO)
