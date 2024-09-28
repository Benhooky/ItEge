print("a b c")
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = a == ((b or b) <= c)
            if F == 1:
                print(a, b, c)
