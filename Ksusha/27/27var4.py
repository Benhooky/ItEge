f = open('ItEge/Ksusha/27/27v04_A.txt')
K = int(f.readline())
N = int(f.readline())
lst = [int(x) for x in f]
answerLst = []
for i in range(N - 2*K):
    for j in range(i+K,N-K):
        for l in range(j+K,N):
            answerLst.append(lst[i]*lst[j]*lst[l])
print(max(answerLst))