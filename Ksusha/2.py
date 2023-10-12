arr = [0, 1]
print("x y z w")
for x in arr:
    for y in arr:
        for z in arr:
            for w in arr:
                if not ((x and (not y)) or (y == z) or (not w)):
                    print(x, y, z, w)
