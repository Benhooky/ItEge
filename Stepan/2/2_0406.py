print("a b c d")
for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if (((a <= b) == c) or (not d) and (d <= (not a))) == 0:
                    print(a, b, c, d)