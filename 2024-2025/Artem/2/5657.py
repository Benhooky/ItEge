print('x y z w')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = w and ((x <= y) ==(y <= z))
                if F == 1:
                    print(x,y,z,w)