file = open('ItEge/Pasha/26/26_1379.txt')
s, n = [int(x) for x in file.readline().split()]
spis = sorted([int(x) for x in file])
cntWeights = 0
id = n-1
lstBoat = []
for i in range(len(spis)):
    if s >= spis[i]:
        s -= spis[i]
        cntWeights += 1
    elif i<id:
        lstBoat.append(spis[id]+spis[i])
        id-=1
print(cntWeights,max(lstBoat))