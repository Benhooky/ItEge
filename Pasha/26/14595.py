file = open('ItEge/Pasha/26/26_14595.txt')
n = int(file.readline())
spis = sorted([[x for x in map(int, i.split())] for i in file.readlines()], key=lambda x:x[1])
spisOfPoss = [spis[0]]
cnt = 1
lastIn = 0
for i in range(1, len(spis)):
    if cnt % 3 != 0:
        if spisOfPoss[-1][1] <= spis[i][0]:
            spisOfPoss.append(spis[i])
            cnt += 1
            lastIn = i
    else:
        if spis[i][0] - spisOfPoss[-1][1] >= 10:
            spisOfPoss.append(spis[i])
            cnt += 1
            lastIn = i
mxCnt = len(spisOfPoss)
print(cnt)
cnt = 0
spis2 = list(reversed(sorted(spis)))
for l in range(len(spis2) - 1):
    for j in range(l + 1, len(spis2)):
        if spisOfPoss[-3][1]>=spis2[j][0]:
            break
        if spis2[l][0] >= spis2[j][1]:
            print(spis2[j][0] - spisOfPoss[-3][1])
            break