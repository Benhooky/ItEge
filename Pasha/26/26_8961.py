f = open('Pasha/26/26_8961.txt')
K, M, N = map(int, f.readline().split())
dictOf = {}
cnt = 0
ourTickets = []
for i in f.readlines():
    ourTickets.append(int(i[:-1]))
ourTickets.sort(reverse=True)
for i in range(K):
    dictOf[i] = M
for i in ourTickets:
    for j in range(K):
        if i <= dictOf[j]:
            dictOf[j] -= i
            cnt += 1
            break
print(cnt, sum(dictOf.values()))
