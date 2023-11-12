cnt = 0
mylist = [(6, 4), (7, 8), (8, 5), (5, 6), (-11, 10), (-5, 7), (-2, 2), (4, 5), (8, 6)]
for i in mylist:
    if i[0] < 6 or i[1] < 6:
        cnt += 1
print(f"Cnt = {cnt}")
