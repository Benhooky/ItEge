file = open('ItEge/Pasha/9/90506.txt')
cnt = 0
sm = 0
for i in file:
    cnt += 1
    s = [int(x) for x in i.split()]
    flag = True
    for l in range(len(s) - 1):
        if s[l] % 2 == s[l + 1] % 2:
            flag = False
            break
    if flag:
        p = []
        np = []
        for j in s:
            if s.count(j) == 1:
                np.append(j)
            else:
                p.append(j)
        t = 1
        for k in p:
            t = t * k
        if len(p) == 0:
            sm+=cnt
        else:
            if sum(np) * 3 >= t:
                sm += cnt
                print(s)
print(sm)