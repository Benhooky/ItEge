print("X Y Z W")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if not( (not(w <= x)) or ( (not (z)) <= (not (y)) ) or z):
                    print(x,y,z,w)