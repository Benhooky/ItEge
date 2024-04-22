Arr=[0,1]
print('x y z w')
for x in Arr:
    for y in Arr:
        for z in Arr:
            for w in Arr:
                if ((not x)and(z <= y) and (not w)) or ((z == w) and ((x or y)<= w)):
                    print (x, y, z, w)