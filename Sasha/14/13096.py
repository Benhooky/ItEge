from string import digits, ascii_uppercase
for x in range(39):
    for y in range(39):
        f = [5,8,x,7,2,3,y,4,9]
        d = [y,x]
        result = 0
        res_yx = 0
        for i in f:
            result += i*39**(len(f)-f.index(i)-1)
        for i in d:
            res_yx += i*39**(len(f)-f.index(i)-1)
        if result%38 == 0:
            if int(res_yx**0.5) == res_yx**0.5:
                print(res_yx)