f = open('ItEge/Pasha/27/27_A_10108.txt')
k = int(f.readline())
n = int(f.readline())
max0 = -1000000000000
a = [int(x) for x in f.readlines()]
for i in range(len(a) - 4):
    for j in range(i + k, len(a) - 2):
        for x in range(j + k, len(a)):
            max0 = max(max0, sum([a[i], a[j], a[x]]))
print(max0)
