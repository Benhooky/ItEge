print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F= (x or ((not z )or w )or w) ==(y and (not x) and w)
                if F==1:
                    print (x, y, z, w)