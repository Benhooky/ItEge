P = [i for i in range(56, 80)]
Q = [j for j in range(63, 86)]

min0 = 100000000000
for Aleft in range(1, 299):
    for Bright in range(Aleft+1, 300):
        A = [i for i in range(Aleft, Bright+1)]
        if min0<= Bright-Aleft:
            break
        flag = True
        for x in range(1, 300):
            if ((not((x in P) <= (x in Q))) <= ((not(x in Q)) <= (x in A))) == 0:
                flag = False
                break
        if flag:
            min0 = min(min0, Bright - Aleft + 1)
print(min0)