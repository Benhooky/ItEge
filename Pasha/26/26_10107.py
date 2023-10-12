f = open('Pasha/26/26_10107.txt')
N = int(f.readline())
slov = {}
for i in range(N):
    a, b = f.readline().split()
    slov[int(a)] = int(b)
slov = dict(sorted(slov.items(), key=lambda x: x[1]))
pass
