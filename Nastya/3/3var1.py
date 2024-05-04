for x in range(0, 1000):
    if not((x < 299) or (not(x%8==0))):
        print(x)
        break