f = open('Pasha/26/26_10107.txt')
N = int(f.readline())
count = 1
slov = []
for i in range(N):
    a, b = f.readline().split()
    slov.append((int(a), int(b)))
slov = sorted(slov, key=lambda x: x[1])
current = slov[0]
predTime = 0
indexOfLast = 0
for a in range(1, len(slov)):
    if current[1] <= slov[a][0]:
        predTime = current[1]
        current = slov[a]
        count += 1
        indexOfLast = a
# key=lambda x: x[0] - лишнее, он работает так по дефолту
predTime = max(slov[indexOfLast:], key=lambda x: x[0])[0]-predTime
print(count, predTime)
