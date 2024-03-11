for x in range(0, 39):
    for y in range(0, 39):
        n = [5,8,x,7,2,3,y,4,9][::-1]
        nyx = [y,x][::-1]
        nyxx = 0
        result = 0
        for i in range(len(n)):
            result += (n[i]) * 39**i
        for i in range(len(nyx)):
            nyxx += (nyx[i]) * 39**i
        if (result % 38 == 0) and (int(nyxx**0.5) == nyxx**0.5):
            print(nyxx)
