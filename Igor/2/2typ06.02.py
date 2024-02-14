print ("X Y Z W F G")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = int((x or (not y)) and (not(x == z)) and w)
                G = int(((x <= y) and (y <= z) and (z <= w)))
                print(x,y,z,w,F,G)