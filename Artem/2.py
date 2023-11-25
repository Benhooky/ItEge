b = 24
b = b + 1
c1 = b / 8  # 3.125
c2 = b % 8  # 1
c3 = b // 8  # 3
# for i in [23, 32, 11, 32]:
#    print(i)
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if ((x and (not y)) or (y == z) or (not (w))) == False:
                    print(x, y, z, w)
