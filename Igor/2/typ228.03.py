print ("X Y Z W")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ( ((not(x)) and (z <= y ) and (not(w))) or ((z==w) and (x or y <= w))  ):
                    print(x,y,z,w)