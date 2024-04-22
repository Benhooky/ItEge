def F1(x, y, z, w):
    if (x == y) and (w <=z):
        return 1
    else:
        return 0
def F2(x, y, z, w):
    if (x <= y) <= (w == z):
        return 1
    else:
        return 0
print('x y z w  F1 F2')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                print(x, y, z, w,"|" , F1(x, y, z, w),F2(x, y, z, w))
