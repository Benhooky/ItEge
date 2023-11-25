f = open('ItEge/Pasha/27/27-A_11485.txt')
N = int(f.readline())
a = []
b = []
min0 = 100000000
for i in range(2 * N):
    if i < N:
        a.append(int(f.readline()))
    else:
        b.append(int(f.readline()))
for x in a:
    for y in b:
        min0 = min(min0, abs(x - y))
print(min0)