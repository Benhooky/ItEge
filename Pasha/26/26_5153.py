f = open('ItEge/Pasha/26/26-80.txt').readlines()
n = f[0]
d = {}
for i in f[1:]:
    values = list(map(int,i.split()))
    if values[0] in d.keys():
        d[values[0]].append(values[1])
    else:
        d[values[0]] = [values[1]]
    d[values[0]]=sorted(d[values[0]])

d = dict(sorted(d.items()))
cntAll = 0 
maxTree = 0
resultNumber = 0
for index, value in d.items():
    cntTree = 0
    for i in range(len(value) - 1):
        if abs(value[i] - value[i + 1]) > 4:
            cntTree+=2
        elif abs(value[i] - value[i + 1]) > 2:
            cntTree+=1
    cntAll += cntTree
    if cntTree > maxTree:
        maxTree = cntTree
        resultNumber = index
print(cntAll, resultNumber)