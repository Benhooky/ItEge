f = [ int(x) for x in open('ItEge/Stepan/17/17 (12).txt')]
minf = min(x for x in f if str(x)[-1] == str(x)[-2])
cnt = 0
mx = 0
for i in range(len(f) -1):
    para = [f[i], f[i + 1]]
    if (str(para[0])[-1] ==  str(para[1])[-2]) or (str(para[1])[-1] ==  str(para[0])[-2]):
        if sum(1 for x in para if abs(x) % 13 == 0) == 1:
            if (para[0] ** 2 + para[1] ** 2) <= minf ** 2:
                mx = max(mx, para[0] ** 2 + para[1] ** 2)
                cnt +=1
print(cnt, mx)