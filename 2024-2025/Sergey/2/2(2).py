print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = (x == (not y)) <= (z == (y or w))
                if F==0:
                    print(x, y, z, w)