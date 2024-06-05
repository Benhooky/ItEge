print("X Y Z W")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ( ( x or ((not z) and w) or w ) == ( y and (not x) and w ) ):
                    print(x,y,z,w)