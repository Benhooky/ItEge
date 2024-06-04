print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (y or w) or (not(x or w)) or z
                if F == 0:
                    print(x, y, z, w)