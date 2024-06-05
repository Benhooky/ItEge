file = [int(x) for x in open('ItEge/Pasha/27/27A_13942.txt')]
n = file[0]
file = file[1:]
res = []
for i in range(n - 1):
    t = [file[i]]
    for j in range(i + 1, len(file)):
        t.append(file[j])
        if sum(t)==0:
            res.append(len(t))
print(max(res))