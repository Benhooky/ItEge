x = [(13,2), (11,12), (-12,12), (2,-2), (-10,-10), (6,-5), (2,8), (9,10), (1,13)]
for A in range(100):
    cnt = 0
    for s,t in x:
        if not((s > A) or (t > 12)):
            cnt +=1
    if cnt == 8:
        print(A)
        break




