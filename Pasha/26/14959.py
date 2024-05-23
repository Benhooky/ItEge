file = open('ItEge/Pasha/26/26_14959.txt')
k, n = map(int, file.readline().split())
spis = sorted([[int(i.split()[0]), int(i.split()[0]) + int(i.split()[1])] for i in file.readlines()], key=lambda x:x[1])
spisOfPoss = [spis[0]]
ind = 0
for i in spis[1:]:
    if i[0] >= spisOfPoss[-1][-1]:
        spisOfPoss.append(i)
        ind = i
spisOfPoss.pop()
answer = min(x[0] for x in spis[spis.index(ind)-1:] if x[0]>spisOfPoss[-1][-1])
print(k*(len(spisOfPoss)+1), answer)