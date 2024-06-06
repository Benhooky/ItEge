file = open('ItEge/Pasha/26/26 (2).txt')
n, k, m = map(int, file.readline().split())
spis = sorted([[x for x in map(int, i.split())] for i in file.readlines()], reverse=True)
sl = {x:[True]*m for x in range(1,k+1)}
for i in spis:
    (sl[i[0]])[i[1]-1]=False
for i in range(2,k+1):
    for j in range(4,m):
        if all(sl[i][j-4:j]) and all(sl[i-1][j-4:j]):
            print(i, j-4)